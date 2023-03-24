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

 Date: 03/06/2021 17:09:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for grade
-- ----------------------------
DROP TABLE IF EXISTS `grade`;
CREATE TABLE `grade`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `source` smallint(6) NOT NULL,
  `test_paper_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `test_paper_id`(`test_paper_id`) USING BTREE,
  CONSTRAINT `grade_test_paper_id_a9ca492b_fk_test_paper_id` FOREIGN KEY (`test_paper_id`) REFERENCES `test_paper` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 134 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of grade
-- ----------------------------
INSERT INTO `grade` VALUES (1, 90, 1);
INSERT INTO `grade` VALUES (2, 0, 2);
INSERT INTO `grade` VALUES (3, 100, 3);
INSERT INTO `grade` VALUES (4, 0, 4);
INSERT INTO `grade` VALUES (5, 0, 5);
INSERT INTO `grade` VALUES (6, 0, 6);
INSERT INTO `grade` VALUES (7, 0, 7);
INSERT INTO `grade` VALUES (8, 0, 8);
INSERT INTO `grade` VALUES (11, 75, 11);
INSERT INTO `grade` VALUES (51, 75, 12);
INSERT INTO `grade` VALUES (52, 75, 13);
INSERT INTO `grade` VALUES (53, 75, 14);
INSERT INTO `grade` VALUES (54, 75, 15);
INSERT INTO `grade` VALUES (55, 75, 16);
INSERT INTO `grade` VALUES (56, 75, 17);
INSERT INTO `grade` VALUES (57, 75, 18);
INSERT INTO `grade` VALUES (58, 75, 19);
INSERT INTO `grade` VALUES (59, 75, 20);
INSERT INTO `grade` VALUES (60, 85, 21);
INSERT INTO `grade` VALUES (61, 85, 22);
INSERT INTO `grade` VALUES (62, 85, 23);
INSERT INTO `grade` VALUES (63, 85, 24);
INSERT INTO `grade` VALUES (64, 85, 25);
INSERT INTO `grade` VALUES (65, 85, 26);
INSERT INTO `grade` VALUES (66, 85, 27);
INSERT INTO `grade` VALUES (67, 85, 28);
INSERT INTO `grade` VALUES (68, 85, 29);
INSERT INTO `grade` VALUES (69, 85, 30);
INSERT INTO `grade` VALUES (70, 55, 31);
INSERT INTO `grade` VALUES (71, 55, 32);
INSERT INTO `grade` VALUES (72, 55, 33);
INSERT INTO `grade` VALUES (73, 55, 34);
INSERT INTO `grade` VALUES (74, 55, 35);
INSERT INTO `grade` VALUES (75, 55, 36);
INSERT INTO `grade` VALUES (76, 55, 37);
INSERT INTO `grade` VALUES (77, 55, 38);
INSERT INTO `grade` VALUES (78, 55, 39);
INSERT INTO `grade` VALUES (79, 55, 40);
INSERT INTO `grade` VALUES (80, 100, 41);
INSERT INTO `grade` VALUES (81, 100, 42);
INSERT INTO `grade` VALUES (82, 100, 43);
INSERT INTO `grade` VALUES (83, 100, 44);
INSERT INTO `grade` VALUES (84, 100, 45);
INSERT INTO `grade` VALUES (85, 95, 46);
INSERT INTO `grade` VALUES (86, 95, 47);
INSERT INTO `grade` VALUES (87, 95, 48);
INSERT INTO `grade` VALUES (88, 95, 49);
INSERT INTO `grade` VALUES (89, 95, 50);
INSERT INTO `grade` VALUES (90, 75, 51);
INSERT INTO `grade` VALUES (91, 75, 52);
INSERT INTO `grade` VALUES (92, 75, 53);
INSERT INTO `grade` VALUES (93, 75, 54);
INSERT INTO `grade` VALUES (94, 75, 55);
INSERT INTO `grade` VALUES (95, 75, 56);
INSERT INTO `grade` VALUES (96, 75, 57);
INSERT INTO `grade` VALUES (97, 75, 58);
INSERT INTO `grade` VALUES (98, 75, 59);
INSERT INTO `grade` VALUES (99, 75, 60);
INSERT INTO `grade` VALUES (100, 65, 61);
INSERT INTO `grade` VALUES (101, 66, 62);
INSERT INTO `grade` VALUES (102, 67, 63);
INSERT INTO `grade` VALUES (103, 85, 64);
INSERT INTO `grade` VALUES (104, 85, 65);
INSERT INTO `grade` VALUES (105, 85, 66);
INSERT INTO `grade` VALUES (106, 85, 67);
INSERT INTO `grade` VALUES (107, 85, 68);
INSERT INTO `grade` VALUES (108, 85, 69);
INSERT INTO `grade` VALUES (109, 85, 70);
INSERT INTO `grade` VALUES (110, 55, 71);
INSERT INTO `grade` VALUES (111, 55, 72);
INSERT INTO `grade` VALUES (112, 55, 73);
INSERT INTO `grade` VALUES (113, 55, 74);
INSERT INTO `grade` VALUES (114, 55, 75);
INSERT INTO `grade` VALUES (115, 55, 76);
INSERT INTO `grade` VALUES (116, 55, 77);
INSERT INTO `grade` VALUES (117, 55, 78);
INSERT INTO `grade` VALUES (118, 55, 79);
INSERT INTO `grade` VALUES (119, 55, 80);
INSERT INTO `grade` VALUES (120, 100, 81);
INSERT INTO `grade` VALUES (121, 100, 82);
INSERT INTO `grade` VALUES (122, 100, 83);
INSERT INTO `grade` VALUES (123, 44, 84);
INSERT INTO `grade` VALUES (124, 43, 85);
INSERT INTO `grade` VALUES (125, 95, 86);
INSERT INTO `grade` VALUES (126, 95, 87);
INSERT INTO `grade` VALUES (127, 95, 88);
INSERT INTO `grade` VALUES (128, 95, 89);
INSERT INTO `grade` VALUES (129, 95, 90);
INSERT INTO `grade` VALUES (130, 85, 91);
INSERT INTO `grade` VALUES (131, 0, 92);
INSERT INTO `grade` VALUES (132, 100, 93);
INSERT INTO `grade` VALUES (133, 95, 94);

SET FOREIGN_KEY_CHECKS = 1;
