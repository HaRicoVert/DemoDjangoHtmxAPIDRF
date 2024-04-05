document.body.addEventListener('htmx:configRequest', function (event) {
    if (event.detail.verb !== 'get') {
        event.detail.headers['X-CSRFToken'] = csrfToken;
    }
});