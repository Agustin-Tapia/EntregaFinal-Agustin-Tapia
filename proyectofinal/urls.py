"""proyectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import (pagina, instagram, email, formulario, about, 
PostList, PostDetail, CrearEjercicio, PostUpdate, PostDelete, BuscarEjercicio, 
Login, SignUp, Logout, MensajeCreate ,ProfileCreate, ProfileUpdate, PostMineList, MensajeList, MensajeDelete
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina, name="pagina"),
    path('sobre/mi', about, name="sobre-mi"),
    path('instagram', instagram, name="instagram"),
    path('email',email, name="email"),
    path('ejercicio', formulario, name="ejercicios"),
    path('post/list', PostList.as_view(), name="post-list"),
    path('post/<pk>/detail', PostDetail.as_view(), name="post-detail"),
    path('post/create', CrearEjercicio.as_view(), name="post-create"),
    path('post/<pk>/update', PostUpdate.as_view(), name="post-update"),
    path('post/<pk>/delete', PostDelete.as_view(), name= "post-delete"),
    path('post/search', BuscarEjercicio.as_view(), name= "post-search"),
    path('login', Login.as_view(), name= "login"),
    path('signup', SignUp.as_view(), name= "signup"),
    path('logout', Logout.as_view(), name= "logout"),
    path('post/list/mine', PostMineList.as_view(), name= "post-mine"), #mis posts
    path('mensajes/create', MensajeCreate.as_view(), name= "crear-mensaje"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list" ),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
    path('profile', ProfileCreate.as_view(), name= "profile-create"),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name= "profile-update"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
