SELECT (SELECT SUM(energy) FROM songs) / (SELECT COUNT(energy) FROM songs) AS the_average_energy_of_alL_the_songs;