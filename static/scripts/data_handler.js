dataHandler = {
    getSongDetails: function (songId, rootUrl, callback) {
        let apiUrl = `${rootUrl}api/song-details/${songId}`;
        $.get(apiUrl, callback)
    }
};