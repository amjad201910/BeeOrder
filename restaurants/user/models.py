from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
from menu.models import Meal



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_on = models.DateField(auto_now_add=True, blank=True)
    Address = models.TextField(blank=True)
    Price = models.FloatField( validators=[MinValueValidator(0.01)])
class CP (models.Model):
    Meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    Cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Quantity = models.BigIntegerField( validators=[MinValueValidator(1)])
    Price = models.FloatField(validators=[MinValueValidator(0.01)])
