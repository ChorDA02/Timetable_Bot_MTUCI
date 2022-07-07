-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Июл 07 2022 г., 15:51
-- Версия сервера: 8.0.29-0ubuntu0.20.04.3
-- Версия PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `para`
--

-- --------------------------------------------------------

--
-- Структура таблицы `para`
--

CREATE TABLE `para` (
  `id` int UNSIGNED NOT NULL,
  `num` int NOT NULL,
  `para` varchar(64) NOT NULL,
  `type` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'lek',
  `day` int NOT NULL,
  `week` int NOT NULL,
  `aud` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `para`
--

INSERT INTO `para` (`id`, `num`, `para`, `type`, `day`, `week`, `aud`) VALUES
(1, 1, '-', 'lek', 1, 1, '0'),
(2, 2, '-', 'lek', 1, 1, '0'),
(3, 3, '-', 'lek', 1, 1, '0'),
(4, 4, '-', 'lek', 1, 1, '0'),
(5, 5, '-', 'lek', 1, 1, '0'),
(6, 1, '-', 'lek', 2, 1, '0'),
(7, 2, '-', 'lek', 2, 1, '0'),
(8, 3, '-', 'lek', 2, 1, '0'),
(9, 4, '-', 'lek', 2, 1, '0'),
(10, 5, '-', 'lek', 2, 1, '0'),
(11, 1, '-', 'lek', 3, 1, '0'),
(12, 2, '-', 'lek', 3, 1, '0'),
(13, 3, '-', 'lek', 3, 1, '0'),
(14, 4, '-', 'lek', 3, 1, '0'),
(15, 5, '-', 'lek', 3, 1, '0'),
(16, 1, '-', 'lek', 4, 1, '0'),
(17, 2, '-', 'lek', 4, 1, '0'),
(18, 3, '-', 'lek', 4, 1, '0'),
(19, 4, '-', 'lek', 4, 1, '0'),
(20, 5, '-', 'lek', 4, 1, '0'),
(21, 1, '-', 'lek', 5, 1, '0'),
(22, 2, '-', 'lek', 5, 1, '0'),
(23, 3, '-', 'lek', 5, 1, '0'),
(24, 4, '-', 'lek', 5, 1, '0'),
(25, 5, '-', 'lek', 5, 1, '0'),
(26, 1, '-', 'lek', 1, 0, '0'),
(27, 2, '-', 'lek', 1, 0, '0'),
(28, 3, '-', 'lek', 1, 0, '0'),
(29, 4, '-', 'lek', 1, 0, '0'),
(30, 5, '-', 'lek', 1, 0, '0'),
(31, 1, '-', 'lek', 2, 0, '0'),
(32, 2, '-', 'lek', 2, 0, '0'),
(33, 3, '-', 'lek', 2, 0, '0'),
(34, 4, '-', 'lek', 2, 0, '0'),
(35, 5, '-', 'lek', 2, 0, '0'),
(36, 1, '-', 'lek', 3, 0, '0'),
(37, 2, '-', 'lek', 3, 0, '0'),
(38, 3, '-', 'lek', 3, 0, '0'),
(39, 4, '-', 'lek', 3, 0, '0'),
(40, 5, '-', 'lek', 3, 0, '0'),
(41, 1, '-', 'lek', 4, 0, '0'),
(42, 2, '-', 'lek', 4, 0, '0'),
(43, 3, '-', 'lek', 4, 0, '0'),
(44, 4, '-', 'lek', 4, 0, '0'),
(45, 5, '-', 'lek', 4, 0, '0'),
(46, 1, '-', 'lek', 5, 0, '0'),
(47, 2, '-', 'lek', 5, 0, '0'),
(48, 3, '-', 'lek', 5, 0, '0'),
(49, 4, '-', 'lek', 5, 0, '0'),
(50, 5, '-', 'lek', 5, 0, '0');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `para`
--
ALTER TABLE `para`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `para`
--
ALTER TABLE `para`
  MODIFY `id` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
