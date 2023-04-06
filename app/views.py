from django.shortcuts import render
from app.models import GymModel
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

#-----renderizar HTML-----#
def pagina(request):
    return render(request, "app/base.html")
def instagram(request):
    return render(request, "app/instagram.html")
def email(request):
    return render(request, "app/email.html")

#>>>>>Formulario>>>>>>#

def formulario(request):
   if request.method == 'POST': #para guardar datos, este metodo
        gym = GymModel(request.POST['tituloejercicio'], request.POST['descripcion'])
        gym.save()
        return render(request, "app/gymmodel_form.html")




#------- CLASES ------#

class PostList(ListView):
    model = GymModel
    context_object_name = "gyms"    

class PostDetail(DetailView):
    model = GymModel
    context_object_name = "detail"

class PostUpdate(LoginRequiredMixin,UpdateView):
    model = GymModel
    context_object_name = "update"
    success_url = reverse_lazy("post-list")
    fields = '__all__'

class PostDelete(LoginRequiredMixin,DeleteView):
    model = GymModel
    context_object_name = "delete"
    success_url = reverse_lazy("post-list")

class CrearEjercicio(LoginRequiredMixin,CreateView):
    model = GymModel
    success_url = reverse_lazy("post-list")
    fields = '__all__'

class BuscarEjercicio(LoginRequiredMixin,ListView):
    model = GymModel
    context_object_name = "gyms"
    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = (GymModel.objects.filter(tituloejercicio__icontains=criterio).all())
        return result

class Login(LoginView):
    next_page = reverse_lazy("post-list")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

class Logout(LogoutView):
    template_name = "registration/logout.html"

