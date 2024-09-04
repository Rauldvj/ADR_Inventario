from django import forms # type: ignore
from django.contrib.auth.models import User # type: ignore #IMPORTAMOS EL MODELO DE USUARIOS
from accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore #IMPORTAMOS EL FORMULARIO DE AUTENTICACIÓN
from .models import AllInOne, AllInOneAdmins, Notebook, MiniPC, Proyectores, BodegaADR, Azotea, Reporte

#_______________________________________________________________________________________________________________________________
#FORMULARIO LOGIN
class LoginForm(AuthenticationForm):
    pass

#_______________________________________________________________________________________________________________________________
#FORMULARIO REGISTRO DE USUARIOS

#CREAMOS EL FORMULARIO EL CUAL REGISTRA Y RETORNA EN FORMATO HTML A NUESTRA VISTA DE NUEVO USUARIO

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='Nombres')
    last_name = forms.CharField(label='Apellidos')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    #FUNCION PARA VALIDAR EL EMAIL EN EL FORMULARIO DE REGISTRO
    def clean_email(self):
        email_field = self.cleaned_data['email']

        #PREGUNTAMOS SI EL EMAIL A EXISTE
        if User.objects.filter(email=email_field).exists(): #
            raise forms.ValidationError('Este email ya existe en los registros') #RETORNAMOS EL MENSAJE DE ERROR

        return email_field #RETORNAMOS EL EMAIL


#________________________________________________________________________________________________________________________________

#CREAMOS EL FORMULARIO EL CUAL HEREDA LOS DATOS DEL USER
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

#____________________________________________________________________________________________________________________________
#FORMULARIO DE PERFIL
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
    



#_______________________________________________________________________________________________________________________________

#FORMULARIO PARA REGISTRO DE NUEVO USUARIO CREADO POR EL ADR

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


#_____________________________________________________________________________________________________________________________

#FORM ALL IN ONE 
class AllInOneForm(forms.ModelForm):
    class Meta:
        model = AllInOne
        fields = '__all__'
        widgets = {
            'estado': forms.Select(),
            'marca': forms.Select(),
            'ubicacion_all_in_one': forms.Select(),
            
        }

    def clean_n_serie(self):
        n_serie = self.cleaned_data.get('n_serie')
        if AllInOne.objects.exclude(id=self.instance.id).filter(n_serie=n_serie).exists():
            raise forms.ValidationError('Este Número de Serie ya existe')
        return n_serie

#________________________________________________________________________________________________________________________________
#FORM ALL IN ONE ADMINISTRADORES

class AllInOneAdminsForm(forms.ModelForm):
    class Meta:
        model = AllInOneAdmins
        fields = '__all__'
        widgets = {
            'estado': forms.Select(),
            'marca': forms.Select(),
            'ubicacion_all_in_one_admin': forms.Select(),        
        }

    def clean_n_serie(self):
        n_serie = self.cleaned_data.get('n_serie')
        if AllInOne.objects.exclude(id=self.instance.id).filter(n_serie=n_serie).exists():
            raise forms.ValidationError('Este Número de Serie ya existe')
        return n_serie

#________________________________________________________________________________________________________________________________

#FORM NOTEBOOKS

class NotebooksForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = '__all__'
        widgets = {
            'estado': forms.Select(),
            'marca': forms.Select(),
            'ubicacion_notebook': forms.Select(),
        }

#________________________________________________________________________________________________________________________________

#FORM MINI PCS

class MiniPCForm(forms.ModelForm):
    class Meta:
        model = MiniPC
        fields = '__all__'
        widgets = {
            'estado': forms.Select(),
            'marca': forms.Select(),
            'ubicacion_mini_pc': forms.Select(),
        }

#________________________________________________________________________________________________________________________________

#FORM PROYECTORES

class ProyectoresForm(forms.ModelForm):
    class Meta:
        model = Proyectores
        fields = '__all__'
        widgets = {
            'estado': forms.Select(),
            'marca': forms.Select(),
            'ubicacion_proyector': forms.Select(),
        }

#________________________________________________________________________________________________________________________________

#FORM BODEGA ADR

class BodegaADRForm(forms.ModelForm):
    class Meta:
        model = BodegaADR
        fields = '__all__'
        widgets = {
            'activo': forms.Select(),
            'marca': forms.Select(),
            'estado_activo': forms.Select(),
        }

#________________________________________________________________________________________________________________________________
#FORM AZOTEAS
class AzoteaForm(forms.ModelForm):
    class Meta:
        model = Azotea
        fields = '__all__'
        widgets = {
            'activo': forms.Select(),
            'marca': forms.Select(),
            'estado_activo': forms.Select(),
        }


#________________________________________________________________________________________________________________________________

#FORM REPORTES
class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = '__all__'
        widgets = {
            'bolso': forms.CheckboxInput(attrs={'class': 'form-input'}),
            'equipo': forms.CheckboxInput(attrs={'class': 'form-input'}),
            'cargador': forms.CheckboxInput(attrs={'class': 'form-input'}),
            'en_reporte': forms.RadioSelect(attrs={'class': 'form-input'}),
            'entregado': forms.RadioSelect(attrs={'class': 'form-input'}),
        }


#________________________________________________________________________________________________________________________________

