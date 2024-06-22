
  SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
  START TRANSACTION;
  SET time_zone = "+00:00";

  CREATE TABLE `giaithuatnhieu` (
    `ma_gt` varchar(10) NOT NULL,
    `ten_gt` varchar(50) NOT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


  INSERT INTO `giaithuatnhieu` (`ma_gt`, `ten_gt`) VALUES
  ('deep', 'Giải thuật DeepFilterNet'),
  ('no', 'Không chọn giải thuật nhiễu'),
  ('noise', 'Giải thuật NoiseReduce');

  

  CREATE TABLE `ketquataophude` (
    `name_video` varchar(50) NOT NULL,
    `username` varchar(50) NOT NULL,
    `ma_gt` varchar(10) NOT NULL,
    `ma_nn_input` varchar(10) NOT NULL,
    `ma_nn_output` varchar(10) NOT NULL,
    `ngay_up` datetime NOT NULL DEFAULT current_timestamp(),
    `thoigianxuly` varchar(50) NOT NULL,
    `output_srt` varchar(50) NOT NULL,
    `output_mp4` varchar(50) NOT NULL,
    `output_txt` varchar(50)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


  CREATE TABLE `ngonngu` (
    `ma_nn` varchar(10) NOT NULL,
    `ten_nn` varchar(50) NOT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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


  CREATE TABLE `user` (
    `username` varchar(50) NOT NULL,
    `password` varchar(50) NOT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

  INSERT INTO `user` (`username`, `password`) VALUES
  ('toan', '202cb962ac59075b964b07152d234b70');
  
  ALTER TABLE `giaithuatnhieu`
    ADD PRIMARY KEY (`ma_gt`);

  ALTER TABLE `ketquataophude`
    ADD PRIMARY KEY (`name_video`),
    ADD KEY `username` (`username`),
    ADD KEY `ma_nn_output` (`ma_nn_output`),
    ADD KEY `ma_nn_input` (`ma_nn_input`),
    ADD KEY `ma_gt` (`ma_gt`);

  ALTER TABLE `ngonngu`
    ADD PRIMARY KEY (`ma_nn`);

  ALTER TABLE `user`
    ADD PRIMARY KEY (`username`);

  ALTER TABLE `ketquataophude`
    ADD CONSTRAINT `taophude_ibfk_4` FOREIGN KEY (`username`) REFERENCES `user` (`username`),
    ADD CONSTRAINT `taophude_ibfk_5` FOREIGN KEY (`ma_nn_input`) REFERENCES `ngonngu` (`ma_nn`),
    ADD CONSTRAINT `taophude_ibfk_6` FOREIGN KEY (`ma_nn_output`) REFERENCES `ngonngu` (`ma_nn`),
    ADD CONSTRAINT `taophude_ibfk_7` FOREIGN KEY (`ma_gt`) REFERENCES `giaithuatnhieu` (`ma_gt`);
  COMMIT;
