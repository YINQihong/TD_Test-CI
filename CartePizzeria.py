

class Pizza:
    def __init__(self,nom,ingredients,prix):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix


class CartePizzeria:
    def __init__(self):
        self.carte = {}

    def is_empty(self):
        return len(self.carte) == 0
    
    def nb_pizzas(self):
        return len(self.carte)
    
    def add_pizza(self,pizza):
        self.carte[pizza.nom] = pizza

    def remove_pizza(self,nom):
        if nom not in self.carte:
            raise CartePizzeriaException(f"La pizza {nom} n'existe pas dans la carte")
        del self.carte[nom]

class CartePizzeriaException(Exception):
    pass


if __name__ == "__main__":
    carte = CartePizzeria()
    print(carte.is_empty())  # True
    
    pizza1 = Pizza("Margherita", ["tomate", "mozzarella", "basilic"], 8.5)
    carte.add_pizza(pizza1)
    
    print(carte.is_empty())  # False
    print(carte.nb_pizzas())  # 1
    
    carte.remove_pizza("Margherita")
    print(carte.is_empty())  # True
