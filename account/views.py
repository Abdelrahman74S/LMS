from django.shortcuts import redirect ,render
from django.views.generic  import CreateView, DetailView ,UpdateView
from django.contrib.auth.views import LoginView ,PasswordChangeView
from .form import CreateUserForm, LoginForm ,changeprofile
from django.contrib.auth import  login , logout 
from account.models import MyUser
from django.urls import reverse_lazy , reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import views as auth_views

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
     
def logout_view(request):
    logout(request)
    return redirect('account:login')

class profile(LoginRequiredMixin,UserPassesTestMixin,DetailView):    
    model = MyUser
    template_name = "account/profile.html"
    context_object_name = "pro" 
    
    def test_func(self):
        profile_to_update = self.get_object()
        return self.request.user == profile_to_update
    
class Updateprofile(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = MyUser
    form_class = changeprofile
    template_name = "account/Updateprofile.html"

    def test_func(self):
        profile_to_update = self.get_object()
        return self.request.user == profile_to_update
    
    def get_success_url(self):
        return reverse("account:profile", kwargs={"pk": self.object.pk})
    

class ChangePasswordView(LoginRequiredMixin,PasswordChangeView):
    model = MyUser
    form_class = PasswordChangeForm
    template_name = 'account/change_password.html'

    def get_success_url(self):
        return reverse("account:profile", kwargs={"pk": self.request.user.pk})
    

class MyPasswordResetView(auth_views.PasswordResetView):
    template_name = 'account/reset_password.html'
    email_template_name = 'account/password_reset_email.html'
    subject_template_name = 'account/password_reset_subject.txt'
    success_url = reverse_lazy('account:password_reset_done')

class MyPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'account/password_reset_sent.html'

class MyPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'account/password_reset_form.html'
    success_url = reverse_lazy('account:password_reset_complete')

class MyPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'account/password_reset_done.html'