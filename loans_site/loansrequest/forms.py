from django import forms
from django.db import models
from .models import Loan


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = (
            "first_name",
            "last_name",
            "dni",
            "gender",
            "age",
            "email",
            "amount",
        )

    def clean(self):
        super(LoanForm, self).clean()

        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

        if not first_name.isalpha():
            self._errors['first_name'] = self.error_class(['Name is not valid.'])

        if not last_name.isalpha():
            self._errors['last_name'] = self.error_class(['Last name is not valid.'])

        return self.cleaned_data


class LoanEditForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = (
            "first_name",
            "last_name",
            "dni",
            "gender",
            "age",
            "email",
            "amount",
            "approved",
        )

    def clean(self):
        super(LoanEditForm, self).clean()

        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

        if not first_name.isalpha():
            self._errors['first_name'] = self.error_class(['Name is not valid.'])

        if not last_name.isalpha():
            self._errors['last_name'] = self.error_class(['Last name is not valid.'])

        return self.cleaned_data