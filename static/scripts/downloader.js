download = {
    initDownloadButton: function () {
        let downloadButton = document.querySelector("#download-slides-button");
        downloadButton.addEventListener("click", function () {
            $.get(initPage.urls.downloadSlides)
        })
    }
};