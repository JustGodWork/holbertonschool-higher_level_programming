const button = document.getElementById('toggle_header');
const header = document.querySelector('header');

button.onclick = () => {
    header.className = header.className !== 'red' ? 'red' : 'green';
};