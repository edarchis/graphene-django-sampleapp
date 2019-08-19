from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Table(models.Model):
    name = models.TextField()
    height = models.IntegerField(null=True)


class Foot(models.Model):
    number = models.IntegerField()
    style = models.TextField()
    table = models.ForeignKey(to=Table, on_delete=CASCADE)
