-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8081
-- Generation Time: Dec 04, 2020 at 01:13 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `trivial pursuit`
--

-- --------------------------------------------------------

--
-- Table structure for table `joueurs`
--

CREATE TABLE `joueurs` (
  `id_joueur` int(2) NOT NULL,
  `nom_joueur` varchar(50) NOT NULL,
  `points_joueur` int(10) NOT NULL,
  `couleur_joueur` char(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `joueurs`
--

INSERT INTO `joueurs` (`id_joueur`, `nom_joueur`, `points_joueur`, `couleur_joueur`) VALUES
(1, 'Joueur1', 0, 'Rose'),
(2, 'Joueur2', 0, 'Rouge'),
(3, 'Joueur3', 0, 'Noir'),
(4, 'Joueur4', 0, 'Blanc');

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `id_question` int(7) NOT NULL,
  `libelle_question` text NOT NULL,
  `theme_question` int(1) NOT NULL,
  `difficulte_question` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id_question`, `libelle_question`, `theme_question`, `difficulte_question`) VALUES
(201, 'Comment appelle-t-on le fait que le résultat d\'un algorithme d\'apprentissage automatique ne soit pas neutre, et qu\'il reflète les valeurs implicites des humains impliqués dans la sélection des données d\'apprentissage ?', 3, 1),
(202, 'Quel était le nom de l\'agent conversationnel développé par Microsoft et déployé sur Twitter en 2016, qui a du être retiré après 24 heures suite à la tenue de propos à caractère racistes ?', 3, 2),
(203, 'Quelle ONG, crée en 2012, mène des actions visant à faire interdire le développement, la production et l’utilisation de l’armement entièrement autonome ?', 3, 3),
(204, 'Comment appelle-t-on les vidéos truquées très réalistes qui emploient des algorithmes d\'IA et sont souvent employées pour changer un visage ou faire prononcer un faux discours par une personnalité ?', 3, 2),
(205, 'Dans quel film le supercalculateur militaire WOPR engage par erreur une \"guerre thermonucléaire globale\" ?', 3, 2),
(206, 'Vrai ou faux : le département R&D de Google s\'est engagé à ne jamais participer au développement ou à la fabrication d\'armes létales autonomes ?', 3, 1),
(207, 'La consommation énergétique de l\'IA Deepmind pour jouer au go est de l\'ordre de : \r\n400 W/h | 4.000 W/h | 40.000 W/h | 400.000 W/h \r\n', 3, 2),
(208, 'Quel organisme français a été chargé par le gouvernement, en 2016  de mener une réflexion sur les problèmes de société soulevés par les technologies numériques? ', 3, 1),
(209, 'Quels sont les deux principes fondateurs pour une intelligence artificielle au service de l’homme d’après la CNIL?', 3, 1),
(210, 'Dans quel but le gouvernement souhaiterait-il retravailler le design des systèmes algorithmiques  au service de la liberté humaine?', 3, 1),
(211, 'Les algorithmes permettent une délégation croissante des tâches, de raisonnements, ou de décisions à des machines. Comment ces machines sont-elles jugées par la plupart des gens:', 3, 1),
(212, 'Quel est l’organisme qui participe au dialogue mondial de l’éthique numérique?', 3, 1),
(213, 'En quelle année a été établie la déclaration universelle sur la Bioéthique?', 3, 3),
(214, 'Où s\'est situé le premier débat sur l’éthique de l’IA le 12 décembre 2018? ', 3, 3),
(215, 'De quoi se préoccupe l\'éthique humaine pour guider la conception des êtres artificiellement intelligents?\r\n', 3, 2),
(216, 'L\'éthique générale et éthique de l’IA sont-elles liées?', 3, 1),
(217, 'Citez une des conséquences néfastes d’une mauvaise utilisation de l’IA?', 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `reponses`
--

CREATE TABLE `reponses` (
  `id_reponse` int(7) NOT NULL,
  `id_question` int(7) NOT NULL,
  `libelle_reponse` varchar(100) NOT NULL,
  `valeur_reponse` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `reponses`
--

INSERT INTO `reponses` (`id_reponse`, `id_question`, `libelle_reponse`, `valeur_reponse`) VALUES
(1, 201, 'Biais', 1),
(2, 202, 'Tay', 1),
(3, 203, 'Stop Killer Robots', 1),
(4, 204, 'Deep Fakes', 1),
(5, 205, 'Wargame\r\n', 1),
(6, 206, 'Vrai', 1),
(7, 207, '400 W/h', 0),
(8, 207, '4.000 W/h', 0),
(9, 207, '40.000 W/h', 0),
(10, 207, '400.000 W/h  ', 1),
(11, 208, 'CNIL\r\n', 1),
(12, 209, 'Loyauté et vigilance', 1),
(13, 209, 'transparence et anonymat\r\n', 0),
(14, 209, 'ouverture et respect', 0),
(15, 209, 'contrôle et sécurité', 0),
(16, 210, 'pour contrer l’effet boîte noire', 1),
(17, 210, 'pour obtenir davantage de renseignements sur les utilisateurs', 0),
(18, 210, 'pour lutter contre le piratage', 0),
(19, 210, 'pour lutter contre la fraude', 0),
(20, 211, 'Infaillibles et neutres', 1),
(21, 211, 'Infaillibles mais biaisées', 0),
(22, 211, 'Impartiales mais pouvant se tromper', 0),
(23, 211, 'peu fiables et biaisées', 0),
(24, 212, 'L\'Unesco', 1),
(25, 213, '2005', 1),
(26, 214, 'MARRAKECH', 1),
(27, 215, 'du comportement moral des agents moraux artificiels', 1),
(28, 216, 'OUI', 1),
(29, 217, 'Perte d’emploi, utilisation de l’Ia comme une arme…', 1);

-- --------------------------------------------------------

--
-- Table structure for table `theme`
--

CREATE TABLE `theme` (
  `id_theme` int(1) NOT NULL,
  `nom_theme` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `theme`
--

INSERT INTO `theme` (`id_theme`, `nom_theme`) VALUES
(1, 'Big Data'),
(2, 'IA'),
(3, 'Ethique'),
(4, 'Python'),
(5, 'Mathématique');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `joueurs`
--
ALTER TABLE `joueurs`
  ADD PRIMARY KEY (`id_joueur`);

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id_question`),
  ADD KEY `theme_question` (`theme_question`);

--
-- Indexes for table `reponses`
--
ALTER TABLE `reponses`
  ADD PRIMARY KEY (`id_reponse`),
  ADD KEY `id_question` (`id_question`) USING BTREE;

--
-- Indexes for table `theme`
--
ALTER TABLE `theme`
  ADD PRIMARY KEY (`id_theme`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `joueurs`
--
ALTER TABLE `joueurs`
  MODIFY `id_joueur` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `theme`
--
ALTER TABLE `theme`
  MODIFY `id_theme` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `questions`
--
ALTER TABLE `questions`
  ADD CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`theme_question`) REFERENCES `theme` (`id_theme`);

--
-- Constraints for table `reponses`
--
ALTER TABLE `reponses`
  ADD CONSTRAINT `reponses_ibfk_1` FOREIGN KEY (`id_question`) REFERENCES `questions` (`id_question`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
