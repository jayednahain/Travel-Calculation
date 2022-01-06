from django.urls import path,include

from chain_drop_down import views

urlpatterns = [


   path('',views.home_view,name='home_view_link'),

   #route cost
   path('source_reponse/',views.source_reponse,name='source_response_link'),
   path('destination_reponse/',views.destination_reponse,name='source_response_link'),
   path('route_reponse_data/',views.route_response,name='route_reponse_data'),
   path('mood_reponse/',views.mood_reponse,name='mood_reponse_link'),
   path('class_reponse/',views.class_reponse,name='class_reponse_link'),
   path('company_name_reponse/',views.company_reponse,name='company_name_link'),
   path('vechile_comfort_reponse/',views.comfort_reponse,name='comfort_link'),
   path('route_cost_response_data/',views.route_cost_reponse,name='route_cost_link'),

   #hotel section !
   path('place_response/',views.place_reponse,name='place_reponse'),
   path('rating_response/',views.rating_response,name='rating_reponse'),
   path('name_response/',views.hotel_name_reponse,name='name_response_link'),
   path('catagory_response/', views.hotel_category_reponse, name='category_name_link'),
   path('hotel_cost_reponse/',views.hotel_cost_reponse,name='cost_reponse_data'),

   #"""food section"'''''
   path('food_place_reponse/',views.food_place_response,name='food_place_reponse_link'),
   path('food_resturant_name_response/',views.resturant_name_reponse,name='returent_name_response'),
   path('food_type_reponse/',views.food_type_reponse,name='food_type_response'),
   path('item_name_reponse/',views.item_name_reponse,name='food_name_repoonse'),
   path('food_cost_response/',views.food_cost_reponse,name= 'food_cost_reponse'),




   path('test_link/',views.testt_data,name='test_link')


]