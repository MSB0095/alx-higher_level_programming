-- lists all records of the table
-- Don’t list rows without a name value
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
