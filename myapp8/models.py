from django.db import models

# Create your models here.
class project(models.Model):
    pid=models.CharField(max_length=3,primary_key=True)
    name=models.CharField(max_length=20)
    language=models.CharField(max_length=30)
    dutration=models.IntegerField(null=True)