/*
		 * Fonction qui permet de sauvegarder les valeurs par défaut du formulaire
		 * @param {Object} form - Formulaire de la modale
		 * @param {Object} data - Données du livre
		 * @returns {void}
		 * @constructor
		 */
function formSaveDefaultValue(form, data) {
    // On sauvegarde les valeurs par défaut du formulaire
    form.querySelectorAll('.fr-input-group').forEach(divInputGroup => {
        const input = divInputGroup.querySelector('input');
        modalBookFormDefaultValue[input.getAttribute('name')] = data[input.getAttribute('name').split('__')[1]]
    });
}

/*
 * Fonction qui permet de réinitialiser les valeurs par défaut du formulaire
 * @param {Object} form - Formulaire de la modale
 * @param {Object} data - Données du livre
 * @returns {void}
 * @constructor
 */
function formResetDefaultValue(form, data) {
    // On réinitialise les valeurs par défaut du formulaire
    form.querySelectorAll('.fr-input-group').forEach(divInputGroup => {
        formValidationClear(divInputGroup);
        const input = divInputGroup.querySelector('input');
        input.value = data[input.getAttribute('name')];
    });

}