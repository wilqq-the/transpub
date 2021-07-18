import requests,unidecode,json,psycopg2
from datetime import datetime, timezone


#Add table if not exists

#Database settings
con = psycopg2.connect(database="postgres", user="postgres", password="root", host="127.0.0.1", port="5432")
print("Database opened successfully")

cur = con.cursor()
try:
    cur.execute('''CREATE TABLE BUSES
      (VEH_ID   SMALLINT PRIMARY KEY NOT NULL,
      GMVID    SMALLINT NOT NULL,
      LINIA TEXT    NOT NULL,
      KIERUNEK  TEXT     NOT NULL,
      Z TEXT NOT NULL,
      W_KIERUNKU    TEXT    NOT NULL,
      LAT   DECIMAL     NOT NULL,
      LON   DECIMAL     NOT NULL,
      OPOZNIENIE    DECIMAL NOT NULL,
      time_stamp timestamp with time zone)''')
except psycopg2.errors.DuplicateTable:
    print("Table already exists")
con.commit()
con.close()


#Get vehicle data from ZDITM
response_api = requests.get('https://www.zditm.szczecin.pl/json/pojazdy.inc.php')

data = response_api.text
parse_json = json.loads(data)
dt = datetime.now(timezone.utc)

#Iterate over response to insert data to SQL

for index,item in enumerate(parse_json):

        #Parsing data to fit model

        veh_id = str(item['id'])
        gmvid = str(item['gmvid'])
        linia = str(item['linia'])
        kierunek = str(item['kierunek'])
        z = str(item['z'])
        do = "Puste" if len(str(item['do'])) < 1 else str(item['do'])
        lat = str(item['lat'])
        lon = str(item['lon'])
        opoznienie = str(item['punktualnosc2']).replace('&minus;','-')
        cur = con.cursor()

        cur.execute(f"""INSERT INTO buses (VEH_ID,GMVID,LINIA,KIERUNEK,Z,W_KIERUNKU,LAT,LON,OPOZNIENIE,time_stamp)
                        VALUES ({veh_id},{gmvid},'{linia}','{kierunek}','{z}','{do}',{lat},{lon},{opoznienie},'{dt}')
                        ON CONFLICT (VEH_ID)
                        DO UPDATE SET 
                            LINIA = EXCLUDED.linia, 
                            KIERUNEK = EXCLUDED.kierunek,
                            Z = EXCLUDED.z,
                            W_KIERUNKU = EXCLUDED.w_kierunku,
                            LAT = EXCLUDED.lat,
                            LON = EXCLUDED.lon,
                            OPOZNIENIE = EXCLUDED.opoznienie,
                            time_stamp = EXCLUDED.time_stamp""");
        
        con.commit()

        #Print for log from Crontab (timestamp + vehicle ID)

        print(f"{dt} : Record inserted successfully. - GMVID: {veh_id}")

        con.close()



