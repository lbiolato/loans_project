from django.core import validators
from django.db import models
from django.db.models.fields import IntegerField
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from localflavor.ar.forms import ARDNIField


class Loan(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("NB", "Non-binary"),
        ("O", "Other"),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni = models.PositiveIntegerField(
        validators=[MinValueValidator(1000000), MaxValueValidator(70000000)]
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(120)]
    )
    email = models.EmailField()
    amount = models.PositiveIntegerField()
    approved = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def request_loan(self):
        pass
