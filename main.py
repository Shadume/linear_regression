import streamlit as st
from price_calc import price_calc
from sklearn.linear_model import LinearRegression
import pickle

with open('modele.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Estimation du prix d'une voiture")

marque = st.selectbox(
    'Marque',
    ('Alfa-Romeo', 'Audi', 'BMW', 'Chevrolet', 'Dodge', 'Honda', 'Isuzu', 'Jaguar', 'Mazda', 'Buick', 'Mercury', 'Mitsubishi', 'Nissan', 'Peugeot', 'Plymouth', 'Porsche', 'Renault', 'Saab', 'Subaru', 'Toyota', 'Volkswagen', 'Volvo'))
modele = st.text_input("Modèle")
carburant = st.selectbox(
    'Carburant',
    ('Gazole', 'Diesel')
)
turbo = st.radio(
    "Turbo",
    ('Sans', 'Avec'))
type_vehicule = st.selectbox(
    'Type de véhicule',
    ('Berline', 'Cabriolet', 'Voiture à hayon', 'Van', 'Cabriolet avec toit rigide')
)
roues_motrices = st.selectbox(
    'Roues motrices',
    ('traction', 'propulsion', '4x4')
)
emplacement_moteur = st.radio(
    "Emplacement du moteur",
    ('Avant', 'Arrière'))
empattement = st.number_input('Empattement (cm)')
longueur = st.number_input('Longueur (cm)')
largeur = st.number_input('Largeur (cm)')
hauteur = st.number_input('Hauteur (cm)')
poids = st.number_input('Poids (kg)')
type_moteur = st.selectbox(
    "Type de moteur",
    ('dohc', 'ohcv', 'ohc', 'l', 'rotor', 'ohcf', 'dohcv')
)
nombre_cylindres = st.number_input('Nombre de cylindres')
taille_moteur = st.number_input('Taille du moteur (cm3)')
systeme_carburant = st.selectbox(
    "Système d'alimentation en carburant",
    ('mpfi', '2bbl', 'mfi', '1bbl', 'spfi', '4bbl', 'idi', 'spdi')
)
taux_alesage = st.number_input("Taux d'alésage du moteur (mm)")
chevaux = st.number_input('Chevaux')
consommation_ville = st.number_input('Consommation en ville (l/100)')
consommation_autoroute = st.number_input('Consommation sur autoroute (l/100)')



if st.button("Estimer le prix"):
    marque_dict = {
        'Alfa-Romeo' : 0,
        'Audi' : 1,
        'BMW' : 2,
        'Chevrolet' : 3,
        'Dodge' : 4,
        'Honda' : 5,
        'Isuzu' : 6,
        'Jaguar' : 7,
        'Mazda' : 8,
        'Buick' : 9,
        'Mercury' : 10,
        'Mitsubishi' : 11,
        'Nissan' : 12,
        'Peugeot' :13,
        'Plymouth' :14,
        'Porsche' :15,
        'Renault' :16,
        'Saab' :17,
        'Subaru' :18,
        'Toyota' :19,
        'Volkswagen' :20,
        'Volvo':21
}
    marque_modif = marque_dict.get(marque)
    carburant_dict = {'Gazole':'0', 'Diesel':'1'}
    carburant = carburant_dict.get(carburant)
    turbo_dict = {'Avec': '1', 'Sans': '0'}
    turbo = turbo_dict.get(turbo)
    vehicule_dict = {'Berline' : '2', 'Cabriolet' : '0', 'Voiture à hayon' : '1', 'Van' : '3', 'Cabriolet avec toit rigide' : '4'}
    type_vehicule = vehicule_dict.get(type_vehicule)
    roues_dict = {'traction' : '2', 'propulsion' : '0', '4x4': '1'}
    roues_motrices = roues_dict.get(roues_motrices)
    empmoteur_dict = {'Avant' : '0', 'Arrière' : '1'}
    emplacement_moteur = empmoteur_dict.get(emplacement_moteur)
    typemoteur_dict = {'dohc' : 0, 'ohcv' : 1, 'ohc' : 2, 'l' : 3, 'rotor' : 4, 'ohcf' : 5, 'dohcv' : 6}
    type_moteur = typemoteur_dict.get(type_moteur)
    syscarbu_dict = {'mpfi' : 0, '2bbl' : 1, 'mfi' : 2, '1bbl' : 3, 'spfi' : 4, '4bbl' : 5, 'idi' : 6, 'spdi' : 7}
    systeme_carburant = syscarbu_dict.get(systeme_carburant)
    price = price_calc(model, carburant, turbo, type_vehicule, roues_motrices, emplacement_moteur, empattement, longueur, largeur, hauteur, poids, type_moteur, nombre_cylindres, taille_moteur, systeme_carburant, taux_alesage, chevaux, consommation_ville, consommation_autoroute, marque_modif)
    st.success(f"Le prix estimé de la voiture {marque} {modele} est de {price} euros")