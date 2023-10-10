from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Adicione campos personalizados aqui, como data de nascimento
    data_de_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username


class DonoDePet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Outros campos relacionados ao perfil de Dono de Pet


class FuncionarioDaTosa(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Outros campos relacionados ao perfil de Funcionário da Tosa


class Administrador(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Outros campos relacionados ao perfil de Administrador
    