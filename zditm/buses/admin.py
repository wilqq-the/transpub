from django.contrib import admin

from .models import Buses

class BusesAdmin(admin.ModelAdmin):
     list_display = ('veh_id', 'linia','kierunek','z','w_kierunku','opoznienie','typ','lat','lon','time_stamp')

admin.site.register(Buses, BusesAdmin)
