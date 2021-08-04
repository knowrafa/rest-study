from django.db import models

# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)
    data_nascimento = models.DateField(null=True)

    class Meta:
        db_table = "pessoa"
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    @staticmethod
    def validar_pessoa(self):
        pass