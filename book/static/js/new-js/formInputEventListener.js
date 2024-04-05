async function formInputAddEventListener(form, apiUrlFormFieldValidation, csrfToken) {
    form.addEventListener('input', async (event) => {
        const fieldName = event.target.name;
        const fieldValue = event.target.value;

        /*
        if (input.type === 'date') {
                formBody = JSON.stringify({[inputName.split('__')[1]]: input.value.split('-').reverse().join('-')})
            } else {
                formBody = JSON.stringify({[inputName.split('__')[1]]: input.value});
            }*/
        let formBody = JSON.stringify({[fieldName]: fieldValue});

        const httpRequest = new XMLHttpRequest();
        httpRequest.open('POST', apiUrlFormFieldValidation);
        httpRequest.setRequestHeader('Content-Type', 'application/json');
        httpRequest.setRequestHeader('X-CSRFToken', csrfToken);
        httpRequest.send(formBody);

        httpRequest.onreadystatechange = function () {
            if (httpRequest.readyState === httpRequest.DONE) {
                if (httpRequest.status === 200) {
                    formValidation(event.target);
                } else if (httpRequest.status === 422) {
                    formValidation(event.target, JSON.parse(httpRequest.responseText)[fieldName]);
                }
            }
        }
    });
}