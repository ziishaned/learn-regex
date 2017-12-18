<br/>
<p align="center">
<img src="https://i.imgur.com/bYwl7Vf.png" alt="Learn Regex">
</p><br/>

## Tłumaczenia:

* [English](README.md)
* [Español](README-es.md)
* [Français](README-fr.md)
* [Português do Brasil](README-pt_BR.md)
* [中文版](README-cn.md)
* [日本語](README-ja.md)
* [한국어](README-ko.md)
* [Turkish](README-tr.md)
* [Greek](README-gr.md)
* [Polish](README-pl.md)

## Co to jest wyrażenie regularne?

> Wyrażenie regularne to grupa znaków lub symboli, które służą do odnalezienia określonego wzoru w tekście.

Wyrażenie regularne to wzorzec, który jest dopasowywany do tekstu od lewej
do prawej strony. Termin "Wyrażenie regularne" (ang. "Regular expression")
jest dość długie, więć zazwyczaj używa się skróconej formy "regex" lub "regexp".
Wyrażenie regularne jest używane do zastępowania tekstu w łańcuchu znaków
(ang. string), walidacji formularzy, wyodrębniania wycinka z łańcucha
(ang. substring) według podanego wzorca, i wielu innych.

Wyobraź sobie, że piszesz aplikację i chcesz ustawić reguły dotyczące tego,
jak użytkownik wybiera swoją nazwę. Chcemy, aby nazwa użytkownika zawierała litery,
liczby, podkreślenia i myślniki. Chcemy również ograniczyć liczbę znaków w nazwie
użytkownika, aby nie wygladała za brzydko. Stosujemy następujące wyrażenie
regularne aby sprawdzić poprawność nazwy:

<br/><br/>
<p align="center">
  <img src="./img/regexp-en.png" alt="Wyrażenie regularne">
</p>

Powyższe wyrażenie akceptuje łańcuchy `john_doe`, `jo-hn_doe`
i `john12_as`. Odrzuca `Jo` ponieważ łańcuch zawiera dużą literę
i jest za krótki.

## Spis treści

- [Najprostsze wyrażenie](#1-najprostsze-wyrażenie)
- [Metaznaki](#2-metaznaki)
  - [Kropka](#21-kropka)
  - [Zestaw znaków](#22-zestaw-znaków)
    - [Odwrócony zestaw znaków](#221-odwrócony-zestaw-znaków)
  - [Powtórzenia](#23-powtórzenia)
    - [Gwiazdka](#231-gwiazdka)
    - [Plus](#232-plus)
    - [Znak zapytania](#233-znak-zapytania)
  - [Klamry](#24-klamry)
  - [Character Group](#25-character-group)
  - [Alternatywa](#26-alternatywa)
  - [Znak ucieczki](#27-znak-ucieczki)
  - [Kotwice](#28-kotwice)
    - [Kareta](#281-kareta)
    - [Dolar](#282-dolar)
- [Shorthand Character Sets](#3-shorthand-character-sets)
- [Lookaround](#4-lookaround)
  - [Positive Lookahead](#41-positive-lookahead)
  - [Negative Lookahead](#42-negative-lookahead)
  - [Positive Lookbehind](#43-positive-lookbehind)
  - [Negative Lookbehind](#44-negative-lookbehind)
- [Flags](#5-flags)
  - [Case Insensitive](#51-case-insensitive)
  - [Global search](#52-global-search)
  - [Multiline](#53-multiline)

## 1. Najprostsze wyrażenie

Wyrażenie regularne to ciąg znaków, których używamy do przeszukania tekstu.
Na przykład, wyrażenie `the` oznacza: literę `t`, następującą
po niej literę `h`, następującą po niej literę `e`.

<pre>
"the" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/dmRygT/1)

Wyrażenie regularne `123` pasuje do łańcucha `123`. Wyrażenie regularne
jest dopasowywane do danego łańcucha poprzez porównanie każdego znaku,
jeden po drugim w wyrażeniu i łańcuchu. Wyrażenia są zwykle wrażliwe
na wielkość znaków, więc wyrażenie `The` nie pasuje do łańcucha `the`.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/1paXsy/1)

## 2. Metaznaki

Metaznaki to składowe elementy wyrażeń regularnych. Znaki te, nie oznaczają
siebie samych, są natomiast interpretowane w specjalny sposób.
Niektóre znaki mają specjalne znaczenie i są zapisywane w kwadratowych nawiasach.
Metaznaki to:

|Metaznaki|Opis|
|:----:|----|
|.|Dowolny znak z wyjątkiem nowej linii.|
|[ ]|Zakres. Każdy znak zapisany w kwadratowym nawiasie.|
|[^ ]|Odwrócony zakres. Każdy znak, który nie znajduje się w kwadratowym nawiasie.|
|*|0 lub więcej poprzedzających znaków.|
|+|1 lub więcej poprzedzających znaków.|
|?|0 lub 1 poprzedzających znaków.|
|{n,m}|Minimum "n" ale nie więcej niż "m" poprzedzających znaków.|
|(xyz)|Grupowanie znaków. Znaki xyz dokładnie w tej kolejności.|
|&#124;|Alternatywa. Znaki przed symbolem lub za symbolem.|
|&#92;|Znak ucieczki. Umożliwa używanie zarezerwowanych znaków <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>.|
|^|Oznacza początek wzorca.|
|$|Oznacza koniec wzorca.|

## 2.1 Kropka

Kropka `.` jest najprostrzym przykładem metaznaku. Oznacza dowonlny znak z wyłączeniem entera
i znaków nowej linii. Na przykład, wyrażenie regularne `.ar` oznacza: dowolny znak, następującą
po niej literę `a`, następującą po niej literę `r`.

<pre>
".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/xc9GkU/1)

## 2.2 Zestaw znaków

Zestawy znaków nazywane też klasami znaków. Nawiasy kwadratowe służą do określenia zestawów znaków.
Użycie myślnika wewnątrz zestawu, określa jego zakres. Kolejność znaków w nawiasach kwadratowych
nie ma znaczenia. Na przykład wyrażenie `[Tt]he` oznacza: dużą literę `T` lub małą `t`,
następującą po niej literę `h`, następującą po niej literę `e`.

<pre>
"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/2ITLQ4/1)

Jednak kropka w zestawie znaków, oznacza dosłownie kropkę. Wyrażenie regularne
`ar[.]` oznacza: małą literę `a`, następującą po niej literę `r`,
następującą po niej `.` kropkę.

<pre>
"ar[.]" => A garage is a good place to park a c<a href="#learn-regex"><strong>ar.</strong></a>
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/wL3xtE/1)

### 2.2.1 Odwrócony zestaw znaków

Generalnie znak karety oznacza początek wyrażenia, ale gdy zostanie użyty zaraz
za otwierającym nawiasem kwadratowym, odwraca zestaw znaków. Na przykład
wyrażenie `[^c]ar` oznacza: każdy znak z wyjątkiem `c`,
następującą po niej literę `a`, następującą po niej literę `r`.

<pre>
"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/nNNlq3/1)

## 2.3 Powtórzenia

Następujące metaznaki `+`, `*` czy `?` określają ile razy wzorzec może się powtórzyć.
Te metaznaki zachowują się różnie, w zależności od sytuacji.

### 2.3.1 Gwiazdka

Symbol `*` oznacza zero lub więcej powtórzeń poprzedzających znaków. Wyrażenie
regularne `a*` oznacza: zero lub więcej powtórzeń poprzedzającej małej
litery `a`. Ale jeśli występuje po zestawie znaków lub klasie, to oznacza
powtórzenia całego zestawu lub klasy. Na przykład, wyrażenie regularne
`[a-z]*` oznacza: każdy ciąg znaków pisany małymi literami.

<pre>
"[a-z]*" => T<a href="#learn-regex"><strong>he</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/7m8me5/1)

Symbol `*` może być użyty z metaznakiem `.` by oznaczyć każdy łańcuch
znaków `.*`. Symbol `*` może być użyty ze znakiem `\s`
by znaleźć wyrażenie zawierające spacje. Na przykład, wyrażenie
`\s*cat\s*` oznacza: zero lub więcej spacji, następującą po niej małą literę `c`,
następującą po niej małą literę `a`, następującą po niej małą literę `t`,
następujące po niej zero lub więcej spacji.

<pre>
"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the <a href="#learn-regex">con<strong>cat</strong>enation</a>.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/gGrwuz/1)

### 2.3.2 Plus

Symbol `+` oznacza jeden lub więcej powtórzeń poprzedzających znaków. Na przykład,
wyrażenie `c.+t` oznacza: małą literę `c`, następujący po niej przynajmniej jeden
znak, następującą po nim małą literę `t`. W tym wypadku, `t` jest ostatnim `t`
w zdaniu.

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/Dzf9Aa/1)

### 2.3.3 Znak zapytania

W wyrażeniach regularnych znak `?` sprawia, że poprzedzający znak jest opcjonalny.
Ten symbol oznacza zero lub jedno wystąpienie poprzedzającego znaku. Na przykład,
regularne wyrażenie `[T]?he` oznacza: Opcjonalną dużą literę `T`, następującą
po niej małą literę `h`, następującą po niej małą literę `e`.

<pre>
"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/cIg9zm/1)

<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/kPpO2x/1)

## 2.4 Klamry

W wyrażeniach regularnych, klamry zwane również kwantyfikatorami, używane są
do określenia, ile razy znak lub grupa znaków może się powtórzyć.
Na przykład wyrażenie regularne `[0-9]{2,3}` oznacza: Przynajmniej
2 znaki, ale nie więcej niż 3 (znaki z zakresu od 0 do 9).

<pre>
"[0-9]{2,3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/juM86s/1)

Możemy opuścić drugą liczbę. Na przykład regularne wyrażenie `[0-9]{2,}`
oznacza: 2 lub więcej znaków. Jeżeli dodatkowo usuniemy przecinek,
to wyrażenie `[0-9]{3}` oznacza: Dokładnie 3 znaki.

<pre>
"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/Gdy4w5/1)

<pre>
"[0-9]{3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to 10.0.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/Sivu30/1)

## 2.5 Grupa znaków

Grupa znaków to grupa podwzorców, które zapisywane są w nawiasach `(...)`.
Jak wspominaliśmy wyżej, jeśli w wyrażeniu regularnym wstawimy kwantyfikator po
znaku, wtedy powtórzy on ten znak. Ale gdy wstawimy kwantyfikator po grupie znaków,
wtedy cała grupa zostanie powtórzona. Na przykład wyrażenie regularne `(ab)*`
oznacza zero lub więcej powtórzeń grupy "ab". Możemy także użyć metaznaku
alternatywy `|` wewnątrz grupy. Na przykład wyrażenie `(c|g|p)ar` oznacza: małą literę `c`,
`g` lub `p`, następującą po niej literę `a`, następującą po niej literę `r`.

<pre>
"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/tUxrBG/1)

## 2.6 Alternatywa

W wyrażeniach regularnych pionowa kreska `|` oznacza alternatywę.
Działa jak warunek pomiędzy różnymi wyrażeniami. Teraz możesz pomyśleć, że
to działa tak samo jak zestaw znaków. Różnica polega na tym, że zestaw znaków
działa na poziomie znaków, natomiast alternatywa na poziomie wyrażenia. Na przykład
wyrażenie regularne `(T|t)he|car` oznacza: dużą literę `T` lub małą `t`,
następującą po niej literę `h`, następującą po niej literę `e` lub `c`, następującą
po niej literę `a`, następującą po niej literę `r`.

<pre>
"(T|t)he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/fBXyX0/1)

## 2.7 Znak ucieczki

Ukośnik `\` w wyrażeniach regularnych jest znakiem ucieczki. Pozwala on
używać w wyrażeniu zarezerwowanych znaków takich jak `{ } [ ] / \ + * . $ ^ | ?`.
Aby użyć znaku specjalnego w wyrażeniu, postaw `\` przed nim.

Na przykład wyrażenie `.` dopasowuje każdy znak z wyjątkiem nowej linii.
Żeby dopasować kropkę `.` w wyrażeniu regularnym, trzeba wstawić przed nią ukośnik. 
Wyrażenie `(f|c|m)at\.?` oznacza: małe litery `f`, `c` lub `m`, następującą po niej
literę `a`, następującą po niej literę `t`, następującą kropkę `.`, która jest opcjonalna.


<pre>
"(f|c|m)at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/DOc5Nu/1)

## 2.8 Kotwice

W wyrażeniach regularnych używamy kotwic aby sprawdzić czy dopasowywany symbol
jest pierwszym lub ostatnim symbolem w łańcuchu. Są dwa typy: pierwszy to
kareta `^`, który sprawdza czy znak jest początkiem łańcucha, drugi to dolar `$`,
który sprawdza czy znak jest ostatnim elementem łańcucha.

### 2.8.1 Kareta

Kareta `^` sprawdza czy znak jest początkiem łańcucha. Jeżeli użyjemy takiego
wyrażenia `^a` (jeśli a jest pierwszym znakiem) na łańcuchu `abc` to dopasuje
nam `a`. Ale jeśli użyjemytakiego wyrażenia `^b` na tym samym łańcuchu, to nie
zwróci nam nic. Ponieważ w łańcuchu `abc` "b" nie jest pierwszym symbolem.
Spójrzmy teraz na wyrażenie `^(T|t)he` które oznacza: dużą literę `T` lub małą
`t`, która jest początkiem łańcucha, następującą po niej literę `h`, następującą
po niej literę `e`.

<pre>
"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/5ljjgB/1)

<pre>
"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/jXrKne/1)

### 2.8.2 Dolar

Symbol dolara `$` używany jest do sprawdzenia czy dopasowywany znak jest ostatni
w łańcuchu. Na przykład, wyrażenie regularne `(at\.)$` oznacza: małą literę `a`,
następującą po niej literę `t`, następującą po niej kropkę `.` i na dodatek
dopasowanie musi być końcem łańcucha.

<pre>
"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/y4Au4D/1)

<pre>
"(at\.)$" => The fat cat. sat. on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/t0AkOd/1)

##  3. Skróty

W wyrażeniach regularnych znajdziemy także skróty dla popularnych zestawów znaków,
które ułatwiają pracę z wyrażeniami regularnymi. Skróty wyglądają następująco:

|Skrót|Opis|
|:----:|----|
|.|Każdy znak z wyjątkiem nowej linii|
|\w|Znaki alfanumeryczne: `[a-zA-Z0-9_]`|
|\W|Znaki nie alfanumeryczne: `[^\w]`|
|\d|Cyfry: `[0-9]`|
|\D|Nie cyfry: `[^\d]`|
|\s|Dowolny biały znak: `[\t\n\f\r\p{Z}]`|
|\S|Każdy znak oprócz białych: `[^\s]`|

## 4. Lookaround

Lookbehind and lookahead (also called lookaround) are specific types of
***non-capturing groups*** (Used to match the pattern but not included in matching
list). Lookaheads are used when we have the condition that this pattern is
preceded or followed by another certain pattern. For example, we want to get all
numbers that are preceded by `$` character from the following input string
`$4.44 and $10.88`. We will use following regular expression `(?<=\$)[0-9\.]*`
which means: get all the numbers which contain `.` character and  are preceded
by `$` character. Following are the lookarounds that are used in regular
expressions:

|Symbol|Opis|
|:----:|----|
|?=|Positive Lookahead|
|?!|Negative Lookahead|
|?<=|Positive Lookbehind|
|?<!|Negative Lookbehind|

### 4.1 Positive Lookahead

The positive lookahead asserts that the first part of the expression must be
followed by the lookahead expression. The returned match only contains the text
that is matched by the first part of the expression. To define a positive
lookahead, parentheses are used. Within those parentheses, a question mark with
equal sign is used like this: `(?=...)`. Lookahead expression is written after
the equal sign inside parentheses. For example, the regular expression
`(T|t)he(?=\sfat)` means: optionally match lowercase letter `t` or uppercase
letter `T`, followed by letter `h`, followed by letter `e`. In parentheses we
define positive lookahead which tells regular expression engine to match `The`
or `the` which are followed by the word `fat`.

<pre>
"(T|t)he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/IDDARt/1)

### 4.2 Negative Lookahead

Negative lookahead is used when we need to get all matches from input string
that are not followed by a pattern. Negative lookahead is defined same as we define
positive lookahead but the only difference is instead of equal `=` character we
use negation `!` character i.e. `(?!...)`. Let's take a look at the following
regular expression `(T|t)he(?!\sfat)` which means: get all `The` or `the` words
from input string that are not followed by the word `fat` precedes by a space
character.

<pre>
"(T|t)he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/V32Npg/1)

### 4.3 Positive Lookbehind

Positive lookbehind is used to get all the matches that are preceded by a
specific pattern. Positive lookbehind is denoted by `(?<=...)`. For example, the
regular expression `(?<=(T|t)he\s)(fat|mat)` means: get all `fat` or `mat` words
from input string that are after the word `The` or `the`.

<pre>
"(?<=(T|t)he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/avH165/1)

### 4.4 Negative Lookbehind

Negative lookbehind is used to get all the matches that are not preceded by a
specific pattern. Negative lookbehind is denoted by `(?<!...)`. For example, the
regular expression `(?<!(T|t)he\s)(cat)` means: get all `cat` words from input
string that are not after the word `The` or `the`.

<pre>
"(?&lt;!(T|t)he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/8Efx5G/1)

## 5. Flags

Flags are also called modifiers because they modify the output of a regular
expression. These flags can be used in any order or combination, and are an
integral part of the RegExp.

|Flag|Description|
|:----:|----|
|i|Case insensitive: Sets matching to be case-insensitive.|
|g|Global Search: Search for a pattern throughout the input string.|
|m|Multiline: Anchor meta character works on each line.|

### 5.1 Case Insensitive

The `i` modifier is used to perform case-insensitive matching. For example, the
regular expression `/The/gi` means: uppercase letter `T`, followed by lowercase
character `h`, followed by character `e`. And at the end of regular expression
the `i` flag tells the regular expression engine to ignore the case. As you can
see we also provided `g` flag because we want to search for the pattern in the
whole input string.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/dpQyf9/1)

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/ahfiuh/1)

### 5.2 Global search

The `g` modifier is used to perform a global match (find all matches rather than
stopping after the first match). For example, the regular expression`/.(at)/g`
means: any character except new line, followed by lowercase character `a`,
followed by lowercase character `t`. Because we provided `g` flag at the end of
the regular expression now it will find all matches in the input string, not just the first one (which is the default behavior).

<pre>
"/.(at)/" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/jnk6gM/1)

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/dO1nef/1)

### 5.3 Multiline

The `m` modifier is used to perform a multi-line match. As we discussed earlier
anchors `(^, $)` are used to check if pattern is the beginning of the input or
end of the input string. But if we want that anchors works on each line we use
`m` flag. For example, the regular expression `/at(.)?$/gm` means: lowercase
character `a`, followed by lowercase character `t`, optionally anything except
new line. And because of `m` flag now regular expression engine matches pattern
at the end of each line in a string.

<pre>
"/.at(.)?$/" => The fat
                cat sat
                on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/hoGMkP/1)

<pre>
"/.at(.)?$/gm" => The <a href="#learn-regex"><strong>fat</strong></a>
                  cat <a href="#learn-regex"><strong>sat</strong></a>
                  on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Przetestuj wyrażenie](https://regex101.com/r/E88WE2/1)

## Contribution

* Report issues
* Open pull request with improvements
* Spread the word
* Reach out to me directly at ziishaned@gmail.com or [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/ziishaned.svg?style=social&label=Follow%20%40ziishaned)](https://twitter.com/ziishaned)

## License

MIT © [Zeeshan Ahmed](mailto:ziishaned@gmail.com)
