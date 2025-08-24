# En cars_repairs_app/forms.py
from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['autor', 'profesion', 'imagen', 'texto', 'servicio'] 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['texto'].widget.attrs['rows'] = 6
        # Si quieres un estilo diferente para el selector de servicio, podrías hacerlo aquí
        # Por ejemplo: self.fields['servicio'].widget.attrs['class'] = 'form-select'