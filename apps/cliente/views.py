from django.shortcuts import render
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Cliente, IpAsignadaCliente, IpAsignada
from sweetify.views import SweetifySuccessMixin
from .forms import NuevoCliente, IpAsignadaClienteForm
from django.forms import formset_factory, inlineformset_factory
from django.http import HttpResponseRedirect

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



class ClienteCreateView(LoginRequiredMixin, SweetifySuccessMixin, CreateView):
    model = Cliente
    form_class = NuevoCliente
    template_name='cliente/create.html'
    login_url='login'

    IpasignadaFormset = inlineformset_factory(Cliente, IpAsignadaCliente, IpAsignadaClienteForm, extra=1, can_delete=False)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(*kwargs)
        context['titulo']='Cliente'
        context['titulo_seccion']='Crear cliente'
        context['titulo_formulario']='Complete el formulario para crear el cliente'
        context['pantalla_anterior']='Cliente'
        context['leyenda']='Los campos marcados con * son obligatorios'
        context['btn_crear']='Crear'
        context['btn_cancelar']='Cancelar'
        #context['ipasignada_formm']= self.IpasignadaFormset(self.request.POST or None)
        return context
    
        def get(self, request, *args, **kwargs):
            self.object = None
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            ipAsignadaCliente_form = self.IpasignadaFormset()
            return self.render_to_response(self.get_context_data(
                form= form
                ,ipAsignadaCliente_form_form = IpAsignadaClienteForm
            
            ))
        
        def post(self, request, *args, **kwargs):
            self.object = None
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            ipAsignadaCliente_form = self.AsociacionDomicilioFormset(self.request.POST)
            if (form.is_valid() and ipAsignadaCliente_form.is_valid()):
                return self.form_valid(form, ipAsignadaCliente_form)
            else:
                print(form.errors,ipAsignadaCliente_form.errors)
                return self.form_invalid(form, ipAsignadaCliente_form)  

        def form_valid(self, form, ipAsignadaCliente_form):
            
            self.object= form.save()
            self.object.save()
            ipAsignadaCliente_form.instance = self.object
            ipAsignadaCliente_form.save()
            return HttpResponseRedirect(self.get_success_url())
        
        def form_invalid(self, form,ipAsignadaCliente_form):
            return self.render_to_response(
            self.get_context_data(
                                    form=form
                                    ,ipAsignadaCliente_form =ipAsignadaCliente_form
                                
                                    ))