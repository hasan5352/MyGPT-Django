from django.urls import path
from . import views

def route_with_slash(route: str, view):
	""" :param route: should not have a trailing / at the end. function already adds a /.
	"""
	return [path(route, view), path(route + '/', view)]
  

urlpatterns = [
    *route_with_slash('signup', views.SignupApi.as_view()),
    *route_with_slash('login', views.LoginApi.as_view()),
    *route_with_slash('verify', views.VerifyJwtApi.as_view()),
]