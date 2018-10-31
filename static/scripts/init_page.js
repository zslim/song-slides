initPage = {
    urls: {},
    getUrls: function() {
        let songsFrame = document.querySelector(".index-table-frame");
        initPage.urls["root"] = songsFrame.dataset["rootUrl"];
        initPage.urls["addSong"] = songsFrame.dataset["addSongUrl"];
        initPage.urls["removeSong"] = songsFrame.dataset["removeSongUrl"];
        initPage.urls["clearCollection"] = songsFrame.dataset["clearCollectionUrl"];
        initPage.urls["downloadSlides"] = songsFrame.dataset["downloadSlidesUrl"];
    },
    getSongDetails: function (songId, callback) {
        let apiUrl = `${initPage.urls["root"]}api/song-details/${songId}`;
        $.get(apiUrl, callback)
    },
    showSongDetails: function (data) {
        let bookInfoDiv = document.querySelector(`#song-${data["song_id"]}-details .song-details-book p`);
        for (let indexRecord of data["index_data"]) {
            let bookInfoParagraph = document.createElement("p");
            bookInfoParagraph.innerText = `${indexRecord["short_name"]} könyv ${indexRecord["song_number"]}`;
            bookInfoDiv.appendChild(bookInfoParagraph);
        }

        let lyricsDiv = document.querySelector(`#song-${data["song_id"]}-details .song-details-lyrics`);
        lyricsDiv.innerText = data["lyrics"];
    },
    initSongDetails: function () {
        let songTitleDivs = document.querySelectorAll(".song-title");
        for (let divElement of songTitleDivs) {
            let songId = divElement.dataset["id"];
            divElement.addEventListener("click", function () {
                initPage.getSongDetails(songId, initPage.showSongDetails);
                this.removeEventListener("click", arguments.callee);
            })
        }
    }
};