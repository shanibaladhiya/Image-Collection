from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login, name='login'),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('dashboard', views.dashboard, name='dashboard'),
    path('about',views.about,name="about"),
    path("contactus",views.contactus,name="contact"),
    path("gallery",views.gallery,name="gallery"),
    path("nature",views.nature,name="nature"),
    path("food",views.food,name="food"),
    path("health",views.health,name="health"),
    path("travel",views.travel,name="travel"),
    path("animal",views.animal,name="animal"),
    path("fashion",views.fashion,name="fashion"),
    path("athlete",views.athlete,name="athlete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)