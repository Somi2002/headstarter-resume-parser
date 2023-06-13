function togglePasswordVisibility() {
    var passwordInput = document.getElementById('password-input');
    var passwordType = passwordInput.getAttribute('type');

    if (passwordType === 'password') {
        passwordInput.setAttribute('type', 'text');
    } else {
        passwordInput.setAttribute('type', 'password');
    }
}
