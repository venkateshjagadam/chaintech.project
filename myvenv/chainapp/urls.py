from django.urls import path,include
from . import views

urlpatterns = [
    #path("",views.IndexView,name="index"),
    ##("",views.htmlform,name="htmlform"),
    path("",views.InsertPageView,name="insertpage"),
    path("insert/",views.InsertData,name="insert"),
    path("showpage/",views.ShowPage,name="showpage"),

]