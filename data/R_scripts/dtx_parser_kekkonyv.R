# !! A kék könyv dtx-ét elkezdtem átnézni, sok dalnál betördeltem a sorokat
# Végig kellene nézni dalonként, kottával, sorrendben.
# hint: a 116-osnál vannak az első látványosan túl hosszú sorok
# Amúgy a script működik, yay! :) - songs és slides táblákat állít elő
# jöhet a következő tábla

# Énekrend projekt, dtx feldolgozás
# 2018.09.21.
# Limbek Zsófia

library(stringr)

# defining some useful functions

get_song_numbers <- function(titles) {
    return(regmatches(titles, regexpr("[0-9]+/?[A-Z]?", titles)))  # remélem ez jó lesz a sárga és a zöld könyvnél is...
}

strip_leading_whitespace <- function(char_vector) {
    return(sub("^ +", "", char_vector))
}
# the yellow & green books don't have song titles so there first lines need to be extracted as titles
get_song_titles <- function(titles) { 
    vect_of_titles <- character()
    for (line in titles) {
        number <- get_song_numbers(line)
        line_start <- paste0(">", number)
        title <- sub(line_start, "", line)
        vect_of_titles <- c(vect_of_titles, title)
    }
    titles_without_spaces <- strip_leading_whitespace(vect_of_titles)
    return(titles_without_spaces) 
}

setwd("~/PycharmProjects/enekrend/data/data_scources/")
# reading file

file_path <- "demo_kek.dtx"

## a fájlnak dalcímmel (>-vel kezdődő sorral) kell kezdődnie!
raw_data <- scan(file_path, "character", sep = "\n", blank.lines.skip = F,
                 strip.white = TRUE)
raw_data <- strip_leading_whitespace(raw_data)

# getting song number & title into data frame
title_lines <- grep("^>", raw_data, value = TRUE)

songs <- data.frame(number = get_song_numbers(title_lines),
                    title = get_song_titles(title_lines),
                    stringsAsFactors = FALSE)

# getting lyrics & slide number & data about lyrics distribution among slides

songs$lyrics <- NA
songs$slide_starts <- list(NA)
lyrics_of_song <- list(number = NA, lyrics = NA, slide_starts = 1)
# sorry about this massive non-R-ish loop
for (line in c(raw_data, ">")) {
    if (substr(line, 1, 1) == ">") { # start of new song; writing last song into table
        if (!is.na(lyrics_of_song$number)) {
            index <- which(songs$number == lyrics_of_song$number) # it would be better to filter by song number as it is unique
            songs$lyrics[index] <- lyrics_of_song$lyrics
            songs$slide_starts[[index]] <- lyrics_of_song$slide_starts
            new_number <- get_song_numbers(line)
            lyrics_of_song <- list(number = new_number, lyrics = NA, slide_starts = 1)
        } else {
            lyrics_of_song$number <- get_song_numbers(line)
        }
    } else if (substr(line, 1, 1) == "/") {
        next
    }else if (substr(line, 1, 1) == "#") { # start of new slide
        if (!is.na(lyrics_of_song$lyrics)) {
            lyrics_of_song$lyrics <- paste(lyrics_of_song$lyrics, "\n", sep = "")
            num_of_lines <- str_count(lyrics_of_song$lyrics, "\n")
            lyrics_of_song$slide_starts <- c(lyrics_of_song$slide_starts, num_of_lines)
        }
    } else { # line of lyrics
        if (is.na(lyrics_of_song$lyrics)) { # first line on slide
            lyrics_of_song$lyrics <- paste0(line, "\n")
        } else {
            lyrics_of_song$lyrics <- paste(lyrics_of_song$lyrics, line, "\n", sep = "")
        }
    }
}
songs$number_of_slides <- sapply(songs$slide_starts, length)
# getting ids for songs
songs$id <- as.numeric(rownames(songs))
# sorting columns in songs
songs <- songs[c("id", "number", "title", "lyrics", "number_of_slides", "slide_starts")]
## cleaning up
rm(index, lyrics_of_song, line, new_number, num_of_lines, title_lines)

# creating a table for slides
slides <- as.data.frame(matrix(ncol = 2, nrow = 0))
for(i in 1:nrow(songs)) {
    for (j in songs$slide_starts[[i]]) {
        slides[nrow(slides) + 1, 1] <- songs$id[i]
        slides[nrow(slides), 2] <- j
    }
}
names(slides) <- c("song_id", "slide_first")
## saving slide numbers
slide_number <- numeric()
for (k in unique(slides$song_id)){
    slides_of_song <- slides[slides$song_id == k,]
    slide_number <- c(slide_number, 1:nrow(slides_of_song))
}
slides$slide_number <- slide_number
slides$id <- rownames(slides)
slides <- slides[c("id", "song_id", "slide_number", "slide_first")]
# works for the sample :)

## cleaning up
rm(file_path, i, j, k, raw_data, slide_number, get_song_numbers, get_song_titles, 
   strip_leading_whitespace, slides_of_song)
