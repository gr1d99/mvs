$(document).ready(function () {
    function removeToken() {
        localStorage.removeItem('auth_token');
    }

    $('#logout-btn').click(function (event) {
        event.preventDefault();
        if (isAuthenticated) {
            const auth_token = JSON.parse(localStorage.getItem('auth_token'))['auth_token'];
            const request = $.ajax({
            url: '/auth/logout',
            beforeSend: function ( xhr ) {
                xhr.setRequestHeader('Authorization', 'Bearer '.concat(auth_token))
            },
            method: 'DELETE',
            dataType: 'json',
            statusCode: {
                200: function () {
                    removeToken();
                    handlePageWhenNotAuthenticated()
                },
                401: function () {
                    alertBox('info', 'You need to login again');
                    removeToken();
                    handlePageWhenNotAuthenticated()
                }
            }
            });
        }
    })
});
