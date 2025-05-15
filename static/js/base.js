const infoModal = document.getElementById('infoModal');
infoModal.addEventListener('show.bs.modal', function (event) {
    const button = event.relatedTarget;
    const modalContent = button.getAttribute('data-modal-content');
    const modalBody = infoModal.querySelector('.modal-body');
    modalBody.innerHTML = `<p>${modalContent}</p><p style="text-align: right;"></p>`;
});
document.querySelectorAll('.side-fixed').forEach(img => {
    img.addEventListener('click', () => {
        img.classList.remove('rotating');
        setTimeout(() => img.classList.add('rotating'), 10);
    });
});
