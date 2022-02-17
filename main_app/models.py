from django.db import models
from django.urls import reverse

SPOTTED = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')
)




# Create your models here.
class Bird(models.Model):
        name = models.CharField(max_length=100)
        family = models.CharField(max_length=100)
        habitat = models.CharField(max_length=100)
        food = models.CharField(max_length=100)
        nesting = models.CharField(max_length=100)
        behavior = models.CharField(max_length=100)
        description = models.TextField(max_length=250)

       
        def __str__(self):
            return self.name
        
        def get_absolute_url(self):
            return reverse('detail', kwargs={'bird_id': self.id})

class Sighting(models.Model):
    date = models.DateField('Sighting Date')
    time = models.CharField(
        max_length=1,
        choices=SPOTTED,
        default=SPOTTED[0][0]
        )

    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date']