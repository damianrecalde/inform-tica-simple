from django import forms
from .models import Cliente, IpAsignadaCliente

class NuevoCliente(forms.ModelForm):
    class Meta:
        model=Cliente
        fields = [
            'nombre',
            'apellido',
            'empresa',
            'tipo_cliente',
            'tipo_documento',
            'documento_nro',
            'localidad',
            'barrio',
            'calle',
            'calle_nro',
            'Fecha_nacimiento',
            'observacion',
            'latitud',
            'longitud',
            'activo'
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'empresa': 'Empresa a la que pertenece',
            'tipo_cliente': 'Tipo de cliente',
            'tipo_documento': 'Tipo de documento',
            'documento_nro': 'Número de documento',
            'localidad': 'Localidad',
            'barrio': 'Barrio',
            'calle': 'Calle',
            'calle_nro': 'Calle número',
            'Fecha_nacimiento': 'Fecha de nacimiento',
            'observacion': 'observaciones',
            'latitud': 'Latitud',
            'longitud': 'Longitud',
            'activo': 'Seleccione si esta actvio el cliente'
        }

        widgets ={
            'nombre': forms.TextInput( attrs={'class':'form-control'}),
            'apellido': forms.TextInput( attrs={'class':'form-control'}),
            'empresa': forms.TextInput( attrs={'class':'form-control'}),
            'tipo_cliente': forms.Select( attrs={'class': 'form-control'}),
            'tipo_documento': forms.TextInput( attrs={'class':'form-control'}),
            'localidad': forms.Select( attrs={'class': 'form-control'}),
            'barrio': forms.Select( attrs={'class': 'form-control'}),
            'calle':forms.Select( attrs={'class': 'form-control'}),
            'calle_nro': forms.TextInput( attrs={'class':'form-control'}),
            'latitud': forms.TextInput( attrs={'class':'form-control'}),
            'longitud': forms.TextInput( attrs={'class':'form-control'}),
            'Fecha_nacimiento': forms.TextInput(attrs = {'class':'form-control','type': 'date'}),
            'activo': forms.CheckboxInput( attrs={'class':'custom-control-input', 'id':'customSwitch3'}),
        }

class IpAsignadaClienteForm(forms.ModelForm):
    class Meta:
        model = IpAsignadaCliente
        fields=[
            'cliente',
            'producto',
            'ipAsignada',
        ]

        labels={
            'cliente':'cliente',
            'producto': 'Antena',
            'ipAsignada': 'Ip asignada'
        }

        widgets ={
             'producto': forms.Select(attrs={'class':'form-control'}),
             'ipAsignada': forms.Select(attrs={'class':'form-control'})
        }
