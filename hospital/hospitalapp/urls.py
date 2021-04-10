from django.urls import path
from . import views

app_name='hospitalapp'
urlpatterns=[
    path('',views.home,name='home'),
    path('news/',views.News,name='news'),
    path('doctor/',views.doctor,name='doctor'),
    path('dept/',views.dept,name='dept'),
    path('apmnt/',views.apmnt,name='apmnt'),
    path('', views.allDoc, name='allDoc'),
    path('<slug:c_slug>/',views.allDoc,name='products_by_category'),

]