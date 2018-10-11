# data handling
# Limbek Zsófia
# 2018.10.07.

# BE CAREFUL BEFORE YOU RUN THIS SCRIPT
# CHECK whether these tables exist in the database and if so what they contain

setwd("~/PycharmProjects/enekrend/data/R_scripts")
source("dtx_parser_kekkonyv.R")
current_book_id <- 1

setwd("~/PycharmProjects/enekrend/data/R_scripts")
source("psql_connection.R")

psql_connection <- get_psql_connection()

# creating tables that can be written into the database

songs_to_db <- data.frame(id = songs$id, title = songs$title, lyrics = songs$lyrics, 
                          stringsAsFactors = FALSE)

book_index_id_start <- NA
greatest_book_id <- get_max_id(psql_connection, "book_index")
if (is.na(greatest_book_id)) {
    book_index_id_start <- 1
} else {book_index_id_start <- greatest_book_id + 1}
number_of_entries <- nrow(songs)
book_index_id <- seq(from = book_index_id_start, by = 1, length.out = number_of_entries)
book_id_vector <- rep(current_book_id, number_of_entries)

book_index_to_db <- data.frame(id = book_index_id, song_id = songs$id, 
                               book_id = book_id_vector, song_number = songs$number, 
                               stringsAsFactors = FALSE)

# write_data_to_table(psql_connection, songs_to_db, "songs") # számít a sorrend, mert a song id foreign key a book index táblában
# write_data_to_table(psql_connection, book_index_to_db, "book_index")

write.csv(slides[, c("song_id", "slide_number", "slide_first", "slide_last")],
          file = "../slides.csv", row.names = FALSE, fileEncoding = "UTF-8")

