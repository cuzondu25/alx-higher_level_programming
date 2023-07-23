-- Lists aall records with a score >= 10 in the table second_table
-- display both the score and the name ordered by score(decending)
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC
