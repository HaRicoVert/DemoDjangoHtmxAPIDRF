/*
		 * Event listener pour le formulaire de la modale
		 * @param {Object} form - Formulaire de la modale
		 * @returns {Promise<void>}
		 * @constructor
		 *
		 * @event htmx:configRequest
		 */
function formSubmitEventListener(form) {
    // On ajoute un listener sur le formulaire de la modale pour configurer la requête envoyée par htmx
    // avant de l'envoyer
    form.addEventListener('htmx:configRequest', function (event) {
        // Fonction qui permet de transformer les clés du JSON envoyé par le formulaire
        // en clé attendue par l'API (ex : text-input-book__title devient title)
        // Il convertit également la date au format attendu par l'API (ex : 2021-01-01 devient 01-01-2021)
        for (const [key, value] of Object.entries(event.detail.parameters)) {
            // Si la clé contient 'text-input-'
            if (key.includes('text-input-')) {
                // Si la clé est une date (c'est-à-dire si elle contient 'year'), on la transforme en clé
                // attendue par l'API, et on modifie la valeur si c'est une date
                // pour la mettre au format attendu par l'API
                if (key.includes('year')) {
                    event.detail.parameters[key.split('__')[1]] = value.split('-').reverse().join('-');
                } else {
                    // Sinon, on transforme la clé en clé attendue par l'API
                    event.detail.parameters[key.split('__')[1]] = value;
                }
                // On supprime l'ancienne clé
                delete event.detail.parameters[key];
            }
        }
    });

    // On ajoute un listener sur le formulaire de la modale pour gérer l'événement après la requête
    form.addEventListener('htmx:afterRequest', (event) => {
        // On vérifie la requête envoyée par htmx
        // Si la requête a été envoyée avec succès
        if (event.detail.successful) {
            // On cache la modale
            dsfr(modalBook).modal.conceal();
            // On actualise le tableau des livres
            htmx.trigger('#book-table-index', 'htmx:afterOnRequest');
        } else {
            alert("Erreur lors de l\'envoi du formulaire");
        }
    });
}