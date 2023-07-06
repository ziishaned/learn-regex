<p align="center">
    <br/>
    <a href="https://github.com/ziishaned/learn-regex">
        <img src="https://i.imgur.com/bYwl7Vf.png" alt="Learn Regex">
    </a>
    <br /><br />
    <p>
        <a href="https://twitter.com/home?status=Learn%20regex%20the%20easy%20way%20by%20%40ziishaned%20http%3A//github.com/ziishaned/learn-regex">
            <img src="https://img.shields.io/badge/twitter-tweet-blue.svg?style=flat-square"/>
        </a>
        <a href="https://twitter.com/ziishaned">
            <img src="https://img.shields.io/badge/feedback-@ziishaned-blue.svg?style=flat-square" />
        </a>
    </p>
</p>


## Traduções:

* [English](../README.md)
* [German](../translations/README-de.md)
* [Español](../translations/README-es.md)
* [Français](../translations/README-fr.md)
* [Português do Brasil](../translations/README-pt_BR.md)
* [中文版](../translations/README-cn.md)
* [日本語](../translations/README-ja.md)
* [한국어](../translations/README-ko.md)
* [Turkish](../translations/README-tr.md)
* [Greek](../translations/README-gr.md)
* [Magyar](../translations/README-hu.md)
* [Polish](../translations/README-pl.md)
* [Русский](../translations/README-ru.md)
* [Tiếng Việt](../translations/README-vn.md)
* [فارسی](../translations/README-fa.md)
* [עברית](../translations/README-he.md)

## O que é uma Expressão Regular?

[![](https://img.shields.io/badge/-Download%20PDF%20-0a0a0a.svg?style=flat&colorA=0a0a0a)](https://gum.co/learn-regex)

> Expressão Regular é um grupo de caracteres ou símbolos utilizado para encontrar um padrão específico a partir de um texto.

Uma expressão regular é um padrão que é comparado com uma cadeia de caracteres da esquerda para a direita. O termo "Expressão regular" é longo e difícil de falar; você geralmente vai encontrar o termo abreviado como "regex" ou "regexp". Expressões regulares são usadas para substituir um texto dentro de uma string, validar formulários, extrair uma parte de uma string baseada em um padrão encontrado e muito mais.

Imagine que você está escrevendo uma aplicação e quer colocar regras para quando um usuário escolher seu username. Nós queremos permitir que o username contenha letras, números, underlines e hífens. Nós também queremos limitar o número de caracteres para não ficar muito feio. Então usamos a seguinte expressão regular para validar o username:

<br/><br/>

<p align="center">
<img src="http://i.imgur.com/8UaOzpq.png" alt="Regular expression">
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
- [Guloso vs Não-Guloso](#6-guloso-vs-não-guloso)

## 1. Combinações Básicas

Uma expressão regular é apenas um padrão de caracteres que usamos para fazer busca em um texto. Por exemplo, a expressão regular `the` significa: a letra `t`, seguida da letra `h`, seguida da letra `e`.

<pre>
"the" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Teste a RegExp](https://regex101.com/r/dmRygT/1)

A expressão regular `123` corresponde à string `123`. A expressão regular é comparada com uma string de entrada, comparando cada caractere da expressão regular para cada caractere da string de entrada, um após o outro. Expressões regulares são normalmente case-sensitive (sensíveis a maiúsculas), então a expressão regular `The` não vai bater com a string `the`.

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
|*|Corresponde a 0 ou mais repetições do símbolo anterior.|
|+|Corresponde a 1 ou mais repetições do símbolo anterior.|
|?|Faz com que o símbolo anterior seja opcional.|
|{n,m}|Chaves. Corresponde a no mínimo "n" mas não mais que "m" repetições do símbolo anterior.|
|(xyz)|Grupo de caracteres. Corresponde aos caracteres xyz nesta exata ordem.|
|&#124;|Alternância. Corresponde aos caracteres antes ou os caracteres depois do símbolo|
|&#92;|Escapa o próximo caractere. Isso permite você utilizar os caracteres reservados <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>|
|^|Corresponde ao início da entrada.|
|$|Corresponde ao final da entrada.|

## 2.1 Ponto final

O ponto final `.` é um simples exemplo de metacaracteres. O metacaractere `.` corresponde a qualquer caractere sozinho. Ele não se iguala ao Enter e à quebra de linha. Por exemplo, a expressão regular `.ar` significa: qualquer caractere, seguido da letra `a`, seguida da letra `r`.

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

O símbolo `*` corresponde a zero ou mais repetições do padrão antecedente. A expressão regular `a*` significa: zero ou mais repetições do caractere minúsculo precedente `a`. Mas se o asterisco aparecer depois de um conjunto de caracteres, ou classe de caracteres, ele irá procurar as repetições de todo o conjunto. Por exemplo, a expressão regular `[a-z]*` significa: qualquer quantidade de letras minúsculas numa linha.

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

O símbolo `+` corresponde a uma ou mais repetições do caractere anterior. Por exemplo, a expressão regular `c.+t` significa: a letra minúscula `c`, seguida por pelo menos um caractere, seguido do caractere minúsculo `t`.

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

[Teste a RegExp](https://regex101.com/r/Dzf9Aa/1)

### 2.3.3 O Ponto de Interrogação

Em expressões regulares, o metacaractere `?` faz o caractere anterior ser opcional. Esse símbolo corresponde a zero ou uma ocorrência do caractere anterior. Por exemplo, a expressão regular `[T]?he` significa: A letra maiúsculo `T` opcional, seguida do caractere minúsculo `h`, seguido do caractere minúsculo `e`.

<pre>
"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Teste a RegExp](https://regex101.com/r/cIg9zm/1)

<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

[Teste a RegExp](https://regex101.com/r/kPpO2x/1)

## 2.4 Chaves

Em expressões regulares, chaves, que também são chamadas de quantificadores, são utilizadas para especificar o número de vezes que o caractere, ou um grupo de caracteres, pode se repetir. Por exemplo, a expressão regular `[0-9]{2,3}` significa: Encontre no mínimo 2 dígitos, mas não mais que 3 (caracteres no intervalo de 0 a 9).

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

Grupo de caracteres é um grupo de sub-padrão que é escrito dentro de parênteses `(...)`. Como falamos antes, se colocaramos um quantificador depois de um caractere, ele irá repetir o caractere anterior. Mas se colocarmos um quantificador depois de um grupo de caracteres, ele irá repetir todo o conjunto. Por exemplo, a expressão regular `(ab)*` corresponde a zero ou mais repetições dos caracteres "ab". Nós também podemos usar o metacaractere de alternância `|` dentro de um grupo de caracteres. Por exemplo, a expressão regular `(c|g|p)ar` significa: caractere minúsculo `c`, `g` ou `p`, seguido do caractere `a`, seguido do caractere `r`.

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

Em empressões regulares, usamos âncoras para verificar se o caractere encontrado está no início ou no final da string de entrada. As âncoras podem ser de dois tipos: O primeiro tipo é o Acento Circunflexo `^`, que verifica se o caractere encontrado está no início da string de entrada, e o segundo tipo é o Sinal de Dólar `$`, que verifica se o caractere encontrado é o último caractere da string.

### 2.8.1 Acento Circunflexo

O símbolo do Acento Circunflexo `^` é usado para verificar se o caractere encontrado é o primeiro caractere da string de entrada. Se aplicarmos a seguinte expressão regular `^a` (se a é o primeiro caractere) à string de entrada `abc`, ela encontra o `a`. Mas se nós aplicarmos a expressão regular `^b` na mesma string, ela não encontrará nada. Isso acontece porque, na string `abc`, "b" não é o caractere inicial. Vamos dar uma olhada em outra expressão regular, `^(T|t)he` que significa: o caractere maiúsculo `T` ou o caractere minúsculo `t` que é o primeiro símbolo da string de entrada, seguido do caractere minúsculo `h`, seguido do caractere minúsculo `e`.

<pre>
"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Teste a RegExp](https://regex101.com/r/5ljjgB/1)

<pre>
"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Teste a RegExp](https://regex101.com/r/jXrKne/1)

### 2.8.2 Sinal de Dólar

O símbolo do Sinal de Dólar `$` é usado para verificar se o caractere encontrado é o último caractere da string de entrada. Por exemplo, a expressão regular `(at\.)$` significa: um caractere minúsculo `a`, seguido do caractere minúsculo `t`, seguido de um ponto final `.` e o grupo deve estar no final da string.

<pre>
"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Teste a RegExp](https://regex101.com/r/y4Au4D/1)

<pre>
"(at\.)$" => The fat cat. sat. on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Teste a RegExp](https://regex101.com/r/t0AkOd/1)

##  3. Forma Abreviada de Conjunto de Caracteres

As expressões regulares fornecem abreviações para conjuntos de caracteres comumente usados, que oferecem atalhos convenientes para expressões regulares comumente usadas. As abreviações são as seguintes:

|Abreviação|Descrição|
|:----:|----|
|.|Qualquer caractere, exceto nova linha|
|\w|Corresponde a caracteres alfanuméricos: `[a-zA-Z0-9_]`|
|\W|Corresponde a caracteres não alfanuméricos: `[^\w]`|
|\d|Corresponde a dígitos: `[0-9]`|
|\D|Corresponde a não dígitos: `[^\d]`|
|\s|Corresponde a caracteres de espaços em branco: `[\t\n\f\r\p{Z}]`|
|\S|Corresponde a caracteres de espaços não em branco: `[^\s]`|

## 4. Olhar ao Redor

Lookbehind (olhar atrás) e lookahead (olhar à frente), às vezes conhecidos como lookarounds (olhar ao redor), são tipos específicos de ***grupo de não captura*** (utilizado para encontrar um padrão, mas não incluí-lo na lista de ocorrências). Lookarounds são usados quando temos a condição de que determinado padrão seja precedido ou seguido de outro padrão. Por exemplo, queremos capturar todos os números precedidos do caractere `$` da seguinte string de entrada: `$4.44 and $10.88`. Vamos usar a seguinte expressão regular `(?<=\$)[0-9\.]*` que significa: procure todos os números que contêm o caractere `.` e são precedidos pelo caractere `$`. A seguir estão os lookarounds que são utilizados em expressões regulares:

|Símbolo|Descrição|
|:----:|----|
|?=|Lookahead Positivo|
|?!|Lookahead Negativo|
|?<=|Lookbehind Positivo|
|?<!|Lookbehind Negativo|

### 4.1 Lookahead Positivo

O lookahead positivo impõe que a primeira parte da expressão deve ser seguida pela expressão lookahead. A combinação retornada contém apenas o texto que é encontrado pela primeira parte da expressão. Para definir um lookahead positivo, deve-se usar parênteses. Dentro desses parênteses, é usado um ponto de interrogação seguido de um sinal de igual, dessa forma: `(?=...)`. Expressões lookahead são escritas depois do sinal de igual dentro do parênteses. Por exemplo, a expressão regular `[T|t]he(?=\sfat)` significa: encontre a letra minúscula `t` ou a letra maiúscula `T`, seguida da letra `h`, seguida da letra `e`. Entre parênteses, nós definimos o lookahead positivo que diz para o motor de expressões regulares para encontrar `The` ou `the` que são seguidos pela palavra `fat`.

<pre>
"[T|t]he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Teste a RegExp](https://regex101.com/r/IDDARt/1)

### 4.2 Lookahead Negativo

O lookahead negativo é usado quando nós precisamos encontrar todas as ocorrências da string de entrada que não são seguidas por um determinado padrão. O lookahead negativo é definido da mesma forma que definimos o lookahead positivo, mas a única diferença é que, no lugar do sinal de igual `=`, usamos o caractere de negação `!`, ex.: `(?!...)`. Vamos dar uma olhada na seguinte expressão regular `[T|t]he(?!\sfat)`, que significa: obtenha as palavras `The` ou `the` da string de entrada que não são seguidas pela palavra `fat`, precedida de um caractere de espaço.

<pre>
"[T|t]he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Teste a RegExp](https://regex101.com/r/V32Npg/1)

### 4.3 Lookbehind Positivo

Lookbehind positivo é usado para encontrar todas as ocorrências que são precedidas por um padrão específico. O lookbehind positivo é indicado por `(?<=...)`. Por exemplo, a expressão regular `(?<=[T|t]he\s)(fat|mat)` significa: obtenha todas as palavras `fat` ou `mat` da string de entrada, que estão depois das palavras `The` ou `the`.

<pre>
"(?<=[T|t]he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Teste a RegExp](https://regex101.com/r/avH165/1)

### 4.4 Lookbehind Negativo

Lookbehind negativo é usado para encontrar todas as ocorrências que não são precedidas por um padrão específico. O lookbehind negativo é indicado por `(?<!...)`. Por exemplo, a expressão regular `(?<!(T|t)he\s)(cat)` significa: obtenha todas as palavras `cat` da string de entrada, que não estão depois das palavras `The` ou `the`.

<pre>
"(?&lt;![T|t]he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

[Teste a RegExp](https://regex101.com/r/8Efx5G/1)

## 5. Flags

Flags (sinalizadores) também são chamados de modificadores, porque eles modificam o resultado da expressão regular. Essas flags podem ser usadas em qualquer ordem ou combinação, e são uma parte integrante da RegExp.

|Flag|Descrição|
|:----:|----|
|i|Case insensitive: Define que o padrão será case-insensitive.|
|g|Busca global: Procura o padrão em toda a string de entrada.|
|m|Multilinhas: Os metacaracteres de âncora funcionam em cada linha.|

### 5.1 Indiferente a Maiúsculas

O modificador `i` é usado para tornar o padrão case-insensitive. Por exemplo, a expressão regular `/The/gi` significa: a letra maiúscula `T`, seguida do caractere minúsculo `h`, seguido do caractere `e`. E ao final da expressão regular, a flag `i` diz ao motor de expressões regulares para ignorar maiúsculas e minúsculas. Como você pode ver, nós também determinamos a flag `g` porque queremos procurar o padrão em toda a string de entrada.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Teste a RegExp](https://regex101.com/r/dpQyf9/1)

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Teste a RegExp](https://regex101.com/r/ahfiuh/1)

### 5.2 Busca Global

O modificador `g` é usado para realizar uma busca global (encontrar todas as ocorrências sem parar na primeira encontrada). Por exemplo, a expressão regular `/.(at)/g` significa: qualquer caractere, exceto nova linha, seguido do caractere minúsculo `a`, seguido do caractere minúsculo `t`. Por causa da flag `g` no final da expressão regular, agora ela vai encontrar todas as ocorrências em toda a string de entrada.

<pre>
"/.(at)/" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

[Teste a RegExp](https://regex101.com/r/jnk6gM/1)

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Teste a RegExp](https://regex101.com/r/dO1nef/1)

### 5.3 Multilinhas

O modificador `m` é usado para realizar uma busca em várias linhas. Como falamos antes, as âncoras `(^, $)` são usadas para verificar se o padrão está no início ou no final da string de entrada respectivamente. Mas se queremos que as âncoras funcionem em cada uma das linhas, usamos a flag `m`. Por exemplo, a expressão regular `/.at(.)?$/gm` significa: o caractere minúsculo `a`, seguido do caractere minúsculo `t`, opcionalmente seguido por qualquer caractere, exceto nova linha. E por causa da flag `m`, agora o motor de expressões regulares encontra o padrão no final de cada uma das linhas da string.

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

### 6. Guloso vs Não-Guloso

Por padrão, uma regex irá realizar uma consulta gulosa, isto significa que a busca irá capturar ao padrão mais longo possível. Nós podemos usar `?` para buscar de uma forma não-gulosa, isto significa que a busca irá capturar ao padrão mais curto possível.

<pre>
"/(.*at)/" => <a href="#learn-regex"><strong>The fat cat sat on the mat</strong></a>. </pre>


[Teste a RegExp](https://regex101.com/r/AyAdgJ/1)

<pre>
"/(.*?at)/" => <a href="#learn-regex"><strong>The fat</strong></a> cat sat on the mat. </pre>


[Teste a RegExp](https://regex101.com/r/AyAdgJ/2)


## Contribution

* Reporte bugs
* Abra pull request com melhorias
* Espalhe a palavra
* Me encontre diretamente em ziishaned@gmail.com ou [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/ziishaned.svg?style=social&label=Follow%20%40ziishaned)](https://twitter.com/ziishaned)

## Licença

MIT &copy; [Zeeshan Ahmad](https://twitter.com/ziishaned)
