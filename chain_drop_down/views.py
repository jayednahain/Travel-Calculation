from django.shortcuts import render


# Create your views here.


def home_view(request):
   return render(request, 'chain_dropdown.html')


from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
# hotel cost model
from travel_calculator.models import Places, HotelCost, HotelRating, HotelName, HotelCategory

# food cost model
from travel_calculator.models import ResturantNames, FoodCost, Foodtype, Fooditems

# route model
from travel_calculator.models import Source, Destination,Route,Vehicle_type,\
   Vehicle_class,Vehicle_company,Vehicle_modes,Travell_cost, Route_cost


# Create your views here.


def home_view(request):
   return render(request, 'chain_dropdown.html')


def place_reponse(request):
   # place_qs = list(Place.objects.values())
   # hotel_cost = HotelCost.objects.all()
   place_data = list(Places.objects.values())

   # place_data = []
   # for data in hotel_cost:
   #     place_data.append(data.hotel_place.place_name)

   return JsonResponse({'data': place_data})


# def rating_response(request):
#     if request.is_ajax():
#         if request.method == 'GET':
#             selected_place = request.GET.get('data')
#             print(selected_place)
#             hotel_cost = HotelCost.objects.all()
#
#             for data in hotel_cost:
#                 if data.hotel_place.place_name == selected_place:
#                     value = data.hotel_place_id
#                     qs = list(HotelCost.objects.raw(f'SELECT * FROM hotel_data_hotelcost WHERE hotel_place_id ={value}'))
#                     for val in qs:
#                         rating_data = []
#                         rating_data.append(val.hotel_raiting)
#                 print(rating_data)
#     return JsonResponse({'data':'rating connected'})

def rating_response(request):
   if request.is_ajax():
      if request.method == 'GET':
         selected_place = request.GET.get('data')
         print(selected_place)

         # cost_data = HotelCost.objects.all().select_related('hotel_place')
         # for data in cost_data:
         #     print(data.hotel_place.place_name)

         cost_table_data = HotelCost.objects.filter(hotel_place__place_name=selected_place).values()
         rating_table_data = HotelRating.objects.all()
         rating_lisat = []

         for place in cost_table_data:
            for rating in rating_table_data:
               if place['hotel_raiting_id'] == rating.id:
                  rating_lisat.append(rating.hotel_ratings)
               else:
                  pass

         print("-------------------------")
         print(rating_lisat)
         rating_lisat = list(dict.fromkeys(rating_lisat))
         print(rating_lisat)
         print("-------------------------")

         rating_table_data = HotelRating.objects.all()
         for val in rating_table_data:
            print(val.id)

         rating_data_list = list(HotelCost.objects.filter(hotel_place__place_name=selected_place).values())
         print(rating_data_list)
         # data = HotelCost.objects.get()

   return JsonResponse({'data': rating_lisat})


def hotel_name_reponse(request):
   if request.is_ajax():
      if request.method == 'GET':
         selected_rating = request.GET.get('data')
         print(selected_rating)

         # cost_data = HotelCost.objects.all().select_related('hotel_place')
         # for data in cost_data:
         #     print(data.hotel_place.place_name)

         cost_table_data = HotelCost.objects.filter(hotel_raiting__hotel_ratings=selected_rating).values()

         name_table_data = HotelName.objects.all()
         name_list = []
         print(cost_table_data)

         for rating in cost_table_data:
            for hotel_name in name_table_data:
               if rating['hotel_names_id'] == hotel_name.id:
                  name_list.append(hotel_name.hotel_name)
               else:
                  pass

         name_list = list(dict.fromkeys(name_list))
         print(name_list)

   return JsonResponse({'data': name_list})


def hotel_category_reponse(request):
   if request.is_ajax():
      if request.method == 'GET':
         selected_name = request.GET.get('data')
         print(selected_name)

         # cost_data = HotelCost.objects.all().select_related('hotel_place')
         # for data in cost_data:
         #     print(data.hotel_place.place_name)

         cost_table_data = HotelCost.objects.filter(hotel_names__hotel_name=selected_name).values()

         Category_table_data = HotelCategory.objects.all()
         category_list = []
         print(cost_table_data)

         for data in cost_table_data:
            for category in Category_table_data:
               if data['hotel_category_names_id'] == category.id:
                  category_list.append(category.hotel_category_name)
               else:
                  pass

         category_list = list(dict.fromkeys(category_list))
         print(category_list)

   return JsonResponse({'data': category_list})


def hotel_cost_reponse(request):
   if request.is_ajax():
      if request.method == "GET":
         place_data = request.GET.get('body[place]')
         raiting_data = request.GET.get('body[raiting]')
         hotelName_data = request.GET.get('body[hotelName]')
         category_data = request.GET.get('body[category]')

         place = Places.objects.get(place_name=place_data)
         place_id = place.id
         print(place_id)
         rating = HotelRating.objects.get(hotel_ratings=raiting_data)
         rating_id = rating.id
         hotelName = HotelName.objects.get(hotel_name=hotelName_data)
         hotelName_id = hotelName.id
         hotelCategory = HotelCategory.objects.get(hotel_category_name=category_data)
         hotelCategory_id = hotelCategory.id

         hotel_cost = []
         qs = HotelCost.objects.raw(
            f'SELECT * FROM travel_calculator_hotelcost WHERE hotel_place_id ={place_id} AND  hotel_raiting_id = {rating_id} AND hotel_names_id = {hotelName_id} AND hotel_category_names_id={hotelCategory_id}')
         for data in qs:
            hotel_cost.append(data.hotel_cost)
         # print(request.GET)
      return JsonResponse({'data': hotel_cost})


"""                     Food section            """


def food_place_response(request):
   place_data = list(Places.objects.values())
   return JsonResponse({'data': place_data})


def resturant_name_reponse(request):
   if request.is_ajax():
      if request.method == 'GET':
         selected_resturan_place = request.GET.get('data')
         print(selected_resturan_place)
         food_cost_table_data = FoodCost.objects.filter(place__place_name=selected_resturan_place).values()

         returant_name = ResturantNames.objects.all()
         resturant_name_list = []

         for data in food_cost_table_data:
            for name in returant_name:
               if data['restaurants_name_id'] == name.id:
                  resturant_name_list.append(name.restaurants_name)
               else:
                  pass
         resturant_name_list = list(dict.fromkeys(resturant_name_list))
         print(resturant_name_list)

         return JsonResponse({'data': resturant_name_list})


def food_type_reponse(request):
   if request.is_ajax():
      if request.method == 'GET':

         selected_resturan_name = request.GET.get('data')
         print(selected_resturan_name)
         qs = FoodCost.objects.filter(restaurants_name__restaurants_name=selected_resturan_name).values()
         print(qs)
         returant_type = Foodtype.objects.all()
         resturant_type_list = []

         for data in qs:
            for type in returant_type:

               if data['type_names_id'] == type.id:
                  resturant_type_list.append(type.food_type_name)
               else:
                  pass
         resturant_type_list = list(dict.fromkeys(resturant_type_list))
         print(resturant_type_list)

   return JsonResponse({'data': resturant_type_list})


def item_name_reponse(request):
   if request.is_ajax():
      if request.method == 'GET':

         type_name = request.GET.get('data')
         print(type_name)
         qs = FoodCost.objects.filter(type_names__food_type_name=type_name).values()
         print(qs)
         food_items = Fooditems.objects.all()
         resturant_item_name_list = []

         for data in qs:
            for item in food_items:
               if data['item_names_id'] == item.id:
                  resturant_item_name_list.append(item.food_item_name)
               else:
                  pass
         resturant_item_name_list = list(dict.fromkeys(resturant_item_name_list))
         print(resturant_item_name_list)

   return JsonResponse({'data': resturant_item_name_list})


def food_cost_reponse(request):
   if request.is_ajax():
      if request.method == 'GET':
         print(request.GET)

         # getting data from front-end
         place_data = request.GET.get('body[place]')
         resturent_name_data = request.GET.get('body[resturent_name]')
         foodtype_data = request.GET.get('body[foodtype]')
         itemName_data = request.GET.get('body[itemName]')

         # getting all data id
         place = Places.objects.get(place_name=place_data)
         place_id = place.id
         print(place_id)

         resturent_name = ResturantNames.objects.get(restaurants_name=resturent_name_data)
         resturent_name_id = resturent_name.id

         food_type_data = Foodtype.objects.get(food_type_name=foodtype_data)
         food_type_id = food_type_data.id

         itemName = Fooditems.objects.get(food_item_name=itemName_data)
         itemName_id = itemName.id

         qs = HotelCost.objects.raw(
            f'SELECT * FROM travel_calculator_foodcost WHERE item_names_id ={itemName_id} AND  place_id = {place_id} AND restaurants_name_id = {resturent_name_id} AND type_names_id={food_type_id}')

         food_cost_list = []

         for data in qs:
            food_cost_list.append(data.food_cost)

         return JsonResponse({'data': food_cost_list})


"""####################################   route data     ###################################"""


def source_reponse(request):
   source_list = []
   source = Source.objects.all()
   for data in source:
      source_list.append(data.source_name.place_name)

   return JsonResponse({'data': source_list})


def destination_reponse(request):
   destination_list = []
   source = Destination.objects.all()
   for data in source:
      destination_list.append(data.destination_place.place_name)
   print(destination_list)

   return JsonResponse({'data': destination_list})

def route_response(request):
   if request.method == 'GET':
      if request.is_ajax():
         source=request.GET.get('body[source]')
         destination=request.GET.get('body[destination]')

         filter_data = Route.objects.raw('SELECT * FROM travel_calculator_route WHERE route_name like %s and route_name like %s',[f'{source}%', f'%{destination}'])
         route_list = []
         for data in filter_data:
            route_list.append(data.route_name)

         print(route_list)
         return JsonResponse({'data':route_list})


def mood_reponse(request):
   if request.is_ajax():
      if request.method == 'GET':
         select_route = request.GET.get('data')
         print(select_route)
         qs_2  = Route_cost.objects.filter(route__route_name=select_route).values()
         for data2 in qs_2:
            print(data2)

         qs = Route_cost.objects.filter(route__route_name=select_route).values()
         mood_type =Vehicle_modes.objects.all()
         mood_list = []
         for data in qs:
            for mood in mood_type:
               if data['mode_id'] == mood.id:
                  mood_list.append(mood.modes_name)
               else:
                  pass
         mood_list = list(dict.fromkeys(mood_list))
         print(mood_list)


         return JsonResponse({'data':mood_list})

#solved !
def class_reponse(request):
   if request.is_ajax():
      if request.method == 'GET':
         select_mood = request.GET.get('data')
         print(select_mood)
         qs = Route_cost.objects.filter(mode__modes_name=select_mood).values()
         Vehicle_class_data = Vehicle_class.objects.all()
         class_list = []
         for data in qs:
            for classes in Vehicle_class_data:
               if data['vehicle_class_id'] == classes.id:
                  class_list.append(classes.class_name)
               else:
                  pass
         class_list = list(dict.fromkeys(class_list))
         print(class_list)
         return JsonResponse({'data': class_list})



#solved
def company_reponse(request):
   if request.is_ajax():
      if request.method == 'GET':
         select_class = request.GET.get('data')
         qs = Route_cost.objects.filter(vehicle_class__class_name=select_class).values()
         company_name = Vehicle_company.objects.all()

         company_list = []
         for data in qs:
            for names in company_name:
               if data['vehicle_company_names_id'] == names.id:
                  company_list.append(names.vehicle_compnay_name)
               else:
                  pass
         company_list = list(dict.fromkeys(company_list))
         return JsonResponse({'data': company_list})



def comfort_reponse(request):
   if request.is_ajax():
      if request.method == 'GET':
         select_company_name = request.GET.get('data')
         print(select_company_name)

         qs = Route_cost.objects.filter(vehicle_company_names__vehicle_compnay_name=select_company_name).values()
         vehicle_comfot = Vehicle_type.objects.all()

         comfort_list = []
         for data in qs:
            for comfort_names in vehicle_comfot:
               if data['vehicle_comfort_id'] == comfort_names.id:
                  comfort_list.append(comfort_names.vehicle_type_name)
               else:
                  pass
         comfort_list = list(dict.fromkeys(comfort_list))
         print(comfort_list)
         return JsonResponse({'data': comfort_list})


def route_cost_reponse(request):
   if request.is_ajax():
      if request.method == 'GET':
         route = request.GET.get('body[route]')
         travell_mood=request.GET.get('body[travell_mood]')
         vehicle_class= request.GET.get('body[vehicle_class]')
         company_names = request.GET.get('body[company_names]')
         vechile_comfort = request.GET.get('body[vechile_comfort]')
         print(route)


         route_data = Route.objects.get(route_name=route)
         route_id = route_data.id

         travell_mood_data = Vehicle_modes.objects.get(modes_name=travell_mood)
         travell_mood_data_id = travell_mood_data.id

         vehicle_class_data = Vehicle_class.objects.get(class_name=vehicle_class)
         vehicle_class_data_id = vehicle_class_data.id

         company_names_data = Vehicle_company.objects.get(vehicle_compnay_name=company_names)
         company_names_data_id = company_names_data.id

         vechile_comfort_data = Vehicle_type.objects.get(vehicle_type_name=vechile_comfort)
         vechile_comfort_data_id = vechile_comfort_data.id


         #qs = Travell_cost.objects.raw(f'SELECT * FROM travel_calculator_travell_cost WHERE company_names_id ={company_names_data_id} AND  travell_mode_id = {travell_mood_data_id} AND travell_route_id = {route_id} AND vehicle_class_id={vehicle_class_data_id} AND vehicle_comfort_id = {vechile_comfort_data_id}')

         qs = Route_cost.objects.raw(f'SELECT * FROM travel_calculator_route_cost WHERE vehicle_company_names_id ={company_names_data_id} AND  mode_id = {travell_mood_data_id} AND route_id = {route_id} AND vehicle_class_id={vehicle_class_data_id} AND vehicle_comfort_id = {vechile_comfort_data_id}')
         cost_list = []
         for data in qs:
            print(data.travel_cost_route)
            cost_list.append(data.travel_cost_route)



         return JsonResponse({'data':cost_list})






def testt_data(request):
   hotel_cost = HotelCost.objects.all()
   # for data in hotel_cost:
   #     print(data.hotel_place_id)
   return HttpResponse("hi")
