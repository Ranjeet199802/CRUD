from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # path('', views.get_req, name='get'),
    path('post_req', csrf_exempt(views.post_req), name='post'),
    path('get_req', csrf_exempt(views.get_req), name='get'),
    path('by_id/<int:val>', views.by_id, name='get')
]
