document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.message-list');

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