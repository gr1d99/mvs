$(document).ready(function () {
    function checkToken() {
        if (isAuthenticated){
            window.location = '/'
        }
    }

    if (pageUrl[2] == 'login') {
        checkToken();
    }

    $('#login-form').submit(function (event) {
        event.preventDefault();

        var email = $('#id_email').val();
        var password = $('#id_password').val();

        function handleSuccessfulLogin() {
            var auth_token = JSON.stringify(request.responseJSON);
            localStorage.setItem('auth_token', auth_token);
            $('#login-form').trigger('reset');
            window.location = '/'
        }

        function handleUnsuccessfulLogin() {
            var error_message = request.responseJSON['message'];
            alertBox('warning', error_message)
        }

        var request = $.ajax({
            url: '/auth/login',
            method: 'POST',
            data: { email: email, password: password },
            dataType: 'json',
            statusCode: {
                200: handleSuccessfulLogin,
                422: handleUnsuccessfulLogin
            }
        });
    });
});
