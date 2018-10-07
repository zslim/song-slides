# connection to psql
# Limbek Zsófia
# 2018. 10. 07.

library(RPostgreSQL)

get_psql_connection <- function () {
    drv <- dbDriver("PostgreSQL")
    psql_connection <- dbConnect(drv, dbname = "song_slides", host = "localhost",
                                 port = 5432, user = "postgres", 
                                 password = "step_in_psql")
    return(psql_connection)
}

get_max_id <- function(connection, table) {
    greatest_id <- dbGetQuery(connection, paste0("SELECT MAX(id) FROM ", table))$max
    return(greatest_id)
}

write_data_to_table <- function(connection, data, table_name) {
    dbWriteTable(connection, table_name, data, append = TRUE, row.names = FALSE)
}

# dbExistsTable(psql_connection, "songs")

## cleaning up
rm(drv)
