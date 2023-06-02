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

## Translations:

* [English](../README.md)
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
* [עברית](translations/README-he.md)

## 什么是正则表达式?

[![](https://img.shields.io/badge/-Download%20PDF%20-0a0a0a.svg?style=flat&colorA=0a0a0a)](https://gum.co/learn-regex)

> 正则表达式是一组由字母和符号组成的特殊文本, 它可以用来从文本中找出满足你想要的格式的句子.


一个正则表达式是在一个主体字符串中从左到右匹配字符串时的一种样式.
例如"Regular expression"是一个完整的句子, 但我们常使用缩写的术语"regex"或"regexp".
正则表达式可以用来替换文本中的字符串,验证形式,提取字符串等等.

想象你正在写一个应用, 然后你想设定一个用户命名的规则, 让用户名包含字符,数字,下划线和连字符,以及限制字符的个数,好让名字看起来没那么丑.
我们使用以下正则表达式来验证一个用户名:

<br/><br/>
<p align="center">
  <img src="../img/regexp-cn.png" alt="Regular expression">
</p>

以上的正则表达式可以接受 `john_doe`, `jo-hn_doe`, `john12_as`.
但不匹配`Jo`, 因为它包含了大写的字母而且太短了.

目录
=================

 * [1. 基本匹配](#1-基本匹配)
 * [2. 元字符](#2-元字符)
 	* [2.1 点运算符 .](#21-点运算符-)
 	* [2.2 字符集](#22-字符集)
		* [2.2.1 否定字符集](#221-否定字符集)
	* [2.3 重复次数](#23-重复次数)
		* [2.3.1 * 号](#231--号)
		* [2.3.2   号](#232--号)
		* [2.3.3 ? 号](#233--号)
	* [2.4 {} 号](#24--号)
	* [2.5 (...) 特征标群](#25--特征标群)
	* [2.6 | 或运算符](#26--或运算符)
	* [2.7 转码特殊字符](#27-转码特殊字符)
	* [2.8 锚点](#28-锚点)
		* [2.8.1 ^ 号](#281--号)
		* [2.8.2 $ 号](#282--号)
* [3. 简写字符集](#3-简写字符集)
* [4. 前后关联约束(前后预查)](#4-前后关联约束前后预查)
	* [4.1 ?=... 前置约束(存在)](#41--前置约束存在)
	* [4.2 ?!... 前置约束-排除](#42--前置约束-排除)
	* [4.3 ?&lt;= ... 后置约束-存在](#43---后置约束-存在)
	* [4.4 ?&lt;!... 后置约束-排除](#44--后置约束-排除)
* [5. 标志](#5-标志)
	* [5.1 忽略大小写 (Case Insensitive)](#51-忽略大小写-case-insensitive)
	* [5.2 全局搜索 (Global search)](#52-全局搜索-global-search)
	* [5.3 多行修饰符 (Multiline)](#53-多行修饰符-multiline)
* [额外补充](#额外补充)
* [贡献](#贡献)
* [许可证](#许可证)

## 1. 基本匹配

正则表达式其实就是在执行搜索时的格式, 它由一些字母和数字组合而成.
例如: 一个正则表达式 `the`, 它表示一个规则: 由字母`t`开始,接着是`h`,再接着是`e`.

<pre>
"the" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat. 
</pre>

[在线练习](https://regex101.com/r/dmRygT/1)

正则表达式`123`匹配字符串`123`. 它逐个字符的与输入的正则表达式做比较.

正则表达式是大小写敏感的, 所以`The`不会匹配`the`.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[在线练习](https://regex101.com/r/1paXsy/1)

## 2. 元字符

正则表达式主要依赖于元字符.  
元字符不代表他们本身的字面意思, 他们都有特殊的含义. 一些元字符写在方括号中的时候有一些特殊的意思. 以下是一些元字符的介绍:

|元字符|描述|
|:----:|----|
|.|句号匹配任意单个字符除了换行符.|
|[ ]|字符种类. 匹配方括号内的任意字符.|
|[^ ]|否定的字符种类. 匹配除了方括号里的任意字符|
|*|匹配>=0个重复的在*号之前的字符.|
|+|匹配>1个重复的+号前的字符.
|?|标记?之前的字符为可选.|
|{n,m}|匹配num个中括号之前的字符 (n <= num <= m).|
|(xyz)|字符集, 匹配与 xyz 完全相等的字符串.|
|&#124;|或运算符,匹配符号前或后的字符.|
|&#92;|转义字符,用于匹配一些保留的字符 <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>|
|^|从开始行开始匹配.|
|$|从末端开始匹配.|

## 2.1 点运算符 `.`

`.`是元字符中最简单的例子. 
`.`匹配任意单个字符, 但不匹配换行符.
例如, 表达式`.ar`匹配一个任意字符后面跟着是`a`和`r`的字符串.

<pre>
".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[在线练习](https://regex101.com/r/xc9GkU/1)

## 2.2 字符集

字符集也叫做字符类.
方括号用来指定一个字符集.
在方括号中使用连字符来指定字符集的范围.
在方括号中的字符集不关心顺序.
例如, 表达式`[Tt]he` 匹配 `the` 和 `The`.

<pre>
"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[在线练习](https://regex101.com/r/2ITLQ4/1)

方括号的句号就表示句号.
表达式 `ar[.]` 匹配 `ar.`字符串

<pre>
"ar[.]" => A garage is a good place to park a c<a href="#learn-regex"><strong>ar.</strong></a>
</pre>

[在线练习](https://regex101.com/r/wL3xtE/1)

### 2.2.1 否定字符集

一般来说 `^` 表示一个字符串的开头, 但它用在一个方括号的开头的时候, 它表示这个字符集是否定的.
例如, 表达式`[^c]ar` 匹配一个后面跟着`ar`的除了`c`的任意字符.

<pre>
"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[在线练习](https://regex101.com/r/nNNlq3/1)

## 2.3 重复次数

后面跟着元字符 `+`, `*` or `?` 的, 用来指定匹配子模式的次数. 
这些元字符在不同的情况下有着不同的意思.

### 2.3.1 `*` 号

`*`号匹配 在`*`之前的字符出现`大于等于0`次.
例如, 表达式 `a*` 匹配以0或更多个a开头的字符, 因为有0个这个条件, 其实也就匹配了所有的字符. 表达式`[a-z]*` 匹配一个行中所有以小写字母开头的字符串.

<pre>
"[a-z]*" => T<a href="#learn-regex"><strong>he</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.
</pre>

[在线练习](https://regex101.com/r/7m8me5/1)

`*`字符和`.`字符搭配可以匹配所有的字符`.*`.
`*`和表示匹配空格的符号`\s`连起来用, 如表达式`\s*cat\s*`匹配0或更多个空格开头和0或更多个空格结尾的cat字符串.

<pre>
"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the <a href="#learn-regex">con<strong>cat</strong>enation</a>.
</pre>

[在线练习](https://regex101.com/r/gGrwuz/1)

### 2.3.2 `+` 号

`+`号匹配`+`号之前的字符出现 >=1 次个字符.
例如表达式`c.+t` 匹配以首字母`c`开头以`t`结尾,中间跟着任意个字符的字符串.

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

[在线练习](https://regex101.com/r/Dzf9Aa/1)

### 2.3.3 `?` 号

在正则表达式中元字符 `?` 标记在符号前面的字符为可选, 即出现 0 或 1 次.
例如, 表达式 `[T]?he` 匹配字符串 `he` 和 `The`.

<pre>
"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[在线练习](https://regex101.com/r/cIg9zm/1)

<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

[在线练习](https://regex101.com/r/kPpO2x/1)

## 2.4 `{}` 号

在正则表达式中 `{}` 是一个量词, 常用来一个或一组字符可以重复出现的次数.
例如,  表达式 `[0-9]{2,3}` 匹配 2~3 位 0~9 的数字.


<pre>
"[0-9]{2,3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[在线练习](https://regex101.com/r/juM86s/1)

我们可以省略第二个参数.
例如, `[0-9]{2,}` 匹配至少两位 0~9 的数字.

如果逗号也省略掉则表示重复固定的次数. 
例如, `[0-9]{3}` 匹配3位数字

<pre>
"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[在线练习](https://regex101.com/r/Gdy4w5/1)

<pre>
"[0-9]{3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to 10.0.
</pre>

[在线练习](https://regex101.com/r/Sivu30/1)

## 2.5 `(...)` 特征标群

特征标群是一组写在 `(...)` 中的子模式. 例如之前说的 `{}` 是用来表示前面一个字符出现指定次数. 但如果在 `{}` 前加入特征标群则表示整个标群内的字符重复 N 次. 例如, 表达式 `(ab)*` 匹配连续出现 0 或更多个 `ab`.

我们还可以在 `()` 中用或字符 `|` 表示或. 例如, `(c|g|p)ar` 匹配 `car` 或 `gar` 或 `par`.

<pre>
"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[在线练习](https://regex101.com/r/tUxrBG/1)

## 2.6 `|` 或运算符

或运算符就表示或, 用作判断条件.

例如 `(T|t)he|car` 匹配 `(T|t)he` 或 `car`.

<pre>
"(T|t)he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[在线练习](https://regex101.com/r/fBXyX0/1)

## 2.7 转码特殊字符

反斜线 `\` 在表达式中用于转码紧跟其后的字符. 用于指定 `{ } [ ] / \ + * . $ ^ | ?` 这些特殊字符. 如果想要匹配这些特殊字符则要在其前面加上反斜线 `\`.

例如 `.` 是用来匹配除换行符外的所有字符的. 如果想要匹配句子中的 `.` 则要写成 `\.`.

<pre>
"(f|c|m)at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[在线练习](https://regex101.com/r/DOc5Nu/1)

## 2.8 锚点

在正则表达式中, 想要匹配指定开头或结尾的字符串就要使用到锚点. `^` 指定开头, `$` 指定结尾.

### 2.8.1 `^` 号

`^` 用来检查匹配的字符串是否在所匹配字符串的开头.

例如, 在 `abc` 中使用表达式 `^a` 会得到结果 `a`. 但如果使用 `^b` 将匹配不到任何结果. 因为在字符串 `abc` 中并不是以 `b` 开头.

例如, `^(T|t)he` 匹配以 `The` 或 `the` 开头的字符串.

<pre>
"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[在线练习](https://regex101.com/r/5ljjgB/1)

<pre>
"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[在线练习](https://regex101.com/r/jXrKne/1)

### 2.8.2 `$` 号

同理于 `^` 号, `$` 号用来匹配字符是否是最后一个.

例如, `(at\.)$` 匹配以 `at.` 结尾的字符串.

<pre>
"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[在线练习](https://regex101.com/r/y4Au4D/1)

<pre>
"(at\.)$" => The fat cat. sat. on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[在线练习](https://regex101.com/r/t0AkOd/1)

##  3. 简写字符集

正则表达式提供一些常用的字符集简写. 如下:

|简写|描述|
|:----:|----|
|.|除换行符外的所有字符|
|\w|匹配所有字母数字, 等同于 `[a-zA-Z0-9_]`|
|\W|匹配所有非字母数字, 即符号, 等同于: `[^\w]`|
|\d|匹配数字: `[0-9]`|
|\D|匹配非数字: `[^\d]`|
|\s|匹配所有空格字符, 等同于: `[\t\n\f\r\p{Z}]`|
|\S|匹配所有非空格字符: `[^\s]`|

## 4. 前后关联约束(前后预查)

前置约束和后置约束都属于**非捕获簇**(用于匹配不在匹配列表中的格式).
前置约束用于判断所匹配的格式是否在另一个确定的格式之后.

例如, 我们想要获得所有跟在 `$` 符号后的数字, 我们可以使用正向向后约束 `(?<=\$)[0-9\.]*`.
这个表达式匹配 `$` 开头, 之后跟着 `0,1,2,3,4,5,6,7,8,9,.` 这些字符可以出现大于等于 0 次.

前后关联约束如下:

|符号|描述|
|:----:|----|
|?=|前置约束-存在|
|?!|前置约束-排除|
|?<=|后置约束-存在|
|?<!|后置约束-排除|

### 4.1 `?=...` 前置约束(存在)

`?=...` 前置约束(存在), 表示第一部分表达式必须跟在 `?=...`定义的表达式之后.

返回结果只瞒住第一部分表达式.
定义一个前置约束(存在)要使用 `()`. 在括号内部使用一个问号和等号: `(?=...)`. 

前置约束的内容写在括号中的等号后面.
例如, 表达式 `[T|t]he(?=\sfat)` 匹配 `The` 和 `the`, 在括号中我们又定义了前置约束(存在) `(?=\sfat)` ,即 `The` 和 `the` 后面紧跟着 `(空格)fat`.

<pre>
"[T|t]he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[在线练习](https://regex101.com/r/IDDARt/1)

### 4.2 `?!...` 前置约束-排除

前置约束-排除 `?!` 用于筛选所有匹配结果, 筛选条件为 其后不跟随着定义的格式
`前置约束-排除`  定义和 `前置约束(存在)` 一样, 区别就是 `=` 替换成 `!` 也就是 `(?!...)`. 

表达式 `[T|t]he(?!\sfat)` 匹配 `The` 和 `the`, 且其后不跟着 `(空格)fat`.

<pre>
"[T|t]he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[在线练习](https://regex101.com/r/V32Npg/1)

### 4.3 `?<= ...` 后置约束-存在

后置约束-存在 记作`(?<=...)` 用于筛选所有匹配结果, 筛选条件为 其前跟随着定义的格式.
例如, 表达式 `(?<=[T|t]he\s)(fat|mat)` 匹配 `fat` 和 `mat`, 且其前跟着 `The` 或 `the`.

<pre>
"(?<=[T|t]he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[在线练习](https://regex101.com/r/avH165/1)

### 4.4 `?<!...` 后置约束-排除

后置约束-排除 记作 `(?<!...)` 用于筛选所有匹配结果, 筛选条件为 其前不跟着定义的格式.
例如, 表达式 `(?<!(T|t)he\s)(cat)` 匹配 `cat`, 且其前不跟着 `The` 或 `the`.

<pre>
"(?&lt;![T|t]he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

[在线练习](https://regex101.com/r/8Efx5G/1)

## 5. 标志

标志也叫修饰语, 因为它可以用来修改表达式的搜索结果.
这些标志可以任意的组合使用, 它也是整个正则表达式的一部分.

|标志|描述|
|:----:|----|
|i|忽略大小写.|
|g|全局搜索.|
|m|多行的: 锚点元字符 `^` `$` 工作范围在每行的起始.|

### 5.1 忽略大小写 (Case Insensitive)

修饰语 `i` 用于忽略大小写.
例如, 表达式 `/The/gi` 表示在全局搜索 `The`, 在后面的 `i` 将其条件修改为忽略大小写, 则变成搜索 `the` 和 `The`, `g` 表示全局搜索.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[在线练习](https://regex101.com/r/dpQyf9/1)

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[在线练习](https://regex101.com/r/ahfiuh/1)

### 5.2 全局搜索 (Global search)

修饰符 `g` 常用于执行一个全局搜索匹配, 即(不仅仅返回第一个匹配的, 而是返回全部). 
例如, 表达式 `/.(at)/g` 表示搜索 任意字符(除了换行) + `at`, 并返回全部结果.

<pre>
"/.(at)/" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

[在线练习](https://regex101.com/r/jnk6gM/1)

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[在线练习](https://regex101.com/r/dO1nef/1)

### 5.3 多行修饰符 (Multiline)

多行修饰符 `m` 常用于执行一个多行匹配.

像之前介绍的 `(^,$)` 用于检查格式是否是在待检测字符串的开头或结尾. 但我们如果想要它在每行的开头和结尾生效, 我们需要用到多行修饰符 `m`.

例如, 表达式 `/at(.)?$/gm` 表示在待检测字符串每行的末尾搜索 `at`后跟0个或1个 `.` 的字符串, 并返回全部结果.

<pre>
"/.at(.)?$/" => The fat
                cat sat
                on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[在线练习](https://regex101.com/r/hoGMkP/1)

<pre>
"/.at(.)?$/gm" => The <a href="#learn-regex"><strong>fat</strong></a>
                  cat <a href="#learn-regex"><strong>sat</strong></a>
                  on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[在线练习](https://regex101.com/r/E88WE2/1)

## 额外补充

* *正整数*: `^\d+$`
* *负整数*: `^-\d+$`
* *手机国家号*: `^+?[\d\s]{3,}$`
* *手机号*: `^+?[\d\s]+(?[\d\s]{10,}$`
* *整数*: `^-?\d+$`
* *用户名*: `^[\w\d_.]{4,16}$`
* *数字和英文字母*: `^[a-zA-Z0-9]*$`
* *数字和应为字母和空格*: `^[a-zA-Z0-9 ]*$`
* *密码*: `^(?=^.{6,}$)((?=.*[A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z]))^.*$`
* *邮箱*: `^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})*$`
* *IP4 地址*: `^((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))*$`
* *纯小写字母*: `^([a-z])*$`
* *纯大写字母*: `^([A-Z])*$`
* *URL*: `^(((http|https|ftp):\/\/)?([[a-zA-Z0-9]\-\.])+(\.)([[a-zA-Z0-9]]){2,4}([[a-zA-Z0-9]\/+=%&_\.~?\-]*))*$`
* *VISA 信用卡号*: `^(4[0-9]{12}(?:[0-9]{3})?)*$`
* *日期 (MM/DD/YYYY)*: `^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](19|20)?[0-9]{2}$`
* *日期 (YYYY/MM/DD)*: `^(19|20)?[0-9]{2}[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])$`
* *MasterCard 信用卡号*: `^(5[1-5][0-9]{14})*$`

## 贡献

* 报告问题
* 开放合并请求
* 传播此文档
* 直接和我联系 ziishaned@gmail.com 或 [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/ziishaned.svg?style=social&label=Follow%20%40ziishaned)](https://twitter.com/ziishaned)

## 许可证

MIT &copy; [Zeeshan Ahmad](https://twitter.com/ziishaned)
