CREATE TABLE `lotto_round_num` (
	`round_key` VARCHAR(20) NOT NULL COLLATE 'utf8mb3_general_ci',
	`num` VARCHAR(20) NOT NULL COLLATE 'utf8mb3_general_ci',
	`round_date` DATETIME NOT NULL,
	`bonus_tf` TINYINT(1) NULL DEFAULT '0',
	PRIMARY KEY (`round_key`, `num`) USING BTREE
)
COLLATE='utf8mb3_general_ci'
ENGINE=InnoDB
;