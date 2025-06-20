from django.test import TestCase
from receitasapp.models import Recipe, RecipeCategory

class RecipeTestCase(TestCase):


    def test_recipe_model_has_the_correct_return_when_using_str_function(self):
        recipe_category = RecipeCategory.objects.create(category_name="Comida")
        recipe = Recipe.objects.create(
            name="Nome",
            category=recipe_category,
            description="Descrição",
            ingredients="Ingredientes",
            ready_time_minutes=30,
            amount=1,
            amount_by="Pessoa",
            img="Imagem"
        )
        self.assertEqual(recipe.name, str(recipe))


    def test_recipe_when_deleted_doesnt_delete_recipe_category(self):
        recipe_category = RecipeCategory.objects.create(category_name="Comida")
        Recipe.objects.create(
            name="Nome",
            category=recipe_category,
            description="Descrição",
            ingredients="Ingredientes",
            ready_time_minutes=30,
            amount=1,
            amount_by="Pessoa",
            img="Imagem"
        )
        Recipe.objects.exclude(name="Nome")
        recipe_category_check = RecipeCategory.objects.filter(category_name="Comida")

        self.assertTrue(recipe_category_check != None)