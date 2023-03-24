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

 Date: 03/06/2021 17:10:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for sign_detail
-- ----------------------------
DROP TABLE IF EXISTS `sign_detail`;
CREATE TABLE `sign_detail`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_time` date NOT NULL,
  `sign_number` smallint(6) NOT NULL,
  `no_sign_number` smallint(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sign_detail
-- ----------------------------
INSERT INTO `sign_detail` VALUES (2, '2021-05-25', 19, 15);
INSERT INTO `sign_detail` VALUES (7, '2021-05-26', 40, 4);
INSERT INTO `sign_detail` VALUES (8, '2021-05-27', 41, 3);
INSERT INTO `sign_detail` VALUES (9, '2021-05-28', 33, 11);
INSERT INTO `sign_detail` VALUES (10, '2021-05-29', 44, 0);
INSERT INTO `sign_detail` VALUES (11, '2021-05-30', 18, 26);
INSERT INTO `sign_detail` VALUES (12, '2021-05-31', 2, 0);
INSERT INTO `sign_detail` VALUES (14, '2021-06-01', 1, 0);

SET FOREIGN_KEY_CHECKS = 1;
