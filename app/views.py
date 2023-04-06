from django.shortcuts import render
from app.models import GymModel, Profile
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class PostMineList(LoginRequiredMixin, PostList):
    def get_queryset(self):
        return GymModel.objects.filter(publisher = self.request.user.id).all()


class PostDetail(DetailView):
    model = GymModel
    context_object_name = "detail"


#-----PermisosTest-----#
class PermisosSolo(UserPassesTestMixin):
     def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get("pk")
        return GymModel.objects.filter(publisher = user_id, id = post_id). exists()

class PostUpdate(LoginRequiredMixin, PermisosSolo, UpdateView):
    model = GymModel
    context_object_name = "update"
    success_url = reverse_lazy("post-list")
    fields = '__all__'

class PostDelete(LoginRequiredMixin, PermisosSolo, DeleteView):
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

#------ Seccion Usuario -----#
class Login(LoginView):
    next_page = reverse_lazy("post-list")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

class Logout(LogoutView):
    template_name = "registration/logout.html"

#------ Creacion Profile ------#

class ProfileCreate(LoginRequiredMixin,CreateView):
    model = Profile
    success_url = reverse_lazy("post-list")
    fields = ['avatar',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(UpdateView):
    model = Profile
    success_url = reverse_lazy("post-list")
    fields = ['avatar']
    def test_func(self):
        return Profile.objects.filter(user = self.request.user).exists("profile")
