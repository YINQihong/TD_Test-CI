

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
            if element.nom in self.pizzas:
                raise CartePizzeriaException(f"La pizza '{element.nom}' est déjà présente dans la carte.")
            self.pizzas[element.nom] = element

        if isinstance(element, Boisson):
            if element.nom in self.boissons:
                raise CartePizzeriaException(f"Le boisson '{element.nom}' est déjà présente dans la carte.")
            self.boissons[element.nom] = element
        if isinstance(element, Dessert):
            if element.nom in self.desserts:
                raise CartePizzeriaException(f"Le dessert '{element.nom}' est déjà présente dans la carte.")
            self.desserts[element.nom] = element 

    def remove(self, nom):
        for collection in [self.pizzas, self.boissons, self.desserts]:
            if nom in collection:
                del collection[nom]
            return  # Suppression réussie
        raise CartePizzeriaException(f"L'élément '{nom}' n'existe pas dans la carte.")

class CartePizzeriaException(Exception):
    pass