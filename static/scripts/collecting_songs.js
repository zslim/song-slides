songCollector = {
    init: function () {
        songCollector.initDropdownItems();
        songCollector.showCurrentCollection();
        songCollector.initClearButton();
    },
    initClearButton: function () {
        let clearButton = document.querySelector("#clear-collection-button");
        clearButton.addEventListener("click", function () {
            $.post(initPage.urls["clearCollection"]);
        })
    },
    initDropdownItems: function () {
        let dropdownItems = document.querySelectorAll(".dropdown-item");
        for (let item of dropdownItems) {
            let songId = item.dataset["id"];
            let dropdownButton = document.querySelector(`#song-${songId}-dropdown-button`);
            let place = item.innerText;
            item.addEventListener("click", function () {
                let songInfo = {id: songId, place: place};
                $.post(initPage.urls["addSong"], songInfo, function () {
                    songCollector.changeDropdownButton(dropdownButton, place);
                });
            })
        }
    },
    changeDropdownButton: function (buttonElement, place) {
        buttonElement.innerHTML = place;
        buttonElement.classList.remove("btn-success");
        buttonElement.classList.add("btn-info");
    },
    getCurrentCollection: function () {
        let bodyTag = document.querySelector("body");
        let collectionString = bodyTag.dataset["currentCollection"];
        let collectionObject = JSON.parse(collectionString);
        return collectionObject;
    },
    showCurrentCollection: function () {
        let collection = songCollector.getCurrentCollection();
        for (let item of collection) {
            let songId = item["id"];
            let dropdownButton = document.querySelector(`#song-${songId}-dropdown-button`);
            songCollector.changeDropdownButton(dropdownButton, item["place"]);

        }
    }
};