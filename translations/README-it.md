<p align="center">
    <br/>
    <a href="https://github.com/ziishaned/learn-regex">	
        <img src="https://i.imgur.com/bYwl7Vf.png" alt="Learn Regex">
    </a>
</p>


## Translations:

* [English](README.md)
* [German](translations/README-de.md)
* [Español](translations/README-es.md)
* [Français](translations/README-fr.md)
* [Português do Brasil](translations/README-pt_BR.md)
* [中文版](translations/README-cn.md)
* [日本語](translations/README-ja.md)
* [한국어](translations/README-ko.md)
* [Turkish](translations/README-tr.md)
* [Greek](translations/README-gr.md)
* [Magyar](translations/README-hu.md)
* [Polish](translations/README-pl.md)
* [Русский](translations/README-ru.md)
* [Tiếng Việt](translations/README-vn.md)
* [فارسی](translations/README-fa.md)
* [עברית](translations/README-he.md)


## Cosa sono le Espressioni Regolari?

<p>
    <a href="https://gum.co/learn-regex">
        <img src="https://img.shields.io/badge/-Download%20PDF%20-0a0a0a.svg?style=flat&colorA=0a0a0a" alt="Download PDF">
    </a>
</p>

> Un'espressione regolare è un insieme di caratteri e simboli utilizzati per trovare una specifica sequenza (pattern) di testo.


Un'espressione regolare è una sequenza che corrisponde a una stringa di testo letta da sinistra a destra. Le espressioni regolari sono utilizzate per sostituire parti di testo in una stringa, validare moduli, estrarre parti di stringhe basate sulla corrispondenza di uno schema e molto altro. Il termine "Espressione regolare" è molto lungo quindi è normalmente abbreviato con "regex" o "regexp".

Immagina che stai scrivendo un applicazione e hai bisogno di impostare una regola per quando un utente sceglie il suo nome utente. Vogliamo consentire che il nome utente contenga lettere, numeri, carattere di sottolineo e il trattino, vogliamo inoltre limitare il numero di caratteri del nome utente. Possiamo utilizzare la seguente espressione regolare per validare il nome utente:
<br/><br/>
<p align="center">
  <img src="./img/regexp-en.png" alt="Regular expression">
</p>

L'espressione regolare riportata sopra può accettare le stringhe `john_doe`, `jo-hn_doe` e `john12_as`. Non c'è corrispondenza con `Jo` perché contiene una lettera maiuscola ed inoltre è troppo breve.

## Sommario

- [Corrispondenze di base](#1-basic-matchers)
- [Caratteri jolly](#2-meta-characters)
  - [Il punto](#21-the-full-stop)
  - [Classe di caratteri](#22-character-sets)
    - [Negazione di classe di carattere](#221-negated-character-sets)
  - [Ripetizioni](#23-repetitions)
    - [Simbolo Asterisco](#231-the-star)
    - [Simbolo Più](#232-the-plus)
    - [Carattere Punto di Domanda](#233-the-question-mark)
  - [Parentesi](#24-braces)
  - [Raggruppamento e cattura di caratteri](#25-capturing-groups)
      - [Raggruppamento di caratteri senza cattura](#251-non-capturing-groups)
  - [Alternativa](#26-alternation)
  - [Carattere speciale Escape](#27-escaping-special-characters)
  - [Ancore](#28-anchors)
    - [Segno di omissione ^](#281-the-caret)
    - [Il simbolo del dollaro](#282-the-dollar-sign)
- [Classe di caratteri rapide](#3-shorthand-character-sets)
- [Guardarsi intorno](#4-lookarounds)
  - [Lookahead positivo](#41-positive-lookahead)
  - [Lookahead negativo](#42-negative-lookahead)
  - [Lookbehind positivo](#43-positive-lookbehind)
  - [Lookbehind negativo](#44-negative-lookbehind)
- [Opzioni](#5-flags)
  - [Sensibilità ai caratteri maiuscoli e minuscoli](#51-case-insensitive)
  - [Ricerca globale](#52-global-search)
  - [Riga multipla](#53-multiline)
- [Corrispondenza vorace vs pigra](#6-greedy-vs-lazy-matching)

## 1. Corrispondenze di base

Un'espressione regolare non è altro che una sequenza di caratteri usati per eseguire ricerche in un testo. Ad esempio, l'espressione regolare `the` corrisponde a: la lettera `t`, seguita dalla lettera `h`, seguita dalla lettera `e`.

<pre>
"the" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/dmRygT/1)

L'espressione regolare `123` corrisponde alla stringa `123`. L'espressione regolare viene confrontata con il testo da ricercare carattere per carattere, al fine di trovare la corrispondenza completa.
Le espressioni regolari sono normalmente sensibili a caratteri maiuscoli e minuscoli, perciò l'espressione regolare `The` non troverà corrispondenza con il testo `the`.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/1paXsy/1)

## 2. Caratteri jolly

I caratteri jolly sono i mattoncini per la costruzione di espressioni regolari. I caratteri jolly non vengono usati letteralmente, vengono invece interpretati come caratteri speciali. Alcuni caratteri jolly hanno un significato speciale se inseriti all'interno di parentesi quadre. I caratteri jolly sono i seguenti:

|Carattere jolly|Descrizione|
|:----:|----|
|.|Il punto corrisponde ad ogni carattere eccetto l'invio e l'interruzione di riga.|
|[ ]|Classe di caratteri. Corrispondenza con ciascun carattere contenuto tra le parentesi.|
|[^ ]|Negazione di classe di caratteri. Corrispondenza con ciascun carattere non contenuto all'interno delle parentesi|
|*|Corrispondenza con zero o più ripetizioni del carattere che lo precede.|
|+|Corrispondenza con una o più ripetizioni del carattere che lo precede|
|?|Rende opzionale il carattere che lo precede.|
|{n,m}|Parentesi graffe. Corrisponde con le ripetizione minima di "n" ma non più di "m", del carattere che le precede.|
|(xyz)|Gruppo di caratteri. Corrispondenza con i caratteri tra parentesi xyz solo nell'ordine esatto.|
|&#124;|Alternativa. Corrispondenza con il carattere che precede o con quello che segue.|
|&#92;|Escape sul carattere successivo. Consente la corrispondenza con i caratteri riservati <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>|
|^|Corrispondenza con l'inizio del testo.|
|$|Corrispondenza con la fine del testo.|

## 2.1 Il punto

Il punto `.` è il più semplice esempio di carattere jolly. Il carattere jolly `.` ha corrispondenza con ogni singolo carattere nel testo da cercare. Non ha corrispondenza con i caratteri di invio e fine riga.
Ad esempio, l'espressione regolare `.ar` significa: ciascun carattere, seguito dalla lettera `a`, seguita dalla lettera `r`.

<pre>
".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/xc9GkU/1)

## 2.2 Classi di carattere

Le parentesi quadre sono utilizzate per definire una classe di caratteri. Si può utilizzare il trattino per definire degli intervalli all'interno della classe. L'ordine dei caratteri utilizzati nella classe non ha influenza sul risultato. Ad esempio, l'espressione regolare `[Tt]he` significa: una lettera maiuscola `T` o una lettera minuscola `t`, seguita dalla lettera `h`, seguita dalla lettera `e`.

<pre>
"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/2ITLQ4/1)

Un punto all'interno di una classe di caratteri, in ogni caso, corrisponde al punto letterale. L'espressione regolare `ar[.]` corrisponde a: una lettera minuscola `a`, seguita dalla lettera `r`, seguita dal carattere `.`.

<pre>
"ar[.]" => A garage is a good place to park a c<a href="#learn-regex"><strong>ar.</strong></a>
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/wL3xtE/1)

### 2.2.1 Negazione di classe di carattere

In generale, il carattere di omissione ^ rappresenta l'inizio di un testo, ma se inserito come primo carattere all'interno di parentesi quadre, funziona come negazione della classe di caratteri. Ad esempio, l'espressione regolare `[^c]ar` corrisponde a: qualsiasi carattere tranne la lettera `c`, seguito dalla lettera `a`, seguita dalla lettera `r`.

<pre>
"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/nNNlq3/1)

## 2.3 Ripetizioni

I caratteri jolly `+`, `*` o `?` sono utilizzati per specificare quante volte uno schema si può ripetere. Questi caratteri jolly agiscono in modo differente per differenti situazioni.

### 2.3.1 Simbolo Asterisco

Il simbolo `*` corrisponde a zero o più ripetizioni della sequenza precedente. L'espressione regolare `a*` corrisponde a: zero o più ripetizioni della precedente lettera minuscola `a`.
Se il simbolo viene utilizzato a seguito di una classe di caratteri allora verranno applicate le ripetizioni all'intera classe. Ad esempio, l'espressione regolare `[a-z]*` corrisponde a: qualsiasi ripetizione di ciascuna lettera minuscola in un testo.

<pre>
"[a-z]*" => T<a href="#learn-regex"><strong>he</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/7m8me5/1)

Il simbolo `*` più essere applicato al carattere jolly `.` per la corrispondenza con qualsiasi numero di caratteri `.*`. Il simbolo `*` può essere usato con lo spazio vuoto `\s` per la corrispondenza con una stringa di spazi vuoti. Ad esempio l'espressione regolare `\s*cat\s*` corrisponde a: nessuno o più spazi, seguiti dalla lettera minuscola `c`, seguita dalla lettera minuscola `a`, seguita dalla lettera minuscola `t`, seguite da nessuno o più spazi vuoti.

<pre>
"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the con<a href="#learn-regex"><strong>cat</strong></a>enation.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/gGrwuz/1)

### 2.3.2 Simbolo Più

Il simbolo `+` corrisponde a una o più ripetizioni della sequenza precedente. Ad esempio, l'espressione regolare `c.+t` corrisponde a: una lettera minuscola `c`, seguita da almeno un carattere, seguito dalla lettera minuscola `t`. 
È importante chiarire che `t` corrisponde all'ultima lettera `t` nella stringa.

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/Dzf9Aa/1)

### 2.3.3 Carattere Punto di Domanda

Nelle espressioni regolari, il carattere jolly `?` rende opzionale il carattere che lo precede. Questo simbolo corrisponde alla ripetizione zero o una volta della sequenza che lo precede.
Ad esempio, l'espressione regolare `[T]?he` corrisponde a: Lettera maiuscola opzionale `T`, seguita, se presente, dalla lettera maiuscola `h`, seguita dalla lettera minuscola `e`.

<pre>
"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/cIg9zm/1)

<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/kPpO2x/1)

## 2.4 Parentesi graffe

Nelle espressioni regolari, le parentesi graffe (chiamate anche quantificatori) sono utilizzate per specificare il numero di volte che un carattere o una classe di caratteri possono essere ripetute per mantenere la corrispondenza. Ad esempio, l'espressione regolare `[0-9]{2,3}` corrisponde a: Almeno 2 cifre, ma non più di 3, nell'intervallo da 0 a 9.

<pre>
"[0-9]{2,3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/juM86s/1)

Si può omettere il secondo numero. Ad esempio, l'espressione regolare `[0-9]{2,}` corrisponde a: 2 o più cifre. Inoltre possiamo rimuove la virgola di separazione, l'espressione regolare `[0-9]{3}` corrisponde a: esattamente 3 cifre.

<pre>
"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/Gdy4w5/1)

<pre>
"[0-9]{3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to 10.0.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/Sivu30/1)

## 2.5 Raggruppamento e cattura di caratteri

Un gruppo di caratteri è un sottoschema scritto all'interno di parentesi `(...)`. Come esposto in precedenza, se inseriamo un quantificatore a seguito di un carattere, viene definita la ripetizione del carattere stesso; allo stesso modo, se inseriamo un quantificatore a seguito di un gruppo di caratteri, definiamo la ripetizione dell'intero gruppo. Ad esempio, l'espressione regolare `(ab)*` corrisponde a zero o più ripetizioni della sequenza esatta di lettere minuscole "ab". 
Si può inoltre utilizzare il carattere di alternativa `|` all'interno di un gruppo di caratteri.
Ad esempio, l'espressione regolare `(c|g|p)ar` corrisponde a: una lettera minuscola a scelta tra `c`, `g` o `p`, seguita dalla lettera minuscola `a`, seguite dalla lettera minuscola `r`.

<pre>
"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/tUxrBG/1)

Nota che il gruppo di carattere non trova solo corrispondenza, ma cattura il contenuto del gruppo, per utilizzarlo in un linguaggio di programmazione. Il linguaggio può essere Python, Javascript o qualsiasi linguaggio che implementi funzioni per l'utilizzo di espressioni regolari.

### 2.5.1 Raggruppamento di caratteri senza cattura

Un gruppo di caratteri senza cattura è un gruppo utilizzato per la corrispondenza ma non per la cattura. È definito dal carattere `?` seguito da `:` all'interno delle parentesi `(...)`. Ad esempio, l'espressione regolare `(?:c|g|p)ar` è simile a `(c|g|p)ar`, corrisponde alla stessa stringa ma non cattura il gruppo.

<pre>
"(?:c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/Rm7Me8/1)

I gruppi senza cattura sono utili per funzioni di ricerca e sostituzione o quando utilizzati in abbinata con gruppi di cattura per produrre diversi tipi di output.
Vedere anche [4. Guardarsi intorno](#4-lookaround).

## 2.6 Alternativa

In un'espressione regolare, la barra verticale `|` è utilizzata per definire alternative.
L'alternativa corrisponde alla dichiarazione OR tra espressioni multiple. Sagrai pensando che gli insiemi di caratteri e le alternative funzionino allo stesso modo, ma la grande differenza è che l'alternativa funziona a livello di espressione. Ad esempio, l'espressione regolare `(T|t)he|car` corrisponde a: sia (una lettera maiuscola `T` o una lettera minuscola `t`, seguita dalla lettera minuscola `h`, seguita da una lettera minuscola `e`), sia
(Una lettera minuscola `c`, seguita da una lettera minuscola `a`, seguita dalla lettera minuscola `r`).
Nota che sono state incluse le parentesi per chiarezza, per dimostrare come le espressioni possono funzionare anche all'interno delle parentesi stesse.

<pre>
"(T|t)he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/fBXyX0/1)

## 2.7 Carattere speciale Escape

Il carattere di escape `\` è utilizzato nelle espressioni regolari per annullare la funzione del carattere jolly seguente. Questo consente di includere caratteri riservati, come `{ } [ ] / \ + * . $ ^ | ?` all'interno di un'espressione regolare per la corrispondenza letterale.

Ad esempio, l'espressione regolare `.` è utilizzata per la corrispondenza con qualsiasi carattere eccetto il carattere di invio e di fine riga. Quindi, per la corrispondenza del carattere `.`, l'espressione regolare `(f|c|m)at\.?` corrisponde a: una lettera minuscola `f`, `c` o `m`, seguita dalla lettera minuscola `a`, seguita dalla lettera minuscola `t`, seguita dal carattere `.` opzionale.

<pre>
"(f|c|m)at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/DOc5Nu/1)

## 2.8 Ancore

Nelle espressioni regolari, si usano le ancore per la corrispondenza dell'espressione stessa, all'inizio o al termine di un testo.
Le ancora sono di due tipi:
Il primo tipo è il carattere di negazione `^`  che verifica la corrispondenza all'inizio del testo, il secondo tipo è il carattere `$` che verifica la corrispondenza al termine del testo.

### 2.8.1 Il carattere di negazione ^

Il simbolo di negazione `^` è usato per verificare la corrispondenza al primo carattere del testo. Utilizzando l'espressione regolare `^a` (significa che 'a' deve essere il primo carattere) con il testo `abc`, ci sarà corrispondenza con `a`. Applicando l'espressione regolare `^b` al testo precedente, non ci sarà alcuna corrispondenza.
Questo perché nel testo `abc`, la lettera "b" non è il carattere iniziale. Vediamo un'altra espressione regolare, `^(T|t)he` che corrisponde a: una lettera maiuscola `T` o una lettera minuscola `t` deve essere la prima lettera del testo, seguita dalla lettera minuscola `h`, seguita dalla lettera minuscola `e`.

<pre>
"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/5ljjgB/1)

<pre>
"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/jXrKne/1)

### 2.8.2 Il simbolo del Dollaro

Il simbolo del collario `$` è utilizzato per verificare la corrispondenza con la parte finale del testo. Ad esempio, l'espressione regolare `(at\.)$` corrisponde a: una lettera minuscola `a`, seguita da una lettera minuscola `t`, seguita dal carattere punto `.`, il tutto deve trovarsi al termine del testo.

<pre>
"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/y4Au4D/1)

<pre>
"(at\.)$" => The fat cat. sat. on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/t0AkOd/1)

##  3. Classe di caratteri rapide

Ci sono alcune classe di caratteri rapide per l'utilizzo nelle espressioni regolari:

|Classe di caratteri rapide|Descrizione|
|:----:|----|
|.|Qualsiasi carattere tranne invio e fine riga|
|\w|Corrispondenza con caratteri alfanumerici: `[a-zA-Z0-9_]`|
|\W|Corrispondenza con caratteri non alfanumerici: `[^\w]`|
|\d|Corrispondenza con numeri: `[0-9]`|
|\D|Corrispondenza con caratteri che non siano numeri: `[^\d]`|
|\s|Corrispondenza con spazi vuoti: `[\t\n\f\r\p{Z}]`|
|\S|Corrispondenza con caratteri che non siano spazi vuoti: `[^\s]`|

## 4. Guardarsi intorno

Lookbehinds e lookaheads sono speciali tipi di ***gruppi di caratteri senza cattura***. Guardarsi intorno sono utilizzati quando uno schema deve essere preceduto o seguito da un altro schema. Ad esempio, pensiamo di dover selezionare i numeri preceduti dal carattere `$` nel testo `$4.44 and $10.88`. Useremo l'espressione regolare `(?<=\$)[0-9\.]*` che corrisponde a: selezionare tutti i numeri che contengono il carattere `.` e sono preceduti dal carattere `$`. Queste sono le espressioni di guardarsi intorno utilizzate:

|Simbolo|Descrizione|
|:----:|----|
|?=|Lookahead positivo|
|?!|Lookahead negativo|
|?<=|Lookbehind positivo|
|?<!|Lookbehind negativo|

### 4.1 Lookahead positivo

Il lookahead positivo assume che la prima parte dell'espressione deve essere seguita dall'espressione di lookahead. Il risultato corrisponde solo alla prima parte dell'espressione. Per definire un lookahead positivo, sono utilizzate le parentesi. All'interno delle parentesi, si utilizza un carattere di punto di domanda seguito dal segno uguale: `(?=...)`. L'espressione lookahead viene scritta dopo il segno di uguale all'interno delle parentesi. Ad esempio, l'espressione regolare `(T|t)he(?=\sfat)` corrisponde a: una lettera minuscola `t` o una lettera maiuscola `T`, seguita dalla lettera minuscola `h`, seguita dalla lettera minuscola `e`. Nelle parentesi è definita l'espressione di lookahead positivo che trova corrispondenza con le parole `The` o `the` solo se seguite dalla parola `fat`.

<pre>
"(T|t)he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/IDDARt/1)

### 4.2 Lookahead negativo

Lookahead negativo è utilizzato per ottenere corrispondenza con una stringa che non è seguita da un determinato schema. Il lookahead negativo è scritto nello stesso modo del lookahead positivo. L'unica differenza consiste nell'utilizzo del carattere di punto esclamativo `!`, al posto del segno uguale `=`, per indicare la negazione, ad esempio `(?!...)`. Vediamo la seguente espressioni regolare `(T|t)he(?!\sfat)` che trova corrispondenza con: tutte le parole `The` o `the` che non sono seguite da uno spazio dalla parola `fat`.

<pre>
"(T|t)he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/V32Npg/1)

### 4.3 Lookbehind positivo

Lookbehind positivo è utilizzato per trovare il testo preceduto da uno specifico schema. Il lookbehind positivo è sxcritto come `(?<=...)`. Ad esempio, l'espressione regolare `(?<=(T|t)he\s)(fat|mat)` corrisponde a: tutte le parole `fat` o `mat` che seguono la parola `The` o `the`.

<pre>
"(?<=(T|t)he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/avH165/1)

### 4.4 Lookbehind negativo

Lookbehind negativo è utilizzato per trovare il testo non preceduto da uno specifico schema. Il lookbehind negativo è sxcritto come `(?<!...)`. Ad esempio, l'espressione regolare `(?<!(T|t)he\s)(cat)` corrisponde a: tutte le parole `fat` o `mat` che non seguono la parola `The` o `the`.

<pre>
"(?&lt;!(T|t)he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/8Efx5G/1)

## 5. Opzioni

Le opzioni (o modificatori) modificano il risultato delle espressioni regolari. Queste opzioni possono essere utilizzate in qualsiasi ordine o combinazione, sono parti integranti di RegExp.

|Opzione|Descrizione|
|:----:|----|
|i|Non sensibilità maiuscolo / minuscolo|
|g|Ricerca globale: trova tutte le corrispondenze, non solo la prima.|
|m|Multi riga: estende il funzionamento delle ancore su ogni riga.|

### 5.1 Non sensibilità maiuscolo / minuscolo

L'opzione `i` è usato per rendere la corrispondenza non sensibile a maiuscolo / minuscolo. Ad esempio, l'espressione regolare `/The/gi` corrisponde a: una lettera maiuscola `T`, seguita da una lettera minuscola `h`, seguita da una lettera minuscola `e`. L'opzione `i` alla fine dell'espressione regolare indica di ignorare minuscole / maiuscole. Come si può notare, l'utilizzo dell'opzione `g` estende la ricerca all'intero testo.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/dpQyf9/1)

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/ahfiuh/1)

### 5.2 Ricerca globale

L'opzione `g` è utilizzata per estendere la ricerca a corrispondenze multiple. Ad esempio, l'espressione regolare `/.(at)/g` corrisponde a: qualsiasi carattere eccetto invio e nuova riga, seguito dalla lettera minuscola `a`, seguita dalla lettera minuscola `t`. L'utilizzo dell'opzione `g` estende la ricerca all'intero testo.

<pre>
"/.(at)/" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/jnk6gM/1)

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/dO1nef/1)

### 5.3 Multi riga

L'opzione `m` è utilizzata per estendere la corrispondenza in modalità multi riga. Come già esposto, le ancore `(^, $)` sono utilizzate per verificare se l'espressione si trova all'inizio o alla fine del testo. Volendo utilizzare le ancore su già righe di testo, si può attivare l'opzione `m`. Ad esempio, l'espressione regolare `/at(.)?$/gm` corrisponde a: una lettera minuscola `a`, seguita da una lettera minuscola `t` e, opzionalmente, qualsiasi carattere eccetto invio e nuova riga. Grazie all'opzione `m`, la corrispondenza viene estesa a ciascuna riga del testo.

<pre>
"/.at(.)?$/" => The fat
                cat sat
                on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/hoGMkP/1)

<pre>
"/.at(.)?$/gm" => The <a href="#learn-regex"><strong>fat</strong></a>
                  cat <a href="#learn-regex"><strong>sat</strong></a>
                  on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Verifica l'espressione regolare](https://regex101.com/r/E88WE2/1)

## 6. Corrispondenza vorace vs pigra
Regex ha un funzionamento predefinito vorace, ,significa che la corrispondenza è più estesa possibile. Si può utilizzare `?` per determinare una corrispondenza più pigra, così la corrispondenza è più breve possibile.

<pre>
"/(.*at)/" => <a href="#learn-regex"><strong>The fat cat sat on the mat</strong></a>. </pre>


[Verifica l'espressione regolare](https://regex101.com/r/AyAdgJ/1)

<pre>
"/(.*?at)/" => <a href="#learn-regex"><strong>The fat</strong></a> cat sat on the mat. </pre>


[Verifica l'espressione regolare](https://regex101.com/r/AyAdgJ/2)


## Contribution

* Open a pull request with improvements
* Discuss ideas in issues
* Spread the word
* Reach out with any feedback [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/ziishaned.svg?style=social&label=Follow%20%40ziishaned)](https://twitter.com/ziishaned)
* Traduzione italiana: Claudio Marconato (cmpro.it)

## License

MIT &copy; [Zeeshan Ahmad](https://twitter.com/ziishaned)