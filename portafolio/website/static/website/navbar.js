document.addEventListener('DOMContentLoaded', function() {

    const header = document.querySelector('.navbar');

    window.onscroll = function() {
        var top = window.scrollY;
        if (top >= 100) {
            header.classList.add('navbar-dark', 'bg-dark');
            console.log('added')
        }
        else {
            header.classList.remove('navbar-dark', 'bg-dark');
            console.log('removed');
        }
    }
});