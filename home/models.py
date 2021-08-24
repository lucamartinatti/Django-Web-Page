from django.db import models

class Characteristics(models.Model):

    description = models.CharField(max_length=200)
