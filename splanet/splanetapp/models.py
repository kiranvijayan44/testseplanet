from django.db import models

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length=250)
    email =models.EmailField(blank=True)
    message =models.TextField()

    def __str__(self):
        return self.name