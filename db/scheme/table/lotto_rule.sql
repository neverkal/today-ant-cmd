CREATE TABLE `lotto_rule` (
	`idx` INT(11) NOT NULL AUTO_INCREMENT,
	`description` VARCHAR(200) NOT NULL COLLATE 'utf8mb3_general_ci',
	PRIMARY KEY (`idx`) USING BTREE
)
COLLATE='utf8mb3_general_ci'
ENGINE=InnoDB
;