from django.db import models







# transport system

class Vehicle_class(models.Model):
   class_name = models.CharField(max_length=100)

   def __str__(self):
      return str(self.class_name)


class Vehicle_modes(models.Model):
   modes_name = models.CharField(max_length=100)
   def __str__(self):
      return str(self.modes_name)

class Vehicle_type(models.Model):
   vehicle_type_name = models.CharField(max_length=50)
   def __str__(self):
      return str(self.vehicle_type_name)


class Places(models.Model):
   place_name = models.CharField(max_length=100)
   def __str__(self):
      return str(self.place_name)

class Route(models.Model):
   route_name = models.CharField(max_length=150,unique=True)

   def __str__(self):
      return str(self.route_name)



class Vehicle_company(models.Model):
   vehicle_compnay_name = models.CharField(max_length=150)
   def __str__(self):
      return str(self.vehicle_compnay_name)


class Source(models.Model):
   source_name = models.ForeignKey(Places,on_delete=models.PROTECT,null=True,blank=True)
   def __str__(self):
      return str(self.source_name)

class Destination(models.Model):
   destination_place = models.ForeignKey(Places,on_delete=models.PROTECT,null=True,blank=True)

   def __str__(self):
      return str(self.destination_place)


class Travell_cost(models.Model):
   source_place = models.ForeignKey(Source,on_delete=models.CASCADE,null=True,blank=True)
   destination_place = models.ForeignKey(Destination,on_delete=models.CASCADE,null=True,blank=True)



   travell_route  = models.ForeignKey(Route,on_delete=models.CASCADE,null=True)

   travell_mode   = models.ForeignKey(Vehicle_modes,on_delete=models.CASCADE,)
   vehicle_class  = models.ForeignKey(Vehicle_class,on_delete=models.CASCADE,null=True,blank=True)
   vehicle_comfort= models.ForeignKey(Vehicle_type,on_delete=models.CASCADE,null=True,blank=True)

   company_names  = models.ForeignKey(Vehicle_company,on_delete=models.CASCADE,null=True,blank=True)
   cost_per_route = models.IntegerField()



#new route model !
class Route_cost(models.Model):
   route = models.ForeignKey(Route, on_delete=models.CASCADE, null=True)
   mode = models.ForeignKey(Vehicle_modes, on_delete=models.CASCADE, )
   vehicle_class = models.ForeignKey(Vehicle_class, on_delete=models.CASCADE, null=True, blank=True)
   vehicle_comfort = models.ForeignKey(Vehicle_type, on_delete=models.CASCADE, null=True, blank=True)

   vehicle_company_names = models.ForeignKey(Vehicle_company, on_delete=models.CASCADE, null=True, blank=True)
   travel_cost_route = models.IntegerField()





class Foodtype(models.Model):
   food_type_name = models.CharField(max_length=50)
   def __str__(self):
      return str(self.food_type_name)


class Fooditems(models.Model):
   food_item_name= models.CharField(max_length=100)
   def __str__(self):
      return str(self.food_item_name)


class ResturantNames(models.Model):
   restaurants_name = models.CharField(max_length=100)
   def __str__(self):
      return str(self.restaurants_name)


class FoodCost(models.Model):
   place            = models.ForeignKey(Places,on_delete=models.CASCADE,null=True,blank=True)
   type_names        = models.ForeignKey(Foodtype,on_delete=models.CASCADE,null=True,blank=True)
   item_names       = models.ForeignKey(Fooditems,on_delete=models.CASCADE,null=True,blank=True)
   restaurants_name = models.ForeignKey(ResturantNames,on_delete=models.CASCADE,null=True,blank=True)
   food_cost        = models.IntegerField()






#hotels

class HotelRating(models.Model):
   hotel_ratings = models.CharField(max_length=100)
   def __str__(self):
      return str(self.hotel_ratings)


class HotelCategory(models.Model):
   hotel_category_name = models.CharField(max_length=100)
   def __str__(self):
      return str(self.hotel_category_name)

class HotelName(models.Model):
   hotel_name = models.CharField(max_length=100)

   def __str__(self):
      return str(self.hotel_name)




class HotelCost(models.Model):
   hotel_place = models.ForeignKey(Places,on_delete=models.CASCADE,null=True,blank=True)
   hotel_raiting = models.ForeignKey(HotelRating,models.CASCADE,null=True,blank=True)
   hotel_category_names = models.ForeignKey(HotelCategory,on_delete=models.CASCADE,null=True,blank=True)
   hotel_names = models.ForeignKey(HotelName,on_delete=models.CASCADE,null=True,blank=True)
   hotel_cost = models.IntegerField()



