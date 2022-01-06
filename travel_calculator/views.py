from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
from .models import Source
from .models import Travell_cost
from .models import Places
from .models import Destination
from .models import Route



def testView(request):
   source_data = Places.objects.all()

   context={
      'source_data':source_data
   }
   return render(request,'calculator.html',context)


def json_source_data(request):
   # source_data_json = list(Source.objects.get())
   #travel_cost_js = list(Source.objects.values())

   source_js=[]
   test_data = Source.objects.all()
   for data in test_data:
      print(data.source_name.place_name)
      source_js.append(data.source_name.place_name)



   return JsonResponse({'data':source_js})



def json_destination_data(request):
   destination_js = []
   destination_data = Destination.objects.all()
   for value in destination_data:
      print(value.destination_place.place_name)
      destination_js.append(value.destination_place.place_name)

   return JsonResponse({'data': destination_js})

def available_route_response(request):
   if request.is_ajax():
      if request.method=='GET':

         selected_source = request.GET.get('selectedSource')
         select_destination = request.GET.get('selectedDestination')

         print(selected_source,'!!', select_destination)

         # if selected_source and select_destination is None:
         #    filter_data = ""
         # else:
            #filter_data = Route.objects.filter(route_name__endswith=select_destination)
         filter_data = Route.objects.raw('SELECT * FROM travel_calculator_route WHERE route_name like %s and route_name like %s',[f'{selected_source}%', f'%{select_destination}'])

         route_names = []

         for items in filter_data:
            route_names.append(items.route_name)


         return JsonResponse({'data': route_names})





#
# def available_routes(request):
#
#    # source = "Dhaka"
#    # destination = "Saint martin"
#
#    filter_data = Route.objects.filter(route_name__endswith='Saint martin')
#    route_names = []
#    for items in filter_data:
#       print(items)
#       route_names.append(items.route_name)
#
#    print(len(route_names))
#
#    # if source in route_names:
#    #    print("hellow")
#
#    #filter_data_serializers = serializers.serialize('json',filter_data)
#
#    return JsonResponse({'data':route_names})



def route_response(request):
   if request.is_ajax():
      if request.method == 'GET':
         selected_route= request.GET.get('selectedRoute')

         print(selected_route)
         route_filter = Route.objects.filter()




         return JsonResponse({'data':selected_route})



#Dhaka-Chittagong-Cox's bazar

def raw_query(request):

   if request.method=="GET":
      source = request.GET.get('source')
      destination = request.GET.get('destination')




      #filted_data = Route.objects.raw(f'SELECT * FROM travel_calculator_route WHERE route_name= %s',[data])
      filted_data = Route.objects.raw('SELECT * FROM travel_calculator_route WHERE route_name like %s and route_name like %s',
                               [f'{source}%', f'%{destination}'])

      for item in filted_data:
         print(item)
      context = {
         'filted_data':filted_data

      }
      return render(request,'test.html',context)




def send_data(request):


   if request.method=="GET":
      print('get connected')
      source = request.POST.get('source')
      destination = request.POST.get('destination')

      print(source)
      print(destination)




   context = {
      'source_data':Source.objects.all(),
      'destination_data':Destination.objects.all()
   }

   return render(request,'form_system.html',context)




#---------------------------search by form

#takeing response source and destination
def main_route_find(request):
   if request.method=="GET":
      source = request.GET.get('source')
      destination = request.GET.get('destination')

      source_d = request.GET.get('source_d')
      destinatio_d = request.GET.get('destination_d')
      #print(source_d,destinatio_d)

      #print(source,destination)

      filter_data = Route.objects.raw(
         'SELECT * FROM travel_calculator_route WHERE route_name like %s and route_name like %s',
         [f'{source_d}%', f'%{destinatio_d}'])

      route_names = []

      for items in filter_data:
         route_names.append(items.route_name)


   src_data = Source.objects.all()
   des_data = Destination.objects.all()
   context = {
      'filtered_data': route_names,
      'source_data':src_data,
      'destination_data':des_data
   }

   return render(request,'search_by_form.html',context)



def sub_route_find(request):


   if request.method == "GET":
      main_route = request.GET.get('main_route')
      print(main_route)

      return redirect('form_link')



   # context={
   #    'sub_routes':
   # }


   return render(request,'form_system.html')




def take_two(request):

   if request.is_ajax():

      if request.method=="GET":


         data = request.GET.get('data')
         print(data)
         # for value in data:
         #    print(value)


         # data2 = request.GET.get('data2')
         # data3 = request.GET.get('data3')
         # print(data2)
         # print(data3)

         print(data)
         return JsonResponse({'data':'ajax connected!'})

   return JsonResponse({'data':'opps no ajax!'})




