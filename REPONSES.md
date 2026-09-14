# Réponses — Partie 2 : Paradigmes de Programmation

## Q1. Quelle est la différence fondamentale entre le paradigme impératif et le paradigme déclaratif ?

Le paradigme impératif décrit **comment** réaliser une tâche en donnant une suite d'instructions à exécuter. Le paradigme déclaratif décrit plutôt **ce que** l'on veut obtenir sans détailler toutes les étapes nécessaires pour y parvenir.

## Q2. Dans votre version fonctionnelle, qu'est-ce qu'une « fonction pure » ? Pourquoi cherche-t-on à éviter les effets de bord ?

Une fonction pure est une fonction qui donne toujours le même résultat pour les mêmes entrées et qui ne modifie pas les données ou l'état extérieur du programme. On cherche à éviter les effets de bord car ils rendent le programme plus difficile à comprendre, à tester et à maintenir.

## Q3. Quels avantages apporte l'approche orientée objet par rapport à l'approche procédurale pour ce problème, quand le programme grossit ?

L'approche orientée objet permet de regrouper les données et les comportements dans des classes et des objets. Lorsque le programme devient plus grand, cela facilite l'organisation, la réutilisation du code, la maintenance et l'ajout de nouvelles fonctionnalités ou de nouveaux types d'objets.

## Q4. Citez un langage principalement associé à chacun des paradigmes suivants : impératif, orienté objet, fonctionnel, déclaratif.

* Impératif : C
* Orienté objet : Java
* Fonctionnel : Haskell
* Déclaratif : SQL

## Q5. Le langage que vous avez choisi (JavaScript ou Python) est-il rattaché à un seul paradigme ? Justifiez votre réponse à l'aide des versions que vous venez d'écrire.

Non, Python n'est pas rattaché à un seul paradigme. C'est un langage multiparadigme. Dans notre travail, nous avons utilisé Python pour une version procédurale, une version orientée objet et une version fonctionnelle. Python permet donc d'utiliser plusieurs styles de programmation selon le problème à résoudre.

## Q6. Dans quel contexte réel préféreriez-vous une approche fonctionnelle plutôt qu'orientée objet ? Donnez un exemple concret.

Je préférerais une approche fonctionnelle lorsqu'il faut effectuer beaucoup de transformations ou de traitements sur des données. Par exemple, pour analyser un grand ensemble de données, les fonctions pures permettent de transformer, filtrer et calculer les données avec moins d'effets de bord.

## Q7. Quel est le lien entre le paradigme orienté objet que vous venez de pratiquer ici (Version 2) et les diagrammes UML réalisés en Partie 1 ?

Les diagrammes UML permettent de concevoir et représenter la structure d'un système orienté objet avant de le programmer. Par exemple, dans notre diagramme de classes, nous avons les classes `Book`, `Member`, `Librarian` et `Loan`. Dans notre version orientée objet en Python, nous avons utilisé une classe `Book` avec des attributs et des méthodes, ce qui correspond directement aux concepts représentés en UML.

## Q8. Django, que vous allez utiliser dans la suite de la formation, repose principalement sur quel(s) paradigme(s) ? Justifiez avec un exemple concret.

Django repose principalement sur l'approche orientée objet, tout en utilisant aussi des concepts impératifs et déclaratifs. Par exemple, les modèles Django sont définis sous forme de classes Python. Un modèle `Book` peut avoir des attributs comme `title` et `author`, tandis que les QuerySets permettent de rechercher et de manipuler les données de manière expressive.
