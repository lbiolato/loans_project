from django.core import validators
from django.db import models
from django.db.models.fields import IntegerField
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from localflavor.ar.forms import ARDNIField


class Loan(models.Model):
    GENDER_CHOICES = (
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("NB", "No Binario"),
        ("O", "Otro"),
    )
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.PositiveIntegerField(
        validators=[MinValueValidator(1000000), MaxValueValidator(70000000)]
    )
    genero = models.CharField(max_length=2, choices=GENDER_CHOICES)
    edad = models.PositiveIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(120)]
    )
    email = models.EmailField()
    monto = models.PositiveIntegerField()
    aprobado = models.BooleanField(default=False)
    fecha = models.DateTimeField(default=timezone.now)

    def request_loan(self):
        pass
