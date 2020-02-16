from django.db import models

# Create your models here.
class PetModel(models.Model):
    name=models.CharField(max_length=150)
    age=models.IntegerField()
    available=models.BooleanField(default=True)
    image=models.ImageField(upload_to="Media/")
    price=models.DecimalField(max_digits=5,decimal_places=2)
