CREATE DATABASE  IF NOT EXISTS `base_datos` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `base_datos`;
-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: base_datos
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
-- Table structure for table `Cliente`
--

DROP TABLE IF EXISTS `Cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cliente` (
  `cliente_id` int(11) NOT NULL AUTO_INCREMENT,
  `cliente_nombre` varchar(45) NOT NULL,
  `cliente_apellido` varchar(45) NOT NULL,
  `cliente_direccion` varchar(45) DEFAULT NULL,
  `cliente_nacimiento` datetime DEFAULT NULL,
  `cliente_telefono` varchar(45) DEFAULT NULL,
  `cliente_mail` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cliente_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cliente`
--

LOCK TABLES `Cliente` WRITE;
/*!40000 ALTER TABLE `Cliente` DISABLE KEYS */;
INSERT INTO `Cliente` VALUES (1,'iuhiuh','kjnkj','kjbnkjb','0000-00-00 00:00:00','kj','kjh');
/*!40000 ALTER TABLE `Cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Detalle`
--

DROP TABLE IF EXISTS `Detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Detalle` (
  `detalle_secuencia` int(11) NOT NULL,
  `detalle_factura` int(11) NOT NULL,
  `detalle_producto` int(11) DEFAULT NULL,
  `detalle_cantidad` int(11) DEFAULT NULL,
  `detalle_descuento` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`detalle_secuencia`,`detalle_factura`),
  KEY `fk_Detalle_factura_idx` (`detalle_factura`),
  KEY `fk_Detalle_Producto_idx` (`detalle_producto`),
  CONSTRAINT `fk_Detalle_factura` FOREIGN KEY (`detalle_factura`) REFERENCES `Factura` (`factura_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Detalle_Producto` FOREIGN KEY (`detalle_producto`) REFERENCES `Producto` (`producto_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Detalle`
--

LOCK TABLES `Detalle` WRITE;
/*!40000 ALTER TABLE `Detalle` DISABLE KEYS */;
/*!40000 ALTER TABLE `Detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Factura`
--

DROP TABLE IF EXISTS `Factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Factura` (
  `factura_id` int(11) NOT NULL,
  `factura_cliente` int(11) DEFAULT NULL,
  `factura_fecha` varchar(45) DEFAULT NULL,
  `factura_modo` int(11) DEFAULT NULL,
  `factura_transaccion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`factura_id`),
  KEY `fk_Factura_cliente_idx` (`factura_cliente`),
  KEY `fk_Factura_modo_idx` (`factura_modo`),
  CONSTRAINT `fk_Factura_modo` FOREIGN KEY (`factura_modo`) REFERENCES `Modo` (`modo_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Factura_cliente` FOREIGN KEY (`factura_cliente`) REFERENCES `Cliente` (`cliente_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Factura`
--

LOCK TABLES `Factura` WRITE;
/*!40000 ALTER TABLE `Factura` DISABLE KEYS */;
/*!40000 ALTER TABLE `Factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Modo`
--

DROP TABLE IF EXISTS `Modo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Modo` (
  `modo_id` int(11) NOT NULL,
  `modo_nombre` varchar(45) DEFAULT NULL,
  `modo_detalles` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`modo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Modo`
--

LOCK TABLES `Modo` WRITE;
/*!40000 ALTER TABLE `Modo` DISABLE KEYS */;
/*!40000 ALTER TABLE `Modo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Producto`
--

DROP TABLE IF EXISTS `Producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Producto` (
  `producto_id` int(11) NOT NULL,
  `producto_nombre` varchar(45) NOT NULL,
  `producto_precio` decimal(10,0) DEFAULT NULL,
  `producto_stock` int(11) DEFAULT NULL,
  PRIMARY KEY (`producto_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Producto`
--

LOCK TABLES `Producto` WRITE;
/*!40000 ALTER TABLE `Producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `Producto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-01-01 11:47:34
