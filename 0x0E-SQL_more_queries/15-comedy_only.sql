-- List Gender
SELECT tv_shows.title
FROM tv_shows
JOIN tv_genres_genres
ON tv_shows.id = tv_shows.genres.genre.show_id
WHERE tv_genres.name = 'Comedy'
ORDER BY show_tv.title;
