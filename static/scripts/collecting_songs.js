songCollector = {
    initDropdownItems: function () {
        let dropdownItems = document.querySelectorAll(".dropdown-item");
        for (let item of dropdownItems) {
            let songId = item.dataset["id"];
            let dropdownButton = document.querySelector(`#song-${songId}-dropdown-button`);
            item.addEventListener("click", function () {
                dropdownButton.innerHTML = item.innerText;
                dropdownButton.classList.remove("btn-success");
                dropdownButton.classList.add("btn-info");
            })
        }
    }
};