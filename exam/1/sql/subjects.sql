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

 Date: 03/06/2021 17:10:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for subjects
-- ----------------------------
DROP TABLE IF EXISTS `subjects`;
CREATE TABLE `subjects`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` smallint(6) NOT NULL,
  `question` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `teachers_id` int(11) NOT NULL,
  `test_bank_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `subjects_teachers_id_9c806626_fk_teachers_info_id`(`teachers_id`) USING BTREE,
  INDEX `subjects_test_bank_id_f86e45af_fk_test_bank_id`(`test_bank_id`) USING BTREE,
  CONSTRAINT `subjects_test_bank_id_f86e45af_fk_test_bank_id` FOREIGN KEY (`test_bank_id`) REFERENCES `test_bank` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `subjects_teachers_id_9c806626_fk_teachers_info_id` FOREIGN KEY (`teachers_id`) REFERENCES `teachers_info` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of subjects
-- ----------------------------
INSERT INTO `subjects` VALUES (2, 2, '2+2=？', 1, 1);
INSERT INTO `subjects` VALUES (3, 2, '5+5=？', 1, 1);
INSERT INTO `subjects` VALUES (4, 2, '3+3=？', 1, 1);
INSERT INTO `subjects` VALUES (5, 2, '1==1？', 1, 2);
INSERT INTO `subjects` VALUES (6, 2, '2*2？', 1, 2);
INSERT INTO `subjects` VALUES (7, 2, '1+1=？', 2, 4);
INSERT INTO `subjects` VALUES (8, 2, '2+2=？', 2, 4);
INSERT INTO `subjects` VALUES (9, 2, '2*2=？', 2, 5);
INSERT INTO `subjects` VALUES (10, 2, '3*3=？', 2, 5);
INSERT INTO `subjects` VALUES (11, 2, '3-2=？', 2, 6);
INSERT INTO `subjects` VALUES (12, 2, '1+1=？', 1, 3);
INSERT INTO `subjects` VALUES (13, 2, '2+2=？', 1, 7);
INSERT INTO `subjects` VALUES (14, 2, '1+1=？', 1, 8);
INSERT INTO `subjects` VALUES (15, 2, '2+2=？', 1, 8);
INSERT INTO `subjects` VALUES (16, 2, '1+1=', 1, 10);
INSERT INTO `subjects` VALUES (17, 2, '1+1=?', 1, 11);
INSERT INTO `subjects` VALUES (18, 2, '2*2=?', 1, 11);

SET FOREIGN_KEY_CHECKS = 1;
