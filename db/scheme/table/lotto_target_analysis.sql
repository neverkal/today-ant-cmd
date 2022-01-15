CREATE TABLE `lotto_target_analysis` (
	`target_round` VARCHAR(20) NOT NULL COLLATE 'utf8mb3_general_ci',
	`target_num` VARCHAR(100) NOT NULL COLLATE 'utf8mb3_general_ci',
	`use_tf` TINYINT(1) NOT NULL DEFAULT '0',
	`rule_idx` INT(11) NULL DEFAULT NULL,
	PRIMARY KEY (`target_num`) USING BTREE
)
COLLATE='utf8mb3_general_ci'
ENGINE=InnoDB
;
