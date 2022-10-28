from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class ColorVarient(models.Model):
    Color = [('Red','Red'), ('Pink','Pink'), ('Black','Black'), ('White','White'),
             ('Blue','Blue'), ('Gray','Gray'), ('Sandal','Sandal'), ('Yellow','Yellow'), 
             ('Meroon','Meroon'), ('Green','Green'),]
    color = models.CharField(max_length = 10, choices=Color)
    
    def __str__(self):
        return self.color

    
class SizeVarient(models.Model):
    
    Sizes = [('S' , 'S'),
            ('M' , 'M'),
            ('L' , 'L'),
            ('XL' , 'XL'),
            ('XXL' , 'XXL'),
            ('XXXL' , 'XXXL'),]

    size = models.CharField(max_length = 10, choices=Sizes)
    
    def __str__(self):
            return self.size
        
class Categories(models.Model):
    Catagory = [("Men's Dresses","Men's Dresses"), ("Womens's Dresses","Womens's Dresses"),
                ("Baby's Dresses","Baby's Dresses"), ("Electronics", "Electronics"), 
                ("Bags","Bags"), ("Shoes", "Shoes"),]
    
    catagory = models.CharField(max_length = 10, choices=Catagory)
    
    def __str__(self):
            return self.catagory
        
class Product(models.Model):
    Name = models.CharField(max_length=50)
    Color = models.ManyToManyField(ColorVarient)
    Sizes = models.ManyToManyField(SizeVarient)
    Price =models.PositiveBigIntegerField()
    Sort_Description = models.TextField()
    Desription = models.TextField()