from backend.utils.routing_helpers import route_with_slash
from . import views

urlpatterns = [
    *route_with_slash('', views.ThreadListCreateApi.as_view()),
    *route_with_slash('<uuid:thread_id>', views.ThreadDetailApi.as_view()),
]