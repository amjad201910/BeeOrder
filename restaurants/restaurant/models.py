from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid
# Create your models here.
def upload_path(instance, filname):
    now = datetime.now()
    date_time = now.strftime("%m%d%Y%H%M%S")
    return '/'.join([str(uuid.uuid4()),str(date_time), str(instance.Name), filname])



class Restaurnat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50,unique=True)
    Image = models.ImageField(upload_to=upload_path, blank=True, null=True)

    Address = models.TextField()

class Category(models.Model):
    Name = models.CharField(max_length=42 )
    Restaurnat = models.ForeignKey(Restaurnat, on_delete=models.CASCADE,)

    def __str__(self):
        return self.Name



