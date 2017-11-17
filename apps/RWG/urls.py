from django.conf.urls import url
from . import views
urlpatterns = [
    # url(r'^process$', views.index)
    url(r'^$',views.index),
    url(r'^generate$', views.generate),
    url(r'^reset$', views.reset),
  ]