-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th12 10, 2022 lúc 06:17 PM
-- Phiên bản máy phục vụ: 10.4.21-MariaDB
-- Phiên bản PHP: 7.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `phude`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `giaithuatnhieu`
--

CREATE TABLE `giaithuatnhieu` (
  `ma_gt` varchar(10) NOT NULL,
  `ten_gt` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `giaithuatnhieu`
--

INSERT INTO `giaithuatnhieu` (`ma_gt`, `ten_gt`) VALUES
('deep', 'Giải thuật DeepFilterNet'),
('no', 'Không chọn giải thuật nhiễu'),
('noise', 'Giải thuật NoiseReduce');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `ketquataophude`
--

CREATE TABLE `ketquataophude` (
  `name_video` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `ma_gt` varchar(10) NOT NULL,
  `ma_nn_input` varchar(10) NOT NULL,
  `ma_nn_output` varchar(10) NOT NULL,
  `ngay_up` datetime NOT NULL DEFAULT current_timestamp(),
  `thoigianxuly` varchar(50) NOT NULL,
  `output_srt` varchar(50) NOT NULL,
  `output_mp4` varchar(50) NOT NULL
  `output_txt` varchar(50)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `ketquataophude`
--

INSERT INTO `ketquataophude` (`name_video`, `username`, `ma_gt`, `ma_nn_input`, `ma_nn_output`, `ngay_up`, `thoigianxuly`, `output_srt`, `output_mp4`) VALUES
('anhang.mp4', 'tong', 'no', 'vi', 'en', '2022-12-01 03:35:06', '0:10:25.738096', 'a123.srt', 'a123.mp4'),
('bun.mp4', 'tong', 'no', 'vi', 'vi', '2022-12-10 23:32:19', '0:01:04.996561', 'tong3k.srt', 'tong3k.mp4');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `ngonngu`
--

CREATE TABLE `ngonngu` (
  `ma_nn` varchar(10) NOT NULL,
  `ten_nn` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `ngonngu`
--

INSERT INTO `ngonngu` (`ma_nn`, `ten_nn`) VALUES
('af', 'Afrikaans'),
('ar', 'Arabic'),
('az', 'Azerbaijani'),
('be', 'Belarusian'),
('bg', 'Bulgarian'),
('bn', 'Bengali'),
('bs', 'Bosnian'),
('ca', 'Catalan'),
('ceb', 'Cebuano'),
('cs', 'Czech'),
('cy', 'Welsh'),
('da', 'Danish'),
('de', 'German'),
('el', 'Greek'),
('en', 'Tiếng Anh'),
('eo', 'Esperanto'),
('es', 'Spanish'),
('et', 'Estonian'),
('eu', 'Basque'),
('fa', 'Persian'),
('fi', 'Finnish'),
('fr', 'French'),
('ga', 'Irish'),
('gl', 'Galician'),
('gu', 'Gujarati'),
('ha', 'Hausa'),
('hi', 'Hindi'),
('hmn', 'Hmong'),
('hr', 'Croatian'),
('ht', 'Haitian Creole'),
('hu', 'Hungarian'),
('hy', 'Armenian'),
('id', 'Indonesian'),
('ig', 'Igbo'),
('is', 'Icelandic'),
('it', 'Italian'),
('iw', 'Hebrew'),
('ja', 'Japanese'),
('jw', 'Javanese'),
('ka', 'Georgian'),
('kk', 'Kazakh'),
('km', 'Khmer'),
('kn', 'Kannada'),
('ko', 'Korean'),
('la', 'Latin'),
('lo', 'Lao'),
('lt', 'Lithuanian'),
('lv', 'Latvian'),
('mg', 'Malagasy'),
('mi', 'Maori'),
('mk', 'Macedonian'),
('ml', 'Malayalam'),
('mn', 'Mongolian'),
('mr', 'Marathi'),
('ms', 'Malay'),
('mt', 'Maltese'),
('my', 'Myanmar(Burmese)'),
('ne', 'Nepale'),
('nl', 'Dutch'),
('no', 'Norwegian'),
('ny', 'Chichewa'),
('pa', 'Punjaabi'),
('pl', 'Polish'),
('pt', 'Portuguese'),
('ro', 'Romanian'),
('ru', 'Russian'),
('si', 'Sinhala'),
('sk', 'Slovak'),
('sl', 'Slovenian'),
('so', 'Somali'),
('sq', 'Albanian'),
('th', 'Thai'),
('tl', 'Filipino'),
('tr', 'Turkish'),
('uk', 'Ukrainian'),
('ur', 'Urdu'),
('uz', 'Uzbek'),
('vi', 'Việt Nam'),
('yi', 'Yiddish'),
('yo', 'Yoruba'),
('zh-CN', 'Tiếng Trung (Giản thể)'),
('zh-TW', 'Tiếng Trung (Truyền thống)'),
('zu', 'Zulu');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `user`
--

CREATE TABLE `user` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `user`
--

INSERT INTO `user` (`username`, `password`) VALUES
('toan', '202cb962ac59075b964b07152d234b70'),
('tong', '202cb962ac59075b964b07152d234b70'),
('tong2', '81dc9bdb52d04dc20036dbd8313ed055');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `giaithuatnhieu`
--
ALTER TABLE `giaithuatnhieu`
  ADD PRIMARY KEY (`ma_gt`);

--
-- Chỉ mục cho bảng `ketquataophude`
--
ALTER TABLE `ketquataophude`
  ADD PRIMARY KEY (`name_video`),
  ADD KEY `username` (`username`),
  ADD KEY `ma_nn_output` (`ma_nn_output`),
  ADD KEY `ma_nn_input` (`ma_nn_input`),
  ADD KEY `ma_gt` (`ma_gt`);

--
-- Chỉ mục cho bảng `ngonngu`
--
ALTER TABLE `ngonngu`
  ADD PRIMARY KEY (`ma_nn`);

--
-- Chỉ mục cho bảng `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `ketquataophude`
--
ALTER TABLE `ketquataophude`
  ADD CONSTRAINT `taophude_ibfk_4` FOREIGN KEY (`username`) REFERENCES `user` (`username`),
  ADD CONSTRAINT `taophude_ibfk_5` FOREIGN KEY (`ma_nn_input`) REFERENCES `ngonngu` (`ma_nn`),
  ADD CONSTRAINT `taophude_ibfk_6` FOREIGN KEY (`ma_nn_output`) REFERENCES `ngonngu` (`ma_nn`),
  ADD CONSTRAINT `taophude_ibfk_7` FOREIGN KEY (`ma_gt`) REFERENCES `giaithuatnhieu` (`ma_gt`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
