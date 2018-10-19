CREATE DATABASE segmented;
CREATE TABLE `segmented`.`athlete` (
  `user_id` BIGINT NULL AUTO_INCREMENT,
  `strava_id` INT,
  `firstname` VARCHAR(45) NULL,
  `lastname` VARCHAR(45) NULL,
  `auth` DATETIME NULL,
  `lastLogon` DATETIME NULL,
  `bearer` VARCHAR(45) NULL,
  `public` BOOLEAN NULL,
  PRIMARY KEY (`user_id`));

CREATE TABLE `segmented`.`activityXref` (
  `id` BIGINT NULL AUTO_INCREMENT,
  `strava_id` INT,
  `activity_id` INT,
  PRIMARY KEY (`id`));

  CREATE TABLE `segmented`.`segmentXref` (
    `id` BIGINT NULL AUTO_INCREMENT,
    `strava_id` INT,
    `segment_id` INT,
    `name` VARCHAR(255),
    `distance` INT,
    `activity_type` VARCHAR(45),
    `elevation` INT,
    `total_efforts` INT,
    `athlete_count` INT,
    `user_pr` INT,
    `user_efforts` INT,
    `first_place` INT,
    `tenth_place` INT,
    `rank` INT,
    PRIMARY KEY (`id`));
