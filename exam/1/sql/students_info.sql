/*
 Navicat MySQL Data Transfer

 Source Server         : oldboy-exa
 Source Server Type    : MariaDB
 Source Server Version : 50568
 Source Host           : 101.200.207.212:3306
 Source Schema         : oldboy_exa

 Target Server Type    : MariaDB
 Target Server Version : 50568
 File Encoding         : 65001

 Date: 03/06/2021 17:10:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for students_info
-- ----------------------------
DROP TABLE IF EXISTS `students_info`;
CREATE TABLE `students_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` smallint(6) NOT NULL,
  `username` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `mobile` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `portrait` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `role_id` smallint(6) NOT NULL,
  `role_name` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `classes` smallint(6) NOT NULL,
  `age` smallint(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  UNIQUE INDEX `mobile`(`mobile`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 45 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of students_info
-- ----------------------------
INSERT INTO `students_info` VALUES (1, '彭万里', 0, 'py-111111', '12', '18256600683', 'icon/default.png', '1771@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (2, '高大山', 0, 'py-111112', '123123', '1772', 'icon/default.png', '1772@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (3, '谢大海', 0, 'py-111113', '123123', '1773', 'icon/default.png', '1773@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (4, '马宏宇', 0, 'py-111114', '123123', '1774', 'icon/default.png', '1774@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (5, '马继祖', 0, 'py-111115', '123123', '1775', 'icon/default.png', '1775@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (6, '关仁', 0, 'py-111116', '123123', '1776', 'icon/default.png', '1776@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (7, '孙露露', 1, 'py-111117', '123123', '1777', 'icon/default.png', '1777@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (8, '孙曦哲', 1, 'py-111118', '123123', '1778', 'icon/default.png', '1778@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (9, '孙春南', 0, 'py-111119', '123123', '1779', 'icon/default.png', '1779@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (10, '刘长胜', 0, 'py-111120', '123123', '1780', 'icon/default.png', '1780@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (11, '吴国梁', 0, 'py-111121', '123123', '1781', 'icon/default.png', '1781@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (12, '徐浩言', 0, 'py-111122', '123123', '1782', 'icon/default.png', '1782@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (13, '许鸿才', 0, 'py-111123', '123123', '1783', 'icon/default.png', '1783@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (14, '宋海昌', 0, 'py-111124', '123123', '1784', 'icon/default.png', '1784@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (15, '郭震海 ', 0, 'py-111125', '123123', '1785', 'icon/default.png', '1785@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (16, '程蝉', 1, 'py-111126', '123123', '1786', 'icon/default.png', '1786@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (17, '崔岱远', 0, 'py-111127', '123123', '1787', 'icon/default.png', '1787@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (18, '李龙飞', 0, 'py-111128', '123123', '1788', 'icon/default.png', '1788@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (19, '古清生', 0, 'py-111129', '123123', '1789', 'icon/default.png', '1789@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (20, '花狸', 1, 'py-111130', '123123', '1790', 'icon/default.png', '1790@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (21, '地瓜猪', 0, 'py-111131', '123123', '1791', 'icon/default.png', '1791@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (22, '路佳瑄', 1, 'py-111132', '123123', '1792', 'icon/default.png', '1792@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (23, '慕雪柠', 0, 'py-111133', '1234', '17718250570', 'icon/default.png', '1793@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (24, '慕雪寒', 0, 'py-111134', '123123', '1794', 'icon/default.png', '1794@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (25, '商吹歌', 0, 'py-111135', '123123', '1795', 'icon/default.png', '1795@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (26, '李小小', 0, 'py-111136', '123123', '1796', 'icon/default.png', '1796@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (27, '王佳', 0, 'py-111137', '123123', '1797', 'icon/default.png', '1797@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (28, '唐佳颖', 0, 'py-111138', '123123', '1798', 'icon/default.png', '1798@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (29, '汤方实', 1, 'py-111139', '123123', '1799', 'icon/default.png', '1799@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (30, '王东', 1, 'py-111140', '123123', '17100', 'icon/default.png', '17100@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (31, '李云', 0, 'py-111141', '123123', '17101', 'icon/default.png', '17101@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (32, '夏雪', 0, 'py-111142', '123123', '17102', 'icon/default.png', '17102@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (33, '易佳丽', 0, 'py-111143', '123123', '17103', 'icon/default.png', '17103@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (34, '董美丽', 0, 'py-111144', '123123', '17104', 'icon/default.png', '17104@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (35, '杨继学', 0, 'py-111145', '123123', '17105', 'icon/default.png', '17105@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (36, '利妮可', 0, 'py-111146', '123123', '17106', 'icon/default.png', '17106@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (37, '应剑杰 ', 0, 'py-111147', '123123', '17107', 'icon/default.png', '17107@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (38, '应敏超', 1, 'py-111148', '123123', '17108', 'icon/default.png', '17108@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (39, '王蓓', 0, 'py-111149', '123123', '17109', 'icon/default.png', '17109@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (40, '陈晨', 0, 'py-111150', '123123', '17110', 'icon/default.png', '17110@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (41, '洛熙', 0, 'py-111151', '123123', '17111', 'icon/default.png', '17111@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (42, '欧辰', 1, 'py-111152', '123123', '17112', 'icon/default.png', '17112@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);
INSERT INTO `students_info` VALUES (43, '衣晨', 0, 'py-111153', '123123', '17113', 'icon/default.png', '17113@163.com', '2021-05-25 19:40:21.202462', 1, 2, '学生', 1, 28);
INSERT INTO `students_info` VALUES (44, '衣渐离', 1, 'py-111154', '123123', '17114', 'icon/default.png', '17114@163.com', '2021-05-25 22:51:32.844648', 1, 2, '学生', 0, 18);

SET FOREIGN_KEY_CHECKS = 1;
