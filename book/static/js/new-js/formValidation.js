function formValidation(input, error) {
    let divInputGroup = input.parentElement;
    let inputType;
    if (input.tagName === 'SELECT') {
        inputType = 'select';
    } else if (input.tagName === 'TEXTAREA') {
        inputType = 'textarea';
    } else if (input.type === 'checkbox' || input.type === 'radio') {
        inputType = input.type;
    } else {
        inputType = 'input';
    }

    const validClassName = ['fr-input-group--valid', 'fr-checkbox-group--valid', 'fr-select-group--valid']
    const errorClassName = ['fr-input-group--error', 'fr-checkbox-group--error', 'fr-select-group--error']

    if (error) {
        formValidationClear(divInputGroup);
    } else if (validClassName.some(cls => divInputGroup.classList.contains(cls))) {
        return;
    } else if (errorClassName.some(cls => divInputGroup.classList.contains(cls))) {
        formValidationClear(divInputGroup);
    }

    function createValidationMessageInputSelect(parentElement, inputId, validClassName, error = false) {
        const pValid = document.createElement('p');
        pValid.id = error ? `${inputId}-desc-error` : `${inputId}-desc-valid`;
        pValid.className = error ? 'fr-error-text show' : 'fr-valid-text show'
        pValid.textContent = error ? error : "Le champ est valide";

        error ? parentElement.classList.add(`${validClassName}-group--error`, 'show') : parentElement.classList.add(`${validClassName}-group--valid`, 'show');
        error ? parentElement.querySelector(inputType).classList.add(`${validClassName}--error`, 'show') : parentElement.querySelector(inputType).classList.add(`${validClassName}--valid`, 'show');
        error ? parentElement.querySelector(inputType).setAttribute('aria-describedby', `${inputId}-desc-error`) : parentElement.querySelector(inputType).setAttribute('aria-describedby', `${inputId}-desc-valid`);
        parentElement.appendChild(pValid);
    }

    function createValidationMessageCheckboxRadio(fieldsetInputGroup, inputType, error, group = false) {
        const pValid = document.createElement('p');
        pValid.className = error ? 'fr-message fr-message--error show' : 'fr-message fr-message--valid show';
        pValid.textContent = error ? error : "Le champ est valide";

        const divError = document.createElement('div');
        divError.className = 'fr-messages-group';
        divError.id = error ? `${inputType}-error-messages` : `${inputType}-valid-messages`;
        divError.ariaLive = 'assertive';
        divError.appendChild(pValid);

        if (!group) {
            error ? fieldsetInputGroup.classList.add('fr-checkbox-group--error', 'show') : fieldsetInputGroup.classList.add('fr-checkbox-group--valid', 'show');
            error ? fieldsetInputGroup.querySelector('input', 'radio').setAttribute('aria-describedby', `${inputType}-error-messages`) : fieldsetInputGroup.querySelector('input', 'radio').setAttribute('aria-describedby', `${inputType}-valid-messages`);
            fieldsetInputGroup.appendChild(divError);
        } else {
            error ? fieldsetInputGroup.classList.add('fr-fieldset--error', 'show') : fieldsetInputGroup.classList.add('fr-fieldset--valid', 'show');
            error ? fieldsetInputGroup.setAttribute('aria-describedby', `${inputType}-error-legend ${inputType}-error-messages`) : fieldsetInputGroup.setAttribute('aria-describedby', `${inputType}-valid-legend ${inputType}-valid-messages`);
            fieldsetInputGroup.appendChild(divError);
        }
    }

    if (inputType === 'input' || inputType === 'textarea' || inputType === 'select') {
        createValidationMessageInputSelect(divInputGroup, input.id, input.classList[0], error);
    } else if (inputType === 'checkbox' || inputType === 'radio') {
        const fieldsetInputGroup = divInputGroup.closest('fieldset');
        if (!fieldsetInputGroup) {
            createValidationMessageCheckboxRadio(divInputGroup, inputType, error);
        } else {
            createValidationMessageCheckboxRadio(fieldsetInputGroup, inputType, error, true);
        }
    }
}

function formValidationClear(divInputGroup) {
    divInputGroup.classList.remove('fr-input-group--valid', 'fr-input-group--error', 'fr-checkbox-group--valid', 'fr-checkbox-group--error', 'fr-select-group--valid', 'fr-select-group--error', 'show');
    const inputElement = divInputGroup.querySelector('input, select, textarea');
    if (inputElement) {
        inputElement.classList.remove('fr-input--valid', 'fr-input--error', 'fr-select--valid', 'fr-select--error', 'show');
        inputElement.removeAttribute('aria-describedby');
    }

    const messageElement = divInputGroup.querySelector('p.fr-valid-text, p.fr-error-text, div.fr-messages-group');
    if (messageElement) {
        messageElement.remove();
    }
}