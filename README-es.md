<br/>
<p align="center">
<img src="https://i.imgur.com/bYwl7Vf.png" alt="Learn Regex">
</p><br/>

## Translations:

* [English](README.md)
* [中文版](README-cn.md)
* [Español](README-es.md)

## What is Regular Expression?
> Una expresión regular es un grupo de caracteres o símbolos, los cuales son usados para buscar un patrón específico dentro de un texto.

Una expresión regular es un patrón que que se compara con una cadena de caracteres de izquierda a derecha. La palabra "expresión regular", puede también ser escrita como "Regex" o "Regexp". Las expresiones regulares se utiliza para remplazar un texto, dentro de un *string* (o cadena de caracteres), validar el formato, extraer un substring de un string completo basado en la coincidencia de una patrón, y muchas cosas más.

Imagina que estas escribiendo una aplicación y quieres agregar reglas para cuando el usuario elija su nombre de usuario. Nosotros vamos a querer que el nombre de usuario contenga letras, números, guión bajo, y guíon medio. También vamos a querer limitar el número de caracteres en el nombre de usuario para que no se vea feo. Para ello usamos la siguiente expresión regular para validar el nombre de usuario


<br/><br/>
<p align="center">
<img src="http://imgur.com/EtlKH14.png" alt="Regular expression">
</p>

De la expresión regular anterior, se puede aceptar las cadenas 'john_doe', 'jo-hn_doe' y 'john12_as'. La expresión no coincide con el nombre de usuario 'Jo', porque es una cadena de caracteres que contiene letras mayúsculas y es demasiado corta.

## Tabla de contenido

- [Introducción](#1-introduccion)
- [Meta caracteres](#2-meta-caracteres)
  - [Full stop](#21-full-stop)
  - [Conjunto de caracteres](#22-conjunto-de-caracteres)
    - [Conjunto de caracteres negados](#221-conjunto-de-caracteres-negado)
  - [Repeticiones](#23-repeticiones)
    - [Asterísco](#231-asterisco)
    - [Signo más](#232-signo-mas)
    - [Signo de pregunta](#233-signo-de-pregunta)
  - [Llaves](#24-llaves)
  - [Grupo de caracteres](#25-grupo-de-caracteres)
  - [Alternancia](#26-alternacia)
  - [Caracteres especiales de escape](#27-caracteres-especiales-de-escape)
  - [Anclas](#28-anclas)
    - [Símbolo de intercalación](#281-simbolo-de-intercalacion)
    - [Símbolo dolar](#282-simbolo-dolar)
- [Conjunto de caracteres abreviados](#3-conjunto-de-caracteres-abreviados)
- [Mirar alrededor](#4-mirar-alrededor)
  - [Mirar hacia delante positivo](#41-mirar-hacia-delante-positivo)
  - [Mirar hacia delante negativo](#41-mirar-hacia-delaten-negativo)
  - [Mirar hacia atrás positivo](#41-mirar-hacia-atras-positivo)
  - [Mirar hacia atrás negativo](#41-mirar-hacia-atras-negativo)
- [Banderas](#5-banderas)
  - [mayúsculas y minúsculas](#51-mayusculas-y-minusculas)
  - [Búsqueda global](#52-busqueda-global)
  - [Multilinea](#53-multilinea)
- [Bonus](#bonus)

## 1. Introducción

Una expresión regular es sólo un patrón de caracteres que utilizamos para realizar búsquedas en un texto. Por ejemplo, la expresión regular «the» significa: la letra `t` seguida de la letra `h` seguida de la letra `e`.

<pre>
"the" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Prueba la expresión regular](https://regex101.com/r/dmRygT/1)

La expresión regular `123` coincide con la cadena `123`. La expresión regular se compara con una cadena de entrada al comparar cada carácter de la expresión regular con cada carácter de la cadena de entrada, uno tras otro. Las expresiones regulares son normalmente sensibles a mayúsculas y minúsculas, por lo que la expresión regular `The` no coincide con la cadena `the`.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Prueba la expresión regular](https://regex101.com/r/1paXsy/1)

## 2. Meta caracteres

Los caracteres meta son los bloques de construcción de las expresiones regulares. Los meta caracteres no se sostienen a sí mismos, sino que se interpretan de alguna manera especial. Algunos meta caracteres tienen un significado especial y se escriben entre corchetes. Los meta caracteres son los siguientes:

|Meta character|Description|
|:----:|----|
|.|Periodo. Coincide con cualquier caracter excepto un salto de línea.|
|[ ]|Clase caracter. Coincide con cualquier caracter contenido entre corchetes.|
|[^ ]|Clase caracter negado. Coincide con cualquier caracter que no está contenido dentro de los corchetes.|
|*|Corresponde con 0 o más repeticiones del símbolo precedente.|
|+|Corresponde con 1 o más repeticiones del símbolo precedente.|
|?|Hace que el símbolo precedente sea opcional.|
|{n,m}|Llaves.Corresponde al menos "n" pero no más de "m" repeticiones del símbolo precedente.|
|(xyz)|Grupo caracter. Hace coincidir los caracteres xyz en ese orden exacto.|
|&#124;|Alternancia. Corresponde a los caracteres anteriores o los caracteres después del símbolo.|
|&#92;|Escapa el siguiente caracter. Esto le permite hacer coincidir los caracteres reservados <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>|
|^|Hace coincidir el principio de la entrada.|
|$|Corresponde al final de la entrada.|

## 2.1 Full stop

Full stop `.` es el ejemplo más simple del meta-caracter. El caracter meta "." coincide con cualquier carácter. No coincidirá con el retorno o nuevos caracteres de línea. Por ejemplo, la expresión regular `.ar` significa: cualquier caracter, seguido de la letra`a`, seguido de la letra "r".

<pre>
".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Prueba la expresión regular](https://regex101.com/r/xc9GkU/1)

## 2.2 Conjunto de caracteres

Los conjuntos de caracteres también se llaman clase de caracteres. Los corchetes se utilizan para especificar conjuntos de caracteres. Utilice un guión dentro de un conjunto de caracteres para especificar el rango de los caracteres. El orden del rango de caracteres dentro de corchetes no importa. Por ejemplo, la expresión regular "[Tt] he" significa: una letra mayúscula "T" o <minúscula> t, seguida de la letra "h" seguida de la letra "e"

<pre>
"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Prueba la expresión regular](https://regex101.com/r/2ITLQ4/1)

Sin embargo, un período dentro de un conjunto de caracteres significa un período literal. La expresión regular `ar [.]` Significa: un carácter minúsculo `a`, seguido de la letra` r`, seguido de un carácter `.`.

<pre>
"ar[.]" => A garage is a good place to park a c<a href="#learn-regex"><strong>ar.</strong></a>
</pre>

[Prueba la expresión regular](https://regex101.com/r/wL3xtE/1)

### 2.2.1 Conjunto de caracteres negados

En general, el símbolo de intercalación representa el comienzo de la cadena, pero cuando se escribe después del corchete de apertura niega el conjunto de caracteres. Por ejemplo, la expresión regular `[^c] ar` significa: cualquier carácter, excepto `c`, seguido del carácter `a`, seguido de la letra `r`.

<pre>
"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Prueba la expresión regular](https://regex101.com/r/nNNlq3/1)

## 2.3 Repeticiones

Siguiendo los caracteres meta +, * o ?, se utilizan para especificar cuántas veces puede producirse un subpatrón. Estos meta-caracteres actúan de manera diferente en diferentes situaciones.

### 2.3.1 Asterísco

El símbolo `*` coincide con cero o más repeticiones del marcador anterior. La expresión regular `a*` significa: cero o más repeticiones del carácter en minúscula precedente `a`. Pero si aparece después de un conjunto de caracteres o una clase, entonces encuentra las repeticiones de todo el conjunto de caracteres. Por ejemplo, la expresión regular `[a-z]*` significa: cualquier número de letras minúsculas en una fila.

<pre>
"[a-z]*" => T<a href="#learn-regex"><strong>he</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.
</pre>

[Prueba la expresión regular](https://regex101.com/r/7m8me5/1)

El símbolo `*` se puede utilizar con el meta-caracter `.` para que coincida con cualquier cadena de caracteres `.*`. El símbolo `*` se lo puede utilizar con el caracter de espacio en blanco `\s` para que coincida con una cadena de caracteres de espacio en blanco. Por ejemplo, la expresión "\s*cat\s*" significa: cero o más espacios, seguido por el carácter en minúscula `c`, seguido del carácter en minúscula `a`, seguido del carácter en minúscula `t`, seguido de cero o más espacios.

<pre>
"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the <a href="#learn-regex">con<strong>cat</strong>enation</a>.
</pre>

[Prueba la expresión regular](https://regex101.com/r/gGrwuz/1)

### 2.3.2 Signo más

El símbolo `+` coincide con una o más repeticiones del carácter anterior. Por ejemplo, la expresión regular `c.+T` significa: letra  en minúscula `c`, seguida por al menos uno del mismo carácter, luego el carácter en minúscula `t`.

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

[Prueba la expresión regular](https://regex101.com/r/Dzf9Aa/1)

### 2.3.3 Signo de pregunta

En expresiones regulares el meta-caracter `?` hace que el caracter precedente sea opcional. Este símnbolo coincide con cero o una instancia del caracter precedente. Por ejemplo, la expresión regular  `[T]?he` significa: El caracteropcional predecesor `T` seguido por la letra en minúscula `h`, seguido del caracter en minúscula `e`.

<pre>
"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Prueba la expresión regular](https://regex101.com/r/cIg9zm/1)

<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

[Prueba la expresión regular](https://regex101.com/r/kPpO2x/1)

## 2.4 Llaves

En la expresión regular, las llaves que también se denominan cuantificadores se utilizan para especificar el número de veces que se puede repetir un carácter o un grupo de caracteres. Por ejemplo, la expresión regular `[0-9]{2,3}` significa: Combina al menos 2 dígitos pero no más de 3 (caracteres del rango de 0 a 9).

<pre>
"[0-9]{2,3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Prueba la expresión regular](https://regex101.com/r/juM86s/1)

Podemos dejar fuera el segundo número. Por ejemplo, la expresión regular `[0-9] {2,}` significa: Combina 2 o más dígitos. Si también eliminamos la coma, la expresión regular `[0-9]{3}` significa: coincidir exactamente con 3 dígitos.

<pre>
"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Prueba la expresión regular](https://regex101.com/r/Gdy4w5/1)

<pre>
"[0-9]{3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to 10.0.
</pre>

[Prueba la expresión regular](https://regex101.com/r/Sivu30/1)

## 2.5 Grupos de caracteres

Grupo de caracteres es un grupo de sub-patrones que se escribe dentro de paréntesis `(...)`. Como hemos discutido antes en la expresión regular si ponemos un cuantificador después de un caracter, repetiremos el caracter anterior. Pero si ponemos cuantificador después de un grupo de caracteres, entonces repetimos todo el grupo de caracteres. Por ejemplo, la expresión regular `(ab)*` coincide con cero o más repeticiones del caracter "ab". También podemos usar el caracter de alternancia `|` meta dentro del grupo de caracteres. Por ejemplo, la expresión regular `(c|g|p)ar` significa: caracter en minúscula `c`, `g` o `p`, seguido del caracter `a`, seguido del caracter `r`.
<pre>
"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Prueba la expresión regular](https://regex101.com/r/tUxrBG/1)

## 2.6 Alternancia

En la expresión regular se usa la barra vertical `|` para definir la alternancia. La alternancia es como una condición entre múltiples expresiones. Ahora, puedes estar pensando que el conjunto de caracteres y la alternancia funciona de la misma manera. Pero la gran diferencia entre el conjunto de caracteres y la alternancia es que el conjunto de caracteres funciona a nivel de caracter pero la alternancia funciona a nivel de expresión. Por ejemplo, la expresión regular `(T|t)he|car` significa: el carcter en mayúscula `T` o en minúscula `t`, seguido del caracter en minúscula `h`, seguido del caracter en minúscula `e` o del caracter en minúscula `c`, seguido de un caracter en minúscula `a`, seguido del carácter en minúscula `r`.

<pre>
"(T|t)he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Prueba la expresión regular](https://regex101.com/r/fBXyX0/1)

## 2.7 Caracteres especiales de escape

La barra invertida `\` se utiliza en la expresión regular para escapar del carácter siguiente. Esto permite especificar un símbolo como un caracter coincidente incluyendo caracteres reservados `{}[]/\+*.^|?`. Por ejemplo, la expresión regular `.` se utiliza para coincidir con cualquier caracter, excepto la nueva línea. Ahora, para emparejar `.` en una cadena de entrada, la expresión regular `(f|c|m)at\.?` significa: la letra minúscula `f`, `c` o `m`, seguida del caracter en minúscula `a`, seguido de la letra minúscula `t`, seguida del caracter opcional `.`.

<pre>
"(f|c|m)at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Prueba la expresión regular](https://regex101.com/r/DOc5Nu/1)

## 2.8 Anchors

In regular expressions, we use anchors to check if the matching symbol is the starting symbol or ending symbol of the
input string. Anchors are of two types: First type is Caret `^` that check if the matching character is the start
character of the input and the second type is Dollar `$` that checks if matching character is the last character of the
input string.

### 2.8.1 Caret

Caret `^` symbol is used to check if matching character is the first character of the input string. If we apply the following regular
expression `^a` (if a is the starting symbol) to input string `abc` it matches `a`. But if we apply regular expression `^b` on above
input string it does not match anything. Because in input string `abc` "b" is not the starting symbol. Let's take a look at another
regular expression `^(T|t)he` which means: uppercase character `T` or lowercase character `t` is the start symbol of the input string,
followed by lowercase character `h`, followed by lowercase character `e`.

<pre>
"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Test the regular expression](https://regex101.com/r/5ljjgB/1)

<pre>
"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Test the regular expression](https://regex101.com/r/jXrKne/1)

### 2.8.2 Dollar

Dollar `$` symbol is used to check if matching character is the last character of the input string. For example, regular expression
`(at\.)$` means: a lowercase character `a`, followed by lowercase character `t`, followed by a `.` character and the matcher
must be end of the string.

<pre>
"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Test the regular expression](https://regex101.com/r/y4Au4D/1)

<pre>
"(at\.)$" => The fat cat. sat. on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Test the regular expression](https://regex101.com/r/t0AkOd/1)

##  3. Shorthand Character Sets

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

## 4. Lookaround

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

### 4.1 Positive Lookahead

The positive lookahead asserts that the first part of the expression must be followed by the lookahead expression. The returned match
only contains the text that is matched by the first part of the expression. To define a positive lookahead, parentheses are used. Within
those parentheses, a question mark with equal sign is used like this: `(?=...)`. Lookahead expression is written after the equal sign inside
parentheses. For example, the regular expression `[T|t]he(?=\sfat)` means: optionally match lowercase letter `t` or uppercase letter `T`,
followed by letter `h`, followed by letter `e`. In parentheses we define positive lookahead which tells regular expression engine to match
`The` or `the` which are followed by the word `fat`.

<pre>
"[T|t]he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Test the regular expression](https://regex101.com/r/IDDARt/1)

### 4.2 Negative Lookahead

Negative lookahead is used when we need to get all matches from input string that are not followed by a pattern. Negative lookahead
defined same as we define positive lookahead but the only difference is instead of equal `=` character we use negation `!` character
i.e. `(?!...)`. Let's take a look at the following regular expression `[T|t]he(?!\sfat)` which means: get all `The` or `the` words from
input string that are not followed by the word `fat` precedes by a space character.

<pre>
"[T|t]he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Test the regular expression](https://regex101.com/r/V32Npg/1)

### 4.3 Positive Lookbehind

Positive lookbehind is used to get all the matches that are preceded by a specific pattern. Positive lookbehind is denoted by
`(?<=...)`. For example, the regular expression `(?<=[T|t]he\s)(fat|mat)` means: get all `fat` or `mat` words from input string that
are after the word `The` or `the`.

<pre>
"(?<=[T|t]he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Test the regular expression](https://regex101.com/r/avH165/1)

### 4.4 Negative Lookbehind

Negative lookbehind is used to get all the matches that are not preceded by a specific pattern. Negative lookbehind is denoted by
`(?<!...)`. For example, the regular expression `(?<!(T|t)he\s)(cat)` means: get all `cat` words from input string that
are not after the word `The` or `the`.

<pre>
"(?&lt;![T|t]he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

[Test the regular expression](https://regex101.com/r/8Efx5G/1)

## 5. Flags

Flags are also called modifiers because they modify the output of a regular expression. These flags can be used in any order or
combination, and are an integral part of the RegExp.

|Flag|Description|
|:----:|----|
|i|Case insensitive: Sets matching to be case-insensitive.|
|g|Global Search: Search for a pattern throughout the input string.|
|m|Multiline: Anchor meta character works on each line.|

### 5.1 Case Insensitive

The `i` modifier is used to perform case-insensitive matching. For example, the regular expression `/The/gi` means: uppercase letter
`T`, followed by lowercase character `h`, followed by character `e`. And at the end of regular expression the `i` flag tells the
regular expression engine to ignore the case. As you can see we also provided `g` flag because we want to search for the pattern in
the whole input string.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Test the regular expression](https://regex101.com/r/dpQyf9/1)

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Test the regular expression](https://regex101.com/r/ahfiuh/1)

### 5.2 Global search

The `g` modifier is used to perform a global match (find all matches rather than stopping after the first match). For example, the
regular expression`/.(at)/g` means: any character except new line, followed by lowercase character `a`, followed by lowercase
character `t`. Because we provided `g` flag at the end of the regular expression now it will find every matches from whole input
string.

<pre>
"/.(at)/" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

[Test the regular expression](https://regex101.com/r/jnk6gM/1)

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Test the regular expression](https://regex101.com/r/dO1nef/1)

### 5.3 Multiline

The `m` modifier is used to perform a multi-line match. As we discussed earlier anchors `(^, $)` are used to check if pattern is
the beginning of the input or end of the input string. But if we want that anchors works on each line we use `m` flag. For example, the
regular expression `/at(.)?$/gm` means: lowercase character `a`, followed by lowercase character `t`, optionally anything except new
line. And because of `m` flag now regular expression engine matches pattern at the end of each line in a string.

<pre>
"/.at(.)?$/" => The fat
                cat sat
                on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Test the regular expression](https://regex101.com/r/hoGMkP/1)

<pre>
"/.at(.)?$/gm" => The <a href="#learn-regex"><strong>fat</strong></a>
                  cat <a href="#learn-regex"><strong>sat</strong></a>
                  on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Test the regular expression](https://regex101.com/r/E88WE2/1)

## Bonus

* *Positive Integers*: `^\d+$`
* *Negative Integers*: `^-\d+$`
* *US Phone Number*: `^+?[\d\s]{3,}$`
* *US Phone with code*: `^+?[\d\s]+(?[\d\s]{10,}$`
* *Integers*: `^-?\d+$`
* *Username*: `^[\w.]{4,16}$`
* *Alpha-numeric characters*: `^[a-zA-Z0-9]*$`
* *Alpha-numeric characters with spaces*: `^[a-zA-Z0-9 ]*$`
* *Password*: `^(?=^.{6,}$)((?=.*[A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z]))^.*$`
* *email*: `^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})*$`
* *IPv4 address*: `^((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))*$`
* *Lowercase letters only*: `^([a-z])*$`
* *Uppercase letters only*: `^([A-Z])*$`
* *URL*: `^(((http|https|ftp):\/\/)?([[a-zA-Z0-9]\-\.])+(\.)([[a-zA-Z0-9]]){2,4}([[a-zA-Z0-9]\/+=%&_\.~?\-]*))*$`
* *VISA credit card numbers*: `^(4[0-9]{12}(?:[0-9]{3})?)*$`
* *Date (DD/MM/YYYY)*: `^(0?[1-9]|[12][0-9]|3[01])[- /.](0?[1-9]|1[012])[- /.](19|20)?[0-9]{2}$`
* *Date (MM/DD/YYYY)*: `^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](19|20)?[0-9]{2}$`
* *Date (YYYY/MM/DD)*: `^(19|20)?[0-9]{2}[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])$`
* *MasterCard credit card numbers*: `^(5[1-5][0-9]{14})*$`
* *Hashtags*: Including hashtags with preceding text (abc123#xyz456) or containing white spaces within square brackets (#[foo bar]) : `\S*#(?:\[[^\]]+\]|\S+)`
* *@mentions*: `\B@[a-z0-9_-]+`
## Contribution

* Report issues
* Open pull request with improvements
* Spread the word
* Reach out to me directly at ziishaned@gmail.com or [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/ziishaned.svg?style=social&label=Follow%20%40ziishaned)](https://twitter.com/ziishaned)

## License

MIT © [Zeeshan Ahmed](mailto:ziishaned@gmail.com)
