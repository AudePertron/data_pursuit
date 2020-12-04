-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:8081
-- Généré le : ven. 04 déc. 2020 à 13:07
-- Version du serveur :  5.7.24
-- Version de PHP : 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `data_pursuit`
--
CREATE DATABASE IF NOT EXISTS `data_pursuit` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `data_pursuit`;

-- --------------------------------------------------------

--
-- Structure de la table `joueurs`
--

CREATE TABLE `joueurs` (
  `id_joueur` int(11) NOT NULL,
  `nom_joueur` varchar(50) NOT NULL,
  `points_joueur` int(11) NOT NULL,
  `couleur_joueur` char(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `questions`
--

CREATE TABLE `questions` (
  `id_question` int(7) NOT NULL,
  `libelle_question` text NOT NULL,
  `id_theme` int(1) NOT NULL,
  `difficulte_question` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `questions`
--

INSERT INTO `questions` (`id_question`, `libelle_question`, `id_theme`, `difficulte_question`) VALUES
(1, 'Quels sont les \"trois V\" du Big Data ?', 1, 1),
(2, 'Quel est le "poids" du big data en 2020', 1, 2),
(3, 'Le volume de données des entreprosesdouble tot les ... ans(s)', 1, 2),
(4, 'Lequel de ces emplacements serait le plus adapté pour stocker un grand jeu de données', 1, 2),
(5, 'En 2020, par combien le volume de données numériques créés a-t-il été multiplié par rapport à 2010 ?', 1, 2),
(6, 'Par combien sera multiplier le volume du big data en 2035 par rapport a 2020', 1, 3),
(7, 'Combien d’heures de vidéo sont téléchargées sur YouTube chaque minute ?', 1, 1),
(8, 'Vrai ou faux ? 90 % des données dans le monde ont été créées dans les deux dernières années.', 1, 2),
(9, 'Quelle entreprise informatique est le plus grand fournisseur Big Data dans le monde ?', 1, 2),
(10, 'Le modèle de programmation MapReduce a été initialement développé par…', 1, 2),
(11, 'Qui a créé le framework logiciel Hadoop, très populaire dans le monde du Big Data ?', 1, 2),
(12, 'Combien de gigaoctets y a-t-il dans un exaoctet ?', 1, 1),
(13, 'Combien d’exaoctets de données le LHC «Large Hadron Collider» peut-il produire par jour ?', 1, 3),
(14, 'Une fois terminé, le flux de données généré par le radiotélescope SKA sera équivalent à…', 1, 3),
(15, 'Lesquels de ces tâches relève du Big Data?', 1, 2),
(16, 'Lequel des éléments suivants est une base de données distribuée à plusieurs niveaux?', 1, 3),
(100, 'Comment s’appel le test permettant de vérifier la capacité d’une machine à faire preuve de signes d’intelligence humaine ? (Nom de famille)', 2, 2),
(101, 'Comment s’appellent les deux apprentissages en intelligence artificielle qui ont permis à une machine de battre les meilleurs joueurs de go au monde en 2016 et 2017 ?', 2, 3),
(102, 'En février dernier, quel pourcentage d\'entreprises canadiennes entendait investir en intelligence artificielle d’ici deux ans ?', 2, 2),
(103, 'Qui a affirmé, l’an dernier, que la concurrence des nations pour la supériorité en IA pourrait déboucher sur une Troisième Guerre mondiale ?', 2, 3),
(104, 'Au tournant des années 90, quelle invention a ouvert la voie à des avancées sans précédent en matière d’apprentissage automatique pour les machines ?', 2, 3),
(105, 'D’après les dernières études, de combien le PIB mondial s’accroîtra-t-il d’ici 2030 grâce au développement de l’intelligence artificielle ?', 2, 2),
(106, 'Quel est le but de l\'intelligence artificielle ?', 2, 1),
(107, 'Quelles sont les matières associées à l\'intelligence artificielle ?', 2, 1),
(108, 'Le logiciel Alpha Go a battu le champion Lee Sedol au jeu de go en 2016?', 2, 1),
(109, 'L’IA permet-t-elle aux juristes d’analyser plus rapidement les contrats ?', 2, 1),
(110, 'John McCarthy a inventé le terme \"IA\" ?', 2, 2),
(111, 'En juin 2017, des chercheurs de Facebook ont fait dialoguer deux IA pour tenter de leur apprendre l\'art de la négociation. Que s\'est-il passé?', 2, 2),
(112, 'En septembre 2016, Sony diffusait Daddy\'s car, le premier morceau pop composé par une intelligence artificielle. Avec quoi cette dernière a-t-elle été \"nourrie\"?', 2, 1),
(113, 'Une IA a déjà participé à la création de la bande-annonce d\'un film: lequel?', 2, 2),
(114, 'Quel jeu de stratégie échappe encore à la domination des intelligences artificielles?', 2, 2),
(115, 'L’IA fait souvent figure de croque mitaine dans les films de science-fiction. Dans ces quatres films, laquelle ne devient pas méchante ?', 2, 3),
(116, 'Qu\'est ce qui distingue une intelligence artificielle forte d\'une intelligence artificielle faible?', 2, 2),
(117, 'Sait-on précisément ce qui se passe dans le “cerveau” d’une IA ?', 2, 1),
(118, 'Comment une IA doit-elle s\'y prendre pour passer le test de Turing?', 2, 1),
(119, 'Le GDPR c’est quoi ?', 2, 3),
(120, 'Le GDPR est une loi européenne qui régit la protection des données personnelles des résidents Européens ?', 2, 2),
(121, 'En mars 2016, Microsoft avait lâché son IA Tay sur Twitter, afin qu\'elle apprenne de nouvelles choses au contact des internautes. Au bout de 24 heures, que s\'était-il passé?', 2, 2),
(122, 'Quel IA d\'un géant américain est déjà couramment utilisée pour répondre aux questions des clients de certaines entreprises, notamment les banques ?', 2, 3),
(123, 'Lesquelles de ces personnalités du monde scientifique ou technologique ont-elles mis en garde contre les dangers potentiels de l\'IA?', 2, 2),
(124, 'Quelle marque, fondée par Elon Musk, fabrique des voitures utilisant l\'IA?', 2, 1),
(125, 'Quelle bibliothèque python, développée par Facebook, est utilisée en Deep Learning?', 2, 3),
(126, 'Quel est le nom de la série se déroulant dans un parc d\'attractions futuriste avec des androïde intelligents?', 2, 3),
(201, 'Quelle ONG, créée en 2012, mène des actions visant à faire interdire le développement, la production et l’utilisation de l’armement entièrement autonome', 3, 3),
(202, 'Comment appelle-t-on le fait que le résultat d\'un algorithme d\'apprentissage automatique ne soit pas neutre, et qu\'il reflète les valeurs implicites des humains impliqués dans la sélection des données d\'apprentissage', 3, 1),
(203, 'Quel était le nom de l\'agent conversationnel développé par Microsoft et déployé sur Twitter en 2016, qui a du être retiré après 24 heures suite à la tenue de propos à caractère racistes', 3, 2),
(204, 'Comment appelle-t-on les vidéos truquées très réalistes qui emploient des algorithmes d\'IA et sont souvent employées pour changer un visage ou faire prononcer un faux discours par une personnalité', 3, 2),
(205, 'Dans quel film le supercalculateur militaire WOPR engage par erreur une \"guerre thermonucléaire globale\" ', 3, 2),
(206, 'le département R&D de Google s\'est engagé à ne jamais participer au développement ou à la fabrication d\'armes létales autonomes ', 3, 1),
(207, 'La consommation énergétique de l\'IA Deepmind pour jouer au go est de l\'ordre de', 3, 2),
(208, 'Quel organisme français a été chargé par le gouvernement, en 2016  de mener une réflexion sur les problèmes de société soulevés par les technologies numériques', 3, 1),
(209, 'Quels sont les deux principes fondateurs pour une intelligence artificielle au service de l’homme d’après la CNIL', 3, 1),
(210, 'Dans quel but le gouvernement souhaiterait-il retravailler le design des systèmes algorithmiques  au service de la liberté humaine', 3, 1),
(211, 'Les algorithmes permettent une délégation croissante des tâches, de raisonnements, ou de décisions à des machines. Comment ces machines sont-elles jugées par la plupart des gens', 3, 1),
(212, 'Quel est l’organisme qui participe au dialogue mondial de l’éthique numérique', 3, 1),
(213, 'En quelle année a été établie la déclaration universelle sur la Bioéthique', 3, 2),
(214, 'Où s\'est situé le premier débat sur l’éthique de l’IA le 12 décembre 2018', 3, 3),
(215, 'De quoi se préoccupe l\'éthique humaine pour guider la conception des êtres artificiellement intelligents', 3, 2),
(216, 'L\'éthique générale et éthique de l’IA sont liées', 3, 1),
(301, 'En quelle année a été concue la 1ere version de python ?', 4, 2),
(302, 'Qui est le fondateur de python ?', 4, 1),
(303, 'Le typage dans python n\'est pas vérifié a la compilation, ceci s\'appelle :', 4, 3),
(304, 'A quoi sert le ramasse-miette Python (“garbage collector”) ?', 4, 2),
(305, 'A quoi sert TensorFlow?', 4, 1),
(306, 'L’interpréteur python a nécessairement besoin de quatre espaces (tabulation) pour comprendre qu’il a affaire à une indentation.', 4, 2),
(307, 'Comment s’appelle une fonction anonyme dans python ?', 4, 1),
(308, 'Trouvez l’intrus :', 4, 2),
(309, 'Trouvez l’intrus :', 4, 2),
(310, 'Quelle ligne de code renverra une erreur ?', 4, 3),
(311, 'Quel nom donne-t-on à un objet créé par une classe ?', 4, 1),
(312, 'Les opérateurs “==” et “is” ont la même signification en Python ', 4, 1),
(313, 'Quelle feature existe déjà sur Python 3.8 :', 4, 2),
(314, 'En python 3, que fait l’opérateur // ?', 4, 1),
(315, 'Que mettons-nous dans une fonction entre parenthèses?', 4, 1),
(316, 'Quelle fonction est utilisée pour ouvrir le fichier en lecture en Python ?', 4, 1),
(317, 'Trouvez l’intrus quant à *args et **kwargs', 3, 2),
(318, 'Lequel des opérateurs suivants en python est évalué à « True » s’il ne trouve pas de variable dans la séquence spécifiée sinon « False »?', 4, 1),
(319, 'Que signifie “Nested”pour une liste ? ', 4, 3),
(320, 'Quel est le titre de De Guido Van Rossum au sein de la communauté Python ?', 4, 2),
(321, 'Lequel de ces logiciels n’est pas codé en Python ?', 4, 1),
(401, 'Quelle est la forme d\'une fonction affine', 5, 1),
(402, 'La courbe en cloche est une caractéristique de la loi', 5, 2),
(403, 'Qui est le créateur de l\'algorithme du \'Shortest path\' en 1959', 5, 3),
(404, 'Quelle est la médiane de cette liste [1, 1, 3, 4, 7, 9, 12, 12, 15]', 5, 1),
(405, 'Quel est le moyenne de cette liste [13, 5, 7, 0, 25]', 5, 1),
(406, 'La variance peut être négative', 5, 1),
(407, 'Quel concept appartient à l\'algèbre de Boole', 5, 2),
(408, 'Quel est le rapport de l\'écart-type à la variance', 5, 2),
(409, 'Parmi ces choix, lequel est un vecteur', 5, 1),
(410, 'Qu\'est-ce qu\'une matrice', 5, 1),
(411, 'Le Coefficient de détermination est le carré du coefficient de', 5, 2),
(412, 'Avec combien de matrice(s) peut-on représenter une image RGB', 5, 1),
(413, 'A quoi correspond le 3ème quantile', 5, 1),
(414, 'Combien de colonne comportera une matrice comportant 10 variables', 5, 1),
(415, 'Le nombre de colonnes de la 1ère matrice doit-il correspondre au nombre de lignes de la 2ème matrice ?', 5, 2),
(416, 'Le calcul matriciel de structure (2,3)*(2,3) est-il Paul-ssible', 5, 2),
(417, 'En tirant une carte au hasard dans un jeu de 32 cartes, la probabilité d\'obtenir une Reine rouge est', 5, 1),
(418, 'Quel test de corrélation doit-on utiliser quand nos variables suivent une loi normale', 5, 2),
(419, 'Il n\'y a aucune corrélation entre 2 variables lorsque le rapport est de -1', 5, 2),
(420, 'Quelle est la célèbre épreuve utiliser dans la loi binomiale de notation n', 5, 3),
(421, 'Une courbe polynomiale indique que plusieurs variables existent dans notre dataset', 5, 2),
(422, 'Pour f(x) = 2x² + 4x + 5, la courbe passerait l\'origine à quelle ordonée ?', 5, 2),
(423, 'Le coefficient directeur peut-il indiquer l\'évolution d\'une droite ', 5, 1),
(424, 'En statistique, un outlier est une valeur ', 5, 1),
(425, 'La valeur sigma d\'une Loi Normale correspond à ', 5, 1),
(426, 'Laquelle de ces propositions présente une forte relation entre x et y ', 5, 3),
(427, 'L\'erreur quadratique moyenne est la racine de ', 5, 3),
(428, 'La somme des carrés des résidus n\'est pas un indicateur de comparaison de 2 séries de valeurs', 5, 3),
(429, 'La variance est une mesure du degré de dispersion d\'un ensemble de données', 5, 2),
(430, 'L\'équation (ih/2 π) d l Ψ>/dt = Hl Ψ> peut-elle être résolue par Paul ?', 5, 1);

-- --------------------------------------------------------

--
-- Structure de la table `reponses`
--

CREATE TABLE `reponses` (
  `id_reponse` int(7) NOT NULL,
  `id_question` int(7) NOT NULL,
  `libelle_reponse` varchar(100) NOT NULL,
  `valeur_reponse` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `reponses`
--

INSERT INTO `reponses` (`id_reponse`, `id_question`, `libelle_reponse`, `valeur_reponse`) VALUES
(19, 1, 'Volume, Vitesse, Variété', 1),
(20, 2, '610 zetaoctet de données', 1),
(23, 5, '24', 1),
(24, 6, '45', 1),
(25, 7, '35', 0),
(26, 7, '60', 0),
(27, 7, '100', 1),
(28, 8, 'VRAI', 1),
(29, 8, 'FAUX', 0),
(30, 9, 'DELL', 0),
(31, 9, 'HP', 0),
(32, 9, 'IBM', 1),
(33, 10, 'Appache Software Foundation', 0),
(34, 10, 'Google', 1),
(35, 10, 'Microsoft Research', 0),
(36, 11, 'Doug CUTTING', 1),
(37, 11, 'Richard STALLMAN', 0),
(38, 11, 'Alan COX', 0),
(39, 12, 'Un millier', 0),
(40, 12, 'Un million', 0),
(41, 12, 'Un milliard', 1),
(42, 13, '5 exaoctets', 0),
(43, 13, '50 exaoctets', 0),
(44, 13, '500 exaoctets', 1),
(45, 14, 'Un dixième du trafic Internet global', 0),
(46, 14, 'Deux fois le  trafic Internet global', 0),
(47, 14, 'Dix fois le trafic Internet global', 1),
(49, 16, 'HDFS', 0),
(50, 16, 'HBase', 1),
(51, 16, 'Les deux ci-dessus', 0),
(52, 16, 'Aucune de ces réponses', 0),
(54, 2, '110 zetaoctet de données', 0),
(55, 2, '1010 zetaoctet de données', 0),
(56, 5, '15', 0),
(57, 5, '30', 0),
(58, 3, '1', 0),
(59, 3, '1,2', 1),
(60, 3, '2', 0),
(61, 4, 'Un SSD avec un système de sécurité', 1),
(62, 4, 'Un disque dur classique', 0),
(63, 4, 'Une clé USB avec un mot de passe', 0),
(64, 15, 'L\'analyse des données', 1),
(65, 15, 'Visualisation des données', 1),
(66, 15, 'Interprétation des données', 0),
(67, 15, 'Stockage des données', 1),
(100, 100, 'Turing', 1),
(101, 101, 'Profond et par renforcement.', 1),
(102, 101, 'Profond et prédictif', 0),
(103, 101, 'Automatique et semi-automatique', 0),
(104, 102, '52 %', 0),
(105, 102, '23 %', 1),
(106, 103, 'Noam Chomsky', 0),
(107, 103, 'Steve Wozniak', 0),
(108, 103, 'Elon Musk', 1),
(109, 104, 'le réseau convolutif', 1),
(110, 104, 'Deep Blue', 0),
(111, 104, 'le perceptron', 0),
(112, 105, '14 %', 1),
(113, 105, '35 %', 0),
(114, 106, 'Toutes les réponses sont exactes', 1),
(115, 106, 'Remplacer des humains', 0),
(116, 106, 'Penser comme des humains', 0),
(117, 107, 'le machine learning et  le deep learning', 1),
(118, 107, 'la littérature', 0),
(119, 107, 'l’art abstrait', 0),
(120, 108, 'Vrai', 1),
(121, 108, 'Faux', 0),
(122, 109, 'Vrai', 1),
(123, 109, 'Faux', 0),
(124, 110, 'Vrai', 1),
(125, 110, 'Faux', 0),
(126, 111, 'Inventé leur propre langage', 1),
(127, 111, 'Répété la même chose en boucle', 0),
(128, 111, 'Sont tombé en panne', 0),
(129, 112, 'La discographie des Beatles', 0),
(130, 112, '10 000 titres de tout genre', 1),
(131, 112, 'Rien', 0),
(132, 113, 'Ghost in the Shell', 0),
(133, 113, 'Le Dictateur (Chaplin)', 0),
(134, 113, 'Star Trek Sans limites', 0),
(135, 113, 'Morgan', 1),
(136, 114, 'Les échecs', 0),
(137, 114, 'Le go', 0),
(138, 114, 'Starcraft', 1),
(139, 114, 'Le poker', 0),
(140, 115, 'HALL9000 : 2001 L’Odyssée de l’espace', 0),
(141, 115, 'Viki :  I-Robot', 0),
(142, 115, 'Samantha : Her', 1),
(143, 115, 'Skynet : Terminator', 0),
(144, 116, 'L’IA forte à conscience d’elle-même', 0),
(145, 116, 'L’IA forte est plus rapide que la faible', 0),
(146, 116, 'L’IA forte écrase la faible aux échecs', 0),
(147, 116, 'L’IA faible ne sait effectuer qu’une seule tâche', 1),
(148, 117, 'Vrai', 0),
(149, 117, 'Faux', 1),
(150, 118, 'Développer le sens de l’humour', 0),
(151, 118, 'Prendre conscience de sa propre existence', 0),
(152, 118, 'Apprendre à apprendre toute seule', 1),
(153, 118, 'Berner les humains lors d’une conversation', 0),
(154, 119, 'General Data Protection Regulation', 1),
(155, 119, 'General Data Position Request', 0),
(156, 120, 'Vrai', 1),
(157, 120, 'Faux', 0),
(158, 121, 'Racontait des choses inintelligibles', 0),
(159, 121, 'Restée muette', 0),
(160, 121, 'S’est désactivé toute seule', 0),
(161, 121, 'Quasiment devenue nazie', 1),
(162, 122, 'Watson (IBM)', 1),
(163, 122, 'Alexa (Amazon)', 0),
(164, 123, 'Siri (Apple)', 0),
(165, 123, 'Google Home (Google)', 0),
(166, 123, 'Bill Gates', 0),
(167, 123, 'Stephen Hawking', 1),
(168, 123, 'Ray Kurzweil', 0),
(169, 124, 'Tesla', 1),
(170, 125, 'PyTorch', 1),
(171, 126, 'Westworld', 1),
(201, 201, 'Stop Killer Robots', 1),
(202, 202, 'Biais', 1),
(203, 203, 'Tay', 1),
(204, 204, 'Deep Fakes', 1),
(205, 205, 'Wargame', 1),
(206, 206, 'Vrai', 1),
(207, 206, 'Faux', 0),
(208, 207, '400 W/h', 0),
(209, 207, '4.000 W/h', 0),
(210, 207, '40.000 W/h ', 0),
(211, 207, '400.000 W/h', 1),
(212, 208, 'CNIL', 1),
(213, 209, 'Loyauté et vigilance', 1),
(214, 209, 'ouverture et respect', 0),
(215, 209, 'transparence et anonymat', 0),
(216, 209, 'contrôle et sécurité', 0),
(217, 210, 'contrer l’effet boîte noire', 1),
(218, 210, 'lutter contre le piratage', 0),
(219, 210, 'obtenir davantage de renseignements sur les utilisateurs', 0),
(220, 210, 'lutter contre la fraude', 0),
(221, 211, 'Infaillibles et neutres', 1),
(222, 211, 'Impartiales mais pouvant se tromper', 0),
(223, 211, 'Infaillibles mais biaisées', 0),
(224, 211, 'Peu fiables et biaisées', 0),
(225, 212, 'l\'UNESCO', 1),
(226, 213, '2005', 1),
(227, 214, 'Marrakech', 1),
(228, 215, 'comportement moral des agents moraux artificiels', 1),
(229, 215, 'de la plus-value des grille-pains ', 0),
(230, 215, 'de la vision de Paul', 0),
(231, 216, 'Vrai', 1),
(232, 216, 'Faux', 0),
(301, 301, '1989', 1),
(302, 302, 'Guido Van Rossum', 1),
(303, 302, 'Martin Odersky', 0),
(304, 302, 'James Gosling', 0),
(305, 302, 'Ryan Gosling', 0),
(306, 303, 'Duck Typing', 1),
(307, 303, 'Full Typing', 0),
(308, 303, 'Typage statique', 0),
(309, 303, 'V-Typing', 0),
(310, 304, 'Gérer automatiquement la mémoire', 1),
(311, 304, 'Nettoyer un code pas propre', 0),
(312, 304, 'Conserver les variables inutilisées', 0),
(313, 304, 'Totalement éliminer les risques de fuite mémoire', 0),
(314, 305, 'Une bibliothèque  permettant d’effectuer des opérations et des calculs de données à l’aide d’une API', 1),
(315, 305, 'Une bibliothèque offrant des algorithmes simples mais puissants pour les tâches de Machine Learning.', 0),
(316, 305, 'Une bibliothèque pour les calculs techniques et scientifiques', 0),
(317, 305, 'Un package utilisé pour les calculs scientifiques en Python.', 0),
(318, 306, 'Vrai', 0),
(319, 306, 'Faux', 1),
(320, 307, 'Fonction anonyme', 0),
(321, 307, 'Fonction spéciale', 0),
(322, 307, 'Fonction Lambda', 1),
(323, 307, 'elle s’appelle pas, elle est anonyme', 0),
(324, 308, 'Python a une bibliothèque standard particulièrement fournie.', 0),
(325, 308, 'Python est open-source et a une bonne portabilité.', 0),
(326, 308, 'Python a une syntaxe relativement simple comparée à d’autres langages.', 0),
(327, 308, 'Python est un langage très rapide car compilé.', 1),
(328, 309, 'Les dictionnaires sont des structures de données non séquentielles.', 0),
(329, 309, 'Les listes sont ordonnées.', 0),
(330, 309, 'Les sets peuvent contenir des doublons.', 1),
(331, 309, 'Les tuples sont protégés.', 0),
(332, 311, 'Fonction', 0),
(333, 311, 'Instance', 1),
(334, 312, 'Vrai', 0),
(335, 312, 'Faux', 1),
(336, 310, 'list(map(lambda x: x[0], [\'Red\', \'Green\', \'Blue\']))', 0),
(337, 310, 'dico = {(\"bonjour\" : \"forme usuelle de salutation\"; \"chien\") : \"sympathique canidé\"}', 1),
(338, 310, 'trucmuches = [k for k in {\"truc\":42, \"bidule\":\"D\", \"chouette\":777}]', 0),
(339, 310, 'print(\"{} est un super {} !\".format(\"Stéphane\", [\"prof\", \"héros\"][0]))', 0),
(340, 311, 'Variable', 0),
(341, 313, 'Des fonctions lambda multilignes', 0),
(342, 313, 'De vraies “constantes”', 0),
(343, 313, 'Le formatage f-Strings', 1),
(344, 313, 'Compilation statique et multiplateforme du code', 0),
(345, 314, 'Division entière', 1),
(346, 314, 'Retourne le reste', 0),
(347, 314, 'Division du float par zéro', 0),
(348, 314, 'a ** b', 0),
(349, 315, 'un argument', 1),
(350, 315, 'une clé', 0),
(351, 315, 'une valeur', 0),
(352, 315, 'une surprise', 0),
(353, 316, 'fopen(file_name, mode)', 0),
(354, 316, 'open(file_name, mode)', 1),
(355, 316, 'openfile(file_name, mode)', 0),
(356, 316, 'open_file(file_name, mode)', 0),
(357, 317, '*args permet de passer une liste ou un tuple en argument d’une fonction', 0),
(358, 317, '*args permet de passer les valeurs d’un dictionnaire en arguments de mot-clé', 0),
(359, 317, 'ça fonctionne aussi avec autre chose que “args” ou “kwargs” après les astérisques', 1),
(360, 318, '**', 0),
(361, 318, 'is', 0),
(362, 318, 'not in', 1),
(363, 318, '//', 0),
(364, 319, 'Une liste dans une liste', 1),
(365, 319, 'Une liste dans un dictionnaire', 0),
(366, 319, 'Un tuple dans une liste', 0),
(367, 319, 'Un set dans une liste', 0),
(368, 320, 'Dictateur bienveillant', 1),
(369, 321, 'Libre Office', 0),
(370, 321, 'Eve Online', 0),
(371, 321, 'Blender', 0),
(372, 321, 'Excel', 1),
(401, 401, 'Sinusoïdale', 0),
(402, 401, 'Exponentielle', 0),
(403, 401, 'Droite', 1),
(404, 402, 'de Gauss', 1),
(405, 402, 'Fisher', 0),
(406, 402, 'de Shapiro-Wilk', 0),
(407, 403, 'Dijkstra', 1),
(408, 404, '7', 1),
(409, 405, '10', 1),
(410, 406, 'Vrai', 0),
(411, 406, 'Faux', 1),
(412, 407, 'XOR', 1),
(413, 407, 'OR', 0),
(414, 407, 'AND', 0),
(415, 408, 'le carré', 0),
(416, 408, 'le cube', 0),
(417, 408, 'la racine', 1),
(418, 409, '3', 0),
(419, 409, '[3 0 1]', 1),
(420, 409, '3-0-1', 0),
(421, 410, 'un tableau', 1),
(422, 410, 'un graphique', 0),
(423, 410, 'un test', 0),
(424, 411, 'variation', 0),
(425, 411, 'linéaire', 0),
(426, 411, 'corrélation', 1),
(427, 412, '3', 1),
(428, 413, '75%', 1),
(429, 414, '10', 1),
(430, 415, 'Vrai', 1),
(431, 415, 'Faux', 0),
(432, 416, 'Vrai', 0),
(433, 416, 'Faux', 1),
(434, 417, '4/32', 0),
(435, 417, '2/16', 0),
(436, 417, '1/16', 1),
(437, 418, 'Kendall', 0),
(438, 418, 'Pearson', 1),
(439, 418, 'Spearman', 0),
(440, 419, 'Vrai', 0),
(441, 419, 'Faux', 1),
(442, 420, 'Bernoulli', 1),
(443, 421, 'Vrai', 0),
(444, 421, 'Faux', 1),
(445, 422, '5', 1),
(446, 423, 'Vrai', 1),
(447, 423, 'Faux', 0),
(448, 424, 'Abérrante', 1),
(449, 424, 'Absente', 0),
(450, 424, 'Fréquente', 0),
(451, 425, 'La variance', 0),
(452, 425, 'L\'écart-type', 1),
(453, 425, 'La moyenne', 0),
(454, 426, 'Corrélation = 0.9', 1),
(455, 426, 'P-value = 1', 0),
(456, 426, 'La réponse D', 0),
(457, 427, 'la MSE', 1),
(458, 427, 'la EAM', 0),
(459, 427, 'la THOMAS', 0),
(460, 428, 'Vrai', 0),
(461, 428, 'Faux', 1),
(462, 429, 'Vrai', 1),
(463, 429, 'Faux', 0),
(464, 430, 'Vrai', 1),
(465, 430, 'Faux', 0);

-- --------------------------------------------------------

--
-- Structure de la table `theme`
--

CREATE TABLE `theme` (
  `id_theme` int(1) NOT NULL,
  `nom_theme` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `theme`
--

INSERT INTO `theme` (`id_theme`, `nom_theme`) VALUES
(1, 'Big Data'),
(2, 'IA'),
(3, 'Ethique'),
(4, 'Python'),
(5, 'Mathematiques');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `joueurs`
--
ALTER TABLE `joueurs`
  ADD PRIMARY KEY (`id_joueur`);

--
-- Index pour la table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id_question`),
  ADD KEY `id_theme` (`id_theme`);

--
-- Index pour la table `reponses`
--
ALTER TABLE `reponses`
  ADD PRIMARY KEY (`id_reponse`),
  ADD KEY `id_question` (`id_question`);

--
-- Index pour la table `theme`
--
ALTER TABLE `theme`
  ADD PRIMARY KEY (`id_theme`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `joueurs`
--
ALTER TABLE `joueurs`
  MODIFY `id_joueur` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `questions`
--
ALTER TABLE `questions`
  MODIFY `id_question` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=431;

--
-- AUTO_INCREMENT pour la table `reponses`
--
ALTER TABLE `reponses`
  MODIFY `id_reponse` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=466;

--
-- AUTO_INCREMENT pour la table `theme`
--
ALTER TABLE `theme`
  MODIFY `id_theme` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `questions`
--
ALTER TABLE `questions`
  ADD CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`id_theme`) REFERENCES `theme` (`id_theme`);

--
-- Contraintes pour la table `reponses`
--
ALTER TABLE `reponses`
  ADD CONSTRAINT `reponses_ibfk_1` FOREIGN KEY (`id_question`) REFERENCES `questions` (`id_question`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
