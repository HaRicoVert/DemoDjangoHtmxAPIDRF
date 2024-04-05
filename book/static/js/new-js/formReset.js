function formReset(form, value = null) {
    form.querySelectorAll('input, select, textarea').forEach((input) => {
        console.log(input);
        if (input.type !== 'hidden') {
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = null;
            }
            if (input.type === 'select-one') {
                input.selectedIndex = 0;
            }
            formValidationClear(input.parentElement);
        }
    });
}