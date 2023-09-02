from django.db import models
from django.urls import reverse

# Create your models here.

CAT = (
   ('CC', 'Cakes and Cupcakes'),
   ('PT', 'Pies and Tarts'),
   ('CB', 'Cookies and Bisquits'),
   ('PP', 'Pastries and Puff Pastry'),
   ('FD', 'Frozen Desserts'),
   ('PC', 'Puddings and Custards'),
   ('FR', 'Fruit-based Desserts'),
   ('ID', 'International Desserts'),
   ('OT', 'Other Desserts'),
)

class Pastryrecipe(models.Model):
    title = models.CharField(max_length=100)
    
    preptime = models.IntegerField()
    cookingtime = models.IntegerField()
    totaltime = models.IntegerField()
    yields = models.IntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()
        
    def __str__(self):
      return f'{self.title} ({self.id})'

    def get_absolute_url(self):
      return reverse('detail', kwargs={'recipe_id': self.id})
    
class Photo(models.Model):
    url = models.ImageField(upload_to='recipes/', default="No Image")
   
    recipe = models.ForeignKey(Pastryrecipe, on_delete=models.CASCADE)

    def __str__(self):
      return f"Photo for recipe_id: {self.recipe_id} @ {self.url}"
    