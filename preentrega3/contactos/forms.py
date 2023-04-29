from django.forms import ModelForm
from .models import Contacto, Profesor, Curso
from django.forms import formset_factory


class ContactoFormulario(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'


class ProfesorFormulario(ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'


class CursoFormulario(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
