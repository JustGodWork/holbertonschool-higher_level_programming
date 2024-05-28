const button = document.getElementById('red_header');
const header = document.querySelector('header');

button.onclick = () => {
    header.classList.add('red');
};