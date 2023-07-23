-- Lists all record of a table. Don't list rows without a name value
-- reslt should display score and name in descending order of score
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
