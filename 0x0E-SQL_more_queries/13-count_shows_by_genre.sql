-- List Gender
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre.id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres_id = tv_genres.id
WHERE tv_show_genres.show_id IS NULL
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
