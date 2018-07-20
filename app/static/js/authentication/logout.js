$(document).ready(function () {
    function deauthenticateUser() {
        localStorage.removeItem('auth_token');
        handlePageWhenNotAuthenticated()
    }

    $('#logout-btn').click(function (event) {
        event.preventDefault();
        if (isAuthenticated) {
            deauthenticateUser();
        }
    })
});
