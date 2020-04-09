from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from accounts.forms import MyForm, MyAuthForm, MyPasswordResetForm, MyPasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from account.views import PasswordResetView
from django.urls import reverse_lazy
from django.template.loader import render_to_string

# Вариант регистрации на базе класса FormView
class MyRegisterFormView(FormView):
    # Указажем какую форму мы будем использовать для регистрации наших пользователей, в нашем случае
    # это UserCreationForm - стандартный класс Django унаследованный
    form_class = MyForm
    form_class.is_active = False


    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/register.html"

    def form_valid(self, form):


        form.save()
        # Функция super( тип [ , объект или тип ] )
        # Возвратите объект прокси, который делегирует вызовы метода родительскому или родственному классу типа .
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)



class MyLoginView(LoginView):
    authentication_form = MyAuthForm


class MyPasswordResetView(PasswordResetView):

    template_name = "account/password_reset.html"
    template_name_sent = "account/password_reset_sent.html"
    form_class = MyPasswordResetForm


class MyPasswordChangeView(PasswordChangeView):
    template_name = "registration/password_change_form.html"
    form_class = MyPasswordChangeForm


def someview(request):
    return redirect(request.session['return_path'])

class MyLogoutView(LogoutView):
    template_name = "registration/login.html"