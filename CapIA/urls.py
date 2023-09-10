from django.contrib import admin
from django.urls import path
from PruebaVocacional import views as test
from django.conf import settings
from django.conf.urls.static import static
from chat import views as chat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test.home,name='home'),
    path('test/',test.test, name='test'),
    path('test/answers',test.answers,name='answers')
    path('chat/',chat.)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
