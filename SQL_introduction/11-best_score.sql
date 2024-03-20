-- List score by descending order from the second_table only if the score is greater or equal to 10
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;