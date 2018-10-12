import db_connection


@db_connection.connection_handler
def get_songs_without_slides(cursor):
    cursor.execute("""
                    SELECT songs.id, title, lyrics
                    FROM songs LEFT JOIN slides s2 on songs.id = s2.song_id
                    WHERE s2.id IS NULL
                    ORDER BY songs.id;
                    """)
    list_of_records = cursor.fetchall()
    return list_of_records


@db_connection.connection_handler
def save_new_slide(cursor, dict_of_slide):
    cursor.execute("""
                    INSERT INTO slides (song_id, slide_number, path) 
                    VALUES (%(song_id)s, %(slide_number)s, %(path)s) 
                    """,
                   dict_of_slide)


@db_connection.connection_handler
def get_songs_with_slides(cursor):
    cursor.execute("""
                    SELECT DISTINCT songs.id, title, lyrics
                    FROM songs LEFT JOIN slides s2 on songs.id = s2.song_id
                    WHERE s2.id IS NOT NULL
                    ORDER BY songs.id;
                    """)
    list_of_records = cursor.fetchall()
    return list_of_records
