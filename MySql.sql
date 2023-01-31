CREATE TABLE `asarr` (
  `PatientID` varchar(200) NOT NULL,
  `NAME` char(200) NOT NULL,
  `BloodGroup` varchar(200) NOT NULL,
  `Branch` varchar(200) NOT NULL,
  `PHONE` varchar(200) NOT NULL,
   PRIMARY KEY (`PatientID`)
);

INSERT INTO `asarr` (`PatientID`, `NAME`, `BloodGroup`, `Branch`, `PHONE`) VALUES
('000000001', 'Jelly', '  A  ', 'Johar Branch', '1230092832'),
('000000002', 'Hammas', '  B  ', 'Clifton Branch', '0328172110'),
('000000003', 'Bong Bong', '  AB  ', 'Liaquatabad', '0928172332'),
('000000004', 'Shafiq', '  O  ', 'Johar Branch', '03280982886'),
('000000005', 'Ceccilla', '  A  ', 'Korangi Branch', '1123982886'),
('000000006', 'Jethalal', '  B  ', 'Liaquatabad', '1112134634'),
('000000007', 'Kiyan', '  AB  ', 'Johar Branch', '1012934634'),
('000000008', 'John', '  O  ', 'Saddar Branch', '1023974123'),
('000000009', 'Ubaid', '  A  ', 'Liaquatabad', '1012973567'),
('000000010', 'Robinito', '  O  ', 'Johar Branch', '1123123123'),
('000000011', 'Komunawa', '  O  ', 'Saddar Branch', '03280986123'),
('000000012', 'Jafar', '  AB  ', 'Liaquatabad', '03280986123'),
('000000013', 'Bisma Mehmood', '  A  ', 'Korangi Branch', '03280986123'),
('000000014', 'Ashraf', '  A  ', 'Johar Branch', '03280986123'),
('000000015', 'Billgates', '  A  ', 'Liaquatabad', '03280986123'),
('000000016', 'Mirza Jameel Baig', '  B  ', 'Clifton Branch', '03280986123'),
('000000017', 'Leonardo Devinci', '  B  ', 'Liaquatabad', '03280986123'),
('000000018', 'Urooj Fatima', '  B  ', 'Saddar Branch', '03280986123'),
('000000019', 'Muhammad Bilal Siddiqui', '  O  ', 'Clifton Branch', '03280986123'),
('000000020', 'Shah Fouz', '  AB  ', 'Liaquatabad', '03280986123');