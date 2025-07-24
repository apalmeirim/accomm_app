-- script updates the geography columns in the accommodation and attraction tables"
UPDATE accommodation
SET geog = ST_SetSRID(ST_MakePoint(longitude, latitude), 4326)::geography
WHERE geog IS NULL;


UPDATE attraction
SET geog = ST_SetSRID(ST_MakePoint(longitude, latitude), 4326)::geography
WHERE geog IS NULL;