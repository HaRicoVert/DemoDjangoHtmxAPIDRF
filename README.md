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
            <a href="">Django</a>
        </li>
        <li>
			<a href="">L'API Django Rest Framework</a>
			<ul>
				<li>
					<a href="">Création</a>
				</li>
				<li>
					<a href="">Utilisation</a>
				</li>
			</ul>
        </li>
        <li>
			<a href="">Explication de la plateforme</a>
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
- Django Browser Reload

## Django

Pour la partie concernant l'installation et le paramétrage de Django, je vous invite à consulter la documentation, étant
donné que le but initial de ce projet n'est pas de vous expliquer comment installer Django, mais comment utiliser une
API Django Rest Framework.

## L'API Django Rest Framework

La réalisation d'une API avec Django Rest Framework s'est faite via le tutorial disponible sur le site officiel de
Django Rest Framework. Vous pouvez retrouver ce tutoriel à
cette [adresse](https://www.django-rest-framework.org/tutorial/1-serialization/).

L'entièreté du tutoriel n'a pas été réalisée, mais seulement les étapes nécessaires pour la réalisation de l'API pour
l'application web. Ce projet n'exclut pas une mise à jour expliquant plus en détail les parties non réalisées de l'API.

### Création

Pour la réalisation de l'API, il faut d'abord avoir mis en place une application Django, avec notamment un modèle de
base de données. Pour ce projet, j'ai utilisé un modèle de base de données pour les livres, avec un titre, un auteur,
une année de parution et un prix. Chaque élément de ce modèle a ses propres attributs, comme le type de donnée, ou si le
champ est obligatoire ou non. Il y a également d'autre validation, comme la validation du prix, qui ne peut pas être
négatif (par exemple).

Une fois le modèle créé et l'application principale Django fonctionnelle, la première étape est de créer d'une nouvelle
application Django, qui sera dédiée à l'API. Pour cela, il faut utiliser la commande suivante :

```bash
python manage.py startapp api
```

Une fois l'application créée, il faut ajouter cette application dans le fichier `settings.py` de l'application
principale Django. Pour cela, il faut ajouter le nom de l'application, ici `rest_framework` dans la
liste `INSTALLED_APPS`, avant le lancement de l'application principale.

Plusieurs fichiers vont être créés pour l'API. Les fichiers qui nous intéressent sont les
fichiers `serializers.py`, `urls.py` et
`views.py`.

---

Le fichier `serializers.py` permet de transformer les données de la base de données en JSON, pour que l'API puisse les
envoyer. Il permet également de déclarer les données que l'API peut recevoir pour les enregistrer dans la base de
données.

Le contenu de ce fichier est le suivant :

```python
from rest_framework import serializers

from book.models import Book


class BookSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Book
        fields = "__all__"
```

Il est semblable à la déclaration d'un formulaire de base de données en Django, avec la classe `Meta` qui permet de
déclarer le modèle de base de données, et les champs que l'on souhaite utiliser, ici tous les champs. Je vous invite à
suivre soit la
[documentation officielle Django,](https://docs.djangoproject.com/fr/5.0/topics/forms/modelforms/) soit la
[documentation officielle de Django Rest Framework](https://www.django-rest-framework.org/api-guide/serializers/) pour
plus d'informations.

---

Le fichier `urls.py` permet de déclarer les différentes routes de l'API. Il permet de déclarer les différentes vues
disponibles pour l'API. Le contenu de ce fichier est le suivant :

```python
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path(
        "books/",
        views.BookList.as_view(),
        name="book-list"
    ),
    path(
        "book/",
        views.BookDetail.as_view(),
        name="book-detail"
    ),
    path(
        "book/<int:book_id>/",
        views.BookDetail.as_view(),
        name="book-detail"
    ),
    path(
        "books/validate-field/",
        views.BookFieldValidation.as_view(),
        name="book-gain-field-validation"
    )
]

urlpatterns = format_suffix_patterns(
    urlpatterns
)
```

Concernant le choix des routes, il est possible de les déclarer de différentes manières, avec des paramètres, ou non.
J'ai essayé de respecter les bonnes pratiques pour la déclaration des routes, mais il est possible que certaines routes
ne soient pas optimales. J'ai essayé de faire une API plus ou moins RESTful.

Une nouvelle fois, je vous invite à consulter, soit
la [documentation officielle de Django](https://docs.djangoproject.com/fr/5.0/topics/http/urls/), soit la
[documentation officielle de Django Rest Framework](https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer)
pour plus d'informations.

À noter, que l'on appelle les vues de l'API, qui sont déclarées dans le fichier `views.py`, via la méthode `as_view()`.

La dernière ligne permet de déclarer les différentes extensions de fichier que l'API peut recevoir. Par exemple, si
l'API peut recevoir des fichiers JSON, XML, ou autre (dans notre seul le JSON a été utilisé / testé).

*Attention* : Il faut également ajouter les routes de l'API dans le fichier `urls.py` de l'application principale
Django, pour que l'API soit accessible. Pour cela, il faut ajouter les routes de l'API dans le fichier `urls.py` de
l'application principale Django, via la méthode `include()`. Pour plus d'informations, je vous invite à consulter
la [documentation officielle de Django Rest Framework](https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer).

---

Et enfin, le fichier `views.py` permet de déclarer les différentes vues de l'API. Il permet de déclarer les différentes
actions que l'API peut réaliser, comme la récupération de données, la modification de données, ou la suppression de
données.

C'est ce fichier qui gère la logique de l'API. Je vous laisse suivre
la [documentation officielle de Django Rest Framework](https://www.django-rest-framework.org/api-guide/views/) pour plus
d'informations étant donné que le contenu de ce fichier est assez conséquent.

Le principe de ce fichier reste le même que les propriétés de base de données de Django, avec des vues qui héritent de
classes de Django Rest Framework, et qui déclarent les différentes actions que l'API peut réaliser. La manière de
traiter les données est plus ou moins semblables à la manière de traiter les données dans les propriétés du modèle de
base de données.

Chaque vue déclare les différentes actions que l'API peut réaliser, comme la récupération de données, la modification de
données, ou la suppression de données. Chaque vue déclare également les différentes méthodes HTTP que l'API peut
recevoir, comme GET, POST, PUT, DELETE, etc. Chaque vue renvoi toujours une réponse, que ce soit un message de succès,
ou un message d'erreur. Le contenu renvoyé est toujours en JSON, il n'est pas forcément rempli, mais il est toujours
présent. Les codes HTTP sont aussi renvoyés, pour indiquer si la requête a été un succès, ou non. Je vous invite à vous
renseigner sur les codes HTTP pour plus d'informations via
la [documentation officielle de Mozilla](https://developer.mozilla.org/fr/docs/Web/HTTP/Status).

### Utilisation

Pour utiliser l'API, il faut d'abord lancer l'application Django. Ensuite, vous pouvez utiliser l'interface proposée par
Django Rest Framework pour tester l'API. Vous pouvez y accéder via l'URL de l'API, par exemple, dans notre cas :
`http://localhost:8000/apiDRF/books/`.

L'interface vous permet de tester les différentes routes de l'API, et de voir les réponses renvoyées par l'API. Vous
pouvez également tester les différentes méthodes HTTP, comme GET, POST, PUT, DELETE, etc.

## Explication de la plateforme

La plateforme est une application web basique, qui permet de visualiser, modifier et supprimer des livres. Elle est
composée d'une page principale, qui liste tous les livres de la base de données via un tableau. Chaque ligne du tableau
correspond à un livre, avec les différentes informations du livre. Il est possible de supprimer un live via le bouton
"Supprimer". Pour modifier les données d'un livre, il suffit de cliquer sur la ligne correspondante, et de modifier les
données dans le formulaire qui apparaît.

Pour l'interactivité de la page, j'ai utilisé la librairie htmx, qui permet de créer des pages web dynamiques. J'ai
utilisé cette librairie pour la modification et la suppression des livres. Je vous invite fortement à consulter
la [documentation officielle de htmx](https://htmx.org/) pour plus d'informations, l'utilisation de la librairie est
assez vaste et complexe, bien que simple à utiliser une fois habitué.

### Explication de la logique de développement

---

### Fonctionnement du tableau HTML

La première étape pour a été de réaliser une troisième application Django, qui sera dédiée à l'interface web. Je l'ai
nommée `apiview` car je l'utilise en tant qu'API, mais qui renvoi une vue HTML, plutôt qu'une API REST, au format JSON.
Cette application se connecte à l'API Django Rest Framework pour récupérer les données de la base de données, et utilise
un custom inclusion_tag pour générer le tableau HTML. Ce tableau a été pensé pour être à utiliser uniquement pour la
page d'accueil, une éventuelle modification permettrait de l'utiliser pour d'autres pages, à la condition de garder la
même logique d'utilisation. Le but d'utiliser cette approche est de pouvoir faire une requête AJAX via HTMX pour
rafraîchir le tableau sans recharger la page.

---

### Fonctionnement de l'ouverture de la modale de modification

La deuxième étape a été de réaliser une modale pour la modification des livres. J'ai utilisé la librairie htmx pour
ouvrir la modale, et pour envoyer les données du formulaire de la modale à l'API. La modale s'ouvre via un clic sur une
ligne du tableau, et se ferme via un clic sur le bouton "Fermer" de la modale. Pour cela, j'ai utilisé
l'attribut `onclick` et l'attribut `hx-get` avec le lien vers la vue de l'API JSON qui renvoi les données du livre à
modifier. L'attribut `hx-swap` avec la valeur `none`permet d'empêcher la modification de la page à la suite de la
requête AJAX. Enfin, l'attribut `onclick` éxécute la fonction JS `showBookModalAndUpdateInputFields()` pour ouvrir la
modale. Cette fonction permet de récupérer les valeurs de la requête AJAX, et de les insérer dans les champs du
formulaire de la modale et d'ouvrir la modale via l'API du DSFR. Je vous invite à consulter le code de la
fonction `showBookModalAndUpdateInputFields()` pour plus d'informations.

---

### Fonctionnement de la validation du formulaire

La troisième étape a été de réaliser la validation du formulaire. J'utilise la fonction
JS `formValidationEventListener()`
pour vérifier si les champs sont conformes aux contraintes de la base de données. Cette fonction est appelée à chaque
modification d'un champ du formulaire. Elle vérifie si les champs sont conformes en envoyant une requête AJAX à l'API.
La fonction regarde la réponse de l'API, et affiche un message d'erreur si la réponse est un message d'erreur. Si la
réponse est un code HTTP 200, alors le message d'erreur est supprimé. Je vous invite à consulter le code de la
fonction `formValidationEventListener()` pour plus d'informations.

---

### Fonctionnement de la suppression d'un livre

La quatrième étape a été de réaliser la suppression d'un livre. J'utilise l'attribut `hx-delete` pour envoyer une
requête AJAX à l'API pour supprimer un livre. L'attribut `hx-confirm` permet d'afficher une boîte de dialogue pour
confirmer la suppression du livre. L'attribut `hx-on::response-error` permet d'afficher un message d'erreur si la
suppression du livre a échoué. Enfin, on utilise l'attribut `hx-target` pour supprimer la ligne du tableau correspondant
au livre supprimé. Je vous invite à consulter le code HTML, qui se trouve dans l'HTML de l'inclusion_tag, pour plus
d'informations.