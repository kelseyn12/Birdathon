from django.db import models

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

        
# birds = [
#     Bird('Northern Flicker', 'Picidae', 'Open Woodlands', 'Insects', 'Cavity', 'Ground Forager', 'Large. brownwood woodpeckers with a gentle expression and handsome black-scalloped plumage'),
#     Bird('Northern Cardinal', 'Cardinalidae', 'Open Woodlands', 'Seeds', 'Shrub', 'Ground Forager', "A shade of red you cant't take your eyes off of."),
#     Bird('Golden Eagle', 'Accipitridae', 'Grasslands', 'Mammals', 'Cliff', 'Soaring', "Large and fast nimble raptor. Gold Feathers gleam on the back of it's head"),
# ]