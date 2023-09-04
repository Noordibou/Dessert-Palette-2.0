from django.db import models
from django.urls import reverse

CAT = (
   ('Cakes and Cupcakes','Cakes and Cupcakes'),
   ('Pies and Tarts','Pies and Tarts'),
   ('Cookies and Biscuits','Cookies and Biscuits'),
   ('Puff Pastry','Puff Pastry'),
   ('Frozen Desserts','Frozen Desserts'),
   ('Puddings and Custards','Puddings and Custards'),
   ('Fruit-based Desserts','Fruit-based Desserts'),
   ('International Desserts','International Desserts'),
   ('Other Desserts','Other Desserts'),
)

class Pastryrecipe(models.Model):
    title = models.CharField(max_length=100)
    preptime = models.IntegerField()
    cookingtime = models.IntegerField()
    totaltime = models.IntegerField()
    yields = models.IntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=30, choices=CAT, default='Other Desserts')  
    featured = models.BooleanField(default=False)  
    
    def __str__(self):
        return f'{self.title} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})

class Photo(models.Model):
    url = models.ImageField(upload_to='recipes/', default="No Image")
    recipe = models.ForeignKey(Pastryrecipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for recipe_id: {self.recipe_id} @ {self.url}"
