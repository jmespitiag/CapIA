from django.contrib import admin
from django.urls import path
from PruebaVocacional import views as test
from django.conf import settings
from django.conf.urls.static import static
from chat import views as chat
from herramientas import views as herramienta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/<int:id_estudiante>', test.home,name='home'),
    path('',test.home_name,name='home_name'),
    path('test/<int:id_estudiante>',test.test, name='test'),
    path('test/answers/<int:id_estudiante>',test.answers,name='answers'),
    path('test/result/<int:id_estudiante>',test.result,name="result"),
    path('chat/<int:id_estudiante>',chat.chat,name="chat"),
    path('metodos-estudio/', herramienta.metodos_estudio, name="metodos-estudio")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
