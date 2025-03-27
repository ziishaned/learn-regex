<p align="center">
    <br/>
    <a href="https://github.com/ziishaned/learn-regex">
        <img src="https://i.imgur.com/bYwl7Vf.png" alt="Learn Regex">
    </a>
</p>

## Translations:

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

## Was sind Reguläre Ausdrücke?

[![](https://img.shields.io/badge/-Download%20PDF%20-0a0a0a.svg?style=flat&colorA=0a0a0a)](https://gum.co/learn-regex)

> Ein regulärer Ausdruck ist eine Gruppe von Buchstaben und Symbolen, die benutzt werden um ein bestimmtes Muster in einem Text zu finden.
Ein regulärer Ausdruck ist ein Muster, das mit einem zu durchsuchenden Text von links nach rechts abgeglichen wird. Die Bezeichnung
"Regulärer Ausdruck" ist in der Praxis unüblich und stattdessen wird häufig die Englische Abkürzung "Regex" oder "RegExp" (*regular expression*) verwendet. Reguläre
Ausdrücke werden verwendet, um Fragemente eines Textes zu ersetzen, Formulare zu validieren, Segmente eines Textes anhand eines
Musters zu extrahieren und für vieles mehr.

Angenommen, Du schreibst eine Anwendung und möchtest die Regeln definieren, nach denen ein Benutzer seinen Benutzernamen auswählen
kann. Wir möchten festlegen, dass der Benutzernamen Buchstaben, Ziffern, Unter- und Bindestriche beinhalten darf. Außerdem wollen
wir die Anzahl der Zeichen limitieren, damit der Name nicht unlesbar wird. Dazu verwenden wir den folgenden regulären Ausdruck:
<br/><br/>
<p align="center">
  <img src="../img/regexp-de.png" alt="Regular expression">
</p>

Der abgebildete reguläre Ausdruck erlaubt bspw. Die Eingaben `john_doe`, `jo-hn_doe` und `john12_as`. Die Eingabe `Jo` wird nicht akzeptiert, weil sie einen Großbuchstaben enthält und zu kurz ist.

## Inhaltsverzeichnis

- [Einfache Muster](#1-einfache-muster)
- [Metazeichen](#2-metazeichen)
  - [Punkt](#21-punkt)
  - [Zeichenklasse](#22-zeichenklasse)
    - [Negierte Zeichenklasse](#221-negierte-zeichenklasse)
  - [Wiederholungen](#23-wiederholungen)
    - [Stern *](#231-stern)
    - [Plus +](#232-plus)
    - [Fragezeichen ?](#233-fragezeichen)
  - [Geschweifte Klammern {}](#24-geschweifte-klammern)
  - [Gruppierung ()](#25-gruppierung)
  - [Alternation |](#26-alternation)
  - [Escaping \](#27-escaping)
  - [Anker](#28-anker)
    - [Zirkumflex ^](#281-zirkumflex)
    - [Dollar $](#282-dollar)
- [Vordefinierte Zeichenklassen](#3-vordefinierte-zeichenklassen)
- [Lookaround](#4-lookaround)
  - [Positiver Lookahead](#41-positiver-lookahead)
  - [Negativer Lookahead](#42-negativer-lookahead)
  - [Positiver Lookbehind](#43-positiver-lookbehind)
  - [Negativer Lookbehind](#44-negativer-lookbehind)
- [Modifikatoren](#5-modifikatoren)
  - [Schreibungsunabhängig i](#51-schreibungsunbhängig)
  - [Globale Suche](#52-globale-suche)
  - [Mehrzeilig](#53-mehrzeilig)
- [Gierige vs Faule Übereinstimmung](#6-gierige-vs-faule-übereinstimmung)

## 1. Einfache Muster

Ein regulärer Ausdruck ist einfach nur ein Muster von Zeichen, welches für eine Suche in Text genutzt wird. Der reguläre Ausdruck `the` heißt zum Beispiel: der Buchstabe `t`, gefolgt von dem Buchstaben `h`, gefolgt von dem Buchstaben `e`.

<pre>
"the" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/dmRygT/1)

Der reguläre Ausdruck `123` entspricht der Zeichenkette `123`. Auf Übereinstimmung mit einer Zeichenkette wird er überprüft, indem jedes Zeichen in dem regulären Ausdruck nacheinander mit jedem Zeichen der Zeichenkette verglichen wird. 
Reguläre Ausdrücke berücksichtigen normalerweise Groß- und Kleinschreibung, sodass etwa der Ausdruck `The` nicht mit der Zeichenkette  `the` übereinstimmen würde. 

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/1paXsy/1)

## 2. Metazeichen

Metazeichen sind Bausteine von regulären Ausdrücken. Sie stehen nicht für sich selbst, sondern haben eine besondere Bedeutung und werden in spezieller Weise interpretiert.
Einige Metazeichen erhalten eine andere Bedeutung oder überhaupt erst eine besondere Bedeutung innerhalb eckiger Klammern `[]`. Folgende Metazeichen gibt es:

|Metazeichen|Beschreibung|
|:----:|----|
|.|Der Punkt entspricht jedem einzelnen Zeichen, außer Zeilenumbrüchen.|
|[ ]|Zeichenklasse, entspricht jedem Zeichen innerhalb der eckigen Klammern.|
|[^ ]|Negierte Zeichenklasse, entspricht jedem Zeichen welches nicht innerhalb der eckigen Klammern definiert ist.|
|*|Entspricht 0 oder mehr Wiederholungen des vorhergehenden Teilausdrucks.|
|+|Entspricht 1 oder mehr Wiederholungen des vorhergehenden Teilausdrucks.|
|?|Macht den vorhergehenden Teilausdruck optional.|
|{n,m}|Entspricht mindestens "n", aber nicht mehr als "m" Wiederholungen des vorhergehenden Teilausdrucks.|
|(xyz)|Gruppierung, entspricht den Zeichen xyz in der exakten Reihenfolge.|
|&#124;|Alternation, entspricht entweder dem Teilausdruck vor oder nach dem \|.|
|&#92;|Escaped das nachfolgende Zeichen. Dies ermöglicht es Zeichen zu blockieren <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>|
|^|Entspricht dem Anfang der Eingabe.|
|$|Entspricht dem Ende der Eingabe.|

## 2.1 Punkt

Der Punkt `.` ist das einfachste Beispiel für ein Metazeichen. Er steht für jedes beliebiges Zeichen mit der Ausnahme von Zeilenumbrüchen/Enter-Zeichen. 
Als Beispiel, der reguläre Ausdruck `.ar` bedeutet: ein beliebiges Zeichen, gefolgt von dem Buchstaben `a`, gefolgt vom Buchstaben `r`.

<pre>
".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>
[Teste den regulären Ausdruck](https://regex101.com/r/xc9GkU/1)

## 2.2 Zeichenklasse

Zeichenklassen werden auch als Zeichenmengen oder -sätze bezeichnet (eng. *character set/class*). Sie werden in eckige Klammern definiert. Um eine Zeichenfolge wie `A-Z` oder `0-9` zu definieren, kann ein Bindestrich `-` verwendet werden. Die Reihenfolge sonstiger Zeichen innerhalb der eckigen Klammern spielt keine Rolle. Zum Beispiel bedeutet der reguläre Ausdruck `[Tt]he`: ein groß geschriebenes `T` oder ein kleingeschriebenes `t`, gefolgt vom Buchstaben `h` und weiter gefolgt vom Buchstaben `e`.

<pre>
"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>
[Teste den regulären Ausdruck](https://regex101.com/r/2ITLQ4/1)

Ein Punkt in einer Zeichenklasse bedeutet, anders als sonst, einen wörtlichen Punkt. Der reguläre Ausdruck `ar[.]` bedeutet: ein kleingeschriebenes Zeichen `a`, gefolgt vom kleingeschriebenen Buchstaben `r`, gefolgt von einem Punkt-Zeichen `.`.

<pre>
"ar[.]" => A garage is a good place to park a c<a href="#learn-regex"><strong>ar.</strong></a>
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/wL3xtE/1)

### 2.2.1 Negierte Zeichenklasse

Im Allgemeinen stellt das Zirkumflex `^` den Anfang einer Zeichenkette dar. Wenn es aber nach der öffnenden eckigen Klammer gesetzt wird, dann wird die Zeichenklasse negiert (eng. *negated character set*). Als Beispiel, der reguläre Ausdruck `[^c]ar` bedeutet: ein beliebiges Zeichen außer `c`, gefolgt vom Buchstaben `a`, gefolgt vom Buchstaben `r`. 

<pre>
"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/nNNlq3/1)

## 2.3 Wiederholungen

Die Metazeichen `+`, `*` und `?` bieten einen einfachen Weg, anzugeben, wie oft sich ein bestimmter Teilausdruck wiederholen soll. Sie gehören damit zu den sogenannten "Quantifizierern" (eng. *quantifier*).
Sie können sich je nach Situation unterschiedlich verhalten.

### 2.3.1 Stern

Das Symbol `*` stimmt mit beliebig vielen Wiederholungen des vorhergehenden Teilausdrucks überein. Der Ausdruck `a*` heißt: 
null, eins oder mehrere `a`s in Folge. Da sich der Stern auf Teilausdrücke bezieht, kann er auch bspw. hinter einer Zeichenklasse stehen
und stimmt dann mit beliebig vielen Zeichen aus der Klasse in Folge überein. Zum Beispiel bedeutet der Ausdruck `[a-z]*`: eine 
beliebige Anzahl von Kleinbuchstaben in Folge.

<pre>
"[a-z]*" => T<a href="#learn-regex"><strong>he</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/7m8me5/1)

Das `*`-Symbol kann zusammen mit dem Metazeichen `.` verwendet werden, um mit einer vollkommen beliebigen Zeichenkette übereinzustimmen `.*`.
Es kann auch mit der vordefinierten Zeichenklasse `\s` verwendet werden, um mit beliebig viel Leerraum (Leerzeichen, Tabulatoren, Zeilenumbrüchen)
übereinzustimmen. Der Ausdruck `\s*cat\s*` heißt zum Beispiel: null oder mehrere Leerzeichen, gefolgt von dem Buchstaben `c`, gefolgt vom Buchstaben `a`, 
gefolgt vom Buchstaben `t` und schließlich gefolgt von null oder mehreren Leerzeichen.

<pre>
"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the con<a href="#learn-regex"><strong>cat</strong></a>enation.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/gGrwuz/1)

### 2.3.2 Plus

Das `+`-Symbol stimmt mit einer oder mehr Wiederholungen des vorhergehenden Teilausdrucks überein. Der reguläre Ausdruck
`c.+t` bedeutet: Buchstabe `c`, gefolgt von mindestens einem beliebigen Zeichen, gefolgt vom Buchstaben `t`. Das `t` ist dabei
das letzte `t` in der hier zu sehenden Übereinstimmung, wobei es hier auch weitere Übereinstimmungen gäbe (siehe "Teste den regulären Ausdruck").

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/Dzf9Aa/1)

### 2.3.3 Fragezeichen

In regulären Ausdrücken sorgt das Metazeichen `?` dafür, dass der vorhergehende Teilausdruck optional wird.
Somit stimmt es mit null oder einer Übereinstimmung des Teilausdrucks überein.
Zum Beispiel heißt der reguläre Ausdruck `[T]?he`: ein oder kein `T`, gefolgt von dem Buchstaben `h`, gefolgt von dem Buchstaben `e`.

<pre>
"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/cIg9zm/1)

<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/kPpO2x/1)

## 2.4 Geschweifte Klammern

Geschweifte Klammern `{}` gehören wie die zuvor behandelten Metazeichen zu den Quantifizierern. Sie werden verwendet, 
um genau anzugeben wie oft ein Teilausdruck minimal und maximal hintereinander übereinstimmen muss.
Zum Beispiel bedeutet der reguläre Ausdruck `[0-9]{2,3}`: Mindestens zwei, aber maximal drei Ziffern (Zeichenfolge 0-9) hintereinander.

<pre>
"[0-9]{2,3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/juM86s/1)

Die zweite Zahl kann ausgelassen werden. Somit heißt der Ausdruck `[0-9]{2,}`: zwei oder mehr Ziffern in Folge.
Wenn wir auch das Komma entfernen, heißt `[0-9]{3}`: genau drei Ziffern in Folge.

<pre>
"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/Gdy4w5/1)

<pre>
"[0-9]{3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to 10.0.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/Sivu30/1)

## 2.5 Gruppierungen

Eine Gruppierung (eng. *capturing group*) fasst eine Gruppe von Teilausdrücken in Klammern `(...)` zusammen. 
Eine Gruppierung selbst ist ebenfalls ein Teilausdruck, weshalb Quantoren wie `{}`, `*` oder `?` auf sie angewendet werden können.
Zum Beispiel stimmt der reguläre Ausdruck `(ab)*` mit null oder mehr Vorkommen von `a` und `b` hintereinander überein.
Auch das "Oder"-Metazeichen `|` kann innerhalb einer Gruppierung verwendet werden. Der reguläre Ausdruck `(c|g|p)ar` bedeutet:
kleines `c`, `g` oder `p`, gefolgt vom Buchstaben `a`, gefolgt vom Buchstaben `r`. Dies ist äquivalent zu `[cgp]ar`.

<pre>
"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/tUxrBG/1)

Gruppierungen stimmen nicht nur mit Zeichenketten überein, sondern "merken" sich auch die übereinstimmenden Zeichen in der Gruppe für die Verwendung in der Elternsprache
(auch Rückwärtsreferenz genannt).
Die Elternsprache kann Python, JavaScript oder sonst irgendeine Sprache sein, die reguläre Ausdrücke implementiert.


### 2.5.1 Gruppierungen ohne Rückwärtsreferenz

Gruppierungen ohne Rückwärtsreferenz (eng. *non-capturing groups*) sind Gruppierungen, die nur mit den Zeichen übereinstimmen, diese aber nicht für spätere Verwendung zwischenspeichern.
Solche Gruppierungen werden mit einem `?`, gefolgt von einem `:` in Klammern `(...)` definiert.
Somit gleicht der reguläre Ausdruck `(?:c|g|p)ar` dem Ausdruck `(c|g|p)ar` in seiner Übereinstimmung mit den Zeichenketten, aber im Gegensatz erzeugt er keine Rückwärtsreferenz.

<pre>
"(?:c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/Rm7Me8/1)

Gruppierungen ohne Rückwärtsreferenz können für Finden-und-Ersetzen oder in Kombination mit normalen Gruppierungen nützlich sein, um den Überblick zu behalten, 
wenn auf Basis der Übereinstimmungen eine Ausgabe erzeugt wird. Siehe auch [4. Lookaround](#4-lookaround).

## 2.6 Alternation

In einem regulären Ausdruck wird der Trennstrich `|` verwendet, um Alternativen (eng. *alternation*) zu definieren.
Alternation ist wie ein "ODER" zwischen mehreren Teilausdrücken. Nun könnte man annehmen, dass
Zeichenklassen und Alternation auf die gleiche Art und Weise funktionieren. Aber der große Unterschied 
zwischen diesen beiden ist, dass Zeichenklassen für einzelne Zeichen funktionieren, während für Alternationen
beliebige Teilausdrücke verwendet werden können. So heißt der reguläre Ausdruck `(T|t)he|car` beispielsweise:
Entweder ein großes `T` oder kleines `t`, dann der Buchstabe `h` gefolgt vom Buchstaben `e` ODER 
`c`, gefolgt von `a`, gefolgt von `r`. Man beachte die Klammern, die zur Trennung der einen Alternation von der anderen
gesetzt wurden.

<pre>
"(T|t)he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/fBXyX0/1)

## 2.7 Escaping

Der Backslash `\` wird in regulären Ausdrücken verwendet, um die besondere Bedeutung des folgenden Zeichens aufzuheben (eng. *escape*) oder ihm eine besondere Bedeutung zu verleihen 
(s. [Vordefinierte Zeichenklassen](#3-vordefinierte-zeichenklassen)).
Er erlaubt es, für andere Zwecke reservierte Zeichen wie die Metazeichen `{ } [ ] / \ + * . $ ^ | ?` als Literale, also wörtliche Übereinstimmungen zu nutzen.
Um mit einem besonderen Zeichen wortwörtlich übereinzustimmen, muss es auf ein `\` folgen.

Der reguläre Ausdruck `.` zum Beispiel wird benutzt, um mit einem beliebigen Zeichen übereinzustimmen. 
Der Ausdruck `(f|c|m)at\.?` hebt diese Bedeutung auf: `f`, `c` oder `m`, gefolgt von `a`, gefolgt von `t`, schließlich gefolgt von einem optionalen `.`.

<pre>
"(f|c|m)at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/DOc5Nu/1)

## 2.8 Anker

In regulären Audrücken werden Anker (eng. *anchor*) verwendet, um zu überprüfen, ob der Teilausdruck mit dem 
Anfang oder dem Ende der Teilausgabe übereinstimmt. Es gibt zwei Arten von Ankern: das Zirkumflex `^`
stimmt mit dem Anfang, das Dollarzeichen `$` mit dem Ende der Eingabe überein.  

### 2.8.1 Zirkumflex

Das Zirkumflex `^` (eng. *caret*) wird benutzt um zu überprüfen, ob der Teilausdruck mit dem Anfang der Zeichenkette übereinstimmt.
Wenn wir den regulären Ausdruck `^a` auf die Eingabe `abc` anwenden, stimmt er mit `a` überein. 
Aber wenn wir auf die gleiche Eingabe den Ausdruck `^b` anwenden, gibt es keine Übereinstimmungen, weil in der Zeichenkette `abc` kein "b"
am Anfang steht. Schauen wir uns einen anderen Ausdruck an: `^(T|t)he`. Dieser bedeutet: kleines `t` oder großes `T` am Anfang der Eingabe,
gefolgt von `h`, gefolgt von `e`.

<pre>
"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/5ljjgB/1)

<pre>
"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/jXrKne/1)

### 2.8.2 Dollar

Das Dollarzeichen `$` wird benutzt um zu überprüfen, ob der Teilausdruck mit dem Ende der Zeichenkette übereinstimmt.
Der reguläre Ausdruck `(at\.)$` etwa bedeutet: `a`, gefolgt von `t` und dann `.` am Ende der Eingabe.

<pre>
"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/y4Au4D/1)

<pre>
"(at\.)$" => The fat cat. sat. on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/t0AkOd/1)

##  3. Vordefinierte Zeichenklassen

Reguläre Ausdrücke haben Kürzel für die am häufigsten benötigten Zeichenklassen, was viele Ausdrücke vereinfacht und kürzer macht.
Das sind die vordefinierten Zeichenklassen:

|Shorthand|Description|
|:----:|----|
|.|Beliebiges Zeichen außer Zeilenumbruch|
|\w|Stimmt mit alphanumerischen Zeichen überein: `[a-zA-Z0-9_]`|
|\W|Stimmt mit nicht-alphanumerischen Zeichen überein: `[^\w]`|
|\d|Stimmt mit Ziffern überein: `[0-9]`|
|\D|Stimmt mit Zeichen, die keine Ziffern sind überein: `[^\d]`|
|\s|Stimmt mit Leerraum überein: `[\t\n\f\r\p{Z}]`|
|\S|Stimmt mit allem außer Leerraum überein: `[^\s]`|

## 4. Umsehen (Lookaround)

Lookbehind ("zurückschauen") und Lookahead ("vorausschauen") (auch Lookaround ("Umsehen") genannt) sind besondere Arten von **Gruppierungen ohne Rückwärtsreferenz**
(zur Erinnerung: das sind Gruppierungen, die zwar mit dem Muster übereinstimmen, aber sich die Übereinstimmung nicht "merken").
Sie werden in Situationen verwendet, wo wir ein Muster einfangen wollen, dem andere Muster folgen oder vorhergehen.
Zum Beispiel wollen wir alle Zahlen aus der Zeichenkette `$4.44 and $10.88`, vor denen ein Dollarzeichen `$` steht. Wir benutzen dafür den folgenden regulären Audruck:
`(?<=\$)[0-9.]*`. Das heißt: Stimme mit allen Zeichenketten überein, die Ziffern `0-9` oder Punkte `.` enthalten und die einem Dollarzeichen `$` folgen.

Das sind die Lookarounds, die es gibt:

|Symbol|Name|
|:----:|----|
|?=|Positiver Lookahead|
|?!|Negativer Lookahead|
|?<=|Positiver Lookbehind|
|?<!|Negativer Lookbehind|

### 4.1 Positives Vorausschauen (Lookahead)

Ein positiver Lookahead versichert, dass der Teilausdruck vor dem Lookahead von dem Lookahead-Teilausdruck gefolgt wird.
Das Ergebnis der Übereinstimmung beinhaltet dabei nur den Teilausdruck vor dem Lookahead.
Klammern werden genutzt, um positive Lookaheads zu definieren. Nach der öffnenden Klammer müssen ein Fragezeichen und ein Gleichheitszeichen
stehen: `(?=...)`. Der Lookahead-Ausdruck wird nach dem Gleichheitszeichen notiert.
Zum Beispiel bedeutet der reguläre Ausdruck `(T|t)he(?=\sfat)`: kleines `t` oder großes `T`, dann ein `h`, dann ein `e`. Der positive Lookahead in den Klammern 
ist eine zusätzliche Bedingung, die dafür sorgt, dass der Ausdruck nur mit `the` oder `The` übereinstimmt, welches von einem Leerzeichen und den Buchstaben 
`f`, `a` und `t` gefolgt wird.

<pre>
"(T|t)he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/IDDARt/1)

### 4.2 Negatives Vorausschauen (Lookahead)

Negative Lookaheads werden verwendet, um alle Übereinstimmungen in einer Zeichenkette zu bekommen, auf die **nicht** ein bestimmtes Muster folgt.
Ein Negativer Lookahead wird wie ein positiver Lookahead definiert, nur dass statt einem Gleichheitszeichen ein Ausrufezeichen `!` benutzt wird, d.h.
`(?!...)`. Aus dem regulären Ausdruck `(T|t)he(?!\sfat)` folgt somit: alle `The` oder `the`, auf die **kein** Leerzeichen und das Wort `fat` folgt, stimmen überein.

<pre>
"(T|t)he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/V32Npg/1)

### 4.3 Positives Zurückschauen (Lookbehind)

Positive Lookbehinds werden verwendet, um alle Übereinstimmungen in einer Zeichenkette zu bekommen, denen ein bestimmtes Muster vorhergeht.
Postive Lookbehinds werden mit `(?<=...)` notiert. Der reguläre Ausdruck `(?<=(T|t)he\s)(fat|mat)` zum Beispiel bedeutet: alle `fat` oder `mat`, 
die nach `The ` oder `the ` kommen, stimmen überein.

<pre>
"(?<=(T|t)he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/avH165/1)

### 4.4 Negativer Lookbehind

Negative Lookbehinds werden verwendet, um alle Übereinstimmungen in einer Zeichenkette zu bekommen, denen **nicht** ein bestimmtes Muster vorhergeht.
Negative Lookbehinds werden mit `(?<!...)` notiert. Der reguläre Ausdruck `(?<!(T|t)he\s)(cat)` zum Beispiel bedeutet: alle `cat`, die nicht nach 
`The ` oder `the ` kommen, stimmen überein.

<pre>
"(?&lt;!(T|t)he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/8Efx5G/1)

## 5. Modifikatoren

Modifikatoren (eng. *flags* oder *modifiers*) verändern die Ausgabe eines regulären Ausdrucks. Sie können in beliebiger Kombination oder Reihenfolge 
genutzt werden und sind ein integraler Bestandteil regulärer Ausdrücke.


|Modifikator|Beschreibung|
|:----:|----|
|i|Schreibungsunabhängig: Unterschiede bei Groß- und Kleinschreibung in den Mustern werden ignoriert.|
|g|Globale Suche: Die Suche geht durch die gesamte Eingabe.|
|m|Mehrzeilig: Anker-Metazeichen funktionieren für Anfang/Ende jeder Zeile.|

### 5.1 Groß-/Kleinschreibung unempfindlich

Der `i` Modifikator wird benutzt, um unabhängige Übereinstimmungen bei der Groß-/Kleinschreibung zu finden. Zum Beispiel heißt der reguläre Ausdruck
`/The/gi`: großes `T`, gefolgt von `h`, dann `e`. Und am Ende des Ausdrucks ist der `i` Modifikator zu finden, welcher der Maschine 
zu verstehen gibt, dass Groß- und Kleinschreibung ignoriert werden sollen. Wie zu sehen ist, wird auch der `g` Modifikator benutzt,
da wir die gesamte Eingabe nach dem Muster absuchen wollen.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/dpQyf9/1)

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/ahfiuh/1)

### 5.2 Globale Suche

Der `g` Modifikator wird benutzt, um eine globale Suche durchzuführen (alle Übereinstimmungen finden, nicht nach der ersten aufhören).
Zum Beispiel heißt der reguläre Ausdruck `/.(at)/g`: ein beliebiges Zeichen (außer Zeilenumbruch), gefolgt von `a`, gefolgt von `t`.
Weil wir den `g` Modifikator angegeben haben, findet der reguläre Ausdruck nun alle Übereinstimmungen in der Eingabe, nicht nur die erste
(was das Standardverhalten ist).

<pre>
"/.(at)/" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/jnk6gM/1)

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/dO1nef/1)

### 5.3 Mehrzeilig

Der `m` Modifikator wird benutzt, um eine mehrzeilige Suche durchzuführen. Wie zuvor erwähnt werden Anker `(^, $)` genutzt, um zu überprüfen,
ob ein Muster dem Anfang oder dem Ende der Eingabe entspricht. Wenn wir stattdessen wollen, dass Anker zeilenweise funktionieren, nutzen wir den `m`
Modifikator. Zum Beispiel bedeutet der reguläre Ausdruck `/at(.)?$/gm`: `a`, gefolgt von `t`, dann optional ein beliebiges Zeichen außer 
Zeilenumbruch. Wegen des `m` Modifikators wird das Muster nun auf das Ende jeder Zeile statt nur das Ende der gesamten Eingabe angewandt.

<pre>
"/.at(.)?$/" => The fat
                cat sat
                on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/hoGMkP/1)

<pre>
"/.at(.)?$/gm" => The <a href="#learn-regex"><strong>fat</strong></a>
                  cat <a href="#learn-regex"><strong>sat</strong></a>
                  on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Teste den regulären Ausdruck](https://regex101.com/r/E88WE2/1)

## 6. Gierige vs. faule Übereinstimmung

Standardmäßig finden reguläre Ausdrücke Übereinstimmungen mit Gier (eng. *greed*), d.h. es wird nach den längsten Übereinstimmungen gesucht. 
Mit `?` können wir faul (eng. *lazy*) suchen, d.h. es wird nach den kürzesten Übereinstimmungen gesucht.

<pre>
"/(.*at)/" => <a href="#learn-regex"><strong>The fat cat sat on the mat</strong></a>.
</pre>


[Teste den regulären Ausdruck](https://regex101.com/r/AyAdgJ/1)

<pre>
"/(.*?at)/" => <a href="#learn-regex"><strong>The fat</strong></a> cat sat on the mat.
</pre>


[Teste den regulären Ausdruck](https://regex101.com/r/AyAdgJ/2)

## Beitragen

* Öffne Pull Requests mit Verbesserungen
* Diskutiere Ideen in Issues
* Erzähl es anderen
* Gib Rückmeldung [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/ziishaned.svg?style=social&label=Follow%20%40ziishaned)](https://twitter.com/ziishaned)

## Lizenz

MIT &copy; [Zeeshan Ahmad](https://twitter.com/ziishaned)
