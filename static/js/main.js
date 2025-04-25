// Wait until the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Select all vote button elements
    const voteButtons = document.querySelectorAll('.vote-button');

    // Add click event listeners to each vote button
    voteButtons.forEach(button => {
        button.addEventListener('click', async (e) => {
            e.preventDefault();
            // Get post ID and vote type from data attributes
            const postId = button.dataset.postId;
            const voteType = button.dataset.voteType;
            // Select the element displaying the vote score
            const voteScoreElement = document.getElementById(`vote-score-${postId}`);
            // Display a loading message while processing the vote
            voteScoreElement.textContent = 'Loading...';

            // Send the vote to the server using fetch API
            try {
                const res = await fetch(`/post/${postId}/vote/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken'),
                    },
                    body: JSON.stringify({ vote: voteType }),
                });
                if (!res.ok) throw new Error('Vote failed');
                const data = await res.json();
                voteScoreElement.textContent = data.vote_score;
            }   catch (err) {
                voteScoreElement.textContent = 'Error during vote';
                console.error(err);
            }
        })
    })
})

// Utility function to retrieve a cookie value by name.
// This is used to get CSRF token for secure requests.
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        // Split document.cookie string into individual cookies
        document.cookie.split(';').forEach(c => {
            c = c.trim();
            if (c.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(c.slice(name.length + 1));
            }
        });
    }
    return cookieValue;
}