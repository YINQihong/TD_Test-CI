import unittest
from unittest.mock import MagicMock
from CartePizzeria import CartePizzeria, Pizza,Boisson,Dessert, CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        """ Initialisation avant chaque test"""
        self.carte = CartePizzeria()
        self.pizza_mock = MagicMock(spec=Pizza)
        self.pizza_mock.nom = "NomPizza"
        self.boisson_mock = MagicMock(spec=Boisson)
        self.boisson_mock.nom = "NomBoisson"
        self.dessert_mock = MagicMock(spec=Dessert)
        self.dessert_mock.nom = "NomDessert"

        self.pizza_mock2 = MagicMock(spec=Pizza)
        self.pizza_mock2.nom = "NomPizza2"
        self.boisson_mock2 = MagicMock(spec=Boisson)
        self.boisson_mock2.nom = "NomBoisson2"
        self.dessert_mock2 = MagicMock(spec=Dessert)
        self.dessert_mock2.nom = "NomDessert2"

    def test_is_empty_initial(self):
        """Tester si la carte est vide au départ"""
        self.assertTrue(self.carte.is_empty())

    def test_add_pizza(self):
        """Tester l'ajout d'une pizza"""
        self.carte.add(self.boisson_mock)
        self.assertFalse(self.carte.is_empty())
        self.assertEqual(self.carte.nb_drinks(), 1)

    def test_add_dessert(self):
        """Tester l'ajout d'une dessert"""
        self.carte.add(self.dessert_mock)
        self.assertFalse(self.carte.is_empty())
        self.assertEqual(self.carte.nb_desserts(), 1)

    def test_add_boisson(self):
        """Tester l'ajout d'un boisson"""
        self.carte.add(self.pizza_mock)
        self.assertFalse(self.carte.is_empty())
        self.assertEqual(self.carte.nb_pizzas(), 1)

    def test_remove_pizza(self):
        self.carte.add(self.pizza_mock)
        self.assertFalse(self.carte.is_empty())
        self.assertEqual(self.carte.nb_pizzas(), 1)
        self.carte.remove("NomPizza")
        self.assertEqual(self.carte.nb_pizzas(), 0)
        self.assertTrue(self.carte.is_empty())

    def test_remove_boisson(self):
        self.carte.add(self.boisson_mock)
        self.assertFalse(self.carte.is_empty())
        self.assertEqual(self.carte.nb_drinks(), 1)
        self.carte.remove("NomBoisson")
        self.assertEqual(self.carte.nb_drinks(), 0)
        self.assertTrue(self.carte.is_empty())

    def test_remove_dessert(self):
        self.carte.add(self.dessert_mock)
        self.assertFalse(self.carte.is_empty())
        self.assertEqual(self.carte.nb_desserts(), 1)
        self.carte.remove("NomDessert")
        self.assertEqual(self.carte.nb_desserts(), 0)
        self.assertTrue(self.carte.is_empty())
    
    def test_remove_pizza_notFound(self):
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove("NonExistante")

    def test_nb_pizzas(self):
        self.carte.add(self.pizza_mock)
        self.carte.add(self.pizza_mock2)
        self.assertEqual(self.carte.nb_pizzas(), 2)

    def test_nb_drinks(self):
        self.carte.add(self.boisson_mock)
        self.carte.add(self.boisson_mock2)
        self.assertEqual(self.carte.nb_drinks(), 2)

    def test_nb_desserts(self):
        self.carte.add(self.dessert_mock)
        self.carte.add(self.dessert_mock2)
        self.assertEqual(self.carte.nb_desserts(), 2)

if __name__ == "__main__":
    unittest.main()