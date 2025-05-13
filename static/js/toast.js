function showToast(message = "Berhasil", duration = 3000) {
    const toast = document.getElementById("toast-bottom-right");
    const messageDiv = document.getElementById("toast-message");

    messageDiv.textContent = message;
    toast.classList.remove("hidden");
    toast.classList.add("animate__fadeInUp");

    setTimeout(() => {
        toast.classList.remove("animate__fadeInUp");
        toast.classList.add("hidden");
    }, duration);
}

function hideToast() {
    const toast = document.getElementById("toast-bottom-right");
    toast.classList.remove("animate__fadeInUp");
    toast.classList.add("hidden");
}
