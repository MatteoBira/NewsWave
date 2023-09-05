from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.feed, name="feed"),
    path("upload", views.upload, name="upload"),
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("settings", views.settings, name="settings"),
    path("upload_page", views.upload_page, name="upload_page"),
    path("logout", views.logout, name="logout"),
    path("<str:user>/<str:pk>", views.article, name="article"),
    path("nyt", views.fetchNytTopstories, name="fetchNytTopstories"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
