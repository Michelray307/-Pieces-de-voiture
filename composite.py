from composant import Composant

class Composite(Composant):
    def __init__(self, nom: str):
        super().__init__(nom)
        self.composants = []

    def ajouter(self, composant: Composant) -> None:
        self.composants.append(composant)

    def prix_total(self) -> float:
        return sum(composant.prix_total() for composant in self.composants)

    def nb_pieces(self) -> int:
        return sum(composant.nb_pieces() for composant in self.composants)

    def afficher(self, prefix: str = "") -> None:
        print(f"{prefix}{self.nom} (Composite)")
        for composant in self.composants:
            composant.afficher(prefix + "  ")


class Assemblage(Composite):
    """Un assemblage de pièces et/ou d'autres assemblages."""
    def __init__(self, nom: str):
        super().__init__(nom)

class Voiture(Composite):
    """Une voiture composée de sous-systèmes."""
    def __init__(self, nom: str):
        super().__init__(nom)

