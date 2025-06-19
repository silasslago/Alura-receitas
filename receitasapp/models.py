from django.db import models

class RecipeCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(RecipeCategory, on_delete=models.PROTECT, null=True)
    description = models.TextField()
    ingredients = models.TextField()
    ready_time_minutes = models.IntegerField()
    amount = models.IntegerField()
    amount_by = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    img = models.TextField()

    def __str__(self):
        return self.name