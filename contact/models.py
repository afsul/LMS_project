from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(blank=True,)
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name