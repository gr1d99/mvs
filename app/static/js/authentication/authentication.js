$(document).ready(function () {
    window.handlePageWhenAuthenticated = function () {
        $('ul#authentication-links #logout-link').remove();
        $('ul#authentication-links').append(
            '<li id="logout-link" class="nav-item"><a class="nav-link" id="logout-btn" href="#">Logout <i class="fa fa-sign-out"></i></a></li>'
        );
    };

    window.handlePageWhenNotAuthenticated = function () {
         $('ul#authentication-links').append(
            '<li id="login-link" class="nav-item"><a class="nav-link" href="/auth/login">Login <i class="fa fa-sign-in"></i></a></li>'
        );
        $('ul#authentication-links #logout-link').remove();
    };

    if (isAuthenticated){
        handlePageWhenAuthenticated()
    }
    else {
        handlePageWhenNotAuthenticated()
    }
});
