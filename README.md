# What is Regular Expression?

Regular expression is a group of character or symbols which is used to find a specific pattern from a text. 
The word "Regular expression" is a mouthful, you will usually find the term abbreviated as "regex" or 
"regexp". Regular expression is used for replacing a text withing a string, validating form, extract a substring 
from a string based upon a pattern match, and so much more.

# Table of Contents 

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


A regular expression is just a pattern of letters and digits that we used to search in a text.  For example the 
regular expression `cat` means: the letter `c`, followed by the letter `a`, followed by the letter `t`. 

<pre>
"cat" => The <strong><u>cat</u></strong> sat on the mat
</pre>

The regular expression `123` matches the string "123". The regular expression is matched against an input string 
by comparing each character in the regular expression to each character in the input string, one after another. 
Regular expressions are normally case-sensitive so the regular expression `Cat` would not match the string "cat".

<pre>
"Cat" => The cat sat on the <strong><u>Cat</u></strong>
</pre>

## 2. Meta Characters

Meta characters are the building blocks of the regular expressions. Some meta characters have a special meaning 
that are written inside the square brackets. The meta character are as follows:

|Meta character|Description|
|:----:|----|
|<b>.</b>|Period matches any single character except a line break.|
|<b>[ ]</b>|Character class. Matches any character contained between the square brackets.|
|<b>[^ ]</b>|Negated character class. Matches any character that is not contained between the square brackets|
|<b>*</b>|Matches 0 or more repetitions of the preceding symbol.|
|<b>+</b>|Matches 1 or more repetitions of the preceding symbol.
|<b>?</b>|Makes the preceding symbol optional.|
|<b>{n}</b>|Braces. Matches “n” repetitions of the preceding symbol.|
|<b>(xyz)</b>|Character group. Matches the characters xyz in that exact order.|
|<b>&#124;</b>|Alternation. Matches either the characters before or the characters after the symbol.|
|<b>&#92;</b>|Escapes the next character. This allows you to match reserved characters <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>|
|<b>^</b>|Matches the beginning of the input.|
|<b>$</b>|Matches the end of the input.|

## 2.1 Full stop

Full stop `.` is the simplest example of meta character. The meta character `.` matches any single character. It 
will not match return or new line characters. For example the regular expression `.ar` means: any character, 
followed by the letter `a`, followed by the letter `r`.

<pre>
".ar" => The <strong><u>car</u></strong> <strong><u>par</u></strong>ked in the <strong><u>gar</u></strong>age.
</pre>

## 2.2 Character set

Character sets are also called character class. Square brackets are used to specify character sets. Use hyphen 
inside character set to specify the characters range. The order of the character range inside square brackets 
doesn't matter. For example the regular expression `[Tt]he` means: an uppercase `T` or lowercase `t`, followed by 
the letter `h`, followed by the letter `e`.

<pre>
"[Tt]he" => <strong><u>The</u></strong> car parked in <strong><u>the</u></strong> garage.
</pre>

### 2.2.1 Negated character set

In general the caret symbol represents the start of the string, but when it is typed after the opening square 
bracket it negates the character set. For example the regular expression `[^c]ar` means: any character except 
`c`, followed by the character `a`, followed by the letter `r`.

<pre>
"[^c]ar" => The car <strong><u>par</u></strong>ked in the <strong><u>gar</u></strong>age.
</pre>


### 2.2.2 Repeating character set

We can repeat a character class by using `+`, `*` or `?` operators. For example the regular expression `[a-z]+` 
means: any number of lowercase letters in a row.

<pre>
"[a-z]+" => <strong><u>The</u></strong> <strong><u>car</u></strong> <strong><u>parked</u></strong> <strong><u>in</u></strong> <strong><u>the</u></strong> <strong><u>garage</u></strong>.
</pre>