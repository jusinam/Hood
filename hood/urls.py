
from django.conf.urls import url,include
from django.conf import settings
from . import views



urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^register/', views.signup, name='signup'),
    url(r'^hoods/$',views.home,name='hood'),
]
