/*
* Event listener pour la validation des champs du formulaire
* @param {Object} gain - Formulaire de la modale
* @param {String} apiVerificationLink - Lien de l'API pour la validation des champs du formulaire
* @returns {Promise<void>}
* @constructor
*/
function formValidationEventListener(form, apiVerificationLink, csrfToken) {
    // On ajoute un listener sur le formulaire de la modale pour valider les champs du formulaire
    // lorsqu'un champ est modifié
    form.addEventListener('input', async (event) => {
        await formValidationLogic(event.target, apiVerificationLink, csrfToken);
    });
}

/*
 * Fonction qui permet de valider les champs du formulaire
 * @param {Object} input - Champ du formulaire
 * @param {String} apiVerificationLink - Lien de l'API pour la validation des champs du formulaire
 * @returns {Promise<void>}
 * @constructor
 */
async function formValidationLogic(input, apiVerificationLink, csrfToken) {
    // On récupère le nom du champ du formulaire
    const inputName = input.getAttribute('name');
    var formBody;

    // On vérifie si le champ est une date
    if (input.type === 'date') {
        // Si c'est une date, on la transforme en clé attendue par l'API
        formBody = JSON.stringify({[inputName.split('__')[1]]: input.value.split('-').reverse().join('-')})
    } else {
        // Sinon, on transforme le champ en clé attendue par l'API
        formBody = JSON.stringify({[inputName.split('__')[1]]: input.value});
    }

    // On envoie une requête à l'API pour valider le champ du formulaire
    try {
        const response = await fetch(apiVerificationLink, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: formBody
        })
        const divInputGroup = input.parentElement;
        if (response.ok) {
            // Si le champ est valide, on affiche un message de validation
            formValidationSuccess(divInputGroup);
        } else {
            // Si le champ n'est pas valide, on affiche un message d'erreur
            const errors = await response.json();
            formValidationError(divInputGroup, errors);
        }
        // Si une erreur se produit, on l'affiche dans la console
    } catch (error) {
        console.error("Une erreur s'est produite : ", error);
    }
}

/*
 * Fonction qui permet d'afficher un message de validation
 * @param {Object} divInputGroup - Groupe de champs du formulaire
 * @returns {void}
 * @constructor
 */
function formValidationSuccess(divInputGroup) {
    // Si le champ contenait une erreur, on l'enlève
    if (divInputGroup.classList.contains('fr-input-group--error')) {
        formValidationClear(divInputGroup);
    }
    // On ajoute un message de validation
    var input = divInputGroup.querySelector('input');
    if (!input) {
        input = divInputGroup.querySelector('select');
    }
    if (!input) {
        input = divInputGroup.querySelector('textarea');
    }
    divInputGroup.classList.add('fr-input-group--valid');
    divInputGroup.classList.add('show');
    input.classList.add('fr-input--valid');
    input.classList.add('show');
    input.setAttribute('aria-describedby', `${input.getAttribute('type')}-input-valid-desc-valid`);

    if (!divInputGroup.querySelector('p.fr-valid-text')) {
        var pValid = document.createElement('p');
        pValid.className = 'fr-valid-text show';
        pValid.textContent = "Le champ est valide";
        var divSuccess = document.createElement('div');
        divSuccess.className = 'fr-messages-group';
        divSuccess.id = input.id + '-messages';
        divSuccess.ariaLive = 'assertive';
        divSuccess.appendChild(pValid);
        divInputGroup.appendChild(divSuccess);
    }
}

/*
 * Fonction qui permet de réinitialiser les messages d'erreur ou de validation
 * @param {Object} divInputGroup - Groupe de champs du formulaire
 * @returns {void}
 * @constructor
 */
function formValidationClear(divInputGroup) {
    divInputGroup.classList.remove('fr-input-group--valid');
    divInputGroup.classList.remove('fr-input-group--error');
    divInputGroup.classList.remove('show');

    var input = divInputGroup.querySelector('input');
    input.classList.remove('fr-input--valid');
    input.classList.remove('fr-input--error');
    input.classList.remove('show');
    input.removeAttribute('aria-describedby');

    if (divInputGroup.querySelector('div.fr-messages-group')) {
        divInputGroup.querySelector('div.fr-messages-group').remove();
    }
}

/*
 * Fonction qui permet d'afficher un message d'erreur
 * @param {Object} divInputGroup - Groupe de champs du formulaire
 * @param {Object} errors - Erreurs du champ du formulaire
 * @returns {void}
 * @constructor
 */
function formValidationError(divInputGroup, errors) {
    if (divInputGroup.classList.contains('fr-input-group--valid')) {
        formValidationClear(divInputGroup);
    }
    var input = divInputGroup.querySelector('input');
    if (!input) {
        input = divInputGroup.querySelector('select');
    }
    divInputGroup.classList.add('fr-input-group--error');
    divInputGroup.classList.add('show');
    input.classList.add('fr-input--error');
    input.classList.add('show');
    input.setAttribute('aria-describedby', `${input.getAttribute('type')}-input-error-desc-error`);

    if (!divInputGroup.querySelector('p.fr-error-text')) {
        var pError = document.createElement('p');
        pError.className = 'fr-error-text show';
        pError.textContent = errors[Object.keys(errors)[0]];
        var divError = document.createElement('div');
        divError.className = 'fr-messages-group';
        divError.id = input.id + '-messages';
        divError.ariaLive = 'assertive';
        divError.appendChild(pError);
        divInputGroup.appendChild(divError);
    }
}