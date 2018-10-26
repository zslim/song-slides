songCollector = {
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
                $.post(initPage.urls["addSong"], songInfo);
                dropdownButton.innerHTML = place;
                dropdownButton.classList.remove("btn-success");
                dropdownButton.classList.add("btn-info");
            })
        }
    }
};