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

1. [Basic Matchers]()
2. [Meta character]()
3. [Quantifiers]()
4. [OR operator]()
5. [Character Sets]()
6. [Shorthand Character Sets]()
7. [Grouping]()
8. [Lookaheads]()
9. [Flags]()

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