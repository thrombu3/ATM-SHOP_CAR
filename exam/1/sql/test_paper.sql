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

 Date: 03/06/2021 17:10:54
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for test_paper
-- ----------------------------
DROP TABLE IF EXISTS `test_paper`;
CREATE TABLE `test_paper`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `commit_time` datetime(6) NULL DEFAULT NULL,
  `answer` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_check` tinyint(1) NOT NULL,
  `students_id` int(11) NOT NULL,
  `test_bank_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `test_paper_students_id_24a4525b_fk_students_info_id`(`students_id`) USING BTREE,
  INDEX `test_paper_test_bank_id_1b0d4cd6_fk_test_bank_id`(`test_bank_id`) USING BTREE,
  CONSTRAINT `test_paper_test_bank_id_1b0d4cd6_fk_test_bank_id` FOREIGN KEY (`test_bank_id`) REFERENCES `test_bank` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `test_paper_students_id_24a4525b_fk_students_info_id` FOREIGN KEY (`students_id`) REFERENCES `students_info` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 95 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of test_paper
-- ----------------------------
INSERT INTO `test_paper` VALUES (1, '2021-05-31 16:10:20.946309', '[{\"id\":2,\"question\":\"2+2=？\",\"answer\":\"4\"},{\"id\":3,\"question\":\"5+5=？\",\"answer\":\"10\"},{\"id\":4,\"question\":\"3+3=？\",\"answer\":\"7\"}]', 1, 1, 1);
INSERT INTO `test_paper` VALUES (2, '2021-05-31 16:12:00.403527', '[{\"id\":2,\"question\":\"2+2=？\",\"answer\":\"4\"},{\"id\":3,\"question\":\"5+5=？\",\"answer\":\"12\"},{\"id\":4,\"question\":\"3+3=？\",\"answer\":\"1231\"}]', 1, 2, 1);
INSERT INTO `test_paper` VALUES (3, '2021-05-31 16:42:59.606148', '[{\"id\":5,\"question\":\"1==1？\",\"answer\":\"一个男人大于一个女人\"},{\"id\":6,\"question\":\"2*2？\",\"answer\":\"4\"}]', 1, 1, 2);
INSERT INTO `test_paper` VALUES (4, '2021-05-31 16:51:00.292043', '[{\"id\":5,\"question\":\"1==1？\",\"answer\":\"true\"},{\"id\":6,\"question\":\"2*2？\",\"answer\":\"4\"}]', 0, 3, 2);
INSERT INTO `test_paper` VALUES (5, '2021-05-31 16:56:59.212909', '[{\"id\":5,\"question\":\"1==1？\",\"answer\":\"true\"},{\"id\":6,\"question\":\"2*2？\",\"answer\":\"4\"}]', 0, 4, 2);
INSERT INTO `test_paper` VALUES (6, '2021-05-31 20:08:58.890946', '[{\"id\":7,\"question\":\"1+1=？\",\"answer\":\"2\"},{\"id\":8,\"question\":\"2+2=？\",\"answer\":\"4\"}]', 0, 2, 4);
INSERT INTO `test_paper` VALUES (7, '2021-05-31 20:09:51.330686', '[{\"id\":9,\"question\":\"2*2=？\",\"answer\":\"4\"},{\"id\":10,\"question\":\"3*3=？\",\"answer\":\"9\"}]', 0, 2, 5);
INSERT INTO `test_paper` VALUES (8, '2021-05-31 20:09:58.974028', '[{\"id\":11,\"question\":\"3-2=？\",\"answer\":\"1\"}]', 0, 2, 6);
INSERT INTO `test_paper` VALUES (11, '2021-05-31 21:19:23.385951', '[{\"id\":12,\"question\":\"1+1=？\",\"answer\":\"2\"}]', 1, 1, 3);
INSERT INTO `test_paper` VALUES (12, '2021-05-31 21:35:21.526263', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 2, 3);
INSERT INTO `test_paper` VALUES (13, '2021-05-31 21:35:21.526263', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 3, 3);
INSERT INTO `test_paper` VALUES (14, '2021-05-31 21:35:21.526263', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 4, 3);
INSERT INTO `test_paper` VALUES (15, '2021-05-31 21:35:21.526263', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 5, 3);
INSERT INTO `test_paper` VALUES (16, '2021-05-31 21:35:21.526263', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 6, 3);
INSERT INTO `test_paper` VALUES (17, '2021-05-31 21:35:21.526263', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 7, 3);
INSERT INTO `test_paper` VALUES (18, '2021-05-31 21:35:21.526263', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 8, 3);
INSERT INTO `test_paper` VALUES (19, '2021-05-31 21:35:21.526263', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 9, 3);
INSERT INTO `test_paper` VALUES (20, '2021-05-31 21:35:21.526263', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 10, 3);
INSERT INTO `test_paper` VALUES (21, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 11, 3);
INSERT INTO `test_paper` VALUES (22, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 12, 3);
INSERT INTO `test_paper` VALUES (23, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 13, 3);
INSERT INTO `test_paper` VALUES (24, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 14, 3);
INSERT INTO `test_paper` VALUES (25, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 15, 3);
INSERT INTO `test_paper` VALUES (26, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 16, 3);
INSERT INTO `test_paper` VALUES (27, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 17, 3);
INSERT INTO `test_paper` VALUES (28, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 18, 3);
INSERT INTO `test_paper` VALUES (29, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 19, 3);
INSERT INTO `test_paper` VALUES (30, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 20, 3);
INSERT INTO `test_paper` VALUES (31, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 21, 3);
INSERT INTO `test_paper` VALUES (32, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 22, 3);
INSERT INTO `test_paper` VALUES (33, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 23, 3);
INSERT INTO `test_paper` VALUES (34, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 24, 3);
INSERT INTO `test_paper` VALUES (35, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 25, 3);
INSERT INTO `test_paper` VALUES (36, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 26, 3);
INSERT INTO `test_paper` VALUES (37, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 27, 3);
INSERT INTO `test_paper` VALUES (38, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 28, 3);
INSERT INTO `test_paper` VALUES (39, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 29, 3);
INSERT INTO `test_paper` VALUES (40, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 30, 3);
INSERT INTO `test_paper` VALUES (41, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 31, 3);
INSERT INTO `test_paper` VALUES (42, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 32, 3);
INSERT INTO `test_paper` VALUES (43, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 33, 3);
INSERT INTO `test_paper` VALUES (44, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 34, 3);
INSERT INTO `test_paper` VALUES (45, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 35, 3);
INSERT INTO `test_paper` VALUES (46, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 36, 3);
INSERT INTO `test_paper` VALUES (47, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 37, 3);
INSERT INTO `test_paper` VALUES (48, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 38, 3);
INSERT INTO `test_paper` VALUES (49, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 39, 3);
INSERT INTO `test_paper` VALUES (50, '2021-05-31 21:35:21.527284', '[{\"id\": 12, \"question\": \"1+1=\\uff1f\", \"answer\": \"2\"}]', 1, 40, 3);
INSERT INTO `test_paper` VALUES (51, '2021-05-31 21:52:02.914255', '[{\"id\":13,\"question\":\"2+2=？\",\"answer\":\"4\"}]', 1, 1, 7);
INSERT INTO `test_paper` VALUES (52, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 2, 7);
INSERT INTO `test_paper` VALUES (53, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 3, 7);
INSERT INTO `test_paper` VALUES (54, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 4, 7);
INSERT INTO `test_paper` VALUES (55, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 5, 7);
INSERT INTO `test_paper` VALUES (56, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 6, 7);
INSERT INTO `test_paper` VALUES (57, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 7, 7);
INSERT INTO `test_paper` VALUES (58, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 8, 7);
INSERT INTO `test_paper` VALUES (59, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 9, 7);
INSERT INTO `test_paper` VALUES (60, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 10, 7);
INSERT INTO `test_paper` VALUES (61, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 11, 7);
INSERT INTO `test_paper` VALUES (62, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 12, 7);
INSERT INTO `test_paper` VALUES (63, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 13, 7);
INSERT INTO `test_paper` VALUES (64, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 14, 7);
INSERT INTO `test_paper` VALUES (65, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 15, 7);
INSERT INTO `test_paper` VALUES (66, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 16, 7);
INSERT INTO `test_paper` VALUES (67, '2021-05-31 21:54:18.102264', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 17, 7);
INSERT INTO `test_paper` VALUES (68, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 18, 7);
INSERT INTO `test_paper` VALUES (69, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 19, 7);
INSERT INTO `test_paper` VALUES (70, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 20, 7);
INSERT INTO `test_paper` VALUES (71, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 21, 7);
INSERT INTO `test_paper` VALUES (72, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 22, 7);
INSERT INTO `test_paper` VALUES (73, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 23, 7);
INSERT INTO `test_paper` VALUES (74, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 24, 7);
INSERT INTO `test_paper` VALUES (75, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 25, 7);
INSERT INTO `test_paper` VALUES (76, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 26, 7);
INSERT INTO `test_paper` VALUES (77, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 27, 7);
INSERT INTO `test_paper` VALUES (78, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 28, 7);
INSERT INTO `test_paper` VALUES (79, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 29, 7);
INSERT INTO `test_paper` VALUES (80, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 30, 7);
INSERT INTO `test_paper` VALUES (81, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 31, 7);
INSERT INTO `test_paper` VALUES (82, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 32, 7);
INSERT INTO `test_paper` VALUES (83, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 33, 7);
INSERT INTO `test_paper` VALUES (84, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 34, 7);
INSERT INTO `test_paper` VALUES (85, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 35, 7);
INSERT INTO `test_paper` VALUES (86, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 36, 7);
INSERT INTO `test_paper` VALUES (87, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 37, 7);
INSERT INTO `test_paper` VALUES (88, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 38, 7);
INSERT INTO `test_paper` VALUES (89, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 39, 7);
INSERT INTO `test_paper` VALUES (90, '2021-05-31 21:54:18.103265', '[{\"id\": 13, \"question\": \"2+2=\\uff1f\", \"answer\": \"4\"}]', 1, 40, 7);
INSERT INTO `test_paper` VALUES (91, '2021-06-01 09:11:59.243409', '[{\"id\":14,\"question\":\"1+1=？\",\"answer\":\"2\"},{\"id\":15,\"question\":\"2+2=？\",\"answer\":\"4\"}]', 1, 4, 8);
INSERT INTO `test_paper` VALUES (92, '2021-06-01 09:11:59.517040', '[{\"id\":14,\"question\":\"1+1=？\"},{\"id\":15,\"question\":\"2+2=？\"}]', 0, 1, 8);
INSERT INTO `test_paper` VALUES (93, '2021-06-01 15:21:59.624376', '[{\"id\":16,\"question\":\"1+1=\",\"answer\":\"2\"}]', 1, 1, 10);
INSERT INTO `test_paper` VALUES (94, '2021-06-01 17:46:10.804476', '[{\"id\":17,\"question\":\"1+1=?\",\"answer\":\"2\"},{\"id\":18,\"question\":\"2*2=?\",\"answer\":\"22\"}]', 1, 1, 11);

SET FOREIGN_KEY_CHECKS = 1;
