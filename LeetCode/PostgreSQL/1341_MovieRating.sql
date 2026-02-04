(SELECT 
    name AS results
FROM MovieRating
INNER JOIN Users
    ON MovieRating.user_id = Users.user_id
GROUP BY Users.name
ORDER BY COUNT(Users.name) DESC, Users.name ASC
LIMIT 1)

UNION ALL

(SELECT
    title AS results
FROM MovieRating
INNER JOIN Movies
    ON MovieRating.movie_id = Movies.movie_id
WHERE created_at >= DATE '2020-02-01' AND created_at < DATE '2020-03-01'
GROUP BY Movies.title
ORDER BY AVG(MovieRating.rating) DESC, Movies.title ASC
LIMIT 1)