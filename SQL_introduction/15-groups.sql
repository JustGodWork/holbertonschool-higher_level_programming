-- List the number of times each score appears in the second_table
SELECT `score`, COUNT(*) AS `number` From `second_table` GROUP BY `score` ORDER BY `number` DESC;