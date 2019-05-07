INSERT INTO project1.tfidf (SELECT song_id, t.token, count*LOG((SELECT COUNT(DISTINCT song_id) as total_number FROM project1.token)/(dfi)) AS score
From project1.token t
LEFT JOIN
(
  SELECT token,COUNT (*) AS dfi
  FROM project1.token
  GROUP BY token
) AS df
ON t.token=df.token);
