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
"cat" => The <strong><u>cat</u></strong> sat on the mat
</pre>

The regular expression `123` matches the string "123". The regular expression is matched against an input string by comparing each 
character in the regular expression to each character in the input string, one after another. Regular expressions are normally
case-sensitive so the regular expression `Cat` would not match the string "cat".

<pre>
"Cat" => The cat sat on the <strong><u>Cat</u></strong>
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
|{n}|Braces. Matches “n” repetitions of the preceding symbol.|
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
".ar" => The <strong><u>car</u></strong> <strong><u>par</u></strong>ked in the <strong><u>gar</u></strong>age.
</pre>

## 2.2 Character set

Character sets are also called character class. Square brackets are used to specify character sets. Use hyphen inside character set to 
specify the characters range. The order of the character range inside square brackets doesn't matter. For example the regular 
expression `[Tt]he` means: an uppercase `T` or lowercase `t`, followed by the letter `h`, followed by the letter `e`.

<pre>
"[Tt]he" => <strong><u>The</u></strong> car parked in <strong><u>the</u></strong> garage.
</pre>

Just like above example the regular expression `ar[.]` means: an lowercase character `a`, followed by letter `r`, followed by any character.

<pre>
"ar[.]" => The car p<strong><u>ark</u></strong>ed in the g<strong><u>ara</u></strong>ge.
</pre>

### 2.2.1 Negated character set

In general the caret symbol represents the start of the string, but when it is typed after the opening square bracket it negates the 
character set. For example the regular expression `[^c]ar` means: any character except `c`, followed by the character `a`, followed by 
the letter `r`.

<pre>
"[^c]ar" => The car <strong><u>par</u></strong>ked in the <strong><u>gar</u></strong>age.
</pre>


## 2.3 Repetitions

Following meta characters `+`, `*` or `?` are used to specify how many times a subpattern can occurs. These meta characters act 
differently in different situations. 

### 2.3.1 The Star

The symbol `*` matches zero or more repetitions of the preceding matcher. The regular expression `a*` means: zero or more repetitions 
of preceding lowercase character `a`. But if it apperas after a character set or class that it finds the repetitions of the whole 
character set. For example the regular expression `[a-z]*` means: any number of lowercase letters in a row.

<pre>
"[a-z]*" => <strong><u>The</u></strong> <strong><u>car</u></strong> <strong><u>parked</u></strong> <strong><u>in</u></strong> <strong><u>the</u></strong> <strong><u>garage</u></strong> #21.
</pre>

The `*` symbol can be used with the meta character `.` to match any string of characters `.*`. The `*` symbol can be used with the 
whitespace character `\s` to match a string of whitespace characters. For example the expression `\s*cat\s*` means: zero or more 
spaces, followed by lowercase character `c`, followed by lowercase character `a`, followed by lowercase character `t`, followed by 
zero or more spaces.

<pre>
"\s*cat\s*" => The fat<strong><u> cat </u></strong>sat on the <strong><u>cat</u></strong>.
</pre>

### 2.3.2 The Plus

The symbol `+` matches one or more repetitions of the preceding character. For example the regular expression `c.+t` means: lowercase 
letter `c`, followed by any number of character, followed by the lowercase character `t`.

<pre>
"c.+t" => The fat <strong><u>cat sat on the mat</u></strong>.
</pre>

### 2.3.3 The Question Mark

In regular expression the meta character `?` makes the preceding character optional. This symbol matches zero or more repetitions of 
the preceding character. For example the regular expression `[T]?he` means: Optional the uppercase letter `T`, followed by the lowercase 
character `h`, followed by the lowercase character `e`.

<pre>
"[T]he" => <strong><u>The</u></strong> car is parked in the garage.
</pre>
<pre>
"[T]?he" => <strong><u>The</u></strong> car is parked in t<strong><u>he</u></strong> garage.
</pre>

