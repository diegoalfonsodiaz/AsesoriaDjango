from django import forms

from .models import Proyecto, Asesor



class AsesorForm(forms.ModelForm):
    class Meta:
        model = Asesor
        fields = ('nombre', 'facultad', 'anios', 'profesion', 'proyectos')
        def __init__ (self, *args, **kwargs):
            super(AsesorForm, self).__init__(*args, **kwargs)   
            self.fields["proyectos"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["proyectos"].help_text = "Ingrese los proyectos que tiene el asesor"
            self.fields["proyectos"].queryset = Proyecto.objects.all()
