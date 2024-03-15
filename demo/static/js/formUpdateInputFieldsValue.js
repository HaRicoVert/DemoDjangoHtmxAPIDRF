/*
		 * Fonction qui permet de mettre à jour les champs du formulaire avec les données du livre
		 * @param {Object} form - Formulaire de la modale
		 * @param {Object} data - Données du livre
		 * @returns {void}
		 * @constructor
		 */
function formUpdateInputFieldsValue(form, data) {
    // On récupère l'attribut hx-put du formulaire
    const formLink = form.getAttribute('hx-put');
    // On crée une regex pour vérifier si l'attribut hx-put se termine par un chiffre
    // ex : /api/books/1/ la regex va matcher
    // ex : /api/books/ la regex ne va pas matcher
    var regex = /\d\/$/;

    // Si l'attribut hx-put se termine par un chiffre
    if (regex.test(formLink)) {
        // On remplace le chiffre par l'id du livre
        form.setAttribute('hx-put', formLink.substring(0, formLink.lastIndexOf('/', formLink.length - 2) + 1) + data.id + '/');
    } else {
        // Sinon, on ajoute l'id du livre à la fin de l'attribut hx-put
        form.setAttribute('hx-put', formLink + data.id + '/');
    }

    // On met à jour les champs du formulaire avec les données du livre
    form.querySelectorAll('.fr-input-group').forEach(divInputGroup => {
        const input = divInputGroup.querySelector('input');
        input.value = data[input.getAttribute('name').split('__')[1]];
    });
    // On réactualise htmx pour qu'il prenne en compte les nouvelles valeurs des champs du formulaire
    htmx.process(form);
}
