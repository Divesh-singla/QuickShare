-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 22, 2024 at 01:08 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quicksharedb`
--

-- --------------------------------------------------------

--
-- Table structure for table `clientuser`
--

CREATE TABLE `clientuser` (
  `clientUserId` int(11) NOT NULL,
  `first_name` text CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `last_name` text CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `email` text CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `user_name` text DEFAULT NULL,
  `password` text DEFAULT NULL,
  `token` text CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `otp` text DEFAULT NULL,
  `date_time` date NOT NULL DEFAULT current_timestamp(),
  `clientRole` text DEFAULT NULL,
  `status` text NOT NULL DEFAULT 'on'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `clientuser`
--

INSERT INTO `clientuser` (`clientUserId`, `first_name`, `last_name`, `email`, `user_name`, `password`, `token`, `otp`, `date_time`, `clientRole`, `status`) VALUES
(1, 'divesh', 'singla', 'diveshsingla9@gmail.com', 'divesh_singla', '25d55ad283aa400af464c76d713c07ad', 'clientabs123', 'Null', '2022-05-04', '1', 'on'),
(27, 'Test ', 'user', 'test@gmail.com', 'test_user', '1234', 'clientTest', NULL, '2024-07-22', NULL, 'on');

-- --------------------------------------------------------

--
-- Table structure for table `fileaccess`
--

CREATE TABLE `fileaccess` (
  `id` int(11) NOT NULL,
  `fileId` int(11) DEFAULT NULL,
  `ClientId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fileaccess`
--

INSERT INTO `fileaccess` (`id`, `fileId`, `ClientId`) VALUES
(7, 27, 1),
(8, 28, 1),
(9, 29, 1),
(10, 30, 1);

-- --------------------------------------------------------

--
-- Table structure for table `fileinfo`
--

CREATE TABLE `fileinfo` (
  `file_id` int(11) NOT NULL,
  `fileName` text NOT NULL,
  `fileLink` text NOT NULL,
  `size` text DEFAULT NULL,
  `date` text NOT NULL,
  `status` text NOT NULL DEFAULT 'ON'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fileinfo`
--

INSERT INTO `fileinfo` (`file_id`, `fileName`, `fileLink`, `size`, `date`, `status`) VALUES
(27, 'Report Format ,B.Tech CSE 8th Sem.docx', '/upload/Report%20Format%20%2CB.Tech%20CSE%208th%20Sem.docx', '94.56 KB', '07/22/2024 01:45:04', 'ON'),
(28, 'TEST of 24 May 2022 (Morning).docx', '/upload/TEST%20of%2024%20May%202022%20(Morning).docx', '474.09 KB', '07/22/2024 01:50:19', 'ON'),
(29, 'sale july till 142.xlsx', '/upload/sale%20july%20till%20142.xlsx', '13.52 KB', '07/22/2024 01:50:22', 'ON'),
(30, 'sale july till 14.xlsx', '/upload/sale%20july%20till%2014.xlsx', '13.52 KB', '22/07/2024 01:50:25', 'ON');

-- --------------------------------------------------------

--
-- Table structure for table `moduleaccess`
--

CREATE TABLE `moduleaccess` (
  `id` int(11) NOT NULL,
  `moduleId` int(11) DEFAULT NULL,
  `roleId` int(11) DEFAULT NULL,
  `edit` int(11) NOT NULL DEFAULT 0,
  `view` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `moduleaccess`
--

INSERT INTO `moduleaccess` (`id`, `moduleId`, `roleId`, `edit`, `view`) VALUES
(1, 1, 1, 1, 1),
(2, 2, 1, 1, 1),
(3, 3, 1, 1, 1),
(4, 4, 1, 1, 1),
(5, 5, 1, 1, 1),
(6, 6, 1, 1, 1),
(7, 7, 1, 1, 1),
(8, 8, 1, 1, 1),
(9, 9, 1, 1, 1),
(10, 10, 1, 1, 1),
(11, 11, 1, 1, 1),
(12, 10, 6, 0, 1),
(13, 2, 6, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `modules`
--

CREATE TABLE `modules` (
  `moduleId` int(11) NOT NULL,
  `module_name` text DEFAULT NULL,
  `date_time` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `modules`
--

INSERT INTO `modules` (`moduleId`, `module_name`, `date_time`) VALUES
(1, 'Upload document', '2024-07-20'),
(14, 'client file download', '2024-07-22');

-- --------------------------------------------------------

--
-- Table structure for table `newmoduleaccess`
--

CREATE TABLE `newmoduleaccess` (
  `id` int(11) NOT NULL,
  `moduleId` int(11) DEFAULT NULL,
  `opsUserId` int(11) DEFAULT NULL,
  `clientUserId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `newmoduleaccess`
--

INSERT INTO `newmoduleaccess` (`id`, `moduleId`, `opsUserId`, `clientUserId`) VALUES
(8, 1, 1, NULL),
(9, 14, NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `userId` int(11) NOT NULL,
  `first_name` text CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `last_name` text CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `email` text CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `user_name` text DEFAULT NULL,
  `password` text DEFAULT NULL,
  `token` text CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `otp` text DEFAULT NULL,
  `date_time` date NOT NULL DEFAULT current_timestamp(),
  `role` text DEFAULT NULL,
  `status` text NOT NULL DEFAULT 'on'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`userId`, `first_name`, `last_name`, `email`, `user_name`, `password`, `token`, `otp`, `date_time`, `role`, `status`) VALUES
(1, 'divesh', 'singla', 'diveshsingla9@gmail.com', 'divesh_singla', '25d55ad283aa400af464c76d713c07ad', 'abs123', '3289', '2022-05-04', '1', 'on');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clientuser`
--
ALTER TABLE `clientuser`
  ADD PRIMARY KEY (`clientUserId`);

--
-- Indexes for table `fileaccess`
--
ALTER TABLE `fileaccess`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fileId` (`fileId`),
  ADD KEY `ClientId` (`ClientId`);

--
-- Indexes for table `fileinfo`
--
ALTER TABLE `fileinfo`
  ADD PRIMARY KEY (`file_id`),
  ADD UNIQUE KEY `filelocation` (`fileLink`) USING HASH;

--
-- Indexes for table `moduleaccess`
--
ALTER TABLE `moduleaccess`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `modules`
--
ALTER TABLE `modules`
  ADD PRIMARY KEY (`moduleId`);

--
-- Indexes for table `newmoduleaccess`
--
ALTER TABLE `newmoduleaccess`
  ADD PRIMARY KEY (`id`),
  ADD KEY `moduleId` (`moduleId`),
  ADD KEY `opsUserId` (`opsUserId`),
  ADD KEY `clientUserId` (`clientUserId`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `clientuser`
--
ALTER TABLE `clientuser`
  MODIFY `clientUserId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `fileaccess`
--
ALTER TABLE `fileaccess`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `fileinfo`
--
ALTER TABLE `fileinfo`
  MODIFY `file_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `moduleaccess`
--
ALTER TABLE `moduleaccess`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `modules`
--
ALTER TABLE `modules`
  MODIFY `moduleId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `newmoduleaccess`
--
ALTER TABLE `newmoduleaccess`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `userId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `fileaccess`
--
ALTER TABLE `fileaccess`
  ADD CONSTRAINT `fileaccess_ibfk_1` FOREIGN KEY (`fileId`) REFERENCES `fileinfo` (`file_id`),
  ADD CONSTRAINT `fileaccess_ibfk_2` FOREIGN KEY (`ClientId`) REFERENCES `clientuser` (`clientUserId`);

--
-- Constraints for table `newmoduleaccess`
--
ALTER TABLE `newmoduleaccess`
  ADD CONSTRAINT `newmoduleaccess_ibfk_1` FOREIGN KEY (`moduleId`) REFERENCES `modules` (`moduleId`),
  ADD CONSTRAINT `newmoduleaccess_ibfk_2` FOREIGN KEY (`opsUserId`) REFERENCES `user` (`userId`),
  ADD CONSTRAINT `newmoduleaccess_ibfk_3` FOREIGN KEY (`clientUserId`) REFERENCES `clientuser` (`clientUserId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
