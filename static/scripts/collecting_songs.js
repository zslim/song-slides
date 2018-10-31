songCollector = {
    init: function () {
        songCollector.initSongPlaceItems();
        songCollector.showCurrentCollection();
        songCollector.initDropSongItems();
    },
    initSongPlaceItems: function () {
        let songPlaceItems = document.querySelectorAll(".add-to-collection");
        for (let item of songPlaceItems) {
            let songId = item.dataset["id"];
            let songTitle = item.dataset["title"];
            let placeId = item.dataset["placeId"];
            let dropdownButton = document.querySelector(`#song-${songId}-dropdown-button`);
            let place = item.innerText;
            item.addEventListener("click", function () {
                let songInfo = {id: songId, title: songTitle, placeId: placeId, place: place};
                $.post(initPage.urls["addSong"], songInfo, function () {
                    songCollector.enableDropFromCollection(songId);
                    songCollector.changeDropdownButton(dropdownButton, place, placeId);
                    songCollector.showSongOnCollectionTab(songTitle, songId, placeId);
                });
            })
        }
    },
    showSongOnCollectionTab: function (songTitle, songId, placeId) {
        let songTitleFrame = document.querySelector(`#collection-tab-row-${placeId} .song-title-frame`);
        songTitleFrame.innerText = songTitle;
        songTitleFrame.id = `song-${songId}-on-place-${placeId}`;
    },
    deleteSongFromCollectionTab: function (songId, placeId) {
        let divToEmpty = document.querySelector(`#song-${songId}-on-place-${placeId}`);
        divToEmpty.innerText = "";
    },
    initDropSongItems: function () {  // TODO: put bin icon into split button instead
        let dropSongItems = document.querySelectorAll(".drop-from-collection");
        for (let item of dropSongItems) {
            let songId = item.dataset["id"];
            let requestData = {id: songId};
            let dropdownButton = document.querySelector(`#song-${songId}-dropdown-button`);
            item.addEventListener("click", function (event) {
                if (item.classList.contains("disabled")) {
                    event.stopPropagation();
                } else {
                    let placeId = dropdownButton.dataset.placeId;
                    $.post(initPage.urls.removeSong, requestData, function () {
                        songCollector.setOriginalDropdownButton(dropdownButton);
                        songCollector.disableDropFromCollection(songId);
                        songCollector.deleteSongFromCollectionTab(songId, placeId);
                    })
                }
            })
        }
    },
    changeDropdownButton: function (buttonElement, place, placeId) {
        buttonElement.innerHTML = place;
        buttonElement.classList.remove("btn-success");
        buttonElement.classList.add("btn-info");
        buttonElement.dataset.placeId = placeId;
    },
    setOriginalDropdownButton: function (buttonElement) {
        buttonElement.innerHTML = '<i class="fas fa-plus">&nbsp;</i>';
        buttonElement.classList.remove("btn-info");
        buttonElement.classList.add("btn-success");
    },
    enableDropFromCollection: function (songId) {
        let dropSongItem = document.querySelector(`#drop-song-${songId}`);
        dropSongItem.classList.remove("disabled");
    },
    disableDropFromCollection: function (songId) {
        let dropSongItem = document.querySelector(`#drop-song-${songId}`);
        dropSongItem.classList.add("disabled");
        dropSongItem.addEventListener("click", function (event) {
            event.stopPropagation();
        })
    },
    getCurrentCollection: function () {
        let bodyTag = document.querySelector("body");
        let collectionString = bodyTag.dataset["currentCollection"];
        if (collectionString === "") collectionString = null;
        let collectionObject = JSON.parse(collectionString);
        return collectionObject;
    },
    showCurrentCollection: function () {
        let collection = songCollector.getCurrentCollection();
        if (collection != null) {
            for (let item of collection) {
                let songId = item["id"];
                let dropdownButton = document.querySelector(`#song-${songId}-dropdown-button`);
                songCollector.changeDropdownButton(dropdownButton, item["place"], item["placeId"]);
                songCollector.enableDropFromCollection(songId);
                songCollector.showSongOnCollectionTab(item["title"], songId, item["placeId"]);
            }
        }
    }/*,
    renderSelectedSongTemplate: function (songTitle, place) {
        let context = {place: place, song_title: songTitle};
        let templateSource = document.querySelector("#selected-song-template").innerHTML;
        let template = Handlebars.compile(templateSource);
        let rowHtml = template(context);
        return rowHtml;
    }*/
};