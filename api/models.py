from django.db import models

# Create your models here.

class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return "%s %s".format(self.first_name, self.last_name)
    
class Movie(models.Model):
    movie_name = models.CharField(max_length=40)
    review = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    date_published = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.movie_name