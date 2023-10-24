// activates bootstrap Tooltips
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))


// this code makes the rows of a table clickale
const rows = document.querySelectorAll('tr');

rows.forEach(row => {
    row.addEventListener('click', () => {
        window.location.href = row.getAttribute('href');
    });
});