from django import forms
from django.db import models
from .models import Loan


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = (
            "nombre",
            "apellido",
            "dni",
            "genero",
            "edad",
            "email",
            "monto",
        )

    def clean(self):
        super(LoanForm, self).clean()

        nombre = self.cleaned_data.get("nombre")
        apellido = self.cleaned_data.get("apellido")

        if not nombre.isalpha():
            self._errors['nombre'] = self.error_class(['El nombre insertado no es válido'])

        if not apellido.isalpha():
            self._errors['apellido'] = self.error_class(['El apellido insertado no es válido'])

        return self.cleaned_data
