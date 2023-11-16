# Projet Personnel météo de Montpellier
## Objectif:
L'objectif de ce projet était de déployer un site affichant la météo des 4 prochains jours à Montpellier. Les principaux languages utilisés pour réaliser cette tache on été html et python.
La météo est disponible à [cette adresse](https://abelsilly.github.io/Projet_Perso/).

## Procédure:
La réalisation de ce projet a nécessité plusieurs étapes:

- Le téléchargement des données météo
- L'affichage de ces données
- La publication du site
- L'autonomie du site

Les deux étapes les plus compliquées pour moi auront été l'affichage des données et l'autonomie du site.

### Téléchargement:

Pour ce qui est du téléchargement, une première idée a été d'utiliser le package **pooch** et plus précisemment la fonction *pooch.retrieve*, mais le défaut de cette fonction était quelle ne remplaçait pas un fichier déjà éxistant et posait donc problème pour le téléchargement quotidien des données météo. Je me suis donc passé de cette fonction sauf pour le téléchargement du fichier json des icônes météo qui ne nécessite lui pas d'actualisation.
J'ai donc préféré utilisé le package **request** déjà installé sur python, qui permet une réécriture des données.

### Affichage:

L'affichage a certainement été la partie qui m'a demandé le plus de temps dans la mesure où je ne savais pas du tout comment afficher de tableau en python. Une première idée a été de tenter de faire un tableau "à la main" avec le package **matplotlib**, mais cela s'annonçait trop compliqué pour un résultat qui ne me convenait pas.
J'ai donc préféré faire un tableau html sous conseils de Mr. Salmon, je me suis d'ailleurs inspiré des tableau présent sur [ce site](https://josephsalmon.github.io/HAX712X/Courses/Numpy/tp.html).
Le problème qui se posait alors était que je ne savais pas comment importer des données d'un code python dans un fichier html. J'ai eu l'idée "d'extraire les données" du code python en créant des images contenant ces données que je pourrai ensuite insérer dans le tableau. C'est ce qui donne le rendu final de mon tableau, c'est un tableau html dans lequel chaque case est une image.

### Déploiement du site:

Le déploiement du site était pour le coup plutôt aisé en suivant [ce tuto](https://quarto.org/docs/publishing/github-pages.html#github-action). Pour ce qui est du fichier *publish.yml* et *_quarto.yml* je me suis inspiré de ceux de Mr. Salmon en les adaptant à mon dépot.

### Autonomie:

Un des défauts de ma méthode d'affichage est quelle repose essentiellement sur la manipulation de fichier en local, le code python sert à créer des fichiers d'images qui seront appellées dans la partie html de mon document quarto.Mon problème était donc qu'initialement le déploiement de mon site se faisait bien en local mais mal de façon autonome. J'ai donc du passer du temps à comprendre comment fonctionne le système de déploiement automatique de github pour m'assurer que le robot dispose bien des bons fichiers à afficher.