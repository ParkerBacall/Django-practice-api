from django.db import models

# Create your models here.
class Pasta(models.Model):
    sauce = models.CharField(max_length=20)
    spiciness = models.IntegerField()