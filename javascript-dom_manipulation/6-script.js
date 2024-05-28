document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
        const character = await response.json();
        const element = document.querySelector('#character');
        element.textContent = character.name;
    } catch (error) {
        console.error("Error fetching character:", error);
    };
});