from abc import ABC, abstractmethod

class Feuille(ABC):
    pass

class Piece(Feuille):
    def __init__(self, nom: str, prix: float):
        self.nom = nom
        self.prix = prix

    def prix_total(self) -> float:
        return self.prix

    def nb_pieces(self) -> int:
        return 1

    def afficher(self, prefix: str = "") -> None:
        print(f"{prefix}{self.nom} - Prix: {self.prix}")