from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    VISITANTE = 'visitante'
    MIEMBRO = 'miembro'
    COLABORADOR = 'colaborador'

    TIPO_PERFIL_CHOICES = [
        (VISITANTE, 'Visitante'),
        (MIEMBRO, 'Miembro'),
        (COLABORADOR, 'Colaborador'),
    ]

    tipo_perfil = models.CharField(max_length=20, choices=TIPO_PERFIL_CHOICES, default=VISITANTE)

    def __str__(self):
        return f"{self.username} ({self.get_tipo_perfil_display()})"
