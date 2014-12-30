CREATE DATABASE  IF NOT EXISTS `proyecto_laboratorio` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `proyecto_laboratorio`;
-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: proyecto_laboratorio
-- ------------------------------------------------------
-- Server version	5.5.40-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Cuenta`
--

DROP TABLE IF EXISTS `Cuenta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cuenta` (
  `cuenta_id` int(11) NOT NULL,
  `cuenta_nombre` varchar(45) DEFAULT NULL,
  `cuenta_nick` varchar(45) NOT NULL,
  `cuenta_pwd` varchar(45) NOT NULL,
  PRIMARY KEY (`cuenta_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cuenta`
--

LOCK TABLES `Cuenta` WRITE;
/*!40000 ALTER TABLE `Cuenta` DISABLE KEYS */;
INSERT INTO `Cuenta` VALUES (1,'Admin','admin','qwerty');
/*!40000 ALTER TABLE `Cuenta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Editorial`
--

DROP TABLE IF EXISTS `Editorial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Editorial` (
  `editorial_id` int(11) NOT NULL AUTO_INCREMENT,
  `editorial_nombre` varchar(45) NOT NULL,
  `editorial_pais` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`editorial_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Editorial`
--

LOCK TABLES `Editorial` WRITE;
/*!40000 ALTER TABLE `Editorial` DISABLE KEYS */;
INSERT INTO `Editorial` VALUES (1,'Prueba 1','Ecuador'),(2,'Prueba 2','Colombia'),(3,'Prueba 3','Ecuador');
/*!40000 ALTER TABLE `Editorial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Libro`
--

DROP TABLE IF EXISTS `Libro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Libro` (
  `libro_id` int(11) NOT NULL,
  `libro_titulo` varchar(45) NOT NULL,
  `libro_autor` varchar(45) DEFAULT NULL,
  `libro_fecha` date NOT NULL,
  `libro_numregistro` varchar(45) NOT NULL,
  `libro_clave` varchar(45) NOT NULL,
  `libro_volumen` varchar(45) DEFAULT NULL,
  `libro_editorial` varchar(45) DEFAULT NULL,
  `libro_edicion_anio` varchar(45) DEFAULT NULL,
  `libro_procedencia` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`libro_id`),
  KEY `fk_Libro_1_idx` (`libro_editorial`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Libro`
--

LOCK TABLES `Libro` WRITE;
/*!40000 ALTER TABLE `Libro` DISABLE KEYS */;
INSERT INTO `Libro` VALUES (1,'Libro','Autor','2014-12-02','4534','sdsd','asdas','1','asdasd','asdasdsd'),(2,'oijasdasd','s','2014-12-16','HOli','kjh','sdf','1','iuh','iou');
/*!40000 ALTER TABLE `Libro` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-12-19 15:23:22
