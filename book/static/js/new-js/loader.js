const loaderDiv = document.createElement('div');
const loaderContentDiv = document.createElement('div');
const loaderSpinnerDiv = document.createElement('div');
const loaderTextP = document.createElement('p');
loaderDiv.id = 'loader';
loaderDiv.classList.add('htmx-indicator');
loaderContentDiv.classList.add('loader-content');
loaderSpinnerDiv.classList.add('loader-spinner');
loaderTextP.textContent = 'Chargement...';
loaderContentDiv.appendChild(loaderSpinnerDiv);
loaderContentDiv.appendChild(loaderTextP);
loaderDiv.appendChild(loaderContentDiv);
document.body.appendChild(loaderDiv);

const styleElement = document.createElement('style');

styleElement.innerHTML = `
    #loader {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: var(--grey-975-75);
    opacity: 90%;
    display: none;
    justify-content: center;
    align-items: center;
    z-index: 1751;
}

.loader-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
}

.htmx-request #loader {
    height: 100%;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.htmx-request#loader {
    height: 100%;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.loader-spinner {
    border: 4px solid rgba(0, 0, 0, 0.3);
    border-top: 4px solid var(--blue-france-sun-113-625);
    border-radius: 50%;
    width: 40px;
    height: 40px;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    to {
        transform: rotate(1turn);
    }
}`;

document.head.appendChild(styleElement);