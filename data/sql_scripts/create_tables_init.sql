CREATE TABLE "songs" (
	"id" serial NOT NULL,
	"title" varchar(60) NOT NULL,
	"lyrics" TEXT NOT NULL,
	CONSTRAINT songs_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "slides" (
	"id" serial NOT NULL,
	"song_id" integer NOT NULL,
	"slide_number" integer NOT NULL,
	"path" varchar(100) NOT NULL,
	CONSTRAINT slides_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "books" (
	"id" serial NOT NULL,
	"title" varchar(50) NOT NULL,
	"short_name" varchar(50) NOT NULL,
	CONSTRAINT books_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "book_index" (
	"id" serial NOT NULL,
	"book_id" integer NOT NULL,
	"song_id" integer NOT NULL,
	"song_number" integer NOT NULL,
	"page_number" integer NOT NULL,
	CONSTRAINT book_index_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);




ALTER TABLE "slides" ADD CONSTRAINT "slides_fk0" FOREIGN KEY ("song_id") REFERENCES "songs"("id");


ALTER TABLE "book_index" ADD CONSTRAINT "book_index_fk0" FOREIGN KEY ("book_id") REFERENCES "books"("id");
ALTER TABLE "book_index" ADD CONSTRAINT "book_index_fk1" FOREIGN KEY ("song_id") REFERENCES "songs"("id");

