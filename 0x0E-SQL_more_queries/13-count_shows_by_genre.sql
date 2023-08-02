-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked

SELECT g.name AS 'genre', COUNT(g.name) AS 'number_of_shows'
FROM tv_genres g INNER JOIN tv_show_genres s
ON g.id = s.genre_id
GROUP BY g.name
ORDER BY COUNT(g.name) DESC;
