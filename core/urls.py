from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
       path('', views.feed, name='feed'),
       path('signin', views.signin, name='signin'),
       path('signup', views.signup, name='signup'),
       path('settings', views.settings, name='settings'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
