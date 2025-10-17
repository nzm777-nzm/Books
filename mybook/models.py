from django.db import models

class Book(models.Model):
    
    name=models.CharField(max_length=100)
    
    price=models.PositiveIntegerField()
    
    author=models.CharField(max_length=100)
    
    category=models.CharField(max_length=100)
    
    picture=models.ImageField(upload_to="bookimage",null=True)
    
    def __str__(self):
        
        return self.name   