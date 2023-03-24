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

 Date: 03/06/2021 17:10:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for test_bank
-- ----------------------------
DROP TABLE IF EXISTS `test_bank`;
CREATE TABLE `test_bank`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `date_time` date NOT NULL,
  `is_commit` tinyint(1) NOT NULL,
  `is_start` tinyint(1) NOT NULL,
  `is_end` tinyint(1) NOT NULL,
  `exam_end_time` datetime(6) NOT NULL,
  `teachers_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `test_bank_teachers_id_cb84017c_fk_teachers_info_id`(`teachers_id`) USING BTREE,
  CONSTRAINT `test_bank_teachers_id_cb84017c_fk_teachers_info_id` FOREIGN KEY (`teachers_id`) REFERENCES `teachers_info` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of test_bank
-- ----------------------------
INSERT INTO `test_bank` VALUES (1, '5月31日早晨修改', '2021-05-31', 1, 1, 1, '2021-05-31 16:12:00.000000', 1);
INSERT INTO `test_bank` VALUES (2, '第二场考试测试', '2021-05-31', 1, 1, 1, '2021-05-31 16:57:00.000000', 1);
INSERT INTO `test_bank` VALUES (3, '第三场考试', '2021-05-31', 1, 1, 1, '2021-06-01 21:10:00.000000', 1);
INSERT INTO `test_bank` VALUES (4, '5月31日第一次考试', '2021-05-31', 1, 1, 1, '2021-05-31 20:09:00.000000', 2);
INSERT INTO `test_bank` VALUES (5, '5月31日第二次考试', '2021-05-31', 1, 1, 1, '2021-05-31 20:10:00.000000', 2);
INSERT INTO `test_bank` VALUES (6, '5月31日第三次考试', '2021-05-31', 1, 1, 1, '2021-05-31 20:10:00.000000', 2);
INSERT INTO `test_bank` VALUES (7, '第四场考试', '2021-05-31', 1, 1, 1, '2021-06-01 21:46:00.000000', 1);
INSERT INTO `test_bank` VALUES (8, '6月1号第一场考试', '2021-06-01', 1, 1, 1, '2021-06-01 09:12:00.000000', 1);
INSERT INTO `test_bank` VALUES (9, '6月2号第二场考试', '2021-06-01', 0, 0, 0, '2021-06-03 09:25:00.000000', 1);
INSERT INTO `test_bank` VALUES (10, '6月1号考试', '2021-06-01', 1, 1, 1, '2021-06-01 15:22:00.000000', 1);
INSERT INTO `test_bank` VALUES (11, '早晨考试', '2021-06-01', 1, 1, 1, '2021-06-01 17:47:00.000000', 1);

SET FOREIGN_KEY_CHECKS = 1;
