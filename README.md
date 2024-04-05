Ce README a pour but d'expliquer les différentes étapes pour la réalisation nécessaire pour la réalisation d'une
application web en utilisant le framework Django, avec une API Django Rest Framework.

<details>
    <summary>Table des matières</summary>
    <ol>
        <li>
            <a href="">À propos du projet</a>
            <ul>
                <li>
					<a href="">Les applications / librairies utilisées</a>
				</li>
            </ul>
        </li>
        <li>
            <a href="">Installation</a>
        </li>
        <li>
            <a href="">Structure du projet</a>
            <ul>
				<li>
					<a href="">Django</a>
				</li>
				<li>
					<a href="">L'API Django Rest Framework</a>
                    <ul>
                        <li>
                            <a href="">Création</a>
                        </li>
                        <li>
                            <a href="">Authentification</a>
                        </li>
                        <li>
                            <a href="">Permissions</a>  
                        </li>
                    </ul>
				</li>
                <li>
                    <a href="">La partie Front-End</a>
                    <ul>
                        <li>
                            <a href="">L'API View</a>
                        </li>
                    </ul>
                </li>
			</ul>
        </li>
    </ol>
</details>

## À propos du projet

Ce projet a été réalisé pour visualiser les différentes étapes pour la réalisation d'une application web en utilisant le
framework Django, avec une API Django Rest Framework. Le but de ce projet est de comprendre l'utilité d'une API dans le
développement d'une application web, et de comprendre comment la mettre en place, puis de l'utiliser.

Ce projet s'axe principalement sur une partie back-end, avec une interface basique pour le front-end. Ce projet se base
sur la gestion d'une base de données de livres. L'utilisateur peut visualiser, modifier et supprimer des livres via la
partie front-end.

### Les applications / librairies utilisées

Pour ce projet, j'ai utilisé les frameworks suivants :

- [Django](https://www.djangoproject.com/) : Framework web en Python
- [Django Rest Framework](https://www.django-rest-framework.org/) : Framework pour la création d'API REST en Django
- [htmx](https://htmx.org/) : Librairie pour la création de pages web dynamiques
- [Django-DSFR](https://numerique-gouv.github.io/django-dsfr/) : Librairie pour l'intégration du Système de Design de
  l'État dans un projet Django

## Installation

Ce projet a été développé avec Python 3.12. Pour installer les dépendances, vous pouvez utiliser la commande suivante :

```bash
pip install -r requirements.txt
```

Pour plus d'informations concernant l'installation de Django Rest Framework, je vous invite à consulter
la [documentation officielle](https://www.django-rest-framework.org/#installation).

Les principales dépendances sont les suivantes :

- Django
- Django Rest Framework
- Django-DSFR

## Structure du projet

Le projet est structuré de la manière suivante :

```
├── api
│   ├── __init__.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── signals.py
│   ├── urls.py
│   └── views.py
├── apiview
│   ├── __init__.py
│   ├── apps.py
│   ├── templates
│   │   └── apiview
│   │       ├── book_table_index.html
│   │       └── templatetags
│   │           └── book_table_index.html
│   ├── templatetags
│   │   ├── __init__.py
│   │   └── apiview_tags.py
│   ├── urls.py
│   └── views.py
├── book
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   └── dsfr_form.css
│   │   ├── images
│   │   │   └── tail-spin.svg
│   │   └── js
│   │       ├── new-js
│   │       │   ├── formInputEventListener.js
│   │       │   ├── formReset.js
│   │       │   ├── formSubmitEventListener.js
│   │       │   ├── formValidation.js
│   │       │   ├── htmxFormEventListenerCsrf.js
│   │       │   └── loader.js
│   │       └── old-js
│   │           ├── formReset.js
│   │           ├── formSubmitEventListener.js
│   │           ├── formUpdateInputFieldsValue.js
│   │           └── formValidationEventListener.js
│   ├── templates
│   │   └── book
│   │       ├── block
│   │       │   └── header.html
│   │       └── index.html
│   ├── urls.py
│   ├── utilities.py
│   └── views.py
├── core
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── gain
│   ├── __init__.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── templates
│   │   └── gain
│   │       ├── index.html
│   │       └── index_separated.html
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── templates
    └── admin
        └── login.html
```

On va retrouver 6 dossiers principaux :

- Les dossiers api, apiview, book et gain, qui correspondent aux différentes applications du projet :

> `api` : Application responsable de l'API Django Rest Framework
>
> `apiview` : Application qui permet de gérer le retour formaté de l'API
>
> `book` : Application simulant la modification et la supprimant de livres d'une bibliothèque
>
> `gain` : Application simulant des formulaires pour la gestion d'indicateurs

- Le dossier `templates` qui contient les templates liées au projet


- Le dossier `core` qui contient les fichiers de configuration de Django

### Django

Pour la partie concernant l'installation et le paramétrage de Django, je vous invite à consulter la documentation, étant
donné que le but initial de ce projet n'est pas de vous expliquer comment installer et utiliser Django, mais comment
utiliser une API Django Rest Framework.

### L'API Django Rest Framework

La réalisation d'une API avec Django Rest Framework s'est faite via le tutorial disponible sur le site officiel de
Django Rest Framework. Vous pouvez retrouver ce tutoriel à
cette [adresse](https://www.django-rest-framework.org/tutorial/1-serialization/).

---

#### Création

Pour la création de l'API, la première étape est d'avoir un modèle Django fonctionnel (exemple : le modèle `Book` dans
l'application `book`). Ensuite, il faut créer un fichier `serializers.py` dans le dossier de l'application de l'API, et
créer un serializer pour le modèle.

```python
from rest_framework import serializers

from book.models import Book
from gain.models import Indicator


class BookSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Book
        fields = '__all__'


class IndicatorSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Indicator
        fields = '__all__'
```

Le but du serializer est d'indiquer à l'API DRF quel modèle utiliser, et quels champs du modèle utiliser. Ensuite, il
faut créer une vue pour l'API, qui va utiliser le serializer pour retourner les données. Pour les vues, elles sont
décomposées en classes, où dans chaque classe, on va définir les méthodes HTTP à utiliser pour la vue (voir le fichier
`views.py` de l'application `api`). C'est à l'utilisateur de définir les méthodes à utiliser pour chaque vue. C'est ici,
que l'on récupère les données du modèle, et que l'on les retourne via le serializer. Chaque vue doit être liée à une
URL. Chaque vue renvoie un objet `Response` de Django Rest Framework, qui va retourner les données au format JSON.
Chaque vue renvoi un code de réponse HTTP.

---

#### Authentification

Pour l'authentification, Django Rest Framework propose plusieurs méthodes d'authentification. On peut définir une
authentification par défaut pour toutes les vues depuis les paramètres du fichier `settings.py` de l'application `core`.

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.SessionAuthentication',
                                       'rest_framework.authentication.TokenAuthentication', ]
}
```

Ainsi chaque vue de l'API va vérifier si l'utilisateur est authentifié via une session ou un token. On peut également
définir des authentifications au niveau de chaque vue avec le code ci-dessous.

```python
class BookList(
    APIView
):
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get(
        self,
        request,
        format=None
    ):
        ...
```

Les sessions et les tokens sont des méthodes d'authentification par défaut de Django Rest Framework.

Les sessions sont des cookies qui permettent de stocker des informations sur le serveur. Cette méthode
d'authentification est surtout utilisé pour l'authentification coté Web.

Les tokens sont des jetons qui permettent de stocker des informations sur le client. Cette méthode d'authentification
est surtout utilisé pour l'authentification cotée API (via CLI par exemple ou pour les requêtes AJAX).

Pour les Tokens, il faut ajouter `rest_framework.authtoken` dans les `INSTALLED_APPS` du fichier `settings.py` de
l'application `core`.

Ensuite, on utilise un signal dès qu'un utilisateur est créé pour lui générer un token.

```python
# api/signals.py

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(
    user_logged_in
)
def create_auth_token(
    sender,
    user,
    request,
    **kwargs
):
    Token.objects.get_or_create(
        user=user
    )
```

Il faut ensuite ajouter le signal dans le fichier `apps.py` de l'application `book`.

```python
def ready(
    self
):
    import api.signals
```

Pour créer un token via CLI, il faut utiliser la commande suivante :

```bash
curl -X POST -d "username=<username>&password=<password>" http://localhost:8000/apiDRF/token/
```

Pour utiliser le token, il faut ajouter le token dans le header de la requête.

```bash
curl -H "Authorization: Token <token>" http://localhost:8000/apiDRF/books/
````
---

#### Permissions

Pour la gestion des permissions, Django Rest Framework propose plusieurs permissions par défaut. On peut définir des
permissions par défaut pour toutes les vues depuis les paramètres du fichier `settings.py` de l'application `core`.

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated',
                                   'rest_framework.permissions.IsAdminUser', ]
}
```

Ainsi chaque vue de l'API va vérifier si l'utilisateur est authentifié, et si l'utilisateur est un administrateur.

On peut également définir des permissions au niveau de chaque vue. Pour cela, il faut définir des permissions Django qui
seront utilisées par les vues. Une fois les permissions Django créées, il faut aussi définir les permissions DRF, qui
seront utilisées par les vues. C'est à l'utilisateur de développer les permissions nécessaires pour son application,
voir ci-dessous.

```python
# Exemple d'une permission DRF pour vérifier si l'utilisateur à le droit de voir les livres de l'éditeur Hachette

class HasViewHachettePermission(
    BasePermission
):
    def has_permission(
        self,
        request,
        view
    ):
        if request.method == 'GET' and request.user and request.user.is_authenticated:
            return request.user.has_perm(
                'book.view_hachette_book'
            )
        return False
```

Pour appliquer la permission à une vue, il suffit de l'ajouter dans la liste des permissions de la vue.

```python
class BookList(
    APIView
):
    permission_classes = [
        IsAdminUser | HasViewPermission | HasViewHachettePermission]

    def get(
        self,
        request,
        format=None
    ):
        ...
```

On peut utiliser les opérateurs | et & pour combiner les permissions.

Si l'on utilise des vues pour renvoyer des données formatées, il est possible de définir des permissions pour ces vues
en utilisant les décorateurs `@login_required` et `@permission_required`.

```python
@login_required
@permission_required(
    'book.view_book',
    raise_exception=True
)
def book_table_index(
    request
):
    ...
```

À noter qu'ici, on utilise les permissions Django, et non les permissions DRF. On vérifie seulement si l'utilisateur a
le droit de voir les livres. Pour gérer ensuite, les permissions de voir en fonction des éditeurs, c'est l'API qui le
gère.
