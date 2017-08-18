<br/>
<p align="center">
<img src="https://i.imgur.com/bYwl7Vf.png" alt="Learn Regex">
</p><br/>

## Traduções:

* [English](README.md)
* [Español](README-es.md)
* [中文版](README-cn.md)
* [日本語](README-ja.md)
* [Português do Brasil](README-pt_BR.md)

## O que é uma Expressão Regular?

> Expressão Regular é um grupo de caracteres ou símbolos utilizado para encontrar um padrão específico a partir de um texto.

Uma expressão regular é um padrão que é comparado com uma cadeia de caracteres da esquerda para a direita. A expressão "Expressão regular" é longa e difícil de falar, você geralmente vai encontrar o termo abreviado como "regex" ou "regexp". Expressões regulares são usadas para substituir um texto dentro de uma string, validar formulários, extrair uma parte de uma string baseada em um padrão encontrado e muito mais.

Imagine que você está escrevendo uma aplicação e quer colocar regras para quando um usuário escolher seu username. Nós queremos permitir que o username contenha letras, números, underlines e hífens. Nós também queremos limitar o número de caracteres para não ficar muito feio. Então usamos a seguinte expressão regular para validar o username:

<br/><br/>
<p align="center">
<img src="https://i.imgur.com/ekFpQUg.png" alt="Regular expression">
</p>

A expressão regular acima aceita as strings `john_doe`, `jo-hn_doe` e `john12_as`. Ela não aceita `Jo` porque essa string contém letras maiúsculas e também é muito curta.

## Sumário

- [Combinações Básicas](#1-combinações-básicas)
- [Metacaracteres](#2-metacaracteres)
  - [Ponto final](#21-ponto-final)
  - [Conjunto de caracteres](#22-conjunto-de-caracteres)
    - [Conjunto de caracteres negados](#221-conjunto-de-caracteres-negados)
  - [Repetições](#23-repetições)
    - [O Asterisco](#231-o-asterisco)
    - [O Sinal de Adição](#232-o-sinal-de-adição)
    - [O Ponto de Interrogação](#233-o-ponto-de-interrogação)
  - [Chaves](#24-chaves)
  - [Grupo de Caracteres](#25-grupo-de-caracteres)
  - [Alternância](#26-alternância)
  - [Escapando Caracteres Especiais](#27-escapando-caracteres-especiais)
  - [Âncoras](#28-Âncoras)
    - [Acento Circunflexo](#281-acento-circunflexo)
    - [Sinal de Dólar](#282-sinal-de-dólar)
- [Forma Abreviada de Conjunto de Caracteres](#3-forma-abreviada-de-conjunto-de-caracteres)
- [Olhar ao Redor](#4-olhar-ao-redor)
  - [Lookahead Positivo](#41-lookahead-positivo)
  - [Lookahead Negativo](#42-lookahead-negativo)
  - [Lookbehind Positivo](#43-lookbehind-positivo)
  - [Lookbehind Negativo](#44-lookbehind-negativo)
- [Flags](#5-flags)
  - [Indiferente à Maiúsculas](#51-indiferente-à-maiúsculas)
  - [Busca Global](#52-busca-global)
  - [Multilinhas](#53-multilinhas)

## 1. Combinações Básicas

Uma expressão regular é apenas um padrão de caracteres que usamos para fazer busca em um texto. Por exemplo, a expressão regular `the` significa: a letra `t`, seguida da letra `h`, seguida da letra `e`.

<pre>
"the" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Teste a RegExp](https://regex101.com/r/dmRygT/1)

A expressão regular `123` corresponde a string `123`. A expressão regular é comparada com uma string de entrada, comparando cada caractere da expressão regular para cada caractere da string de entrada, um após o outro. Expressões regulares são normalmente case-sensitive (sensíveis à maiúsculas), então a expressão regular `The` não vai bater com a string `the`.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Teste a RegExp](https://regex101.com/r/1paXsy/1)

## 2. Metacaracteres

Metacaracteres são elementos fundamentais das expressões regulares. Metacaracteres não representam a si mesmos mas, ao invés disso, são interpretados de uma forma especial. Alguns metacaracteres tem um significado especial e são escritos dentro de colchetes.
Os metacaracteres são os seguintes:

|Metacaracter|Descrição|
|:----:|----|
|.|Corresponde a qualquer caractere, exceto uma quebra de linha|
|[ ]|Classe de caracteres. Corresponde a qualquer caractere contido dentro dos colchetes.|
|[^ ]|Classe de caracteres negada. Corresponde a qualquer caractere que não está contido dentro dos colchetes.|
|*|Corresponde à 0 ou mais repetições do símbolo anterior.|
|+|Corresponde à 1 ou mais repetições do símbolo anterior.|
|?|Faz com que o símbolo anterior seja opcional.|
|{n,m}|Chaves. Corresponde à no mínimo "n" mas não mais que "m" repetições do símbolo anterior.|
|(xyz)|Grupo de caracteres. Corresponde aos caracteres xyz nesta exata ordem.|
|&#124;|Alternância. Corresponde os caracteres antes ou os caracteres depois do símbolo|
|&#92;|Escapa o próximo caractere. Isso permite você utilizar os caracteres reservados <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>|
|^|Corresponde ao início da entrada.|
|$|Corresponde ao final da entrada.|

## 2.1 Ponto final

O ponto final `.` é um simples exemplo de metacaracteres. O metacaractere `.` corresponde à qualquer caractere sozinho. Ele não se iguala ao Enter e à quebra de linha. Por exemplo, a expressão regular `.ar` significa: qualquer caractere, seguido da letra `a`, seguida da letra `r`.

<pre>
".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Teste a RegExp](https://regex101.com/r/xc9GkU/1)

## 2.2 Conjunto de caracteres

Conjuntos de caracteres também são chamados de classes de caracteres. Utilizamos colchetes para especificar conjuntos de caracteres. Use um hífen dentro de um conjunto de caracteres para especificar o intervalo de caracteres. A ordem dos caracteres dentro dos colchetes não faz diferença. Por exemplo, a expressão regular `[Tt]he` significa: um caractere maiúsculo `T` ou minúsculo `t`, seguido da letra `h`, seguida da letra `e`.

<pre>
"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Teste a RegExp](https://regex101.com/r/2ITLQ4/1)

No entanto, um ponto final dentro de um conjunto de caracteres, significa apenas um ponto final. A expressão regular `ar[.]` significa: o caractere minúsculo `a`, seguido da letra `r`, seguida pelo caractere de ponto final `.`.

<pre>
"ar[.]" => A garage is a good place to park a c<a href="#learn-regex"><strong>ar.</strong></a>
</pre>

[Teste a RegExp](https://regex101.com/r/wL3xtE/1)

### 2.2.1 Conjunto de caracteres negados

No geral, o símbolo do circunflexo representa o início da string, mas quando está logo após o colchete de abertura, ele faz a negação do conjunto de caracteres. Por exemplo, a expressão regular `[^c]ar` significa: qualquer caractere com exceção do `c`, seguido pelo caractere `a`, seguido da letra `r`.

<pre>
"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Teste a RegExp](https://regex101.com/r/nNNlq3/1)

## 2.3 Repetições

Seguindo os metacaracteres `+`, `*` ou `?` são utilizados para especificar quantas vezes um sub-padrão pode ocorrer. Esses metacaracteres atuam de formas diferentes em diferentes situações.

### 2.3.1 O Asterisco

O símbolo `*` corresponde à zero ou mais repetições do padrão antecedente. A expressão regular `a*` significa: zero ou mais repetições do caractere minúsculo precedente `a`. Mas se o asterisco aparecer depois de um conjunto de caracteres, ou classe de caracteres, ele irá procurar as repetições de todo o conjunto. Por exemplo, a expressão regular `[a-z]*` significa: qualquer quantidade de letras minúsculas numa linha.

<pre>
"[a-z]&ast;" => T<a href="#learn-regex"><strong>he</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.
</pre>

[Teste a RegExp](https://regex101.com/r/7m8me5/1)

O símbolo `*` pode ser usado junto do metacaractere `.` para encontrar qualquer string de caracteres `.*`. O símbolo `*` pode ser usado com o caractere de espaço em branco `\s` para encontrar uma string de caracteres em branco. Por exemplo, a expressão `\s*cat\s*` significa: zero ou mais espaços, seguidos do caractere minúsculo `c`, seguido do caractere minúsculo `a`, seguido do caractere minúsculo `t`, seguido de zero ou mais espaços.

<pre>
"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the <a href="#learn-regex">con<strong>cat</strong>enation</a>.
</pre>

[Teste a RegExp](https://regex101.com/r/gGrwuz/1)

### 2.3.2 O Sinal de Adição

O símbolo `+` corresponde à uma ou mais repetições do caractere anterior. Por exemplo, a expressão regular `c.+t` significa: a letra minúscula `c`, seguida por pelo menos um caractere, seguido do caractere minúsculo `t`.

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

[Teste a RegExp](https://regex101.com/r/Dzf9Aa/1)

### 2.3.3 O Ponto de Interrogação

Em expressões regulares, o metacaractere `?` faz o caractere anterior ser opcional. Esse símbolo corresponde à zero ou uma ocorrência do caractere anterior. Por exemplo, a expressão regular `[T]?he` significa: A letra maiúsculo `T` opcional, seguida do caractere minúsculo `h`, seguido do caractere minúsculo `e`.

<pre>
"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Teste a RegExp](https://regex101.com/r/cIg9zm/1)

<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

[Teste a RegExp](https://regex101.com/r/kPpO2x/1)

## 2.4 Chaves

Em expressões regulares, chaves, que também são chamadas de quantificadores, são utilizadas para especificar o número de vezes que o caractere, ou um grupo de caracteres, pode se repetir. Por exemplo, a expressão regular `[0-9]{2,3}` significa: Encontre no mínimo 2 dígitos, mas não mais que 3 (caracteres no intervalo de 0 à 9).

<pre>
"[0-9]{2,3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Teste a RegExp](https://regex101.com/r/juM86s/1)

Nós podemos retirar o segundo número. Por exemplo, a expressão regular `[0-9]{2,}` significa: Encontre 2 ou mais dígitos. Se removermos a vírgula a expressão regular `[0-9]{3}` significa: Encontre exatamente 3 dígitos.

<pre>
"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Teste a RegExp](https://regex101.com/r/Gdy4w5/1)

<pre>
"[0-9]{3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to 10.0.
</pre>

[Teste a RegExp](https://regex101.com/r/Sivu30/1)

## 2.5 Grupo de Caracteres

Grupo de caracteres é um grupo de sub-padrão que é escrito dentro de parênteses `(...)`. Como falamos antes, se colocaramos um quantificador depois de um caractere, ele irá repetir o caractere anterior. Mas se colocarmos um quantificador depois de um grupo de caracteres, ele irá repetir todo o conjunto. Por exemplo, a expressão regular `(ab)*` corresponde à zero ou mais repetições dos caracteres "ab". Nós também podemos usar o metacaractere de alternância `|` dentro de um grupo de caracteres. Por exemplo, a expressão regular `(c|g|p)ar` significa: caractere minúsculo `c`, `g` ou `p`, seguido do caractere `a`, seguido do caractere `r`.

<pre>
"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Teste a RegExp](https://regex101.com/r/tUxrBG/1)

## 2.6 Alternância

Em expressões regulares, a barra vertical `|` é usada para definir alternância. Alternância é como uma condição entre múltiplas expressões. Agora, você pode estar pensando que um conjunto de caracteres e a alternância funcionam da mesma forma. Mas a grande diferença entre eles é que o conjunto de caracteres trabalha no nível de caracteres, enquanto a alternância trabalha no nível das expressões. Por exemplo, a expressão regular `(T|t)he|car` significa: o caractere maiúsculo `T` ou minúsculo `t`, seguido do caractere minúsculo `h`, seguido do caractere minúsculo `e` ou o caractere minúsculo `c`, seguido do caractere minúsculo `a`, seguido do caractere minúsculo `r`.

<pre>
"(T|t)he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Teste a RegExp](https://regex101.com/r/fBXyX0/1)

## 2.7 Escapando Caracteres Especiais

Em expressões regulares, a contrabarra `\` é usada para escapar o próximo caractere. Isso possibilita especificar um símbolo como um caractere correspondente, incluindo os caracteres reservados `{ } [ ] / \ + * . $ ^ | ?`. Para usar um caractere especial como um caractere correspondente, utilize `\` antes dele. Por exemplo, a expressão regular `.` é usada para encontrar qualquer caractere, exceto nova linha. Agora, para encontrar `.` em uma string de entrada, a expressão regular `(f|c|m)at\.?` significa: letra minúscula `f`, `c` ou `m`, seguida do caractere minúsculo `a`, seguido da letra minúscula `t`, seguida do caractere `.` opcional.

<pre>
"(f|c|m)at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Teste a RegExp](https://regex101.com/r/DOc5Nu/1)

## 2.8 Âncoras

In regular expressions, we use anchors to check if the matching symbol is the starting symbol or ending symbol of the
input string. Âncoras are of two types: First type is Acento Circunflexo `^` that check if the matching character is the start
character of the input and the second type is Sinal de Dólar `$` that checks if matching character is the last character of the
input string.

### 2.8.1 Acento Circunflexo

Acento Circunflexo `^` symbol is used to check if matching character is the first character of the input string. If we apply the following regular
expression `^a` (if a is the starting symbol) to input string `abc` it matches `a`. But if we apply regular expression `^b` on above
input string it does not match anything. Because in input string `abc` "b" is not the starting symbol. Let's take a look at another
regular expression `^(T|t)he` which means: uppercase character `T` or lowercase character `t` is the start symbol of the input string,
followed by lowercase character `h`, followed by lowercase character `e`.

<pre>
"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Teste a RegExp](https://regex101.com/r/5ljjgB/1)

<pre>
"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Teste a RegExp](https://regex101.com/r/jXrKne/1)

### 2.8.2 Sinal de Dólar

Sinal de Dólar `$` symbol is used to check if matching character is the last character of the input string. For example, regular expression
`(at\.)$` means: a lowercase character `a`, followed by lowercase character `t`, followed by a `.` character and the matcher
must be end of the string.

<pre>
"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Teste a RegExp](https://regex101.com/r/y4Au4D/1)

<pre>
"(at\.)$" => The fat cat. sat. on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Teste a RegExp](https://regex101.com/r/t0AkOd/1)

##  3. Forma Abreviada de Conjunto de Caracteres

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

## 4. Olhar ao Redor

Lookbehind and lookahead sometimes known as lookaround are specific type of ***non-capturing group*** (Use to match the pattern but not
included in matching list). Lookaheads are used when we have the condition that this pattern is preceded or followed by another certain
pattern. For example, we want to get all numbers that are preceded by `$` character from the following input string `$4.44 and $10.88`.
We will use following regular expression `(?<=\$)[0-9\.]*` which means: get all the numbers which contain `.` character and  are preceded
by `$` character. Following are the lookarounds that are used in regular expressions:

|Symbol|Description|
|:----:|----|
|?=|Lookahead Positivo|
|?!|Lookahead Negativo|
|?<=|Lookbehind Positivo|
|?<!|Lookbehind Negativo|

### 4.1 Lookahead Positivo

The positive lookahead asserts that the first part of the expression must be followed by the lookahead expression. The returned match
only contains the text that is matched by the first part of the expression. To define a positive lookahead, parentheses are used. Within
those parentheses, a question mark with equal sign is used like this: `(?=...)`. Lookahead expression is written after the equal sign inside
parentheses. For example, the regular expression `[T|t]he(?=\sfat)` means: optionally match lowercase letter `t` or uppercase letter `T`,
followed by letter `h`, followed by letter `e`. In parentheses we define positive lookahead which tells regular expression engine to match
`The` or `the` which are followed by the word `fat`.

<pre>
"[T|t]he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Teste a RegExp](https://regex101.com/r/IDDARt/1)

### 4.2 Lookahead Negativo

Negative lookahead is used when we need to get all matches from input string that are not followed by a pattern. Negative lookahead
defined same as we define positive lookahead but the only difference is instead of equal `=` character we use negation `!` character
i.e. `(?!...)`. Let's take a look at the following regular expression `[T|t]he(?!\sfat)` which means: get all `The` or `the` words from
input string that are not followed by the word `fat` precedes by a space character.

<pre>
"[T|t]he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Teste a RegExp](https://regex101.com/r/V32Npg/1)

### 4.3 Lookbehind Positivo

Positive lookbehind is used to get all the matches that are preceded by a specific pattern. Positive lookbehind is denoted by
`(?<=...)`. For example, the regular expression `(?<=[T|t]he\s)(fat|mat)` means: get all `fat` or `mat` words from input string that
are after the word `The` or `the`.

<pre>
"(?<=[T|t]he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Teste a RegExp](https://regex101.com/r/avH165/1)

### 4.4 Lookbehind Negativo

Negative lookbehind is used to get all the matches that are not preceded by a specific pattern. Negative lookbehind is denoted by
`(?<!...)`. For example, the regular expression `(?<!(T|t)he\s)(cat)` means: get all `cat` words from input string that
are not after the word `The` or `the`.

<pre>
"(?&lt;![T|t]he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

[Teste a RegExp](https://regex101.com/r/8Efx5G/1)

## 5. Flags

Flags (sinalizadores) are also called modifiers because they modify the output of a regular expression. These flags can be used in any order or
combination, and are an integral part of the RegExp.

|Flag|Description|
|:----:|----|
|i|Case insensitive: Sets matching to be case-insensitive.|
|g|Global Search: Search for a pattern throughout the input string.|
|m|Multilinhas: Anchor meta character works on each line.|

### 5.1 Indiferente à Maiúsculas

The `i` modifier is used to perform case-insensitive matching. For example, the regular expression `/The/gi` means: uppercase letter
`T`, followed by lowercase character `h`, followed by character `e`. And at the end of regular expression the `i` flag tells the
regular expression engine to ignore the case. As you can see we also provided `g` flag because we want to search for the pattern in
the whole input string.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Teste a RegExp](https://regex101.com/r/dpQyf9/1)

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Teste a RegExp](https://regex101.com/r/ahfiuh/1)

### 5.2 Busca Global

The `g` modifier is used to perform a global match (find all matches rather than stopping after the first match). For example, the
regular expression`/.(at)/g` means: any character except new line, followed by lowercase character `a`, followed by lowercase
character `t`. Because we provided `g` flag at the end of the regular expression now it will find every matches from whole input
string.

<pre>
"/.(at)/" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

[Teste a RegExp](https://regex101.com/r/jnk6gM/1)

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Teste a RegExp](https://regex101.com/r/dO1nef/1)

### 5.3 Multilinhas

The `m` modifier is used to perform a multi-line match. As we discussed earlier anchors `(^, $)` are used to check if pattern is
the beginning of the input or end of the input string. But if we want that anchors works on each line we use `m` flag. For example, the
regular expression `/at(.)?$/gm` means: lowercase character `a`, followed by lowercase character `t`, optionally anything except new
line. And because of `m` flag now regular expression engine matches pattern at the end of each line in a string.

<pre>
"/.at(.)?$/" => The fat
                cat sat
                on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Teste a RegExp](https://regex101.com/r/hoGMkP/1)

<pre>
"/.at(.)?$/gm" => The <a href="#learn-regex"><strong>fat</strong></a>
                  cat <a href="#learn-regex"><strong>sat</strong></a>
                  on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Teste a RegExp](https://regex101.com/r/E88WE2/1)

## Contribution

* Report issues
* Open pull request with improvements
* Spread the word
* Reach out to me directly at ziishaned@gmail.com or [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/ziishaned.svg?style=social&label=Follow%20%40ziishaned)](https://twitter.com/ziishaned)

## License

MIT © [Zeeshan Ahmed](mailto:ziishaned@gmail.com)
