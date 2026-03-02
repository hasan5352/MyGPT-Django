from backend.utils.routing_helpers import route_with_slash
from . import views

urlpatterns = [
    *route_with_slash('signup', views.SignupApi.as_view()),
    *route_with_slash('login', views.LoginApi.as_view()),
    *route_with_slash('verify', views.VerifyJwtApi.as_view()),
]