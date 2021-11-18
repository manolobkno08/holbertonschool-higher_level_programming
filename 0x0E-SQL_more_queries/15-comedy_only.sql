-- List Gender
SELECT tv_shows.title
FROM tv_shows
JOIN tv_genres
ON tv_shows.genre_id = tv_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY show_tv.title;
