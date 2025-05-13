// Toggle functionality for the first switch
// document.getElementById('light-toggle').addEventListener('change', function () {
//     const sunIcon = document.querySelector('.sun-icon');
//     const moonIcon = document.querySelector('.moon-icon');

//     if (this.checked) {
//         sunIcon.classList.remove('hidden');
//         moonIcon.classList.add('hidden');
//     } else {
//         sunIcon.classList.add('hidden');
//         moonIcon.classList.remove('hidden');
//     }
// });
// Toggle functionality for the second switch
document.getElementById('dark-toggle').addEventListener('change', function () {
    const sunIcon2 = document.querySelector('.sun-icon-2');
    const moonIcon2 = document.querySelector('.moon-icon-2');

    if (this.checked) {
        sunIcon2.classList.add('hidden');
        moonIcon2.classList.remove('hidden');
    } else {
        sunIcon2.classList.remove('hidden');
        moonIcon2.classList.add('hidden');
    }
});