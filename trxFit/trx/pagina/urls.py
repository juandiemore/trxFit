from django.conf.urls import include,url
from django.contrib.auth.views import login

from . import views
from .views import Registrar

urlpatterns = [

url(r'^$', views.inicio, name='inicio'),
url(r'^sedes', views.sedes , name='sedes' ),
url(r'^entrenadores', views.entrenadores , name='ent' ),
url(r'^Clase', views.Clase , name='Clase' ),
url(r'^registrar', Registrar.as_view() , name='reg'),
url(r'^login', login , {'template_name':'login.html'}, name='login'),
url(r'^new_Class', views.unirseAclase , name='claseE')
]