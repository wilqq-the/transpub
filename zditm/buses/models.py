from django.db import models

class Buses(models.Model):
    veh_id = models.SmallIntegerField(primary_key=True)
    gmvid = models.SmallIntegerField()
    linia = models.TextField()
    kierunek = models.TextField()
    z = models.TextField()
    w_kierunku = models.TextField()
    lat = models.DecimalField(max_digits=15, decimal_places=2)
    lon = models.DecimalField(max_digits=15, decimal_places=2)
    opoznienie = models.DecimalField(max_digits=15, decimal_places=2)
    typ = models.TextField()
    time_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buses'  