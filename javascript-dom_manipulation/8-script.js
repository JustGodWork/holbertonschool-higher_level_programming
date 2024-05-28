document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
        const translation = await response.json();
        const element = document.querySelector('#hello');
        element.innerHTML = translation.hello;
    } catch (error) {
        console.error("Error fetching translation:", error);
    };
});