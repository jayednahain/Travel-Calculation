#path('__debug__/', include(debug_toolbar.urls))
import debug_toolbar
from .import views

from django.urls import path,include



urlpatterns = [

   path('',views.testView,name='name_test_link'),

   #json_response
   #sending source
   path('source_json_res/',views.json_source_data,name='source_js_link'),

   #sending destination
   path('destination_json_res/',views.json_destination_data,name='source_js_link'),

   #receving route
   path('avalable_route/',views.available_route_response,name ='available_route_response_link'),


   path('reoute_response/',views.route_response,name='route_response'),

   #test
   #path('route_response/',views.available_routes,name='route_response'),

   path('form_system/',views.send_data,name='form_data_link'),
   # raw query data

   #new test
   path('raw_query/',views.raw_query,name = 'raw_query'),
   path('search_by_form/',views.main_route_find,name='form_link'),
   path('sub_route/',views.sub_route_find,name='sub_route_find_link'),
   path('take_two_test/',views.take_two,name ='take_two_link'),


   #debug
   path('__debug__/', include(debug_toolbar.urls))



]