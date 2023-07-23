-- Liststhe number of records with the same score
-- display score
-- display the number of records for the score with the label number
-- the kist should be sorted by the nummber of records(descending)
SELECT score, COUNT(score) AS `number`
FROM second_table
GROUP BY score
ORDER BY `number` DESC;
