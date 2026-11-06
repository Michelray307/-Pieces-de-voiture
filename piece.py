class PieceSimple:
    """Une pièce qu'on ne peut pas décomposer davantage."""
    def __init__(self, nom: str, prix: float):
        self.nom = nom
        self.prix = prix


class SousSysteme:
    """Un assemblage de pièces simples."""
    def __init__(self, nom: str):
        self.nom = nom
        self.pieces: list[PieceSimple] = []

    def ajouter_piece(self, piece: PieceSimple) -> None:
        self.pieces.append(piece)

    def prix_total(self) -> float:
        return sum(p.prix for p in self.pieces)

    def nb_pieces(self) -> int:
        return len(self.pieces)


class Voiture:
    """Un assemblage de sous-systèmes."""
    def __init__(self, nom: str):
        self.nom = nom
        self.sous_systemes: list[SousSysteme] = []

    def ajouter_sous_systeme(self, ss: SousSysteme) -> None:
        self.sous_systemes.append(ss)

    def prix_total(self) -> float:
        total = 0.0
        for ss in self.sous_systemes:
            for piece in ss.pieces:
                total += piece.prix
        return total

    def nb_pieces(self) -> int:
        count = 0
        for ss in self.sous_systemes:
            count += len(ss.pieces)
        return count

    def afficher(self) -> None:
        print(f"Voiture : {self.nom}")
        for ss in self.sous_systemes:
            print(f"  [{ss.nom}]")
            for piece in ss.pieces:
                print(f"    {piece.nom} ({piece.prix:.2f} $)")