initPage = {
    urls: {},
    getUrls: function() {
        let songsFrame = document.querySelector(".index-table-frame");
        initPage.urls["root"] = songsFrame.dataset["rootUrl"];
        initPage.urls["addSong"] = songsFrame.dataset["addSongUrl"];
        initPage.urls["removeSong"] = songsFrame.dataset[""];
        initPage.urls["clearCollection"] = songsFrame.dataset["clearCollectionUrl"];
    },
    getSongDetails: function (songId, callback) {
        let apiUrl = `${initPage.urls["root"]}api/song-details/${songId}`;
        $.get(apiUrl, callback)
    },
    showSongDetails: function (data) {
        let bookInfoDiv = document.querySelector(`#song-${data["song_id"]}-details .song-details-book p`);
        let lyricsDiv = document.querySelector(`#song-${data["song_id"]}-details .song-details-lyrics`);

        bookInfoDiv.innerText = `${data["title_of_book"]} (${data["short_name"]} könyv) ${data["song_number"]}`;
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