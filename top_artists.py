import duckdb

duckdb.sql("""
    SELECT master_metadata_album_artist_name,
           ROUND(SUM(ms_played) / 3600000.0, 1) AS total_hours,
           COUNT(*) AS total_streams,
           ROUND(SUM(ms_played) / COUNT(*) / 60000.0, 1) AS avg_minutes_per_stream
    FROM read_json_auto('data/raw/Streaming_History_Audio_*.json')
    GROUP BY master_metadata_album_artist_name
    ORDER BY total_hours DESC
    LIMIT 10;

""").show()