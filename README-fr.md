<br/>
<p align="center">
<img src="https://i.imgur.com/bYwl7Vf.png" alt="Learn Regex">
</p><br/>

## Traductions:

* [English](README.md)
* [Español](README-es.md)
* [Français](README-fr.md)
* [中文版](README-cn.md)
* [日本語](README-ja.md)

## Qu'est-ce qu'une expression régulière?

> Une expression régulière est un groupement de caractères ou symboles utilisés pour trouver un modèle spécifique dans un texte.

Une expression régulière est un modèle qui est comparée à une chaîne de caractères de gauche à droite. Le mot "Expression régulière"
est un terme entier, souvent abrégé par "regex" ou "regexp". Une expression régulière est utilisée pour remplacer un texte à l'intérieur
d'une *string* (une chaîne de caractères), valider un formulaire, extraire une portion de string basée sur un modèle, et bien plus encore.

Imaginons que nous écrivons une application et que nous voulons définir des règles pour le choix du pseudonyme. Nous voulons autoriser
le pseudonyme à contenir des lettres, des nombres, des underscores et des traits d'union. Nous voulons aussi limiter le nombre
de caractères dans le pseudonyme pour qu'il n'ait pas l'air moche. Nous utilisons l'expression régulière suivante pour valider un pseudonyme:
<br/><br/>
<p align="center">
<img src="https://i.imgur.com/ekFpQUg.png" alt="Regular expression">
</p>

L'expression régulière ci-dessus peut accepter les strings `john_doe`, `jo-hn_doe` et `john12_as`. Ça ne fonctionne pas avec `Jo` car
cette string contient une lettre majuscule et elle est trop courte.

## Table des matières

- [Introduction](#1-introduction)
- [Meta-caractères](#2-meta-caractères)
  - [Full stop](#21-full-stop)
  - [Inclusion de caractères](#22-inclusion-de-caractères)
    - [Exclusion de caractères](#221-exclusion-de-caractères)
  - [Répétitions](#23-répétitions)
    - [Astérisque](#231-Asterisque)
    - [Le Plus](#232-le-plus)
    - [Le Point d'Interrogation](#233-le-point-d'interrogation)
  - [Accolades](#24-accolades)
  - [Groupement de caractères](#25-groupement-de-caractères)
  - [Alternation](#26-alternation)
  - [Caractère d'échappement](#27-caractère-d'échappement)
  - [Ancres](#28-ancres)
    - [Circonflexe](#281-circonflexe)
    - [Dollar](#282-dollar)
- [Liste de caractères abrégés](#3-liste-de-caractères-abrégés)
- [Recherche](#4-recherche)
  - [Recherche avant positive](#41-recherche-avant-positive)
  - [Recherche avant négative](#42-recherche-avant-négative)
  - [Recherche arrière positive](#43-recherche-arrière-positive)
  - [Recherche arrière négative](#44-recherche-arrière-négative)
- [Drapeaux](#5-drapeaux)
  - [Insensible à la casse](#51-insensible-à-la-casse)
  - [Recherche globale](#52-recherche-globale)
  - [Multilignes](#53-multilignes)
- [Bonus](#bonus)

## 1. Introduction

Une expression régulière est un motif de caractères utilisés pour opérer une recherche dans un text. Par exemple, l'expression régulère `the` signifie: la lettre `t`, suivie de la lettre `h`, suivie de la lettre `e`.

<pre>
"the" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/dmRygT/1)

L'expression régulière `123` coïncide à la chaîne `123`. Chaque caractère de l'expression régulière est comparée à la chaine passée en entrée, caractère par caractère. Les expressions régulières sont normalement sensibles à la casse, donc l'expression régulière `The` ne va pas coïncider à la chaîne de caractère `the`.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/1paXsy/1)

## 2. Meta-caractères

Les meta-caractères sont les bloques de construction des expressions régulières. Les meta-caractères sont interprétés de manière particulière. Certains meta-caractères ont des significations spéciales et sont écrits entre crochets.
Significations des meta-caractères:

|Meta-caractère|Description|
|:----:|----|
|.|Un point coïncide avec n'importe quel caractère unique à part le retour à la ligne.|
|[ ]|Classe de caractères. Coïncide avec n'importe quels caractères entre crochets.|
|[^ ]|Négation de classe de caractère. Coïncide avec n'importe quels caractères qui n'est pas entre les crochets.|
|*|Coïncide avec 0 ou plus répétitions du caractère précédent.|
|+|Coïncide avec 1 ou plus répétitions du caractère précédent.|
|?|Rend le caractère précédent optionel.|
|{n,m}|Accolades. Coïncide avec au moins "n" mais pas plus que "m" répétition du caractère précédent.|
|(xyz)|Groupe de caractères. Coïncide avec les caractères "xyz" dans l'ordre exact.|
|&#124;|Alternation (ou). Coïncide soit avec le caractère avant ou après le symbol.|
|&#92;|Echappe le prochain caractère. Cela permet de faire coïncider des caractères réservés tels que <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>|
|^|Coïncide avec le début de la chaîne de caractère.|
|$|Coïncide avec le fin de la chaîne de caractère.|

## 2.1 Full stop

Full stop `.` est l'exemple le plus simple d'un meta-caratère. Le `.` coïncide avec n'importe caractère unique, mais ne coïcide pas avec les caractères de retour ou de nouvelle ligne. Par exemple, l'expression régulière `.ar` signifie: n'importe quel caractère suvit par la lettre `a`, suivie par la lettre `r`.

<pre>
".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/xc9GkU/1)

## 2.2 Inclusions de caractères


Les inclusions de caractères sont également appelés classe de caractères. Les crochets sont utilisé pour spécifier les inclusion de caractères. Un trait d'union utilisé dans une inclusion de caractères permet de définir une gamme de caractères. L'ordre utilisé dans la gamme de caractère n'a pas d'importance. Par exemple, l'expression régulière `[Tt]he` signifie: un `T` majuscule ou `t` minucule, suivit par la lettre `h`, suivie par la lettre `e`.

<pre>
"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/2ITLQ4/1)

L'utilisation du point dans une inclusion de caractère signifie toutefois un `.` littéral. L'expression régulière `ar[.]` signifie: un `a` minuscule, suivi par la lettre `r`, suvie par un `.` (point)).

<pre>
"ar[.]" => A garage is a good place to park a c<a href="#learn-regex"><strong>ar.</strong></a>
</pre>

[Essayer l'expression régulière](https://regex101.com/r/wL3xtE/1)

### 2.2.1 Exclusion de caractères

En règle générale, le caractère circonflexe représente le début d'une chaîne de caractère. Néanmoins, lorsqu'il est utilisé après le crochet ouvrant, il permet d'inverser la gamme de caractère (exclusion). Par exemple, l'expression régulière `[^c]ar` signifie: n'importe quel caractère sauf `c`, suivi par la lettre `a`, suivie par la lettre `r`.

<pre>
"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/nNNlq3/1)

## 2.3 Répétitions

Les meta-caractères suivants `+`, `*` ou `?` sont utilisés pour spécifier combien de fois un sous-modèle peut apparaître. Ces meta-caractères agissent
différemment selon la situation dans laquelle ils sont utilisés.

### 2.3.1 Astérisque

Le symbole `*` correspond à zéro ou plus de répétitions du modèle précédent. L'expression régulière `a*` signifie: zéro ou plus de répétitions
du précédent `a` minuscule. Mais si il se trouve après une liste de caractères alors il s'agit de la répétition de la liste entière.
Par exemple, l'expression régulière `[a-z]*` signifie: n'importe combien de lettres minuscules.

<pre>
"[a-z]*" => T<a href="#learn-regex"><strong>he</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/7m8me5/1)

Le symbole `*` peut être utilisé avec le meta-caractère `.` pour correspondre à n'importe quel chaîne de caractères `.*`. Le symbole `*` peut être utilisé avec le
caractère espace vide `\s` pour correspondre à une chaîne d'espaces vides. Par exemple, l'expression `\s*cat\s*` signifie: zéro ou plus
d'espaces, suivits du caractère `c` minuscule, suivit par le caractère `a` minuscule, suivit par le caractère `t` minuscule, suivit par
zéro ou plus d'espaces.

<pre>
"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the <a href="#learn-regex">con<strong>cat</strong>enation</a>.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/gGrwuz/1)

### 2.3.2 Le Plus

Le meta-caractère `+` coïncide à une ou plusieurs répétitions du caractère précédent. Par exemple, l'expression régulière `c.+t` signifie: la lettre `c` minuscule, suivie par au moins un caractère, suivi par la lettre `t` minuscule. Le `t` coïncide par conséquent avec le dernier `t` de la phrase.

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/Dzf9Aa/1)

### 2.3.3 Le point d'interrogation

Le meta-caractère `?` rend le caractère précédent optionel. Ce symbol permet de faire coïncider 0 ou une instance du caractère précédent. Par exemple, l'expression régulière `[T]?he` signifie: lettre `T` majuscule optionelle, suivie par la lettre `h` minuscule, suivie par la lettre `e` minuscule.

<pre>
"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/cIg9zm/1)

<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/kPpO2x/1)

## 2.4 Accolades

Dans une expression régulière, les accolades, qui sont aussi appelée quantifieurs, sont utilisés pour spécifier le nombre de fois qu'un
caractère ou un groupe de caractères peut être répété. Par exemple, l'expression régulière `[0-9]{2,3}` signifie: Trouve au moins 2 chiffres mais pas plus de 3 (
caractères dans la gamme de 0 à 9).

<pre>
"[0-9]{2,3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/juM86s/1)

Nous pouvons ommettre le second nombre. Par exemple, l'expression régulière `[0-9]{2,}` signifie: Trouve 2 chiffres ou plus. Si nous supprimons aussi
la virgule l'expression régulière `[0-9]{3}` signifie: Trouve exactement 3 chiffres.

<pre>
"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/Gdy4w5/1)

<pre>
"[0-9]{3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to 10.0.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/Sivu30/1)

## 2.5 Groupement de caractères

Un groupement de caractères est un groupe de sous-modèles qui sont écris dans des parenthèses `(...)`. Nous avions mentionné plus tôt que dans une expression régulière
si nous mettons un quantifieur après un caractère alors le caractère précédent sera répété. Mais si nous mettons un quantifieur après un groupement de caractères alors
il répète le groupement de caractères entier. Par exemple, l'expression régulière `(ab)*` trouve zéro ou plus de répétitions du caractère "ab".
Nous pouvons aussi utiliser le meta-caractère d'alternation `|` à l'intérieur d'un groupement. Par exemple, l'expression régulière `(c|g|p)ar` signifie: caractère `c` minuscule,
`g` ou `p`, suivit par le caractère `a`, suivit par le caractère `r`.

<pre>
"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/tUxrBG/1)

## 2.6 Alternation

Dans une expression régulière, la barre verticale `|` est utilisée pour définir une alternation. l'alternation est comme une condition entre plusieurs expression. Maintenant,
nous pourrions penser que la liste de caractère et l'alternation sont la même chose. Mais la grande différence entre une liste de caractère et l'alternation
est que la liste de caractère fonctionne au niveau des caractères mais l'alternation fonctionne au niveau de l'expression. Par exemple, l'expression régulière
`(T|t)he|car` signifie: le caractère `T` majuscule ou `t` minuscule, suivit par le caractère `h` minuscule, suivit par le caractère `e` minuscule
ou le caractère `c` minuscule, suivit par le caractère `a` minuscule, suivit par le caractère `r` minuscule.

<pre>
"(T|t)he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/fBXyX0/1)

## 2.7 Caractère d'échappement

L'antislash `\` est utilisé dans les expression régulières pour échapper (ignorer) le caractère suivant. Cela permet de spécifier un symbole comme caractère à trouver
y compris les caractères réservés `{ } [ ] / \ + * . $ ^ | ?`. Pour utiliser un caractère spécial comme caractère à trouver, préfixer `\` avant celui-ci.
Par exemple, l'expression régulière `.` est utilisée pour trouver n'importe quel caractère sauf le retour de ligne. Donc pour trouver `.` dans une string
l'expression régulière `(f|c|m)at\.?` signifie: la lettre `f` minuscule, `c` or `m`, suivit par le caractère `a` minuscule, suivit par la lettre
`t` minuscule, suivit par le caractère optionnel `.`.

<pre>
"(f|c|m)at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Essayer l'expression régulière](https://regex101.com/r/DOc5Nu/1)

## 2.8 Ancres

Dans les expressions régulières, nous utilisons des ancres pour vérifier si le symbole trouvé est le premier ou dernier symbole de la
string. Il y a 2 types d'ancre: Le premier type est le circonflexe `^` qui cherche si le caractère est le premier
caractère de la string et le deuxième type est le Dollar `$` qui vérifie si le caractère est le dernier caractère de la string.

### 2.8.1 Circonflexe

Le symbole circonflexe `^` est utilisé pour vérifier si un caractère est le premier caractère de la string. Si nous appliquons l'expression régulière
suivante `^a` (si a est le premier symbole) à la string `abc`, ça coïncide. Mais si nous appliquons l'expression régulière `^b` sur cette même string,
ça ne coïncide pas. Parce que dans la string `abc` "b" n'est pas le premier symbole. Regardons une autre expression régulière
`^(T|t)he` qui signifie: le caractère `T` majuscule ou le caractère `t` minuscule est le premier symbole de la string,
suivi par le caractère `h` minuscule, suivit par le caractère `e` minuscule.

<pre>
"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/5ljjgB/1)

<pre>
"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/jXrKne/1)

### 2.8.2 Dollar

Dollar `$` symbol is used to check if matching character is the last character of the input string. For example, regular expression
`(at\.)$` means: a lowercase character `a`, followed by lowercase character `t`, followed by a `.` character and the matcher
must be end of the string.

<pre>
"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Essayer l'expression régulière](https://regex101.com/r/y4Au4D/1)

<pre>
"(at\.)$" => The fat cat. sat. on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Essayer l'expression régulière](https://regex101.com/r/t0AkOd/1)

##  3. Liste de caractères abrégés

Regular expression provides shorthands for the commonly used character sets, which offer convenient shorthands for commonly used
regular expressions. The shorthand character sets are as follows:

|Shorthand|Description|
|:----:|----|
|.|Any character except new line|
|\w|Matches alphanumeric characters: `[a-zA-Z0-9_]`|
|\W|Matches non-alphanumeric characters: `[^\w]`|
|\d|Matches digit: `[0-9]`|
|\D|Matches non-digit: `[^\d]`|
|\s|Matches whitespace character: `[\t\n\f\r\p{Z}]`|
|\S|Matches non-whitespace character: `[^\s]`|

## 4. Recherche

Lookbehind and lookahead sometimes known as lookaround are specific type of ***non-capturing group*** (Use to match the pattern but not
included in matching list). Lookaheads are used when we have the condition that this pattern is preceded or followed by another certain
pattern. For example, we want to get all numbers that are preceded by `$` character from the following input string `$4.44 and $10.88`.
We will use following regular expression `(?<=\$)[0-9\.]*` which means: get all the numbers which contain `.` character and  are preceded
by `$` character. Following are the lookarounds that are used in regular expressions:

|Symbol|Description|
|:----:|----|
|?=|Positive Lookahead|
|?!|Negative Lookahead|
|?<=|Positive Lookbehind|
|?<!|Negative Lookbehind|

### 4.1 Recherche avant positive

The positive lookahead asserts that the first part of the expression must be followed by the lookahead expression. The returned match
only contains the text that is matched by the first part of the expression. To define a positive lookahead, parentheses are used. Within
those parentheses, a question mark with equal sign is used like this: `(?=...)`. Lookahead expression is written after the equal sign inside
parentheses. For example, the regular expression `[T|t]he(?=\sfat)` means: optionally match lowercase letter `t` or uppercase letter `T`,
followed by letter `h`, followed by letter `e`. In parentheses we define positive lookahead which tells regular expression engine to match
`The` or `the` which are followed by the word `fat`.

<pre>
"[T|t]he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/IDDARt/1)

### 4.2 Recherche avant négative

Negative lookahead is used when we need to get all matches from input string that are not followed by a pattern. Negative lookahead
defined same as we define positive lookahead but the only difference is instead of equal `=` character we use negation `!` character
i.e. `(?!...)`. Let's take a look at the following regular expression `[T|t]he(?!\sfat)` which means: get all `The` or `the` words from
input string that are not followed by the word `fat` precedes by a space character.

<pre>
"[T|t]he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/V32Npg/1)

### 4.3 Recherche arrière positive

Positive lookbehind is used to get all the matches that are preceded by a specific pattern. Positive lookbehind is denoted by
`(?<=...)`. For example, the regular expression `(?<=[T|t]he\s)(fat|mat)` means: get all `fat` or `mat` words from input string that
are after the word `The` or `the`.

<pre>
"(?<=[T|t]he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/avH165/1)

### 4.4 Recherche arrière négative

Negative lookbehind is used to get all the matches that are not preceded by a specific pattern. Negative lookbehind is denoted by
`(?<!...)`. For example, the regular expression `(?<!(T|t)he\s)(cat)` means: get all `cat` words from input string that
are not after the word `The` or `the`.

<pre>
"(?&lt;![T|t]he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/8Efx5G/1)

## 5. Drapeaux

Flags are also called modifiers because they modify the output of a regular expression. These flags can be used in any order or
combination, and are an integral part of the RegExp.

|Flag|Description|
|:----:|----|
|i|Case insensitive: Sets matching to be case-insensitive.|
|g|Global Search: Search for a pattern throughout the input string.|
|m|Multiline: Anchor meta character works on each line.|

### 5.1 Insensible à la casse

The `i` modifier is used to perform case-insensitive matching. For example, the regular expression `/The/gi` means: uppercase letter
`T`, followed by lowercase character `h`, followed by character `e`. And at the end of regular expression the `i` flag tells the
regular expression engine to ignore the case. As you can see we also provided `g` flag because we want to search for the pattern in
the whole input string.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/dpQyf9/1)

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/ahfiuh/1)

### 5.2 Recherche globale

The `g` modifier is used to perform a global match (find all matches rather than stopping after the first match). For example, the
regular expression`/.(at)/g` means: any character except new line, followed by lowercase character `a`, followed by lowercase
character `t`. Because we provided `g` flag at the end of the regular expression now it will find every matches from whole input
string.

<pre>
"/.(at)/" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/jnk6gM/1)

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Essayer l'expression régulière](https://regex101.com/r/dO1nef/1)

### 5.3 Multilignes

The `m` modifier is used to perform a multi-line match. As we discussed earlier anchors `(^, $)` are used to check if pattern is
the beginning of the input or end of the input string. But if we want that anchors works on each line we use `m` flag. For example, the
regular expression `/at(.)?$/gm` means: lowercase character `a`, followed by lowercase character `t`, optionally anything except new
line. And because of `m` flag now regular expression engine matches pattern at the end of each line in a string.

<pre>
"/.at(.)?$/" => The fat
                cat sat
                on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Essayer l'expression régulière](https://regex101.com/r/hoGMkP/1)

<pre>
"/.at(.)?$/gm" => The <a href="#learn-regex"><strong>fat</strong></a>
                  cat <a href="#learn-regex"><strong>sat</strong></a>
                  on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Essayer l'expression régulière](https://regex101.com/r/E88WE2/1)

## Contribution

* Report issues
* Open pull request with improvements
* Spread the word
* Reach out to me directly at ziishaned@gmail.com or [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/ziishaned.svg?style=social&label=Follow%20%40ziishaned)](https://twitter.com/ziishaned)

## License

MIT © [Zeeshan Ahmed](mailto:ziishaned@gmail.com)
