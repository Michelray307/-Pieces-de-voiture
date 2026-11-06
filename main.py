from composite import Voiture, Assemblage
from feuille import Piece

# Pièces atomiques
bloc_moteur = Piece("Bloc moteur", 1200.00)
pistons = Piece("Pistons (x4)", 320.00)
joint = Piece("Joint de culasse", 85.00)
injecteur_1 = Piece("Injecteur 1", 210.00)
injecteur_2 = Piece("Injecteur 2", 210.00)
rampe = Piece("Rampe d'injection", 145.00)

# Sous-assemblage dans un sous-assemblage
injection = Assemblage("Système d'injection")
injection.ajouter(rampe)
injection.ajouter(injecteur_1)
injection.ajouter(injecteur_2)

moteur = Assemblage("Moteur")
moteur.ajouter(bloc_moteur)
moteur.ajouter(pistons)
moteur.ajouter(joint)
moteur.ajouter(injection)   # ← un assemblage dans un assemblage

disques = Piece("Disques avant (x2)", 180.00)
plaquettes = Piece("Plaquettes avant (x4)", 60.00)
maitre_cylindre = Piece("Maître-cylindre", 95.00)

freins = Assemblage("Système de freinage")
freins.ajouter(disques)
freins.ajouter(plaquettes)
freins.ajouter(maitre_cylindre)

ma_voiture = Voiture("Honda Civic 2024")
ma_voiture.ajouter(moteur)
ma_voiture.ajouter(freins)

print(f"Prix total : {ma_voiture.prix_total():.2f} $")
print(f"Nombre de pièces : {ma_voiture.nb_pieces()}")
ma_voiture.afficher()