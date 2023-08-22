CREATE TABLE IF NOT EXISTS "doc"."netflix_titles" (
   "show_id" TEXT PRIMARY KEY,
   "type" TEXT,
   "title" TEXT,
   "director" TEXT,
   "cast" ARRAY(TEXT),
   "country" TEXT,
   "date_added" TIMESTAMP,
   "release_year" TEXT,
   "rating" TEXT,
   "duration" TEXT,
   "listed_in"  ARRAY(TEXT),
   "description" TEXT INDEX using fulltext
) CLUSTERED INTO 1 SHARDS;