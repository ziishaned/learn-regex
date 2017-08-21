<br/>
<p align="center">
<img src="https://i.imgur.com/bYwl7Vf.png" alt="Learn Regex">
</p><br/>

## Çeviriler:

* [English](README.md)
* [Español](README-es.md)
* [Français](README-fr.md)
* [中文版](README-cn.md)
* [日本語](README-ja.md)
* [한국어](README-ko.md)
* [Turkish](README-tr.md)

## Düzenli İfade Nedir?

> Düzenli ifade, bir metinden belirli bir deseni bulmak için kullanılan bir karakter veya sembol grubudur.

Bir düzenli ifade soldan sağa söz konusu harf öbekleriyle eşleşen bir desendir. "Regular expression" söylemesi zor bir tabirdir, genellikle "regex" ya da "regexp" olarak kısaltılmış terimler olarak bulacaksınız. Düzenli ifade bir harf öbeğinde ki bir metin değiştirmek, form doğrulamak, bir desen eşleşmesine dayalı harf öbeğinden bir alt harf öbeği ayıklamak ve çok daha fazlası için kullanılır.

Bir uygulama yazdığınızı hayal edin ve bir kullanıcı kullanıcı adını seçtiğinde kullanıcı adı için kurallar belirlemek istiyorsunuz. Kullanıcı adının harfler, sayılar, altçizgiler ve tireler içermesine izin vermek istiyoruz. Ayrıca, Kullanıcı adındaki karakter sayısını sınırlamak istiyoruz böylece çirkin görünmeyecek. Bir kullanıcı adını doğrulamak için aşağıdaki düzenli ifadeyi kullanıyoruz:

<br/><br/>
<p align="center">
  <img src="./img/regexp-tr.png" alt="Regular expression">
</p>

Yukardaki düzenli ifade `john_doe`, `jo-hn_doe` ve `john12_as` gibi girişleri kabul edebilir.
`Jo` girişi uyuşmaz, çünkü harf öbeği büyük harf içeriyor ve aynı zamanda uzunluğu 3 karakterden az.

## İçindekiler

- [Temel Eşleştiriciler](#1-basic-matchers)
- [Meta Karakterler](#2-meta-characters)
  - [Nokta](#21-full-stop)
  - [Karakter takımı](#22-character-set)
    - [Negatiflenmiş karakter seti](#221-negated-character-set)
  - [Tekrarlar](#23-repetitions)
    - [Yıldız İşareti](#231-the-star)
    - [Artı İşareti](#232-the-plus)
    - [Soru İşareti](#233-the-question-mark)
  - [Süslü Parantez](#24-braces)
  - [Karakter Grubu](#25-character-group)
  - [Birbirini İzleme](#26-alternation)
  - [Özel Karakter Hariç Tutma](#27-escaping-special-character)
  - [Sabitleyiciler](#28-anchors)
    - [Ters v işareti](#281-caret)
    - [Dolar işareti](#282-dollar)
- [Kısaltma Karakter Takımları](#3-shorthand-character-sets)
- [Bakınmak](#4-lookaround)
  - [Olumlu Bakınma](#41-positive-lookahead)
  - [Olumsuz Bakınma](#42-negative-lookahead)
  - [Positive Lookbehind](#43-positive-lookbehind)
  - [Negative Lookbehind](#44-negative-lookbehind)
- [İşaretler](#5-flags)
  - [Büyük/Küçük harf duyarlılığı](#51-case-insensitive)
  - [Bütünsel Arama](#52-global-search)
  - [Çok satırlı](#53-multiline)

## 1. Temel Eşleştiriciler

Bir düzenli ifade bir metin içinde arama yapabilmek için kullandığımız bir karakter desenidir.
Örneğin, `the` düzenli ifadesi şu anlama gelir: `t` harfi ardından `h`, ardından `e` harfi gelir.

<pre>
"the" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Düzenli ifadeyi test edin](https://regex101.com/r/dmRygT/1)

`123` düzenli ifadesi `123` harf öbeğiyle eşleşir. Düzenli ifade birbiri ardına, girilen harf öbeğindeki her karakter düzenli ifadenin içindeki her karakterle karşılaştırılarak eşleştirilir. Düzenli ifadeler normal olarak büyük/küçük harfe duyarlıdırlar, yani `The` düzenli ifadesi `the` harf öbeğiyle eşleşmez.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Düzenli ifadeyi test edin](https://regex101.com/r/1paXsy/1)

## 2. Meta Karakterler

Meta karakterler düzenli ifadelerin yapı taşlarıdırlar. Meta karakterler kendileri için değil bunun yerine bazı özel yollarla yorumlanırlar. Bazı meta karakterler özel anlamları vardır ve bunlar köşeli parantez içinde yazılırlar.

Meta karakterler aşağıdaki gibidir:

|Meta karakter|Açıklama|
|:----:|----|
|.|Satır sonuc hariç herhangi bir karakterle eşleşir.|
|[ ]|Köşeli parantezler arasında bulunan herhangi bir karakterle eşleşir.|
|[^ ]|Köşeli parantez içerisinde yer alan `^` işaretinden sonra girilen karakterler haricindeki karakterlerle eşleşir.|
|*|Kendisinden önce yazılan karakterin sıfır veya daha fazla tekrarı ile eşleşir.|
|+|Kendisinden önce yazılan karakterin bir veya daha fazla tekrarı ile eşleşir.|
|?|Kendisinden önce yazılan karakterin varlık durumunu opsiyonel kılar.|
|{n,m}|Kendisinden önce yazılan karakterin en az `n` en fazla `m` değeri kadar olmasını ifade eder.|
|(xyz)|Verilen sırayla `xyz` karakterleriyle eşleşir.|
|&#124;|`&#124;` karakterinden önce veya sonra verilen ifadelerin herhangi biriyle eşleşir. Or anlamı verir.|
|&#92;|Sonraki karakteri kaçırır. Bu, ayrılmış karakterleri eşleştirmenizi sağlar <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>|
|^|Girilen verinin başlangıcını ifade eder.|
|$|Girilen veririnin sonunu ifade eder.|

## 2.1 Nokta

Nokta `.` meta karakterin en basit örneğidir. `.` meta karakteri satır başlangıcı hariç herhangi bir karakterle eşleşir.
Örneğin, `.ar` düzenli ifadesinin anlamı: herhangi bir karakterin ardından `a` harfi ve `r` harfi gelir.

<pre>
".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Düzenli ifadeyi test edin](https://regex101.com/r/xc9GkU/1)

## 2.2 Karakter Takımı

Karakter takımları aryıca Karakter sınıfı olarak bilinir. Karakter takımlarını belirtmek için köşeli ayraçlar kullanılır.
Karakterin aralığını belirtmek için bir karakter takımında tire kullanın. Köşeli parantezlerdeki karakter aralığının sıralaması önemli değildir. 

Örneğin, `[Tt]he` düzenli ifadesinin anlamı: bir büyük `T` veya küçük `t` harflerinin ardından sırasıyla `h` ve `e` harfi gelir.

<pre>
"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Düzenli ifadeyi test edin](https://regex101.com/r/2ITLQ4/1)

Bununla birlikte, bir karakter takımı içerisindeki bir periyot bir tam periyot demektir.

`ar[.]` düzenli ifadesinin anlamı: Küçük `a` karakteri ardından `r` harfi gelir, ardından bir `.` karakteri gelir.

<pre>
"ar[.]" => A garage is a good place to park a c<a href="#learn-regex"><strong>ar.</strong></a>
</pre>

[Düzenli ifadeyi test edin](https://regex101.com/r/wL3xtE/1)

### 2.2.1 Negatiflenmiş karakter seti

Genellikle, şapka `^` sembolü harf öbeğinin başlangıcını temsil eder, ama köşeli parantez içinde kullanıldığında verilen karakter takımını hariç tutar.

Örneğin, `[^c]ar` ifadesinin anlamı: `c` harfinden hariç herhangi bir harfin ardından `a`, ardından `r` gelir.

<pre>
"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Düzenli ifadeyi test edin](https://regex101.com/r/nNNlq3/1)

## 2.3 Tekrarlar

`+`, `*` ya da `?` meta karakterlerinden sonra bir alt desenin kaç defa tekrar edebileceğini belirtmek için kullanılır. Bu meta karakterler farklı durumlarda farklı davranırlar.

### 2.3.1 Yıldız İşareti

`*` sembolü, kendinden önce girilen eşlemenin sıfır veya daha fazla tekrarıyla eşleşir. Ama bir karakter seti ya da sınıf sonrasına girildiğinde, tüm karakter setinin tekrarlarını bulur.

`a*` düzenli ifadesinin anlamı: `a` karakterinin sıfır veya daha fazla tekrarı. 
`[a-z]*` düzenli ifadesinin anlamı: bir satırdaki herhangi bir sayıdaki küçük harfler.

<pre>
"[a-z]*" => T<a href="#learn-regex"><strong>he</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.
</pre>

[Düzenli ifadeyi test edin](https://regex101.com/r/7m8me5/1)

`*` sembolü `.` meta karakteri ile `.*` karakterinin herhangi harf öbeğine eşleştirmek için kullanılabilir. `*` sembolü boşluk karakteriyle `\s` bir harf öbeğinde boşluk karakterlerini eşleştirmek için kullanılabilir.

Örneğin, `\s*cat\s*` düzenli ifadesinin anlamı: sıfır veya daha fazla boşluk ardından küçük `c` karakteri gelir, ardından küçük `a` karakteri gelir, ardından küçük `t` karakteri gelir, ardından sıfır veya daha fazla boşluk gelir.

<pre>
"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the <a href="#learn-regex">con<strong>cat</strong>enation</a>.
</pre>

[Düzenli ifadeyi test edin](https://regex101.com/r/gGrwuz/1)

### 2.3.2 Artı İşareti

`+` sembolü, kendinden önce girilen eşlemenin bir veya daha fazla tekrarıyla eşleşir.

Örneğin, `c.+t` ifadesinin anlamı: küçük `c` harfi, ardından en az bir karakter gelir, ardından küçük `t` karakteri gelir.
Örnekte açıklamak gereken önemli nokta: `t` harfi cümledeki son `t` harfi olacaktır. `c` ve `t` harfi arasında en az bir karakter vardır.

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

[Düzenli ifadeyi test edin](https://regex101.com/r/Dzf9Aa/1)

### 2.3.3 Soru İşareti

Düzenli ifadelerde `?` meta karakterinden önce girilen karakteri opsiyonel olarak tanımlar. Bu sembol önce gelen karakterin sıfır veya bir örbeğiyle eşleşir.

Örneğin, `[T]?he` ifadesinin anlamı: opsiyonel büyük `T` harfi, ardından küçük `h` karakteri gelir, ardından küçük `e` karakteri gelir.

<pre>
"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Düzenli ifadeyi test edin](https://regex101.com/r/cIg9zm/1)

<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

[Düzenli ifadeyi test edin](https://regex101.com/r/kPpO2x/1)

## 2.4 Süslü Parantez

Düzenli ifadelerde miktar belirliyiciler olarakda bilinen süslü parantezler, bir karakterin veya karakter grubunun kaç defa tekrar edebileceğini belirtmek için kullanılırlar.

Örneğin, `[0-9]{2,3}` ifadesinin anlamı: 0 ile 0 aralığındaki karakterlerden, en az 2 en fazla 3 defa ile eşleş.

<pre>
"[0-9]{2,3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Düzenli ifadeyi test edin](https://regex101.com/r/juM86s/1)

İkinci numarayı boş bırakabiliriz.

Örneğin, `[0-9]{2,}` ifadesinin anlamı: En az 2 veya daha fazla defa eşleş.
Düzenli ifadeden virgülü kaldırırsak `[0-9]{3}`: doğrudan 3 defa eşleşir.

<pre>
"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Düzenli ifadeyi test edin](https://regex101.com/r/Gdy4w5/1)

<pre>
"[0-9]{3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to 10.0.
</pre>

[Düzenli ifadeyi test edin](https://regex101.com/r/Sivu30/1)

## 2.5 Karakter Grubu

Character group is a group of sub-patterns that is written inside Parentheses `(...)`.
As we discussed before that in regular expression if we put a quantifier after a
character then it will repeat the preceding character. But if we put quantifier
after a character group then it repeats the whole character group. For example,
the regular expression `(ab)*` matches zero or more repetitions of the character
"ab". We can also use the alternation `|` meta character inside character group.
For example, the regular expression `(c|g|p)ar` means: lowercase character `c`,
`g` or `p`, followed by character `a`, followed by character `r`.

<pre>
"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Test the regular expression](https://regex101.com/r/tUxrBG/1)

## 2.6 Alternation

In regular expression Vertical bar `|` is used to define alternation.
Alternation is like a condition between multiple expressions. Now, you may be
thinking that character set and alternation works the same way. But the big
difference between character set and alternation is that character set works on
character level but alternation works on expression level. For example, the
regular expression `(T|t)he|car` means: uppercase character `T` or lowercase
`t`, followed by lowercase character `h`, followed by lowercase character `e` or
lowercase character `c`, followed by lowercase character `a`, followed by
lowercase character `r`.

<pre>
"(T|t)he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Test the regular expression](https://regex101.com/r/fBXyX0/1)

## 2.7 Escaping special character

Backslash `\` is used in regular expression to escape the next character. This
allows us to specify a symbol as a matching character including reserved
characters `{ } [ ] / \ + * . $ ^ | ?`. To use a special character as a matching
character prepend `\` before it.

For example, the regular expression `.` is used to match any character except
newline. Now to match `.` in an input string the regular expression
`(f|c|m)at\.?` means: lowercase letter `f`, `c` or `m`, followed by lowercase
character `a`, followed by lowercase letter `t`, followed by optional `.`
character.

<pre>
"(f|c|m)at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Test the regular expression](https://regex101.com/r/DOc5Nu/1)

## 2.8 Anchors

In regular expressions, we use anchors to check if the matching symbol is the
starting symbol or ending symbol of the input string. Anchors are of two types:
First type is Caret `^` that check if the matching character is the start
character of the input and the second type is Dollar `$` that checks if matching
character is the last character of the input string.

### 2.8.1 Caret

Caret `^` symbol is used to check if matching character is the first character
of the input string. If we apply the following regular expression `^a` (if a is
the starting symbol) to input string `abc` it matches `a`. But if we apply
regular expression `^b` on above input string it does not match anything.
Because in input string `abc` "b" is not the starting symbol. Let's take a look
at another regular expression `^(T|t)he` which means: uppercase character `T` or
lowercase character `t` is the start symbol of the input string, followed by
lowercase character `h`, followed by lowercase character `e`.

<pre>
"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Test the regular expression](https://regex101.com/r/5ljjgB/1)

<pre>
"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Test the regular expression](https://regex101.com/r/jXrKne/1)

### 2.8.2 Dollar

Dollar `$` symbol is used to check if matching character is the last character
of the input string. For example, regular expression `(at\.)$` means: a
lowercase character `a`, followed by lowercase character `t`, followed by a `.`
character and the matcher must be end of the string.

<pre>
"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Test the regular expression](https://regex101.com/r/y4Au4D/1)

<pre>
"(at\.)$" => The fat cat. sat. on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Test the regular expression](https://regex101.com/r/t0AkOd/1)

##  3. Shorthand Character Sets

Regular expression provides shorthands for the commonly used character sets,
which offer convenient shorthands for commonly used regular expressions. The
shorthand character sets are as follows:

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

Lookbehind and lookahead sometimes known as lookaround are specific type of
***non-capturing group*** (Use to match the pattern but not included in matching
list). Lookaheads are used when we have the condition that this pattern is
preceded or followed by another certain pattern. For example, we want to get all
numbers that are preceded by `$` character from the following input string
`$4.44 and $10.88`. We will use following regular expression `(?<=\$)[0-9\.]*`
which means: get all the numbers which contain `.` character and  are preceded
by `$` character. Following are the lookarounds that are used in regular
expressions:

|Symbol|Description|
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
`[T|t]he(?=\sfat)` means: optionally match lowercase letter `t` or uppercase
letter `T`, followed by letter `h`, followed by letter `e`. In parentheses we
define positive lookahead which tells regular expression engine to match `The`
or `the` which are followed by the word `fat`.

<pre>
"[T|t]he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Test the regular expression](https://regex101.com/r/IDDARt/1)

### 4.2 Negative Lookahead

Negative lookahead is used when we need to get all matches from input string
that are not followed by a pattern. Negative lookahead defined same as we define
positive lookahead but the only difference is instead of equal `=` character we
use negation `!` character i.e. `(?!...)`. Let's take a look at the following
regular expression `[T|t]he(?!\sfat)` which means: get all `The` or `the` words
from input string that are not followed by the word `fat` precedes by a space
character.

<pre>
"[T|t]he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Test the regular expression](https://regex101.com/r/V32Npg/1)

### 4.3 Positive Lookbehind

Positive lookbehind is used to get all the matches that are preceded by a
specific pattern. Positive lookbehind is denoted by `(?<=...)`. For example, the
regular expression `(?<=[T|t]he\s)(fat|mat)` means: get all `fat` or `mat` words
from input string that are after the word `The` or `the`.

<pre>
"(?<=[T|t]he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Test the regular expression](https://regex101.com/r/avH165/1)

### 4.4 Negative Lookbehind

Negative lookbehind is used to get all the matches that are not preceded by a
specific pattern. Negative lookbehind is denoted by `(?<!...)`. For example, the
regular expression `(?<!(T|t)he\s)(cat)` means: get all `cat` words from input
string that are not after the word `The` or `the`.

<pre>
"(?&lt;![T|t]he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

[Test the regular expression](https://regex101.com/r/8Efx5G/1)

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

[Test the regular expression](https://regex101.com/r/dpQyf9/1)

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Test the regular expression](https://regex101.com/r/ahfiuh/1)

### 5.2 Global search

The `g` modifier is used to perform a global match (find all matches rather than
stopping after the first match). For example, the regular expression`/.(at)/g`
means: any character except new line, followed by lowercase character `a`,
followed by lowercase character `t`. Because we provided `g` flag at the end of
the regular expression now it will find every matches from whole input string.

<pre>
"/.(at)/" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

[Test the regular expression](https://regex101.com/r/jnk6gM/1)

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Test the regular expression](https://regex101.com/r/dO1nef/1)

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

[Test the regular expression](https://regex101.com/r/hoGMkP/1)

<pre>
"/.at(.)?$/gm" => The <a href="#learn-regex"><strong>fat</strong></a>
                  cat <a href="#learn-regex"><strong>sat</strong></a>
                  on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Test the regular expression](https://regex101.com/r/E88WE2/1)

## Contribution

* Report issues
* Open pull request with improvements
* Spread the word
* Reach out to me directly at ziishaned@gmail.com or [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/ziishaned.svg?style=social&label=Follow%20%40ziishaned)](https://twitter.com/ziishaned)

## License

MIT © [Zeeshan Ahmed](mailto:ziishaned@gmail.com)
