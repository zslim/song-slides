import os
import psycopg2
from psycopg2 import extras


def get_connection_string():
    db_user_name = os.environ.get("PSQL_USER")
    db_password = os.environ.get("PSQL_PASSWORD")
    db_host = os.environ.get("PSQL_HOST")
    db_database_name = os.environ.get("PSQL_DB_NAME")

    environment_variables_defined = db_user_name and db_password and db_host and db_database_name

    if not environment_variables_defined:
        raise KeyError("Some of the needed environment variables are not defined")

    connection_string = f"postgresql://{db_user_name}:{db_password}@{db_host}/{db_database_name}"
    return connection_string


def open_database():
    try:
        connection_string = get_connection_string()
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print("Database connection problem")
        raise exception
    return connection


def connection_handler(function_to_wrap):
    def wrapper(*args, **kwargs):
        connection = open_database()
        cursor = connection.cursor(cursor_factory = extras.RealDictCursor)
        returned_value = function_to_wrap(cursor, *args, **kwargs)
        cursor.close()
        connection.close()
        return returned_value
    return wrapper
