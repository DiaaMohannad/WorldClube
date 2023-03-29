from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=100  )
    description = models.TextField(null=True ,blank=True )
    image = models.ImageField(upload_to='images/' , null=True , blank=True )
    image1 = models.ImageField(upload_to='images/' , null=True , blank=True )
    image2 = models.ImageField(upload_to='images/' , null=True , blank=True )

    def __str__(self):
        return self.name

class Custom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    people = models.ForeignKey(People, on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100, null=True , blank=True)
    description = models.TextField( null=True , blank=True)
    date = models.DateField(null=True , blank=True)
    people = models.ForeignKey(People , on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    people = models.ManyToManyField(People)



    def __str__(self):
        return self.name

