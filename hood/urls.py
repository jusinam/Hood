
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^register/', views.signup, name='signup'),
    url(r'^hoods/$',views.home,name='hood'),
    url(r'^new-hood/',views.addhood,name='new-hood'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),

    url(r'^profile/(?P<username>\w+)/edit', views.editprofile, name='edit-profile'),
    url(r'^hood/(?P<id>\d+)',views.unohood,name='unhood'),
    url(r'^neighbours/(?P<hood_id>\d+)',views.hoodneighbours,name='neighbours'),
    url(r'^new-post/(?P<hood_id>\d+)',views.addpost,name='post'),
   
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
