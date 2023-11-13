from django.contrib import admin
from django.urls import path
from PruebaVocacional import views as test
from django.conf import settings
from django.conf.urls.static import static
from chat import views as chat
from herramientas import views as herramientas
from cuentas import views as cuentas



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/<int:id_estudiante>', cuentas.home,name='home'),
    path('',cuentas.home_name,name='home_name'),
    path('test/<int:id_estudiante>',test.test, name='test'),
    path('chat/<int:id_estudiante>',chat.chat,name="chat"),
    path('metodos-estudio/<int:id_estudiante>', herramientas.metodos_estudio, name="metodos-estudio"),
    path('test/answers/<int:id_estudiante>',test.answers,name='answers'),
    path('test/result/<int:id_estudiante>',test.result,name="result"),
    path('horario/<int:id_estudiante>',herramientas.horario,name='horario'),
    path('horario/agregar/<int:id_estudiante>', herramientas.agregar_clase , name='agregar_clase' ),
    path('calcular-promedio/<int:id_estudiante>', herramientas.calcular_promedio, name="calcular-promedio"),
    path('registro/',cuentas.register, name='registro'),
    path('profile/<int:id_estudiante>',cuentas.profile,name='perfil'),
    path('chat/<int:id_estudiante>',chat.chat,name="chat"),
    path('metodos-estudio/<int:id_estudiante>', herramientas.metodos_estudio, name="metodos-estudio"),
    path('analisis/<int:id_estudiante>', test.data, name="analisis")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
