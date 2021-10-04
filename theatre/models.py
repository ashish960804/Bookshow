from django.db import models
from django.contrib.auth.models import User
from django.forms.utils import flatatt
from movies.models import Movie


# Create your models here.

class Theatre(models.Model):
    city_choice=(
        ('DELHI','Delhi'),
        ('KOLKATA','Kolkata'),
        ('MUMBAI','Mumbai'),
        ('CHENNAI','Chennai'),
        ('BANGALORE','Bangalore'),
        ('HYDERABAD','Hyderabad'),
    )
    name = models.CharField(max_length=50,null=False)
    city = models.CharField(max_length=9,choices=city_choice,null=False)
    address = models.CharField(max_length=30)
    no_of_screen = models.IntegerField()
    admin_id = models.ForeignKey(User,on_delete=models.CASCADE,)

    def __str__(self):
        return self.name+"-"+self.address+"-"+self.city

class Show(models.Model):
    time_choice=(
        ('09:30','09:30'),
        ('12:00','12:00'),
        ('15:30','15:30'),
        ('18:00','18:00'),
        ('21:30','21:30'),
    )

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screen = models.IntegerField(null=False,default=1)
    date = models.DateField(null=False,blank=True)
    totaldays = models.IntegerField(null=False,default=1)
    time = models.TimeField()

    def __str__(self):
        return str(self.movie) + "-" + str(self.theatre) + "-" + str(self.date) + "-" + str(self.time)
