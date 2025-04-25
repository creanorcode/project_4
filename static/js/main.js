// Wait until the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Select all vote button elements
    const voteButtons = document.querySelectorAll('.vote-button');

    // Add click event listeners to each vote button
    voteButtons.forEach(button => {
        button.addEventListener('click', async (e) => {
            e.preventDefault();
            // Get post ID and vote type from data attributes
            const postId = this.dataset.postId;
            const voteType = this.dataset.voteType;
            // Select the element displaying the vote score
            const voteScoreElement = document.getElementById(`vote-score-${postId}`);
            // Display a loading message while processing the vote
            voteScoreElement.textContent = 'Loading...';

            // Send the vote to the server using fetch API
            fetch(`/post/${postId}/vote/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({ vote: voteType }),
            })
            .then(response => {
                // Throw an error if the response is not OK
                if (!response.ok) {
                    throw new Error("An error occurred during voting");
                }
                return response.json();
            })
            .then(data => {
                // Update the vote score with the returned data
                voteScoreElement.textContent = data.vote_score;
            })
            .catch(error => {
                // Display an error message and log the error
                voteScoreElement.textContent = 'Error during vote';
                console.error(error);
            })
        })
    })
})

// Utility function to retrieve a cookie value by name.
// This is used to get CSRF token for secure requests.
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        // Split document.cookie string into individual cookies
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if the cookie string starts with the name we´re looking for
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}