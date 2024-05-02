$(document).ready(function() {
    // Function to fetch live values using AJAX
    function fetchLiveValues() {
        $.ajax({
            url: '/get_live_values/',  // URL to your Django API endpoint
            type: 'GET',
            success: function(data) {
                // Update HTML elements with live values
                $('#live-value-1').text(data);
                // Update more HTML elements as needed
            },
            error: function(xhr, status, error) {
                console.error('Error fetching live values:', error);
            }
        });
    }

    // Fetch live values initially when the page loads
    fetchLiveValues();

    // Set interval to fetch live values periodically (e.g., every 5 seconds)
    setInterval(fetchLiveValues, 5000);  // Adjust the interval as needed
});
