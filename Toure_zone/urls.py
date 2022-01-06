
import debug_toolbar

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('chain_drop_down.urls'))


]

