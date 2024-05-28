document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
        const data = await response.json();
        const movie_list = document.querySelector('#list_movies');
        /** @type {Array} */
        const movies = data.results;

        movies.forEach(movie => {
            const item = document.createElement('li');
            item.textContent = movie.title;
            movie_list.appendChild(item);
        });
    } catch (error) {
        console.error("Error fetching movies:", error);
    };
});