utils = {
    appendToElement: function (parentElement, textToAppend) {
        let tempDiv = document.createElement("div");
        tempDiv.innerHTML = textToAppend.trim();
        for (let node of tempDiv.childNodes) {
            parentElement.appendChild(node);
        }
    }
};