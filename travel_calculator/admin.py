from django.contrib import admin
from .models import Vehicle_modes,\
   Vehicle_type,\
   Places,\
   Route,\
   Vehicle_company,\
   Vehicle_class,\
   Travell_cost,\
   Route_cost



from .models import Source,Destination


#trans port
admin.site.register(Source)
admin.site.register(Destination)


admin.site.register(Vehicle_modes)
admin.site.register(Vehicle_type)
admin.site.register(Places)
admin.site.register(Route)
admin.site.register(Vehicle_company)

admin.site.register(Vehicle_class)


@admin.register(Travell_cost)
class TravellcostAdmin(admin.ModelAdmin):
   list_display = ['source_place','destination_place','travell_route','travell_mode','vehicle_class','vehicle_comfort','company_names','cost_per_route']

@admin.register(Route_cost)
class RouteCostAdmin(admin.ModelAdmin):
   list_display = ['route', 'mode', 'vehicle_class', 'vehicle_comfort', 'vehicle_company_names','travel_cost_route']






#####################Food
from . models import Foodtype,\
   Fooditems,\
   ResturantNames,\
   FoodCost

admin.site.register(Foodtype)
admin.site.register(Fooditems)
admin.site.register(ResturantNames)

@admin.register(FoodCost)
class FoodcostAdmin(admin.ModelAdmin):
   list_display = ['place', 'type_names', 'item_names', 'restaurants_name', 'food_cost']



#####################Hotel

from .models import HotelRating,HotelCategory,HotelName,HotelCost


admin.site.register(HotelRating)
admin.site.register(HotelCategory)
admin.site.register(HotelName)



@admin.register(HotelCost)
class HotelcostAdmin(admin.ModelAdmin):
   list_display = ['hotel_place', 'hotel_raiting', 'hotel_category_names', 'hotel_names', 'hotel_cost']






