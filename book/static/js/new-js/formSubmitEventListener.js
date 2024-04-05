function formSubmitEventListener(form, actionOnSuccess, actionOnError = null) {
    form.addEventListener('htmx:afterRequest', function (event) {
        if (event.detail.successful) {
            actionOnSuccess(event);
        } else if (event.detail.xhr.status === 403) {
            if (actionOnError !== null) {
                actionOnError(event);
            } else {
                alert("Une erreur est survenue, veuillez réessayer plus tard");
            }
        } else if (event.detail.xhr.status === 422) {
            for (const [error, value] of Object.entries(JSON.parse(event.detail.xhr.responseText))) {
                formValidation(form.querySelector(`[name=${error}]`), value);
            }
            form.querySelector('.fr-error-text, .fr-message--error').scrollIntoView({
                behavior: "smooth", block: "center", inline: "nearest"
            });
        }
    });
}