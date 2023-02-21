from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from restaurant.models import upload_path,Restaurnat,Category





class Meal(models.Model):
    Name = models.CharField(max_length=42 )
    Restaurnat = models.ForeignKey(Restaurnat, on_delete=models.CASCADE,)
    Image = models.ImageField(upload_to=upload_path, blank=True, null=True)
    Body = models.TextField(blank=True)
    Type = models.ForeignKey(Category, on_delete=models.CASCADE,)
    Price = models.FloatField( validators=[MinValueValidator(0.01)])