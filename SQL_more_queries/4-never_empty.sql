-- Create a table with a column `id` that cannot be NULL.
CREATE TABLE IF NOT EXISTS `id_not_null`
(
    `id` INT DEFAULT 1,
    `name` VARCHAR(256)
)