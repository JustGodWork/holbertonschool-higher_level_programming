document.addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector('#add_item');

    button.addEventListener('click', () => {
        const list = document.querySelector('.my_list');
        const item = document.createElement('li');

        item.textContent = 'Item';
        list.appendChild(item);
    });
});