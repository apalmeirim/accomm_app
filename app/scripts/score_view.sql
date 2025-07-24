-- script creates a view to calculate accommodation scores based on proximity to attractions
CREATE OR REPLACE VIEW accommodation_scores AS
SELECT
    a.id,
    a.name,
    COUNT(atr.id) AS nearby_count,
    a.price,
    (COUNT(atr.id)::FLOAT / a.price) AS score
FROM
    accommodation a
JOIN
    attraction atr
    ON ST_DWithin(a.geog, atr.geog, 1000)  -- within 1 km
GROUP BY
    a.id, a.name, a.price
ORDER BY
    score DESC;