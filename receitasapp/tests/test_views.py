from django.test import TestCase, Client
from django.urls import reverse

from receitasapp.models import RecipeCategory, Recipe


class ViewsTestCase(TestCase):


    def test_if_recipe_and_categories_is_being_returned_from_the_view(self):

        client = Client()

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

        response = client.get(reverse('receita', args=["1"]))
        self.assertEqual(response.status_code, 200)

        self.assertFalse(response.context[-1]['recipe'] == None)
        self.assertGreater(len(response.context[-1]['categories']), 0)