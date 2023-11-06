from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Toplan(models.Model):
    subject = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    is_completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__ (self):
        return self.subject