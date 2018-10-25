dom = {
    showSongDetails: function (data) {
        let bookInfoDiv = document.querySelector(`#song-${data["song_id"]}-details .song-details-book p`);
        let lyricsDiv = document.querySelector(`#song-${data["song_id"]}-details .song-details-lyrics`);

        bookInfoDiv.innerText = `${data["title_of_book"]} (${data["short_name"]} könyv) ${data["song_number"]}`;
        lyricsDiv.innerText = data["lyrics"];
    },
    initSongDetails: function () {
        let songsContainer = document.querySelector(".index-table-frame");
        let rootUrl = songsContainer.dataset["root"];

        let songTitleDivs = document.querySelectorAll(".song-title");
        for (let divElement of songTitleDivs) {
            let songId = divElement.dataset["id"];
            divElement.addEventListener("click", function () {
                dataHandler.getSongDetails(songId, rootUrl, dom.showSongDetails);
                this.removeEventListener("click", arguments.callee);
            })
        }
    }
};
