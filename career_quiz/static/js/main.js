// Main navigation and authentication handling
function checkLoginStatus() {
    const isLoggedIn = localStorage.getItem('logged_in') === 'true';
    const isAdmin = localStorage.getItem('is_admin') === 'true';
    
    const loginLink = document.getElementById('login-link');
    const registerLink = document.getElementById('register-link');
    const logoutLink = document.getElementById('logout-link');
    const adminLink = document.getElementById('admin-link');

    if (loginLink && registerLink && logoutLink) {
        if (isLoggedIn) {
            loginLink.style.display = 'none';
            registerLink.style.display = 'none';
            logoutLink.style.display = 'block';
            if (adminLink && isAdmin) {
                adminLink.style.display = 'block';
                adminLink.href = '/admin';
            }
        } else {
            loginLink.style.display = 'block';
            registerLink.style.display = 'block';
            logoutLink.style.display = 'none';
            if (adminLink) {
                adminLink.style.display = 'none';
            }
        }
    }
}

function logout() {
    fetch('/logout')
        .then(response => response.json())
        .then(data => {
            localStorage.clear();
            window.location.href = '/';
        })
        .catch(error => console.error('Error:', error));
}

// Run on page load
document.addEventListener('DOMContentLoaded', checkLoginStatus);
