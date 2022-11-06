from django.contrib import admin
from .models import City, Ads, Segment, Material, HaveBalcony, Conditions, CountRooms

admin.site.register(City)
admin.site.register(CountRooms)
admin.site.register(Segment)
admin.site.register(Material)
admin.site.register(HaveBalcony)
admin.site.register(Conditions)
admin.site.register(Ads)

