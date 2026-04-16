document.addEventListener('DOMContentLoaded', function () {
    const messages = document.querySelector('.message-list');
    /*https://stackoverflow.com/questions/3331353/transitions-on-the-css-display-property*/

    if (messages) {
        setTimeout(() => {
            messages.style.transition = 'opacity 0.5s ease-out';
            messages.style.opacity = '0';

            setTimeout(() => {
                messages.style.display = 'none';
            }, 500);
        }, 3000);
    }
});