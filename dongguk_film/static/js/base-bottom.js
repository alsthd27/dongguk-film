//
// Sub functions
//

function hideNavbarAndFooter() {
    let httpStatusCode = document.querySelector("#http_status_code");

    if (location.pathname.indexOf("accounts") != -1 ||
        httpStatusCode != null) {
        navbar.hidden = true;
        footer.hidden = true;
    };
}

hideNavbarAndFooter();

function redirectAfterLoginLogout() {
    let loginsLogouts = document.querySelectorAll(".login-button, .logout-button");

    loginsLogouts.forEach((loginLogout) => {
        loginLogout.href = loginLogout.href + "?next=" + location.pathname;
    });
}

redirectAfterLoginLogout();