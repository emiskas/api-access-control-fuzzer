from django.db import models
from django.contrib.auth.models import User


class SuperSecretBankAccount(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=6, decimal_places=2)