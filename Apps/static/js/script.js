document.addEventListener('DOMContentLoaded', function() {
    fetch('trending-words/')
        .then(response => response.json())
        .then(data => {
            console.log(data); // Log the data to see its structure
            const container = document.getElementById('trending-words-container');
            
            // Access the list of words using the key
            const words = data.keywords; // Replace 'trending_words' with the actual key from your API response
            
            // Check if words is an array
            if (Array.isArray(words)) {
                words.forEach(word => {
                    const paragraph = document.createElement('p');
                    const icon = document.createElement('i');
                    icon.className = "fa fa-check text-primary-gradient me-3"; // Set the classes for the icon
                    paragraph.innerHTML = icon.outerHTML + word; // Combine icon and word
                    container.appendChild(paragraph); // Append the paragraph to the container
                });
            } else {
                console.error('Expected an array but got:', words);
                container.innerHTML = '<p>Error: Expected an array of words.</p>';
            }
        })
        .catch(error => console.error('Error fetching data:', error));
});