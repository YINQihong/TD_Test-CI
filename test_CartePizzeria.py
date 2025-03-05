import unittest
from unittest.mock import MagicMock
from CartePizzeria import CartePizzeria, Pizza, CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        """ Initialisation avant chaque test"""
        self.carte = CartePizzeria()
        self.pizza_mock1 = MagicMock(spec=Pizza)
        self.pizza_mock1.nom = "NomPizza1"
        self.pizza_mock2 = MagicMock(spec=Pizza)
        self.pizza_mock2.nom = "NomPizza2"
        self.pizza_mock3 = MagicMock(spec=Pizza)
        self.pizza_mock3.nom = "NomPizza3"

    def test_is_empty_initial(self):
        """Tester si la carte est vide au départ"""
        self.assertTrue(self.carte.is_empty())

    def test_add_pizza(self):
        """Tester l'ajout d'une pizza"""
        self.carte.add_pizza(self.pizza_mock1)
        self.assertFalse(self.carte.is_empty())
        self.assertEqual(self.carte.nb_pizzas(), 1)

    def test_remove_pizza(self):
        self.carte.add_pizza(self.pizza_mock1)
        self.assertFalse(self.carte.is_empty())
        self.assertEqual(self.carte.nb_pizzas(), 1)
        self.carte.remove_pizza("NomPizza1")
        self.assertTrue(self.carte.is_empty())
    
    def test_remove_pizza_notFound(self):
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("NonExistante")

    def test_nb_pizzas(self):
        self.carte.add_pizza(self.pizza_mock1)
        self.carte.add_pizza(self.pizza_mock2)
        self.carte.add_pizza(self.pizza_mock3)
        self.assertEqual(self.carte.nb_pizzas(), 3)


if __name__ == "__main__":
    unittest.main()