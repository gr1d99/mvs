window.pageUrl = window.location.pathname.split('/');
window.isAuthenticated = !(JSON.parse(localStorage.getItem('auth_token')) == null);
window.alertBox = function (alert_type, alert_message) {
    console.log('called');
    var alert_div = '<div class="alert alert-dismissible alert-' + alert_type +'">' +
        '<button type="button" class="close" data-dismiss="alert">&times;</button>' +
        '<span class="alert-text">' + alert_message + '</span>' +
    '</div>';

    $('.alerts').html(alert_div)
};
