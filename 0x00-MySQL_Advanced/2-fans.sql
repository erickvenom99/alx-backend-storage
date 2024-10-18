-script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name,
       DATEDIFF(CURDATE(), debut_date) AS longevity_years
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY longevity_years DESC;
