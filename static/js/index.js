const nav_items = document.getElementsByClassName("navigation__item");

function onNavigationItemClick(event) {
    for (let i = 0; i < nav_items.length; i++) {
        nav_items[i].classList.remove("selected");
    }

    event.currentTarget.classList.add("selected");
}

for (let i = 0; i < nav_items.length; i++) {
    nav_items[i].addEventListener('click', onNavigationItemClick, false);
}