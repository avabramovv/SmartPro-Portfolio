function filterProjects() {
    var input, filter, cards, cardContainer, title, i;
    input = document.getElementById("search-input");
    filter = input.value.toLowerCase();
    cardContainer = document.getElementsByClassName("card-container")[0];
    cards = cardContainer.getElementsByClassName("fair-card");

    for (i = 0; i < cards.length; i++) {
        title = cards[i].getElementsByClassName("fair-card-title")[0];
        if (title.innerHTML.toLowerCase().indexOf(filter) > -1) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}