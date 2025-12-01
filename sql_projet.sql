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
DROP TABLE IF EXISTS horaire;
DROP TABLE IF EXISTS lieux_collecte;

#DROP TABLE IF EXISTS saison;
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
   id_lieu_de_collecte INT NOT NULL,
   id_jour INT NOT NULL,

   PRIMARY KEY(id_horaire),
   #UNIQUE KEY uk_horaire_saison (id_saison, id_jour),
   #NIQUE KEY uk_horaire_jour(id_jour, id_lieu_de_collecte),
   #FOREIGN KEY (id_saison) REFERENCES saison(id_saison),
   FOREIGN KEY (id_jour) REFERENCES jour(id_jour),
   FOREIGN KEY (id_lieu_de_collecte) REFERENCES lieux_collecte(id_lieu_de_collecte)

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

CREATE TABLE distance(
    valeur FLOAT,
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
(NULL, 'Volvo'),
(NULL, 'Iveco'),
(NULL, 'Mercedes-Benz'),
(NULL, 'Scania');

INSERT INTO couleur (id_couleur, nom_couleur, correspond) VALUES
(NULL, 'Vert', 'Verre'),
(NULL, 'Jaune', 'Plastique'),
(NULL, 'Bleu', 'Papier'),
(NULL, 'Rouge', 'Métal'),
(NULL, 'Marron', 'Carton');

INSERT INTO localisation (id_localisation, latitude, longitude, adresse)
VALUES
    (1, 47.6397, 6.8645, '1 Rue de la République, Belfort'),
    (2, 47.6354, 6.8612, '15 Avenue Jean Jaurès, Belfort'),
    (3, 47.6389, 6.8678, '5 Place de la Gare, Belfort'),
    (4, 47.6321, 6.8598, '10 Rue du Docteur Fréry, Belfort'),
    (5, 47.6405, 6.8693, '22 Boulevard Anatole France, Belfort'),
    (6, 47.6372, 6.8631, '7 Rue de Mulhouse, Belfort'),
    (7, 47.6345, 6.8587, '3 Rue du Général de Gaulle, Belfort'),
    (8, 47.6412, 6.8705, '18 Rue de la Préfecture, Belfort'),
    (9, 47.6368, 6.8654, '9 Rue du Lycée, Belfort'),
    (10, 47.6333, 6.8576, '12 Rue des Jardins, Belfort'),
    (11, 47.6420, 6.8718, '25 Rue de la République, Danjoutin'),
    (12, 47.6310, 6.8565, '8 Rue de la Gare, Valdoie'),
    (13, 47.6435, 6.8730, '14 Rue du Stade, Bavilliers'),
    (14, 47.6298, 6.8552, '5 Rue des Écoles, Offemont'),
    (15, 47.6448, 6.8742, '19 Rue de la Mairie, Essert'),
    (16, 47.6285, 6.8540, '11 Rue des Vignes, Pérouse'),
    (17, 47.6460, 6.8755, '2 Rue du Château, Chèvremont'),
    (18, 47.6272, 6.8528, '16 Rue des Prés, Sevenans'),
    (19, 47.6472, 6.8768, '3 Rue de la Forêt, Andelnans'),
    (20, 47.6259, 6.8516, '20 Rue des Fleurs, Argiésans');





INSERT INTO jour (id_jour, ajouter_jour) VALUES
(NULL, 'lundi'),
(NULL, 'mardi'),
(NULL, 'mercredi'),
(NULL, 'jeudi'),
(NULL, 'vendredi'),
(NULL, 'samedi'),
(NULL, 'dimanche');


INSERT INTO conteneur (id_conteneur, capacite_max, id_localisation, date_creation, id_couleur, id_type_dechet) VALUES
(NULL, '123.5L', 1, '2021-04-17', 2, 4),
(NULL, '178.3L', 1, '2022-08-02', 1, 2),
(NULL, '201.7L', 1, '2022-01-23', 4, 1),
(NULL, '145.9L', 2, '2021-12-11', 3, 5),
(NULL, '232.4L', 2, '2022-06-19', 2, 3),
(NULL, '198.6L', 2, '2021-03-05', 5, 2),
(NULL, '215.2L', 2, '2022-09-30', 1, 4),
(NULL, '167.8L', 3, '2021-07-22', 4, 3),
(NULL, '241.0L', 3, '2022-02-14', 3, 1),
(NULL, '134.5L', 3, '2021-05-28', 2, 5),
(NULL, '189.7L', 5, '2022-11-08', 1, 2),
(NULL, '223.9L', 5, '2021-08-16', 5, 4),
(NULL, '156.3L', 6, '2022-04-03', 3, 3),
(NULL, '208.4L', 6, '2021-10-25', 2, 1),
(NULL, '198.1L', 6, '2022-07-12', 4, 5),
(NULL, '176.5L', 6, '2021-06-30', 1, 2),
(NULL, '239.8L', 8, '2022-03-19', 5, 3),
(NULL, '142.6L', 9, '2021-09-14', 3, 4),
(NULL, '211.2L', 9, '2022-12-01', 2, 1),
(NULL, '125.4L', 16, '2021-11-20', 4, 5);



INSERT INTO centre_tri (id_centre_de_tri, libelle_centre_de_tri, id_localisation)
VALUES
    (1, 'Centre de Tri de Belfort Nord', 17),
    (2, 'ÉcoCentre de Valdoie', 18),
    (3, 'Tri’Est - Bavilliers', 19),
    (4, 'Pôle Recyclage du Pays de Belfort', 20);


INSERT INTO lieux_collecte (id_lieu_de_collecte, libelle_lieu_de_collecte, id_localisation)
VALUES
    (1, 'ÉcoPoint', 1),
    (2, 'Recycl’Ville', 2),
    (3, 'Déchet’Rie', 3),
    (4, 'Vert’Collecte', 4),
    (5, 'Tri’Top', 5),
    (6, 'La Boîte à Tout', 6),
    (7, 'ReSource', 7),
    (8, 'Le Relais Vert', 8),
    (9, 'Collect’R', 9),
    (10, 'ZéroDéchet', 10),
    (11, 'Tri’Mobil', 11),
    (12, 'L’Atelier du Réemploi', 12),
    (13, 'La Mine Urbaine', 13),
    (14, 'Le Comptoir du Tri', 14),
    (15, 'ReCyclea', 15),
    (16, 'L’Escale Verte', 16);


INSERT INTO modele (id_modele, nom_modele, poids, capacité_de_conteneur, poids_max, consommation_moyenne, hauteur, id_marque) VALUES
(NULL, 'EcoTruck 3000', 3500, '10m3', '5000kg', 20, 250, 1),
(NULL, 'GreenHauler X', 4200, '12m3', '6000kg', 22, 260, 2),
(NULL, 'UrbanCleaner 220', 3300, '8m3', '4500kg', 18, 240, 3),
(NULL, 'Reiser Abfall', 5000, '14m3', '7000kg', 25, 275, 4),
(NULL, 'CityRunner S', 3600, '9m3', '4800kg', 19, 248, 3),
(NULL, 'Volvo Recycle Pro', 4700, '13m3', '6500kg', 23, 265, 2),
(NULL, 'Renault CleanMaster', 3900, '11m3', '5500kg', 21, 255, 1),
(NULL, 'Grün Müllwagen', 3000, '7m3', '4000kg', 17, 235, 4),
(NULL, 'GreenCompact 150', 5000, '14m3', '4500kg', 18, 260, 5);

-- Horaires pour les lieux de collecte (id_lieu_de_collecte de 1 à 10)
INSERT INTO horaire (id_horaire, ouverture, fermeture, id_jour, id_lieu_de_collecte) VALUES
-- ÉcoPoint (id_lieu_de_collecte = 1)
(NULL, '08:00:00', '18:00:00', 1, 1),  -- Lundi
(NULL, '08:00:00', '16:00:00', 3, 1),  -- Mercredi
(NULL, '09:00:00', '12:00:00', 6, 1),  -- Samedi

-- Recycl’Ville (id_lieu_de_collecte = 2)
(NULL, '09:30:00', '17:30:00', 2, 2),  -- Mardi
(NULL, '09:30:00', '16:00:00', 4, 2),  -- Jeudi
(NULL, '10:00:00', '14:00:00', 7, 2),  -- Dimanche

-- Déchet’Rie (id_lieu_de_collecte = 3)
(NULL, '08:00:00', '12:00:00', 1, 3),  -- Lundi
(NULL, '13:00:00', '17:00:00', 5, 3),  -- Vendredi
(NULL, '08:00:00', '10:00:00', 6, 3),  -- Samedi

-- Vert’Collecte (id_lieu_de_collecte = 4)
(NULL, '09:00:00', '17:00:00', 2, 4),  -- Mardi
(NULL, '09:00:00', '17:00:00', 4, 4),  -- Jeudi
(NULL, '10:00:00', '16:00:00', 7, 4),  -- Dimanche

-- Tri’Top (id_lieu_de_collecte = 5)
(NULL, '07:00:00', '15:00:00', 3, 5),  -- Mercredi
(NULL, '07:00:00', '13:00:00', 5, 5),  -- Vendredi
(NULL, '08:00:00', '12:00:00', 7, 5); -- Dimanche




INSERT INTO  camion (id_camion, kilometrage, date_de_mise_en_service, id_localisation, id_modele, id_conducteur) VALUES
(NULL, 150000, '2018-03-12', 1, 1, 1),
(NULL, 90000, '2020-06-20', 2, 2, 2),
(NULL,110000, '2019-05-10', 3, 3, 5),
(NULL,76000,  '2021-11-23', 5, 4, 6),
(NULL,134500, '2017-09-14', 2, 5, 7),
(NULL,98000,  '2020-01-30', 4, 6, 8),
(NULL,45000,  '2022-07-19', 6, 7, 9),
(NULL,160000, '2016-12-03', 7, 8, 10),
(NULL,89000,  '2020-09-15', 8, 3, 1),
(NULL,123000, '2018-02-10', 9, 4, 2),
(NULL,72000,  '2021-04-21', 10, 5, 3),
(NULL,54000,  '2022-10-05', 1, 6, 4),
(NULL,101000, '2019-03-12', 2, 7, 5),
(NULL,87000,  '2020-06-28', 3, 8, 6),
(NULL,143500, '2017-11-08', 4, 3, 7),
(NULL,69000,  '2021-06-14', 5, 4, 8),
(NULL,83000,  '2020-08-19', 6, 5, 9),
(NULL,92000,  '2020-12-03', 7, 6, 10),
(NULL,57000,  '2022-03-25', 8, 7, 1),
(NULL,119000, '2018-10-02', 9, 8, 2);

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



-- Distances depuis le Centre de Tri de Belfort Nord (id_localisation = 17)
INSERT INTO distance (valeur, id_localisation, id_localisation_1)
VALUES
    (1.23, 17, 1),   -- Centre de Tri de Belfort Nord -> 1 Rue de la République
    (1.45, 17, 5),   -- Centre de Tri de Belfort Nord -> 22 Boulevard Anatole France
    (1.78, 17, 8),   -- Centre de Tri de Belfort Nord -> 18 Rue de la Préfecture
    (2.01, 17, 11),  -- Centre de Tri de Belfort Nord -> 25 Rue de la République, Danjoutin
    (2.34, 17, 13),  -- Centre de Tri de Belfort Nord -> 14 Rue du Stade, Bavilliers

-- Distances depuis l'ÉcoCentre de Valdoie (id_localisation = 18)

    (1.89, 18, 4),   -- ÉcoCentre de Valdoie -> 10 Rue du Docteur Fréry
    (2.12, 18, 7),   -- ÉcoCentre de Valdoie -> 3 Rue du Général de Gaulle
    (2.45, 18, 10),  -- ÉcoCentre de Valdoie -> 12 Rue des Jardins
    (2.78, 18, 12),  -- ÉcoCentre de Valdoie -> 8 Rue de la Gare, Valdoie
    (3.01, 18, 14),  -- ÉcoCentre de Valdoie -> 5 Rue des Écoles, Offemont

-- Distances depuis Tri’Est - Bavilliers (id_localisation = 19)

    (0.45, 19, 13),  -- Tri’Est - Bavilliers -> 14 Rue du Stade, Bavilliers
    (0.78, 19, 5),   -- Tri’Est - Bavilliers -> 22 Boulevard Anatole France
    (1.12, 19, 8),   -- Tri’Est - Bavilliers -> 18 Rue de la Préfecture
    (1.34, 19, 15),  -- Tri’Est - Bavilliers -> 19 Rue de la Mairie, Essert
    (1.56, 19, 17),  -- Tri’Est - Bavilliers -> 2 Rue du Château, Chèvremont

-- Distances depuis le Pôle Recyclage du Pays de Belfort (id_localisation = 20)

    (2.11, 20, 16),  -- Pôle Recyclage -> 11 Rue des Vignes, Pérouse
    (2.33, 20, 18),  -- Pôle Recyclage -> 16 Rue des Prés, Sevenans
    (2.55, 20, 2),   -- Pôle Recyclage -> 15 Avenue Jean Jaurès
    (2.77, 20, 6),   -- Pôle Recyclage -> 7 Rue de Mulhouse
    (3.00, 20, 9);   -- Pôle Recyclage -> 9 Rue du Lycée




-- Test fetch
SELECT conducteur.Nom_conducteur, camion.kilometrage, camion.date_de_mise_en_service, modele.nom_modele, localisation.adresse
FROM camion
LEFT JOIN localisation ON camion.id_localisation = localisation.id_localisation
LEFT JOIN modele ON camion.id_modele = modele.id_modele
LEFT JOIN  conducteur ON camion.id_conducteur = conducteur.id_conducteur;



SELECT
    l.id_lieu_de_collecte,
    l.libelle_lieu_de_collecte,
    l.id_localisation,
    loc.adresse,
    (SELECT COUNT(*) FROM conteneur c WHERE c.id_localisation = l.id_localisation) AS nombre_conteneurs,
    (SELECT h.ouverture FROM horaire h JOIN jour j ON h.id_jour = j.id_jour
     WHERE h.id_lieu_de_collecte = l.id_lieu_de_collecte AND j.ajouter_jour = 'dimanche' ) AS ouverture,
    (SELECT h.fermeture FROM horaire h JOIN jour j ON h.id_jour = j.id_jour
     WHERE h.id_lieu_de_collecte = l.id_lieu_de_collecte AND j.ajouter_jour = 'dimanche' ) AS fermeture
FROM lieux_collecte l
         LEFT JOIN localisation loc ON l.id_localisation = loc.id_localisation
ORDER BY l.id_lieu_de_collecte;

SELECT
    lieux_collecte.id_lieu_de_collecte,
    lieux_collecte.libelle_lieu_de_collecte,
    lieux_collecte.id_localisation,
    localisation.id_localisation,
    localisation.adresse,
    COUNT(conteneur.id_conteneur) AS nombre,
    horaire.ouverture, horaire.fermeture, lieux_collecte.libelle_lieu_de_collecte, jour.ajouter_jour
FROM
    lieux_collecte
        LEFT JOIN
    localisation ON lieux_collecte.id_localisation = localisation.id_localisation
        LEFT JOIN
    conteneur ON conteneur.id_localisation = lieux_collecte.id_localisation
        LEFT JOIN
    horaire ON horaire.id_lieu_de_collecte = lieux_collecte.id_lieu_de_collecte
        LEFT JOIN
    jour ON horaire.id_jour = jour.id_jour
GROUP BY
    lieux_collecte.id_lieu_de_collecte,
    lieux_collecte.libelle_lieu_de_collecte,
    lieux_collecte.id_localisation,
    localisation.id_localisation,
    localisation.adresse, horaire.ouverture, horaire.fermeture, lieux_collecte.libelle_lieu_de_collecte, jour.ajouter_jour
ORDER BY
    lieux_collecte.id_lieu_de_collecte;



SELECT COUNT(*)AS 'nbre' FROM lieux_collecte;

# compter le nombre de conteneur par lieux
SELECT lieux_collecte.libelle_lieu_de_collecte, COUNT(conteneur.id_conteneur) AS "nombre de conteneur" FROM lieux_collecte
LEFT JOIN localisation on lieux_collecte.id_localisation = localisation.id_localisation
LEFT JOIN conteneur on localisation.id_localisation = conteneur.id_localisation
GROUP BY lieux_collecte.libelle_lieu_de_collecte ;

# les lieux qui sont a une distance supérieure à 1km d'un centre de tri
SELECT lieux_collecte.libelle_lieu_de_collecte , ct.libelle_centre_de_tri, distance.valeur AS distance
FROM lieux_collecte
INNER JOIN localisation on lieux_collecte.id_localisation = localisation.id_localisation
INNER JOIN distance on localisation.id_localisation = distance.id_localisation
INNER JOIN centre_tri ct on localisation.id_localisation = ct.id_localisation
WHERE distance.valeur <= 1.0;


# Quantité de déchets par lieux de collecte
SELECT lc.libelle_lieu_de_collecte AS Lieu, SUM(conteneur.capacite_max) AS 'Quantité déchets'
FROM conteneur
JOIN localisation ON conteneur.id_localisation = localisation.id_localisation
JOIN lieux_collecte lc on localisation.id_localisation = lc.id_localisation
WHERE lc.id_localisation = conteneur.id_localisation
GROUP BY lc.libelle_lieu_de_collecte ;

# déchets les plus présents
SELECT td.nom_dechet, AVG(conteneur.capacite_max) AS Moyenne ,(conteneur.capacite_max *100 /SUM(conteneur.capacite_max))AS pourcentage
FROM localisation
LEFT JOIN conteneur ON localisation.id_localisation = conteneur.id_localisation
LEFT JOIN lieux_collecte lc on localisation.id_localisation = lc.id_localisation
LEFT JOIN type_dechet td on conteneur.id_type_dechet = td.id_type_dechet
WHERE conteneur.id_type_dechet = td.id_type_dechet
GROUP BY td.nom_dechet, conteneur.capacite_max ;

SELECT lieux_collecte.id_lieu_de_collecte AS id_lieu, lieux_collecte.libelle_lieu_de_collecte AS libelle,
       COUNT(conteneur.id_conteneur) AS nb_conteneur, SUM(conteneur.capacite_max) AS qte_max
FROM lieux_collecte
LEFT JOIN conteneur on lieux_collecte.id_localisation = conteneur.id_localisation
LEFT JOIN localisation on lieux_collecte.id_localisation = localisation.id_localisation
GROUP BY lieux_collecte.id_lieu_de_collecte, lieux_collecte.libelle_lieu_de_collecte ;

SELECT lieux_collecte.libelle_lieu_de_collecte as lieu, MAX(distance.valeur)
FROM lieux_collecte
         INNER JOIN localisation ON lieux_collecte.id_localisation = localisation.id_localisation
         INNER JOIN distance ON localisation.id_localisation = distance.id_localisation
GROUP BY lieux_collecte.libelle_lieu_de_collecte;

SELECT AVG(distance.valeur)
FROM lieux_collecte
         INNER JOIN localisation ON lieux_collecte.id_localisation = localisation.id_localisation
         INNER JOIN distance ON localisation.id_localisation = distance.id_localisation;