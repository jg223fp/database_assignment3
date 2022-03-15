CREATE DATABASE  IF NOT EXISTS `disc_golf` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `disc_golf`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: disc_golf
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bags`
--

DROP TABLE IF EXISTS `bags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bags` (
  `owner_id` varchar(10) NOT NULL,
  `disc_name` varchar(30) NOT NULL,
  `plastic_type` varchar(25) NOT NULL,
  `weigth` int NOT NULL,
  PRIMARY KEY (`owner_id`,`disc_name`,`plastic_type`,`weigth`),
  KEY `disc_name` (`disc_name`),
  CONSTRAINT `bags_ibfk_1` FOREIGN KEY (`disc_name`) REFERENCES `discs` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bags`
--

LOCK TABLES `bags` WRITE;
/*!40000 ALTER TABLE `bags` DISABLE KEYS */;
INSERT INTO `bags` VALUES ('1002','compass','opto',179),('1004','compass','opto',169),('1005','compass','opto',169),('1006','compass','opto',169),('1007','compass','retro',179),('1002','cutlass','opto',175),('1004','cutlass','opto',175),('1006','cutlass','retro',165),('1007','cutlass','retro',175),('1001','explorer','opto',170),('1003','explorer','retro',167),('1004','explorer','retro',176),('1007','explorer','retro',176),('1003','fuse','opto',171),('1004','fuse','opto',171),('1007','fuse','opto',181),('1003','gauntlet','retro',176),('1004','gauntlet','retro',176),('1007','gauntlet','opto',176),('1001','keystone','opto',175),('1004','keystone','opto',175),('1005','keystone','retro',175),('1007','keystone','opto',175),('1002','knigth','retro',168),('1004','knigth','opto',175),('1007','knigth','retro',175),('1002','pain','retro',170),('1004','pain','opto',180),('1007','pain','opto',180),('1001','pure','opto',168),('1003','pure','opto',166),('1004','pure','opto',176),('1006','pure','retro',156),('1007','pure','opto',176),('1001','river','opto',175),('1003','river','opto',175),('1004','river','retro',178),('1005','river','opto',165),('1006','river','opto',178),('1007','river','opto',178);
/*!40000 ALTER TABLE `bags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `competition_results`
--

DROP TABLE IF EXISTS `competition_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `competition_results` (
  `name` varchar(40) NOT NULL,
  `year` int NOT NULL,
  `course` varchar(40) DEFAULT NULL,
  `hole` int NOT NULL,
  `player_id` varchar(10) NOT NULL,
  `result` int DEFAULT NULL,
  `tee_pad_disc` varchar(40) DEFAULT NULL,
  `finish_disc` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`name`,`year`,`player_id`,`hole`),
  KEY `player_id` (`player_id`),
  CONSTRAINT `competition_results_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `players` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `competition_results`
--

LOCK TABLES `competition_results` WRITE;
/*!40000 ALTER TABLE `competition_results` DISABLE KEYS */;
INSERT INTO `competition_results` VALUES ('Almhult open',2019,'almhults discgolfbana',1,'1003',3,'knigth','pure'),('Almhult open',2019,'almhults discgolfbana',2,'1003',3,'knigth','pure'),('Almhult open',2019,'almhults discgolfbana',3,'1003',3,'knigth','pure'),('Almhult open',2019,'almhults discgolfbana',4,'1003',3,'knigth','pure'),('Almhult open',2019,'almhults discgolfbana',5,'1003',3,'knigth','pure'),('Almhult open',2019,'almhults discgolfbana',6,'1003',3,'knigth','pure'),('Almhult open',2019,'almhults discgolfbana',7,'1003',3,'knigth','pure'),('Almhult open',2019,'almhults discgolfbana',8,'1003',3,'river','pure'),('Almhult open',2019,'almhults discgolfbana',9,'1003',3,'river','pure'),('Almhult open',2019,'almhults discgolfbana',10,'1003',3,'keystone','pure'),('Almhult open',2019,'almhults discgolfbana',11,'1003',3,'knigth','pure'),('Almhult open',2019,'almhults discgolfbana',12,'1003',3,'knigth','pure'),('Almhult open',2019,'almhults discgolfbana',13,'1003',3,'knigth','pure'),('Almhult open',2019,'almhults discgolfbana',14,'1003',3,'knigth','pure'),('Almhult open',2019,'almhults discgolfbana',15,'1003',3,'knigth','pure'),('Almhult open',2019,'almhults discgolfbana',16,'1003',3,'knigth','pure'),('Almhult open',2019,'almhults discgolfbana',17,'1003',3,'knigth','pure'),('Almhult open',2019,'almhults discgolfbana',18,'1003',3,'knigth','pure'),('Slottsskogen open',2019,'Teleborgs discgolfbana',1,'1001',2,'explorer','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',2,'1001',2,'river','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',3,'1001',3,'explorer','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',4,'1001',2,'river','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',5,'1001',4,'explorer','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',6,'1001',3,'explorer','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',7,'1001',3,'explorer','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',8,'1001',2,'explorer','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',9,'1001',2,'explorer','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',1,'1004',4,'knigth','pure'),('Slottsskogen open',2019,'Teleborgs discgolfbana',2,'1004',4,'knigth','pure'),('Slottsskogen open',2019,'Teleborgs discgolfbana',3,'1004',5,'knigth','pure'),('Slottsskogen open',2019,'Teleborgs discgolfbana',4,'1004',6,'knigth','pure'),('Slottsskogen open',2019,'Teleborgs discgolfbana',5,'1004',7,'knigth','pure'),('Slottsskogen open',2019,'Teleborgs discgolfbana',6,'1004',3,'knigth','pure'),('Slottsskogen open',2019,'Teleborgs discgolfbana',7,'1004',4,'knigth','pure'),('Slottsskogen open',2019,'Teleborgs discgolfbana',8,'1004',4,'knigth','pure'),('Slottsskogen open',2019,'Teleborgs discgolfbana',9,'1004',5,'knigth','pure'),('Slottsskogen open',2019,'Teleborgs discgolfbana',1,'1005',5,'river','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',2,'1005',7,'river','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',3,'1005',3,'river','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',4,'1005',3,'river','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',5,'1005',5,'river','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',6,'1005',3,'river','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',7,'1005',4,'river','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',8,'1005',5,'river','keystone'),('Slottsskogen open',2019,'Teleborgs discgolfbana',9,'1005',4,'river','keystone'),('Slottsskogen open',2020,'Teleborgs discgolfbana',1,'1004',3,'pain','pure'),('Slottsskogen open',2020,'Teleborgs discgolfbana',2,'1004',3,'explorer','keystone'),('Slottsskogen open',2020,'Teleborgs discgolfbana',3,'1004',3,'pain','pure'),('Slottsskogen open',2020,'Teleborgs discgolfbana',4,'1004',5,'pain','keystone'),('Slottsskogen open',2020,'Teleborgs discgolfbana',5,'1004',5,'keystone','pure'),('Slottsskogen open',2020,'Teleborgs discgolfbana',6,'1004',5,'gauntlet','pure'),('Slottsskogen open',2020,'Teleborgs discgolfbana',7,'1004',4,'gauntlet','keystone'),('Slottsskogen open',2020,'Teleborgs discgolfbana',8,'1004',6,'gauntlet','keystone'),('Slottsskogen open',2020,'Teleborgs discgolfbana',9,'1004',6,'gauntlet','keystone'),('Slottsskogen open',2020,'Teleborgs discgolfbana',1,'1007',2,'pain','pure'),('Slottsskogen open',2020,'Teleborgs discgolfbana',2,'1007',3,'pain','pure'),('Slottsskogen open',2020,'Teleborgs discgolfbana',3,'1007',1,'pain','keystone'),('Slottsskogen open',2020,'Teleborgs discgolfbana',4,'1007',3,'pain','pure'),('Slottsskogen open',2020,'Teleborgs discgolfbana',5,'1007',2,'river','keystone'),('Slottsskogen open',2020,'Teleborgs discgolfbana',6,'1007',3,'explorer','pure'),('Slottsskogen open',2020,'Teleborgs discgolfbana',7,'1007',2,'fuse','keystone'),('Slottsskogen open',2020,'Teleborgs discgolfbana',8,'1007',2,'explorer','pure'),('Slottsskogen open',2020,'Teleborgs discgolfbana',9,'1007',3,'pain','keystone');
/*!40000 ALTER TABLE `competition_results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discs`
--

DROP TABLE IF EXISTS `discs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discs` (
  `name` varchar(20) NOT NULL,
  `max_weigth` int DEFAULT NULL,
  `speed` smallint DEFAULT NULL,
  `glide` smallint DEFAULT NULL,
  `turn` smallint DEFAULT NULL,
  `fade` smallint DEFAULT NULL,
  `classification` varchar(15) DEFAULT NULL,
  `average_range_beginner` int DEFAULT NULL,
  `average_range_advanced` int DEFAULT NULL,
  `average_range_pro` int DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discs`
--

LOCK TABLES `discs` WRITE;
/*!40000 ALTER TABLE `discs` DISABLE KEYS */;
INSERT INTO `discs` VALUES ('compass',179,5,5,0,1,'midrange',45,70,100),('Cutlass',175,13,5,0,4,'driver',70,100,130),('Explorer',176,7,5,0,2,'fairway driver',60,90,120),('Fuse',181,5,6,1,0,'midrange',50,75,100),('Gauntlet',176,2,4,0,1,'putt',40,65,90),('Keystone',175,2,5,-1,1,'putt',40,65,90),('Knigth',175,14,4,-1,3,'driver',75,105,135),('Pain',180,4,4,0,3,'midrange',55,80,105),('Pure',176,3,3,-1,1,'putt',40,65,90),('river',178,7,7,-1,1,'fairway driver',60,90,120);
/*!40000 ALTER TABLE `discs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `holes`
--

DROP TABLE IF EXISTS `holes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `holes` (
  `name` varchar(40) NOT NULL,
  `hole` int NOT NULL,
  `par` int DEFAULT NULL,
  `distance` int DEFAULT NULL,
  PRIMARY KEY (`name`,`hole`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `holes`
--

LOCK TABLES `holes` WRITE;
/*!40000 ALTER TABLE `holes` DISABLE KEYS */;
INSERT INTO `holes` VALUES ('almhults discgolfbana',1,3,112),('almhults discgolfbana',2,3,76),('almhults discgolfbana',3,3,75),('almhults discgolfbana',4,3,120),('almhults discgolfbana',5,4,127),('almhults discgolfbana',6,3,91),('almhults discgolfbana',7,3,65),('almhults discgolfbana',8,3,100),('almhults discgolfbana',9,3,87),('almhults discgolfbana',10,3,83),('almhults discgolfbana',11,3,67),('almhults discgolfbana',12,3,104),('almhults discgolfbana',13,4,110),('almhults discgolfbana',14,3,100),('almhults discgolfbana',15,3,88),('almhults discgolfbana',16,3,75),('almhults discgolfbana',17,4,128),('almhults discgolfbana',18,3,94),('Teleborgs discgolfbana',1,3,70),('Teleborgs discgolfbana',2,3,71),('Teleborgs discgolfbana',3,3,60),('Teleborgs discgolfbana',4,3,11),('Teleborgs discgolfbana',5,3,57),('Teleborgs discgolfbana',6,4,103),('Teleborgs discgolfbana',7,3,77),('Teleborgs discgolfbana',8,3,91),('Teleborgs discgolfbana',9,3,93);
/*!40000 ALTER TABLE `holes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `playerinfo`
--

DROP TABLE IF EXISTS `playerinfo`;
/*!50001 DROP VIEW IF EXISTS `playerinfo`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `playerinfo` AS SELECT 
 1 AS `id`,
 1 AS `name`,
 1 AS `level`,
 1 AS `nationality`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `players` (
  `id` varchar(20) NOT NULL,
  `name` varchar(25) DEFAULT NULL,
  `level` varchar(14) DEFAULT NULL,
  `nationality` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES ('1001','Alex Smith','pro','USA'),('1002','John Longarm','pro','USA'),('1003','Mia Venetto','advanced','Italy'),('1004','Daniel Ekstrom','advanced','Sweden'),('1005','Johan Gustafsson','beginner','Sweden'),('1006','Max Pettersson','advanced','Sweden'),('1007','Linus Carlsson','pro','Sweden');
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'disc_golf'
--

--
-- Dumping routines for database 'disc_golf'
--

--
-- Final view structure for view `playerinfo`
--

/*!50001 DROP VIEW IF EXISTS `playerinfo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `playerinfo` AS select `players`.`id` AS `id`,`players`.`name` AS `name`,`players`.`level` AS `level`,`players`.`nationality` AS `nationality` from `players` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-15 18:38:04
