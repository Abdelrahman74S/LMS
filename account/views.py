from django.shortcuts import redirect ,render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .form import CreateUserForm, LoginForm
from django.contrib.auth import authenticate , login , logout 
from django.urls import reverse_lazy
# Create your views here.

def home_view(request):
    return render(request, "account/home.html")

class RegisterView(CreateView):
    form_class = CreateUserForm
    template_name = "account/register.html"
    success_url = reverse_lazy("account:login")

    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)

        return super().form_valid(form)
    
class loginView(LoginView):
      form_class = LoginForm 
      template_name = "account/login.html"
      success_url = reverse_lazy("account:home")
      
      def form_valid(self, form):
         login(self.request, form.get_user())
         return super().form_valid(form)
     
def logout_view(request):
    logout(request)
    return redirect('register')