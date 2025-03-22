// Wait until the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Select all vote button elements
    const voteButtons = document.querySelectorAll('.vote-button');

    // Add click event listeners to each vote button
    voteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Get post ID and vote type from data attributes
            const postId = this.dataset.postId;
            const voteType = this.dataset.voteType;
            // Select the element displaying the vote score
            const voteScoreElement = document.getElementById('vote-score-${postId}');
            // Display a loading message while processing the vote
            voteScoreElement.textContent = 'Loading...';

            // Send the vote to the server using fetch API
            fetch('/post/${postId}/vote/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ vote: voteType })
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