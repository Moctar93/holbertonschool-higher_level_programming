-- Import the database dump from hbtn_0d_tvshows to your MySQL server


SELECT tv_genres.name AS 'genre', COUNT(*) AS 'number_of_shows'
FROM tv_show_genres
LEFT JOIN tv_genres ON tv_genres.id = genre_id
GROUP BY genre_id
ORDER BY COUNT(*) DESC;
