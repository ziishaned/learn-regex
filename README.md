## What is Regular Expression?

> Regular expression is a group of characters or symbols which is used to find a specific pattern from a text. 

A regular expression is a pattern that is matched against a subject string from left to right. The word "Regular expression" is a 
mouthful, you will usually find the term abbreviated as "regex" or "regexp". Regular expression is used for replacing a text withing 
a string, validating form, extract a substring from a string based upon a pattern match, and so much more.

Imagine you are writing an application and you want to set the rules when user chosing their username. We want the username can 
contains letter, number, underscore and hyphen. We also want to limit the number of characters in username so it does not look ugly. 
We use the following regular expression to validate a username:

<p align="center">
<img src="https://i.imgur.com/UrDb9qc.png" alt="Regular expression">
</p>

Above regular expression can accepts the strings "john_doe", "jo-hn\_doe" and "john12\_as". It does not match "Jo" because that string 
contains uppercase letter and also it is too short.  

## Table of Contents 

- [Basic Matchers]()
- [Meta character]()
  - [Full stop]()
  - [Character set]()
    - [Negated character set]()
  - [Repetitions]()
    - [The Star]()
    - [The Plus]()
    - [The Question Mark]()
  - [Character Group]()
  - [Alternation]()
  - [Escaping special character]()
  - [Anchors]()
    - [Caret]()
    - [Dolar]()
- [Shorthand Character Sets]()
- [Lookaheads]()
- [Flags]()
  - [Case Insensitive]()
  - [Global search]()
  - [Multiline]()

## 1. Basic Matchers

A regular expression is just a pattern of letters and digits that we used to search in a text.  For example the regular expression 
`cat` means: the letter `c`, followed by the letter `a`, followed by the letter `t`. 

<pre>
"cat" => The <a href="#learn-regex"><strong>cat</strong></a> sat on the mat
</pre>

The regular expression `123` matches the string "123". The regular expression is matched against an input string by comparing each 
character in the regular expression to each character in the input string, one after another. Regular expressions are normally
case-sensitive so the regular expression `Cat` would not match the string "cat".

<pre>
"Cat" => The cat sat on the <a href="#learn-regex"><strong>Cat</strong></a>
</pre>

## 2. Meta Characters

Meta characters are the building blocks of the regular expressions.  Meta characters do not stand for themselves but instead are 
interpreted in some special way. Some meta characters have a special meaning that are written inside the square brackets. 
The meta character are as follows:

|Meta character|Description|
|:----:|----|
|.|Period matches any single character except a line break.|
|[ ]|Character class. Matches any character contained between the square brackets.|
|[^ ]|Negated character class. Matches any character that is not contained between the square brackets|
|*|Matches 0 or more repetitions of the preceding symbol.|
|+|Matches 1 or more repetitions of the preceding symbol.
|?|Makes the preceding symbol optional.|
|{n,m}|Braces. Matches at least "n" but not more than "m" repetitions of the preceding symbol.|
|(xyz)|Character group. Matches the characters xyz in that exact order.|
|&#124;|Alternation. Matches either the characters before or the characters after the symbol.|
|&#92;|Escapes the next character. This allows you to match reserved characters <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>|
|^|Matches the beginning of the input.|
|$|Matches the end of the input.|

## 2.1 Full stop

Full stop `.` is the simplest example of meta character. The meta character `.` matches any single character. It will not match return 
or new line characters. For example the regular expression `.ar` means: any character, followed by the letter `a`, followed by the 
letter `r`.

<pre>
".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

## 2.2 Character set

Character sets are also called character class. Square brackets are used to specify character sets. Use hyphen inside character set to 
specify the characters range. The order of the character range inside square brackets doesn't matter. For example the regular 
expression `[Tt]he` means: an uppercase `T` or lowercase `t`, followed by the letter `h`, followed by the letter `e`.

<pre>
"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

Just like above example the regular expression `ar[.]` means: an lowercase character `a`, followed by letter `r`, followed by any character.

<pre>
"ar[.]" => The car p<a href="#learn-regex"><strong>ark</strong></a>ed in the g<a href="#learn-regex"><strong>ara</strong></a>ge.
</pre>

### 2.2.1 Negated character set

In general the caret symbol represents the start of the string, but when it is typed after the opening square bracket it negates the 
character set. For example the regular expression `[^c]ar` means: any character except `c`, followed by the character `a`, followed by 
the letter `r`.

<pre>
"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>


## 2.3 Repetitions

Following meta characters `+`, `*` or `?` are used to specify how many times a subpattern can occurs. These meta characters act 
differently in different situations. 

### 2.3.1 The Star

The symbol `*` matches zero or more repetitions of the preceding matcher. The regular expression `a*` means: zero or more repetitions 
of preceding lowercase character `a`. But if it apperas after a character set or class that it finds the repetitions of the whole 
character set. For example the regular expression `[a-z]*` means: any number of lowercase letters in a row.

<pre>
"[a-z]*" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.
</pre>

The `*` symbol can be used with the meta character `.` to match any string of characters `.*`. The `*` symbol can be used with the 
whitespace character `\s` to match a string of whitespace characters. For example the expression `\s*cat\s*` means: zero or more 
spaces, followed by lowercase character `c`, followed by lowercase character `a`, followed by lowercase character `t`, followed by 
zero or more spaces.

<pre>
"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

### 2.3.2 The Plus

The symbol `+` matches one or more repetitions of the preceding character. For example the regular expression `c.+t` means: lowercase 
letter `c`, followed by any number of character, followed by the lowercase character `t`.

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

### 2.3.3 The Question Mark

In regular expression the meta character `?` makes the preceding character optional. This symbol matches zero or more repetitions of 
the preceding character. For example the regular expression `[T]?he` means: Optional the uppercase letter `T`, followed by the lowercase 
character `h`, followed by the lowercase character `e`.

<pre>
"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>
<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

## 2.4 Braces

In  regular expression braces that are also called quantifiers used to specify the number of times that a group of character or a 
character can be repeated. For example the regular expression `[0-9]{2,3}` means: Match at least 2 digits but not more than 3 (
characters in the range of 0 to 9).

<pre>
"[0-9]{2}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

We can leave out the second number. For example the regular expression `[0-9]{2,}` means: Match 2 or more digits. If we also remove 
the comma the regular expression `[0-9]{2}` means: Match exactly 2 digits.

<pre>
"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

<pre>
"[0-9]{2}" => The number was 9.<a href="#learn-regex"><strong>99</strong></a><a href="#learn-regex"><strong>97</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

## 2.4 Character Group

Character group is a group of sub-pattern that is written inside Parentheses `(...)`. As we discussed before that in regular expression 
if we put quantifier after character than it will repeats the preceding character. But if we put quantifier after a character group than 
it repeats the whole character group. For example the regular expression `(ab)*` matches zero or more repetitions of the character "ab".
We can also use the alternation `|` meta character inside character group. For example the regular expression `(c|g|p)ar` means: lowercase character `c`, 
`g` or `p`, followed by character `a`, followed by character `r`.

<pre>
"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

## 2.5 Alternation

In regular expression Vertical bar `|` is used to define alternation. Alternation is like a condition between multiple expressions. Now, 
you maybe thinking that character set and alternation works the same way. But the big difference between character set and alternation 
is that character set works on character level but alternation works on expression level. For example the regular expression 
`[T|t]he|car` means: uppercase character `T` or lowercase `t`, followed by lowercase character `h`, followed by lowercase character `e` 
or lowercase character `c`, followed by lowercase character `a`, followed by lowercase character `r`.

<pre>
"[T|t]he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

## 2.6 Escaping special character

Backslash `\` is used in regular expression to escape the next character. This allows to to specify a symbol as a matching character 
including reserved characters `{ } [ ] / \ + * . $ ^ | ?`. To use a special character as a matching character prepend `\` before it. 
For example the regular expression `.` is used to match any character except new line. Now to match `.` in an input string the regular
expression `[f|c|m]at\.?` means: lowercase letter `f`, `c` or `m`, followed by lowercase character `a`, followed by lowercase letter 
`t`, followed by optional `.` character.

<pre>
"[f|c|m]at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

## 2.7 Anchors

In regular expression to check if the matching symbol is the starting symbol or endnig symbol of the input string for this purpose
we use anchors. Anchors are of two types: First type is Caret `^` that check if the matching character is the start character of the 
input and the second type is Dolar `$` that checks if matching character is the last character of the input string.

### 2.7.1 Caret

Caret `^` symbol is use to check if matching character is the first character of the input string. If we apply the following regular 
expression `^a` (if a is the starting symbol) to input string `abc` it matches `a`. But if we apply regular expression `^b` on above 
input string it does not match anything. Beacause in input string `abc` "b" is not the starting symbol. Lets take a look on another 
regular expression `^[T|t]he` which means: uppercase character `T` or lowercase character `t` is the start symbol of the input string, 
followed by lowercase character `h`, followed by lowercase character `e`.

<pre>
"[T|t]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

<pre>
"^[T|t]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

### 2.7.2 Dolar

Dolar `$` symbol is use to check if matching character is the last character of the input string. For example regular expression 
`(at.)$` means: lowercase character `a`, followed by lowercase character `t`, followed by anything except new line and the matcher 
must be end of the string.

<pre>
"(at.)" => The f<a href="#learn-regex"><strong>at </strong></a>c<a href="#learn-regex"><strong>at </strong></a>s<a href="#learn-regex"><strong>at </strong></a>on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

<pre>
"(at.)$" => The fat cat sat on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

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
pattern. For example we want to get all numbers that are preceded by `$` character from the following input string `$4.44 and $10.88`. 
We will use following regular expression `(?<=\$)[0-9\.]*` which means: get all the numbers which contains `.` character and preceded 
by `$` character. Following are the lookarounds that are used in regular expressions:

|Symbol|Description|
|:----:|----|
|?=|Positive Lookahead|
|?!|Negative Lookahead|
|?<=|Positive Lookbehind|
|?<!|Negative Lookbehind|

### 4.1 Positive Lookahead

The positive lookahead asserts that the first part of the expression must be followed by the lookahead expression. The returned match
only contains the text that is matched by the first part of the expression. To define a positive lookahead braces are used and within 
those braces question mark with equal sign is used like this `(?=...)`. Lookahead expression is written after the equal sign inside 
braces. For example the regular expression `[T|t]he(?=\sfat)` means: optionally match lowercase letter `t` or uppercase letter `T`, 
followed by letter `h`, followed by letter `e`. In braces we define positive lookahead which tells regular expression engine to match
`The` or `the` which are followed by the word `fat`. 

<pre>
"[T|t]he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

### 4.2 Negative Lookahead

Negative lookahead is used when we need to get all matches from input string that are not followed by a pattern. Negative lookahead 
defined same as we define positive lookahead but the only difference is instead of equal `=` character we use negation `!` character 
i.e. `(?!...)`. Lets take a look at the following regular expression `[T|t]he(?!\sfat)` which means: get all `The` or `the` words from 
input string that are not followed by the word `fat` precedes by a space character.

<pre>
"[T|t]he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

### 4.3 Positive Lookbehind

Positive lookbehind is used to get all the matches that are preceded by a specific pattern. Positive lookbehind is denoted by 
`(?<=...)`. For example the regular expression `(?<=[T|t]he\s)(fat|mat)` means: get all `fat` or `mat` words from input string that 
are after the word `The` or `the`.

<pre>
"(?<=[T|t]he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

### 4.4 Negative Lookbehind

Negative lookbehind is used to get all the matches that are not preceded by a specific pattern. Negative lookbehind is denoted by 
`(?<!...)`. For example the regular expression `(?&lt;![T|t]he\s)(cat)` means: get all `cat` words from input string that 
are after not after the word `The` or `the`.

<pre>
"(?&lt;![T|t]he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

## 5. Flags

Flags are also called modifiers beacause they modifies the output of a regular expression. These flags can be used in any order or 
combination, and are an integral part of the RegExp.

|Flag|Description|
|:----:|----|
|i|Case insensitive: Sets matching to be case-insensitive.|
|g|Global Search: Search for a pattern throughout the input string.|
|m|Multiline: Anchor meta character works on each line.|

### 5.1 Case Insensitive

The `i` modifier is used to perform case-insensitive matching. For example the regular expression `/The/gi` means: uppercase letter 
`T`, followed by lowercase character `h`, followed by character `e`. And at the end of regular expression the `i` flag tells the 
regular expression engine to ignore the case. As you can see we also provided `g` flag beacause we want to search for the pattern in 
the whole input string.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

### 5.2 Global search


The `g` modifier is used to perform a global match (find all matches rather than stopping after the first match). For example the 
regular expression`/.(at)/g` means: any character except new line, followed by lowercase character `a`, followed by lowercase 
character `t`. Beacause we provided `g` flag at the end of the regular expression now it will find every matches from whole input 
string.



<pre>
".(at)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

### 5.3 Multiline

The `m` modifier is used to perform a multiline match. As we discussed earlier anchors `(^, $)` are used to check if pattern is 
the beginning of the input or end fo the input string. But if we want that anchors works on each line we use `m` flag. For example the
regular expression `/at(.)?$/gm` means: lowercase character `a`, followed by lowercase character `t`, optionally anything except new 
line. And beacause of `m` flag now regular expression engine matches pattern at the end of each line in a string.

<pre>
"/.at(.)?$/" => The fat
                cat sat
                on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

<pre>
"/.at(.)?$/gm" => The <a href="#learn-regex"><strong>fat</strong></a>
                  cat <a href="#learn-regex"><strong>sat</strong></a>
                  on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

## Contribution

* Report issues
* Open pull request with improvements
* Spread the word 
* Reach out to me directly at ziishaned@gmail.com or [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/ziishaned.svg?style=social&label=Follow%20%40ziishaned)](https://twitter.com/ziishaned)

## License

MIT © [Zeeshan Ahmed](mailto:ziishaned@gmail.com)