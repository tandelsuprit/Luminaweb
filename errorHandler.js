/**
 * Global Error Handler for Lumina Care Web App
 * Catches fetch errors and handles session expiration (401 Unauthorized)
 */

// Override the native fetch to add global error handling
const originalFetch = window.fetch;
window.fetch = async function(...args) {
    try {
        const response = await originalFetch.apply(this, args);
        
        // Check for 401 Unauthorized (session expired)
        if (response.status === 401) {
            console.error('Session expired. Redirecting to login...');
            
            // Clear all localStorage data
            localStorage.clear();
            
            // Redirect to auth page
            window.location.href = 'auth.html';
            
            // Return an empty response to prevent further processing
            return new Response(JSON.stringify({ error: 'Session expired' }), {
                status: 401,
                headers: { 'Content-Type': 'application/json' }
            });
        }
        
        return response;
    } catch (error) {
        // Handle network errors
        console.error('Network error:', error);
        throw error;
    }
};

// Alternative: Create a handleApiError function that can be used in try-catch blocks
function handleApiError(error, errorMessage = 'An error occurred') {
    console.error(errorMessage, error);
    
    // Check if it's a 401 error
    if (error.response && error.response.status === 401) {
        console.error('Session expired. Redirecting to login...');
        localStorage.clear();
        window.location.href = 'auth.html';
        return true;
    }
    
    // Check for network errors
    if (error.message && error.message.includes('Network')) {
        alert('Network error. Please check your internet connection.');
        return true;
    }
    
    return false;
}

// Export for use in modules (if using ES modules)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { handleApiError };
}
