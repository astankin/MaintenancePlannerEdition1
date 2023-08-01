document.addEventListener('DOMContentLoaded', function () {
    const sidebarMenu = document.getElementById('sidebarMenu');
    const navToggle = document.querySelector('.navbar-toggler');

    navToggle.addEventListener('click', function () {
        sidebarMenu.classList.toggle('show');
    });
});