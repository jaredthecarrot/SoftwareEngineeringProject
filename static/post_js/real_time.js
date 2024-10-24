// JavaScript file (e.g., script.js)

// Function to toggle the visibility of the comments section
function toggleComments(event, postId) {
    event.preventDefault(); // Prevent default link behavior
    const commentsSection = document.querySelector(`.comments-section-${postId}`);
    if (commentsSection.style.display === "none" || commentsSection.style.display === "") {
        commentsSection.style.display = "block"; // Show the comments section
    } else {
        commentsSection.style.display = "none"; // Hide the comments section
    }
}

$(document).ready(function() {
    $('.like-btn').click(function(e) {
        e.preventDefault();

        var post_id = $(this).data('post-id');
        var csrf_token = "{{ csrf_token }}";  // Keep the CSRF token here
        // Use the rendered likePostUrl
        var url = likePostUrl;

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'post_id': post_id,
                'csrfmiddlewaretoken': csrf_token
            },
            success: function(response) {
                var likeCountElement = $('#like-count-' + post_id);
                likeCountElement.text('Liked by ' + response.likes_count + ' people');
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });
});