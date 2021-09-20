from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^department$',views.deptApi),
    url(r'^department/([0-9]+)$',views.deptApi),
]
