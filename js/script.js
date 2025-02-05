window.addEventListener('scroll', function () {
    var navbar = document.querySelector('.navbar-container');
    if (window.scrollY > 0) {
        navbar.classList.add('navbar-scrolled');
    } else {
        navbar.classList.remove('navbar-scrolled');
    }
});

year = new Date().getFullYear();
// change copyrigth year
document.getElementsByClassName('copyright')[0].innerHTML = `Dzulfikri Adjmal &copy; ${year}`;

