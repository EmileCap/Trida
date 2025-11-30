-- DROP
DROP TABLE IF EXISTS passe;
DROP TABLE IF EXISTS depose;
DROP TABLE IF EXISTS charge;
DROP TABLE IF EXISTS planning;
DROP TABLE IF EXISTS horaire_lieu_de_collecte;
DROP TABLE IF EXISTS horaire_centre_tri;
DROP TABLE IF EXISTS distance;
DROP TABLE IF EXISTS camion;
DROP TABLE IF EXISTS conteneur;
DROP TABLE IF EXISTS modele;
DROP TABLE IF EXISTS centre_tri;
DROP TABLE IF EXISTS lieux_collecte;
DROP TABLE IF EXISTS horaire;
DROP TABLE IF EXISTS saison;
DROP TABLE IF EXISTS jour;
DROP TABLE IF EXISTS localisation;
DROP TABLE IF EXISTS couleur;
DROP TABLE IF EXISTS type_dechet;
DROP TABLE IF EXISTS marque;
DROP TABLE IF EXISTS conducteur;


-- Creation des tables
CREATE TABLE conducteur(
   id_conducteur INT AUTO_INCREMENT,
   Nom_conducteur VARCHAR(50),
   prenom_conducteur VARCHAR(50),
   PRIMARY KEY(id_conducteur)
);

CREATE TABLE type_dechet(
   id_type_dechet INT AUTO_INCREMENT,
   nom_dechet VARCHAR(50),
   PRIMARY KEY(id_type_dechet)
);

CREATE TABLE marque(
   id_marque INT AUTO_INCREMENT,
   nom_marque VARCHAR(50),
   PRIMARY KEY(id_marque)
);

CREATE TABLE couleur(
   id_couleur INT AUTO_INCREMENT,
   nom_couleur VARCHAR(50),
   correspond VARCHAR(50),
   PRIMARY KEY(id_couleur)
);

CREATE TABLE localisation(
   id_localisation INT AUTO_INCREMENT,
   latitude DOUBLE,
   longitude DOUBLE,
   adresse VARCHAR(50),
   PRIMARY KEY(id_localisation)
);

CREATE TABLE saison(
   id_Saison INT AUTO_INCREMENT,
   libelle VARCHAR(50),
   PRIMARY KEY(id_Saison)
);

CREATE TABLE jour(
   id_jour INT AUTO_INCREMENT,
   ajouter_jour VARCHAR(50),
   PRIMARY KEY(id_jour)
);

CREATE TABLE conteneur(
   id_conteneur INT AUTO_INCREMENT,
   capacite_max CHAR(50),
   id_localisation INT NOT NULL,
   date_creation DATE,
   id_couleur INT NOT NULL,
   id_type_dechet INT NOT NULL,
   PRIMARY KEY(id_conteneur),
   CONSTRAINT conteneur_localisation_id FOREIGN KEY(id_localisation) REFERENCES localisation(id_localisation),
   CONSTRAINT couleur_id FOREIGN KEY(id_couleur) REFERENCES couleur(id_couleur),
   CONSTRAINT type_dechet_id FOREIGN KEY(id_type_dechet) REFERENCES type_dechet(id_type_dechet)
);

CREATE TABLE centre_tri(
   id_centre_de_tri INT AUTO_INCREMENT,
   libelle_centre_de_tri VARCHAR(50),
   id_localisation INT NOT NULL,
   PRIMARY KEY(id_centre_de_tri),
   CONSTRAINT centre_tri_localisation_id FOREIGN KEY(id_localisation) REFERENCES localisation(id_localisation)
);

CREATE TABLE lieux_collecte(
   id_lieu_de_collecte INT AUTO_INCREMENT,
   libelle_lieu_de_collecte VARCHAR(50),
   id_localisation INT NOT NULL,
   PRIMARY KEY(id_lieu_de_collecte),
   CONSTRAINT lieux_collecte_localisation_id FOREIGN KEY(id_localisation) REFERENCES localisation(id_localisation)
);

CREATE TABLE modele(
   id_modele INT AUTO_INCREMENT,
   nom_modele VARCHAR(50),
   poids INT,
   capacité_de_conteneur VARCHAR(50),
   poids_max VARCHAR(50),
   consommation_moyenne INT,
   hauteur INT,
   id_marque INT NOT NULL,
   PRIMARY KEY(id_modele),
   CONSTRAINT marque_id FOREIGN KEY(id_marque) REFERENCES marque(id_marque)
);

CREATE TABLE horaire(
   id_horaire INT AUTO_INCREMENT,
   ouverture TIME,
   fermeture TIME,
   id_saison INT NOT NULL,
   id_jour INT NOT NULL,
   PRIMARY KEY(id_horaire),
   CONSTRAINT saison_id FOREIGN KEY(id_saison) REFERENCES saison(Id_Saison),
   CONSTRAINT jour_id FOREIGN KEY(id_jour) REFERENCES jour(id_jour)
);

CREATE TABLE camion(
   id_camion INT AUTO_INCREMENT,
   kilometrage INT,
   date_de_mise_en_service VARCHAR(50),
   id_localisation INT NOT NULL,
   id_modele INT NOT NULL,
   id_conducteur INT NOT NULL,
   PRIMARY KEY(id_camion),
   CONSTRAINT camion_localisation_id FOREIGN KEY(id_localisation) REFERENCES localisation(id_localisation),
   CONSTRAINT modele_id FOREIGN KEY(id_modele) REFERENCES modele(id_modele),
   CONSTRAINT conducteur_id FOREIGN KEY(id_conducteur) REFERENCES conducteur(id_conducteur)
);

CREATE TABLE planning(
   id_tournee INT AUTO_INCREMENT,
   date_de_la_tournee DATE,
   id_centre_de_tri INT NOT NULL,
   id_camion INT NOT NULL,
   PRIMARY KEY(id_tournee),
   CONSTRAINT centre_tri_id FOREIGN KEY(id_centre_de_tri) REFERENCES centre_tri(id_centre_de_tri),
   CONSTRAINT camion_id FOREIGN KEY(id_camion) REFERENCES camion(id_camion)
);

CREATE TABLE charge(
   id_camion INT,
   id_conteneur INT,
   date_charge VARCHAR(50),
   poids_mesure VARCHAR(50),
   PRIMARY KEY(id_camion, id_conteneur),
   CONSTRAINT charge_camion_id FOREIGN KEY(id_camion) REFERENCES camion(id_camion),
   CONSTRAINT charge_conducteur_id FOREIGN KEY(id_conteneur) REFERENCES conteneur(id_conteneur)
);

CREATE TABLE depose(
   id_camion INT,
   id_centre_de_tri INT,
   PRIMARY KEY(id_camion, id_centre_de_tri),
   CONSTRAINT depose_camion_id FOREIGN KEY(id_camion) REFERENCES camion(id_camion),
   CONSTRAINT depose_centre_tri_id FOREIGN KEY(id_centre_de_tri) REFERENCES centre_tri(id_centre_de_tri)
);

CREATE TABLE passe(
   id_lieu_de_collecte INT,
   id_tournee INT,
   ordre_passage VARCHAR(50),
   PRIMARY KEY(id_lieu_de_collecte, id_tournee),
   CONSTRAINT passe_lieu_de_collecte_id FOREIGN KEY(id_lieu_de_collecte) REFERENCES lieux_collecte(id_lieu_de_collecte),
   CONSTRAINT passe_tournee_id FOREIGN KEY(id_tournee) REFERENCES planning(id_tournee)
);

CREATE TABLE horaire_centre_tri (
   id_centre_de_tri INT,
   id_horaire INT,
   PRIMARY KEY(id_centre_de_tri, id_horaire),
   CONSTRAINT horaire_centre_tri_id FOREIGN KEY(id_centre_de_tri) REFERENCES centre_tri(id_centre_de_tri),
   CONSTRAINT id_centre_de_tri_horaire FOREIGN KEY(id_horaire) REFERENCES horaire(id_horaire)
);

CREATE TABLE horaire_lieu_de_collecte (
   id_lieu_de_collecte INT,
   id_horaire INT,
   PRIMARY KEY(id_lieu_de_collecte, id_horaire),
   CONSTRAINT horaire_lieu_de_collecte_id FOREIGN KEY(id_lieu_de_collecte) REFERENCES lieux_collecte(id_lieu_de_collecte),
   CONSTRAINT id_lieu_de_collecte_horaire FOREIGN KEY(id_horaire) REFERENCES horaire(id_horaire)
);

CREATE TABLE distance(
   id_localisation INT,
   id_localisation_1 INT,
   PRIMARY KEY(id_localisation, id_localisation_1),
   CONSTRAINT distance_localisation_id FOREIGN KEY(id_localisation) REFERENCES localisation(id_localisation),
   CONSTRAINT distance_localisation1_id FOREIGN KEY(id_localisation_1) REFERENCES localisation(id_localisation)
);


-- INSERT
INSERT INTO conducteur (id_conducteur, Nom_conducteur, prenom_conducteur) VALUES
(NULL, 'Martin', 'Lucas'),
(NULL, 'Satler', 'Hans'),
(NULL, 'Börer', 'Monique'),
(NULL, 'Durand', 'Sophie');

INSERT INTO type_dechet (id_type_dechet, nom_dechet) VALUES
(NULL, 'Plastique'),
(NULL, 'Verre'),
(NULL, 'Papier'),
(NULL, 'Métal'),
(NULL, 'Carton');

INSERT INTO marque (id_marque, nom_marque) VALUES
(NULL, 'Renault Trucks'),
(NULL, 'Volvo');

INSERT INTO couleur (id_couleur, nom_couleur, correspond) VALUES
(NULL, 'Vert', 'Verre'),
(NULL, 'Jaune', 'Plastique'),
(NULL, 'Bleu', 'Papier'),
(NULL, 'Rouge', 'Métal'),
(NULL, 'Marron', 'Carton');

INSERT INTO localisation (id_localisation, latitude, longitude, adresse) VALUES
(NULL, 48.8566, 2.3522, 'Paris Centre'),
(NULL, 48.8600, 2.3400, 'Rue des Artisans'),
(NULL, 48.8700, 2.3300, 'Boulevard Vert'),
(NULL, 48.8750, 2.3350, 'Place des Fleurs'),
(NULL, 48.8650, 2.3450, 'Avenue des Champs'),
(NULL, 48.8550, 2.3600, 'Rue du Commerce'),
(NULL, 48.8580, 2.3420, 'Place de la République'),
(NULL, 48.8620, 2.3480, 'Rue Saint-Honoré'),
(NULL, 48.8670, 2.3550, 'Boulevard Haussmann'),
(NULL, 48.8530, 2.3490, 'Place Vendôme');

INSERT INTO saison (id_Saison, libelle) VALUES
(NULL, 'Été'),
(NULL, 'Hiver'),
(NULL, 'Printemps'),
(NULL, 'Automne');

INSERT INTO jour (id_jour, ajouter_jour) VALUES
(NULL, 'Lundi'),
(NULL, 'Mardi'),
(NULL, 'Mercredi'),
(NULL, 'Jeudi'),
(NULL, 'Vendredi');

INSERT INTO conteneur (id_conteneur, capacite_max, id_localisation, date_creation, id_couleur, id_type_dechet)  VALUES
(NULL, '120L', 1, '2021-01-10', 1, 2),
(NULL, '150L', 1, '2021-02-12', 2, 1),
(NULL, '180L', 3, '2021-03-15', 3, 3),
(NULL, '200L', 4, '2021-04-18', 4, 4),
(NULL, '240L', 5, '2021-05-20', 5, 5),
(NULL, '120L', 6, '2021-06-22', 1, 2),
(NULL, '150L', 7, '2021-07-25', 2, 1),
(NULL, '180L', 8, '2021-08-28', 3, 3),
(NULL, '200L', 9, '2021-09-30', 4, 4),
(NULL, '240L', 10, '2021-10-02', 5, 5),
(NULL, '120L', 1, '2021-11-05', 1, 2),
(NULL, '150L', 2, '2021-12-08', 2, 1),
(NULL, '180L', 3, '2022-01-10', 3, 3),
(NULL, '200L', 4, '2022-02-12', 4, 4),
(NULL, '240L', 5, '2022-03-15', 5, 5),
(NULL, '120L', 6, '2022-04-18', 1, 2),
(NULL, '150L', 7, '2022-05-20', 2, 1),
(NULL, '180L', 8, '2022-06-22', 3, 3),
(NULL, '200L', 9, '2022-07-25', 4, 4),
(NULL, '240L', 10, '2022-08-28', 5, 5);

INSERT INTO centre_tri (id_centre_de_tri, libelle_centre_de_tri, id_localisation) VALUES
(NULL, 'Centre Nord', 1),
(NULL, 'Centre Sud', 2);

INSERT INTO lieux_collecte (id_lieu_de_collecte, libelle_lieu_de_collecte, id_localisation) VALUES
(NULL, 'Place A', 1),
(NULL, 'Place B', 2),
(NULL, 'Place C', 3);

INSERT INTO modele (id_modele, nom_modele, poids, capacité_de_conteneur, poids_max, consommation_moyenne, hauteur, id_marque) VALUES
(NULL, 'EcoTruck 3000', 3500, '10m3', '5000kg', 20, 250, 1),
(NULL, 'GreenHauler X', 4200, '12m3', '6000kg', 22, 260, 2);

INSERT INTO horaire (id_horaire, ouverture, fermeture, id_saison, id_jour) VALUES
(NULL, '08:00:00', '16:00:00', 1, 1),
(NULL, '09:00:00', '17:00:00', 2, 2),
(NULL, '07:00:00', '15:00:00', 1, 3);

INSERT INTO  camion (id_camion, kilometrage, date_de_mise_en_service, id_localisation, id_modele, id_conducteur) VALUES
(NULL, 150000, '2018-03-12', 1, 1, 1),
(NULL, 90000, '2020-06-20', 2, 2, 2);

INSERT INTO planning (id_tournee, date_de_la_tournee, id_centre_de_tri, id_camion) VALUES
(NULL, '2024-02-01', 1, 1),
(NULL, '2024-02-02', 2, 2);

INSERT INTO charge (id_camion, id_conteneur, date_charge, poids_mesure) VALUES
(1, 1, '2024-02-01', '120kg'),
(1, 2, '2024-02-01', '150kg'),
(2, 3, '2024-02-02', '200kg');

INSERT INTO depose (id_camion, id_centre_de_tri) VALUES
(1, 1),
(2, 2);

INSERT INTO passe (id_lieu_de_collecte, id_tournee, ordre_passage) VALUES
(1, 1, '1'),
(2, 1, '2'),
(3, 2, '1');

INSERT INTO horaire_centre_tri (id_centre_de_tri, id_horaire) VALUES
(1, 1),
(1, 3),
(2, 2);

INSERT INTO horaire_lieu_de_collecte (id_lieu_de_collecte, id_horaire) VALUES
(1, 1),
(2, 2),
(3, 3);

INSERT INTO distance (id_localisation, id_localisation_1) VALUES
(1, 2),
(2, 3),
(1, 3);


-- Test fetch
SELECT conducteur.Nom_conducteur, camion.kilometrage, camion.date_de_mise_en_service, modele.nom_modele, localisation.adresse
FROM camion
LEFT JOIN localisation ON camion.id_localisation = localisation.id_localisation
LEFT JOIN modele ON camion.id_modele = modele.id_modele
LEFT JOIN  conducteur ON camion.id_conducteur = conducteur.id_conducteur;

SELECT COUNT(conteneur.id_conteneur) AS Total, couleur.nom_couleur
FROM conteneur
INNER JOIN couleur ON conteneur.id_couleur = couleur.id_couleur
GROUP BY couleur.nom_couleur
ORDER BY couleur.nom_couleur ASC;

SELECT AVG(conteneur.capacite_max) AS capacite_moyenne_par_couleur,couleur.nom_couleur
FROM conteneur
INNER JOIN couleur ON conteneur.id_couleur = couleur.id_couleur
GROUP BY couleur.nom_couleur
ORDER BY couleur.nom_couleur ASC;

SELECT
couleur.nom_couleur,
COUNT(conteneur.id_conteneur) AS total_conteneurs,
AVG(conteneur.capacite_max) AS capacite_moyenne
FROM conteneur
INNER JOIN couleur ON conteneur.id_couleur = couleur.id_couleur
GROUP BY couleur.nom_couleur
ORDER BY couleur.nom_couleur;


SELECT AVG(conteneur.capacite_max) AS capacite_moyenne_de_tous_les_conteneurs
FROM conteneur
INNER JOIN couleur ON conteneur.id_couleur = couleur.id_couleur
WHERE couleur.nom_couleur='rouge';



SELECT AVG(conteneur.capacite_max) AS capacite_moyenne_de_tous_les_conteneurs
FROM conteneur;

SELECT * FROM conteneur
WHERE capacite_max > (SELECT AVG(capacite_max)FROM conteneur);

SELECT COUNT(conteneur.id_conteneur) AS Total_conteneur_par_type_dechet, type_dechet.nom_dechet
FROM conteneur
INNER JOIN type_dechet ON conteneur.id_couleur = type_dechet.id_type_dechet
GROUP BY nom_dechet
ORDER BY type_dechet.nom_dechet ASC;

SELECT COUNT(type_dechet.id_type_dechet) AS Total_type_dechet_par_couleur, couleur.id_couleur
FROM type_dechet
INNER JOIN type_dechet ON couleur.id_couleur = couleur.id_type_dechet
GROUP BY nom_couleur
ORDER BY type_dechet.nom_dechet ASC;

SELECT MIN(conteneur.capacite_max) AS capacite_minmun,
        MAX(conteneur.capacite_max) AS capacite_maximun
FROM conteneur;

SELECT couleur.nom_couleur,
MIN(capacite_max) AS capacite_minimun_par_couleur,
MAX(capacite_max) AS capacite_maximun_par_couleur
FROM conteneur
INNER JOIN couleur ON conteneur.id_couleur = couleur.id_couleur
GROUP BY couleur.nom_couleur;

SELECT type_dechet.nom_dechet,
MIN(capacite_max) AS capacite_minimun_par_type_dechet,
MAX(capacite_max) AS capacite_minimun_par_type_dechet
FROM conteneur
INNER JOIN type_dechet ON conteneur.id_type_dechet = type_dechet.id_type_dechet
GROUP BY type_dechet.nom_dechet;



