Top Artists by Plays
SELECT artist, COUNT(*) AS play_count
FROM songs_data
GROUP BY artist
ORDER BY play_count DESC
LIMIT 10;

Album Popularity
SELECT album, COUNT(*) AS total_plays
FROM songs_data
GROUP BY album
ORDER BY total_plays DESC;

Total Songs Played
SELECT COUNT(*) AS total_songs
FROM songs_data;
Unique Artists
SELECT COUNT(DISTINCT artist) AS unique_artists
FROM songs_data;

Unique Artists
SELECT COUNT(DISTINCT artist) AS unique_artists
FROM songs_data;