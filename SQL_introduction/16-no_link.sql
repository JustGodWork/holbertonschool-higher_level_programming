-- List row with score by descending and name from the second_table only if name is valid
SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL ORDER BY `score` DESC;