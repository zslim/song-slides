import db_connection


@db_connection.connection_handler
def get_song_places(cursor):
    cursor.execute("""
                    SELECT * FROM places
                    """)
    query_result = cursor.fetchall()
    return query_result


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


@db_connection.connection_handler
def get_slide_paths_by_song_id(cursor, tuple_of_song_ids):
    cursor.execute("""
                    SELECT path FROM slides
                    JOIN unnest(%(array_of_song_ids)s::int[])
                        WITH ORDINALITY t(id, ord)
                        ON t.id = slides.song_id
                    WHERE song_id IN %(list_of_song_ids)s
                    ORDER BY t.ord, slide_number;
                    """,
                   {"array_of_song_ids": list(tuple_of_song_ids),
                    "list_of_song_ids": tuple_of_song_ids})
    query_result = cursor.fetchall()
    list_of_slide_paths = [row["path"] for row in query_result]
    return list_of_slide_paths


@db_connection.connection_handler
def get_song_details(cursor, song_id):
    cursor.execute("""
                    SELECT songs.id AS song_id, songs.title, lyrics, b.title AS title_of_book, short_name, song_number
                    FROM songs 
                    JOIN book_index i on songs.id = i.song_id
                    JOIN books b on i.book_id = b.id
                    WHERE songs.id = %(song_id)s
                    """,
                   {"song_id": song_id})
    result = cursor.fetchone()
    return result
