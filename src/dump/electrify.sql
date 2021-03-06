-- MariaDB dump 10.19  Distrib 10.6.5-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: electrify
-- ------------------------------------------------------
-- Server version	10.6.5-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `electrify`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `electrify` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `electrify`;

--
-- Table structure for table `chat`
--

DROP TABLE IF EXISTS `chat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chat` (
  `sender_id` varchar(100) NOT NULL,
  `receiver_id` varchar(100) NOT NULL,
  `message` text NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat`
--

LOCK TABLES `chat` WRITE;
/*!40000 ALTER TABLE `chat` DISABLE KEYS */;
/*!40000 ALTER TABLE `chat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credential`
--

DROP TABLE IF EXISTS `credential`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `credential` (
  `user_id` varchar(100) NOT NULL DEFAULT uuid(),
  `username` varchar(100) NOT NULL,
  `password` text NOT NULL,
  `role` enum('Pelanggan','Teknisi','Admin') NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credential`
--

LOCK TABLES `credential` WRITE;
/*!40000 ALTER TABLE `credential` DISABLE KEYS */;
INSERT INTO `credential` (`user_id`, `username`, `password`, `role`) VALUES ('dce749d4-e2b4-47ca-87c7-e4397f9b10d9','Lizardy','$2b$12$Pfwl17XrlfDNjZ.cs1NeAuMzQ9TKQRHUHr5AaQMYylwbWKAkG0ley','Pelanggan'),('e64e24aa-1f82-4dcc-8b5e-8736afc701bc','mahesa','$2b$12$T8eZMrFkgT6IiiC8.3APte5DJtTIQWWOe7h1HI1VuWUGa/kkjdBvu','Teknisi');
/*!40000 ALTER TABLE `credential` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `feedback_id` varchar(100) NOT NULL DEFAULT uuid(),
  `user_id` varchar(100) NOT NULL,
  `order_id` varchar(100) NOT NULL,
  `rating` int(11) NOT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`feedback_id`),
  KEY `user_id` (`user_id`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `userdetail` (`user_id`),
  CONSTRAINT `feedback_ibfk_2` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `installeditem`
--

DROP TABLE IF EXISTS `installeditem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `installeditem` (
  `order_id` varchar(100) NOT NULL,
  `product_id` varchar(100) NOT NULL,
  `installation_date` date NOT NULL,
  `quantity` int(11) NOT NULL,
  `technician_id` varchar(100) NOT NULL,
  PRIMARY KEY (`order_id`,`product_id`,`installation_date`),
  KEY `product_id` (`product_id`),
  KEY `technician_id` (`technician_id`),
  CONSTRAINT `installeditem_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`),
  CONSTRAINT `installeditem_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`),
  CONSTRAINT `installeditem_ibfk_3` FOREIGN KEY (`technician_id`) REFERENCES `userdetail` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `installeditem`
--

LOCK TABLES `installeditem` WRITE;
/*!40000 ALTER TABLE `installeditem` DISABLE KEYS */;
/*!40000 ALTER TABLE `installeditem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderitem`
--

DROP TABLE IF EXISTS `orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orderitem` (
  `order_id` varchar(100) NOT NULL,
  `product_id` varchar(100) NOT NULL,
  `quantity` int(11) NOT NULL,
  PRIMARY KEY (`order_id`,`product_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `orderitem_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`),
  CONSTRAINT `orderitem_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderitem`
--

LOCK TABLES `orderitem` WRITE;
/*!40000 ALTER TABLE `orderitem` DISABLE KEYS */;
INSERT INTO `orderitem` (`order_id`, `product_id`, `quantity`) VALUES ('10ee370d-c063-11ec-a7d7-8030493e57b8','866078fc-c062-11ec-a7d7-8030493e57b8',4),('981b7506-c062-11ec-a7d7-8030493e57b8','866078fc-c062-11ec-a7d7-8030493e57b8',2),('e356dea8-c05c-11ec-a7d7-8030493e57b8','866078fc-c062-11ec-a7d7-8030493e57b8',2),('e356dea8-c05c-11ec-a7d7-8030493e57b8','a82ad5c5-c05c-11ec-a7d7-8030493e57b8',1);
/*!40000 ALTER TABLE `orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `order_id` varchar(100) NOT NULL DEFAULT uuid(),
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `customer_id` varchar(100) NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` (`order_id`, `timestamp`, `customer_id`) VALUES ('10ee370d-c063-11ec-a7d7-8030493e57b8','2022-04-20 04:33:31','dce749d4-e2b4-47ca-87c7-e4397f9b10d9'),('981b7506-c062-11ec-a7d7-8030493e57b8','2022-04-20 04:30:08','dce749d4-e2b4-47ca-87c7-e4397f9b10d9'),('e356dea8-c05c-11ec-a7d7-8030493e57b8','2022-04-20 03:49:17','e64e24aa-1f82-4dcc-8b5e-8736afc701bc');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `product_id` varchar(100) NOT NULL DEFAULT uuid(),
  `name` varchar(100) NOT NULL,
  `stock` int(11) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` (`product_id`, `name`, `stock`) VALUES ('866078fc-c062-11ec-a7d7-8030493e57b8','Produk2',10),('a82ad5c5-c05c-11ec-a7d7-8030493e57b8','Produk1',10);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `techniciancertificate`
--

DROP TABLE IF EXISTS `techniciancertificate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `techniciancertificate` (
  `certificate_id` varchar(100) NOT NULL,
  `user_id` varchar(100) NOT NULL,
  `certificate_name` varchar(300) NOT NULL,
  `certificate_url` text NOT NULL,
  PRIMARY KEY (`certificate_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `techniciancertificate_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `credential` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `techniciancertificate`
--

LOCK TABLES `techniciancertificate` WRITE;
/*!40000 ALTER TABLE `techniciancertificate` DISABLE KEYS */;
/*!40000 ALTER TABLE `techniciancertificate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket` (
  `ticket_id` varchar(100) NOT NULL DEFAULT uuid(),
  `title` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `priority` enum('1','2','3') NOT NULL,
  `type` enum('1','2','3','4') NOT NULL,
  `attachment_url` text DEFAULT NULL,
  `user_id` varchar(100) NOT NULL,
  PRIMARY KEY (`ticket_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `userdetail` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userdetail`
--

DROP TABLE IF EXISTS `userdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userdetail` (
  `user_id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `address` text NOT NULL,
  `telephone` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `userdetail_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `credential` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userdetail`
--

LOCK TABLES `userdetail` WRITE;
/*!40000 ALTER TABLE `userdetail` DISABLE KEYS */;
INSERT INTO `userdetail` (`user_id`, `name`, `address`, `telephone`) VALUES ('dce749d4-e2b4-47ca-87c7-e4397f9b10d9','Lizardy','Kebakkramat,Karanganyar','08231570042'),('e64e24aa-1f82-4dcc-8b5e-8736afc701bc','Mahesa','Antapani, Bandung','08231570041');
/*!40000 ALTER TABLE `userdetail` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-20 11:48:11
