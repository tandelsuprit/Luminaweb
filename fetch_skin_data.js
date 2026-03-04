// Standalone fetch request for dashboard.html - Copy this into your <script> tag

// Get user_id from localStorage
var user_id = localStorage.getItem('user_id');

if (user_id) {
    // Call FastAPI endpoint to get skin analysis history
    fetch('http://127.0.0.1:8000/history/' + user_id)
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            if (data.history && data.history.length > 0) {
                // Sort by timestamp (newest first)
                var sortedRecords = data.history.sort(function(a, b) {
                    return new Date(b.timestamp) - new Date(a.timestamp);
                });
                
                // Get the most recent skin type
                var latestRecord = sortedRecords[0];
                var skinType = latestRecord.skin_type || 'Unknown';
                var acneCount = latestRecord.acne_count || 0;
                
                console.log('Most recent skin type:', skinType);
                console.log('Acne count:', acneCount);
                
                // Display on screen - update these element IDs in your HTML
                var skinTypeElement = document.getElementById('skinTypeDisplay');
                if (skinTypeElement) {
                    skinTypeElement.textContent = skinType + ' Skin';
                }
            } else {
                console.log('No analysis history found');
            }
        })
        .catch(function(error) {
            console.error('Error fetching skin data:', error);
        });
} else {
    console.log('No user_id found in localStorage');
}
