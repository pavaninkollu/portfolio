from django.db import models

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    technologies_used=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    
    def __str__(self) -> str:
        return self.title