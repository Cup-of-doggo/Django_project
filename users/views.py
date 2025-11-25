import os
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .form import AbstractUserCreationForm
from django .core.mail import send_mail

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = AbstractUserCreationForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_message(user.email)
        return super().form_valid(form)

    def send_welcome_message(self, user_email):
        subject = 'Добро пожаловать на сайт'
        message = 'Спасибо за регистрацию!'
        from_email = os.getenv('MYEMAIL')
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)

