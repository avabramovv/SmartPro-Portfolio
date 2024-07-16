function parseDate(str) {
    var parts = str.split('.');
    return new Date(parts[2], parts[1] - 1, parts[0]);
}

function sortProjects() {
    var select, sortBy, cards, cardContainer, i;
    select = document.getElementById("sort-select");
    sortBy = select.value;
    cardContainer = document.getElementsByClassName("card-container")[0];
    cards = Array.from(cardContainer.getElementsByClassName("fair-card"));

    cards.sort(function(a, b) {
        var aValue, bValue;
        if (sortBy === "name_ru") {
            aValue = a.getElementsByClassName("fair-card-title")[0].innerHTML.toLowerCase();
            bValue = b.getElementsByClassName("fair-card-title")[0].innerHTML.toLowerCase();
            if (aValue < bValue) {
                return -1;
            }
            if (aValue > bValue) {
                return 1;
            }
            return 0;
        } else if (sortBy === "grade") {
            aValue = parseFloat(a.getElementsByClassName("grade")[0].innerHTML);
            bValue = parseFloat(b.getElementsByClassName("grade")[0].innerHTML);
            return bValue - aValue; // Сортировка по убыванию
        } else if (sortBy === "leader") {
            aValue = a.getElementsByClassName("fair-card-supervisor")[0].innerHTML.toLowerCase();
            bValue = b.getElementsByClassName("fair-card-supervisor")[0].innerHTML.toLowerCase();
            if (aValue < bValue) {
                return -1;
            }
            if (aValue > bValue) {
                return 1;
            }
            return 0;
        } else if (sortBy === "finish_date") {
            aValue = parseDate(a.getElementsByClassName("finish-date")[0].innerHTML);
            bValue = parseDate(b.getElementsByClassName("finish-date")[0].innerHTML);

            return bValue - aValue; // Сортировка по убыванию
        }
    });

    // Очистите контейнер и добавьте отсортированные карточки
    while (cardContainer.firstChild) {
        cardContainer.removeChild(cardContainer.firstChild);
    }
    for (i = 0; i < cards.length; i++) {
        cardContainer.appendChild(cards[i]);
    }
}