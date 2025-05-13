document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("login-form");
    const isError = loginForm.dataset.error === "true";

    if (isError) {

        loginForm.parentElement.classList.add("dark:border-red-500");
        console.log("Error in login form");
        setTimeout(() => {
            loginForm.parentElement.classList.remove("dark:border-red-500");
        }, 1000);
    }

});
