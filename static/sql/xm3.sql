/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50722
Source Host           : localhost:3306
Source Database       : xm2

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2021-06-07 21:28:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `_password` varchar(255) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('2', 'test', 'pbkdf2:sha256:150000$4M02BF6G$41bbbb98516cd6ec8a294fc4facdf42ef572507f6e8021228237d061c4d2d9a5', '1569987766@qq.com', 'top');
INSERT INTO `admin` VALUES ('3', '测试', 'pbkdf2:sha256:150000$RorN81ys$0148bde8c25b03bb44f66f5fadd12e386060cc37998b5f8ea9694d7c665aaac0', '159888657@qq.com', 'top');

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('7e3b0a57807d');

-- ----------------------------
-- Table structure for apply
-- ----------------------------
DROP TABLE IF EXISTS `apply`;
CREATE TABLE `apply` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `applyId` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `cost` varchar(50) DEFAULT NULL,
  `level` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `zip` varchar(255) DEFAULT NULL,
  `applyDate` datetime DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `applyId` (`applyId`),
  KEY `ix_apply_applyDate` (`applyDate`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of apply
-- ----------------------------
INSERT INTO `apply` VALUES ('1', '1', '测试名称', '500000000000', '0', '项目完成', '/static/front/images/2.jpg', 'static/front/zips/tupian.rar', '2021-06-04 23:50:12', '得瑟得瑟得瑟得瑟得瑟的');
INSERT INTO `apply` VALUES ('3', '3', '测试名称', '500000000000', '0', '项目归档', '/static/front/images/3.jpg', 'static/front/zips/tupian.rar', '2021-06-01 01:26:04', '得瑟得瑟得瑟得瑟得瑟的');
INSERT INTO `apply` VALUES ('4', '4', 'cccc', '2222', '0', '开展', '/static/front/images/1.jpg', 'static/front/zips/ces.rar', '2021-06-04 23:49:52', 'wwwwww');
INSERT INTO `apply` VALUES ('5', '5', '测试项目', '5000000.00', '0', '申请中', '/static/front/images/1.jpg', 'static/front/zips/8.rar', '2021-06-04 23:48:36', '设计一个测试案例');

-- ----------------------------
-- Table structure for record
-- ----------------------------
DROP TABLE IF EXISTS `record`;
CREATE TABLE `record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userId` int(11) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  `addDate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userId` (`userId`),
  KEY `ix_context_addDate` (`addDate`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of record
-- ----------------------------
INSERT INTO `record` VALUES ('1', '1', '测试sfsfsfsfsfsfsfsfsfsf', '2021-05-31 21:53:47');
INSERT INTO `record` VALUES ('2', '1', 'cecccececec', '2021-05-31 22:26:09');
INSERT INTO `record` VALUES ('5', '1', 'dsdsds', '2021-06-01 00:04:01');
INSERT INTO `record` VALUES ('6', '2', '项目开始', '2021-06-01 21:34:59');
INSERT INTO `record` VALUES ('7', '1', '测试测试', '2021-06-01 22:47:48');
INSERT INTO `record` VALUES ('8', '8', '项目起步', '2021-06-02 23:09:58');
INSERT INTO `record` VALUES ('9', '5', '项目开始动工....', '2021-06-04 23:48:56');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `_password` varchar(100) NOT NULL,
  `phone` varchar(50) NOT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('2', 'test', 'pbkdf2:sha256:150000$nTWWo7w8$679a6fb793448d477667c977b39625d03de73e0791f672ba73b5445429652c44', '1639872000');
INSERT INTO `user` VALUES ('3', 'test123', 'pbkdf2:sha256:150000$vagcvO7G$c9fb1273559608d902117dc1a2c48ea0ed3c72f7c481002c9dc1a27ee77ea45a', '1639872001');
INSERT INTO `user` VALUES ('5', 'abc123', 'pbkdf2:sha256:150000$I4IxreZz$586ce3088ed39ae0452cd521eddecb121ab06ef9ce55864a47adef87a49710b2', '1235978466');

-- ----------------------------
-- Table structure for xiangmu
-- ----------------------------
DROP TABLE IF EXISTS `xiangmu`;
CREATE TABLE `xiangmu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `picture` varchar(255) DEFAULT NULL,
  `detail` varchar(255) DEFAULT NULL,
  `applyId` int(11) DEFAULT NULL,
  `applydate` datetime DEFAULT NULL,
  `finishdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `applyId` (`applyId`),
  KEY `ix_xiangmu_applydate` (`applydate`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xiangmu
-- ----------------------------
INSERT INTO `xiangmu` VALUES ('1', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', '1', '2021-06-01 01:26:04', '2021-06-01 21:41:57');
INSERT INTO `xiangmu` VALUES ('2', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', '2', '2021-06-01 01:26:04', '2021-06-01 21:41:57');
INSERT INTO `xiangmu` VALUES ('3', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', '3', '2021-06-01 01:26:04', '2021-06-01 21:41:57');
INSERT INTO `xiangmu` VALUES ('4', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', '5', '2021-06-01 01:26:04', '2021-06-01 21:41:57');
INSERT INTO `xiangmu` VALUES ('9', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', null, '2021-06-01 01:26:04', null);
INSERT INTO `xiangmu` VALUES ('10', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', null, '2021-06-01 01:26:04', null);
INSERT INTO `xiangmu` VALUES ('11', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', null, '2021-06-01 01:26:04', null);
INSERT INTO `xiangmu` VALUES ('12', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', null, '2021-06-01 01:26:04', null);
INSERT INTO `xiangmu` VALUES ('13', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', null, '2021-06-01 01:26:04', null);
INSERT INTO `xiangmu` VALUES ('14', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', null, '2021-06-01 01:26:04', null);
INSERT INTO `xiangmu` VALUES ('15', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', null, '2021-06-01 01:26:04', null);
INSERT INTO `xiangmu` VALUES ('16', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', '8', '2021-06-01 01:26:04', null);
INSERT INTO `xiangmu` VALUES ('17', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', '8', '2021-06-01 01:26:04', null);
INSERT INTO `xiangmu` VALUES ('18', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', '5', '2021-06-01 01:26:04', null);
INSERT INTO `xiangmu` VALUES ('19', '测试名称', '/static/front/images/3.jpg', '得瑟得瑟得瑟得瑟得瑟的', '5', '2021-06-01 01:26:04', null);
