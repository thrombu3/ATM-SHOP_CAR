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

 Date: 03/06/2021 17:10:37
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for teachers_info
-- ----------------------------
DROP TABLE IF EXISTS `teachers_info`;
CREATE TABLE `teachers_info`  (
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
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  UNIQUE INDEX `mobile`(`mobile`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of teachers_info
-- ----------------------------
INSERT INTO `teachers_info` VALUES (1, '林海峰', 0, 'linhaifeng', '123', '110', 'icon/default.png', '12323@11.com', '2021-05-31 15:58:02.709459', 1, 1, '教师');
INSERT INTO `teachers_info` VALUES (2, '刘清政', 0, 'liuqingzheng', '123', '120', 'icon/default.png', '110@qq.com', '2021-05-31 15:58:33.709075', 1, 1, '教师');
INSERT INTO `teachers_info` VALUES (3, '陈阳', 0, 'chenyang', '123', '130', 'icon/default.png', '111@qq.com', '2021-05-31 15:59:05.086777', 1, 1, '教师');

SET FOREIGN_KEY_CHECKS = 1;
