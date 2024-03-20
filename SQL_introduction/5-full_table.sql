-- Lists all columns from table named first_table in your database.
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';