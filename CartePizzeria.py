

class Pizza:
    def __init__(self,nom,prix,description,ingredients,indicationBase):
        self.nom = nom
        self.prix = prix
        self.description = description
        self.ingredients = ingredients
        self.indicationBase = indicationBase

class Boisson:
     def __init__(self,nom,prix,indicationAlcool):
        self.nom = nom
        self.prix = prix
        self.indicationAlcool = indicationAlcool

class Dessert:
    def __init__(self,nom,prix,ingredients,indicationMaison):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.indicationMaison = indicationMaison

class CartePizzeria:
    def __init__(self):
        self.pizzas = {}
        self.boissons = {}
        self.desserts = {}

    def is_empty(self):
        return len(self.pizzas) == 0 and len(self.boissons) == 0 and len(self.desserts) == 0
    
    def nb_pizzas(self):
        return len(self.pizzas)
    
    def nb_drinks(self):
        return len(self.boissons)
    
    def nb_desserts(self):
        return len(self.desserts)
    
    def add(self,element):
        if isinstance(element, Pizza):
            if any(pizza == element for pizza in self.pizzas):
                raise CartePizzeriaException(f"La pizza '{element.nom}' est déjà présente dans la carte.")
            self.pizzas[element.nom] = element

        if isinstance(element, Boisson):
            if any(boisson == element for boisson in self.boissons):
                raise CartePizzeriaException(f"Le boisson '{element.nom}' est déjà présente dans la carte.")
            self.boissons[element.nom] = element
        if isinstance(element, Dessert):
            if any(dessert == element for dessert in self.desserts):
                raise CartePizzeriaException(f"Le dessert '{element.nom}' est déjà présente dans la carte.")
            self.desserts[element.nom] = element 

    def remove(self,nom):
        if nom in self.pizzas:
            del self.pizzas[nom]

        elif nom in self.boissons: 
            del self.boissons[nom]

        elif nom in self.desserts: 
            del self.desserts[nom]

        else: 
            raise CartePizzeriaException(f"L'element {nom} n'existe pas dans la carte")

class CartePizzeriaException(Exception):
    pass


if __name__ == "__main__":

    pizza1 = Pizza("Margarita", 8.5, "Tomate, mozzarella", ["tomate", "mozzarella"], "tomate")
    boisson1 = Boisson("Coca-Cola", 2.5, False)
    dessert1 = Dessert("Tiramisu", 5.0, ["mascarpone", "café"], True)
    
    carte = CartePizzeria()
    print(carte.is_empty())  # True
    
    carte.add(pizza1)
    carte.add(boisson1)
    carte.add(dessert1)
    
    print(carte.is_empty())  # False
    print(carte.nb_pizzas()) # 1
    print(carte.nb_drinks()) # 1
    print(carte.nb_desserts())  # 1
    
    carte.remove("Tiramisu")
    print(carte.nb_desserts())  # 0

    carte.remove("Coca-Cola")
    carte.remove("Margarita")
    print(carte.is_empty())  # True

