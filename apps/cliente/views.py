from django.shortcuts import render
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Cliente


class ClienteListView(LoginRequiredMixin, ListView):
    model=Cliente
    template_name='cliente/list.html'
    login_url='login'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['titulo']='Clientes'
        context['titulo_tabla']='Listado de clientes'
        context['pantalla_principal']='Panel principal'
        context['btn_crear']='Crear cliente'
        return context
