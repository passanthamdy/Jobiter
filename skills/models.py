from django.db import models

# Create your models here.
class Skill(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
<<<<<<< HEAD
    
=======
    
>>>>>>> 258d32b3c188bb550623582b7a09a7b3e53c5378
