window.addEventListener('scroll', function () {
    var navbar = document.querySelector('.navbar-container');
    if (window.scrollY > 0) {
        navbar.classList.add('navbar-scrolled');
    } else {
        navbar.classList.remove('navbar-scrolled');
    }
});