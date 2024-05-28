
const button = document.getElementById('red_header');
const header = document.querySelector('header');

const colorChanger = () => {
    header.style.color = '#FF0000';
}

button.addEventListener('click', colorChanger);