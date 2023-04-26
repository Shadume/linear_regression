import numpy as np

def price_calc(model, carburant, turbo, type_vehicule, roues_motrices, emplacement_moteur, empattement, longueur, largeur, hauteur, poids, type_moteur, nombre_cylindres, taille_moteur, systeme_carburant, taux_alesage, chevaux, consommation_ville, consommation_autoroute, marque):
    x = np.array([carburant, turbo, type_vehicule, roues_motrices, emplacement_moteur, empattement, longueur, largeur, hauteur, poids, type_moteur, nombre_cylindres, taille_moteur, systeme_carburant, taux_alesage, chevaux, consommation_ville, consommation_autoroute, marque]).reshape(1, 19)
    price = model.predict(x)
    return int(price)
