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


## 翻訳

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

## 正規表現とは

[![](https://img.shields.io/badge/-Download%20PDF%20-0a0a0a.svg?style=flat&colorA=0a0a0a)](https://gum.co/learn-regex)

> 正規表現とは文中からある文字列のパターンを見つけるために使用される文字列や記号の組み合わせのことです。

正規表現とは対象の文字列に左から右にマッチするパターンのことを言います。
"Regular expression" （正規表現）という言葉は "regex" や "regexp" などと一言で言い表すことがあります。
正規表現を使うことで文字列の置換・検証・抽出などを行うことが可能です。

アプリケーション中において、ユーザがユーザ名を決めるときに
守るべきルールを定義したいとしましょう。
ユーザ名には文字・数字・アンダースコア・ハイフンが使用可能であるとします。
また、ユーザ名が単調にならないように文字数にも制約を設けるものとします。
この場合、次のような正規表現でユーザ名を検証することができます。

<br/><br/>
<p align="center">
  <img src="../img/regexp-en.png" alt="Regular expression">
</p>

この正規表現によって `john_doe, jo-hn_doe, john12_as` などは許容されることになります。
一方で `Jo` は大文字を含む上に短すぎるため許容されません。

## 目次

- [基本的な Matcher](#1-基本的な-matcher)
- [メタ文字](#2-メタ文字)
  - [ピリオド](#21-ピリオド)
  - [文字集合](#22-文字集合)
    - [否定文字集合](#221-否定文字集合)
  - [繰り返し](#23-繰り返し)
    - [アスタリスク](#231-アスタリスク)
    - [プラス記号](#232-プラス記号)
    - [疑問符](#233-疑問符)
  - [括弧](#24-括弧)
  - [文字グループ](#25-文字グループ)
  - [選言](#26-選言)
  - [特殊文字をエスケープする](#27-特殊文字をエスケープする)
  - [アンカー](#28-アンカー)
    - [キャレット](#281-キャレット)
    - [ドル記号](#282-ドル記号)
- [文字集合の短縮表記](#3-文字集合の短縮表記)
- [前後参照](#4-前後参照)
  - [肯定的な先読み](#41-肯定的な先読み)
  - [否定的な先読み](#42-否定的な先読み)
  - [肯定的な後読み](#43-肯定的な後読み)
  - [否定的な後読み](#44-否定的な後読み)
- [フラグ](#5-フラグ)
  - [大文字・小文字を区別しない](#51-大文字・小文字を区別しない)
  - [グローバル検索](#52-グローバル検索)
  - [複数行](#53-複数行)
- [おまけ](#おまけ)

## 1. 基本的な Matcher

文中から特定の文字列を検索する時の正規表現は単なる文字の並びとして表されます。
例えば `the` という正規表現は `t` という文字のあとに `h` が続き、さらに `e` が続くものだと
解釈されます。

<pre>
"the" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/dmRygT/1)

`123` という正規表現は `123` という文字列にマッチします。
正規表現は正規表現の文字列と入力文字列を1文字ずつ比較しながらマッチングを行います。
また大文字と小文字は区別されるため、 `The` は `the` にはマッチしません。

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/1paXsy/1)

## 2. メタ文字

メタ文字は正規表現の構成要素として使用される文字のことです。
メタ文字はそれ自身が示す文字を表すものではなく、特別な解釈がなされます。
一部のメタ文字は角括弧内に記述されることで特別な意味を持つものもあります。
メタ文字には次のようなものがあります。

|メタ文字|説明                                                                                         |
|:------:|---------------------------------------------------------------------------------------------|
|.       |ピリオド。改行を除く任意の1文字にマッチ。                                                    |
|[ ]     |文字集合。角括弧内の任意の文字にマッチ。                                                     |
|[^ ]    |否定文字集合。角括弧内に含まれない任意の文字にマッチ。                                       |
|*       |直前の文字の 0 個以上の並びにマッチ。                                                        |
|+       |直前の文字の 1 個以上の並びにマッチ。                                                        |
|?       |直前の文字がオプションであるとみなす。                                                       |
|{n,m}   |括弧でくくる。直前の文字が n 個以上 m 個以下続く場合にマッチ。                               |
|(xyz)   |文字グループ。 xyz という文字列がその順に現れる場合にマッチ。                                |
|&#124;  |選言。記号の前後の文字列どちらかにマッチ。                                                   |
|&#92;   |次に来る文字をエスケープする。予約語 <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code> にマッチ。|
|^       |入力値の開始にマッチする。                                                                   |
|$       |入力値の終了にマッチする。                                                                   |

## 2.1 ピリオド

ピリオド `.` は最もシンプルなメタ文字の例です。
メタ文字 `.` は任意の 1 文字にマッチします。
キャリッジリターンと改行にはマッチしません。
例えば `.ar` は任意の文字の後に `a` と `r` が続く文字列にマッチします。

<pre>
".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/xc9GkU/1)

## 2.2 文字集合

文字集合は文字クラスとも呼ばれます。
文字集合を指定するには角括弧でくくります。
文字の範囲を指定するにはハイフンを使用します。
角括弧内の文字の記述順はマッチングには関係ありません。
例えば `[Tt]he` という正規表現は大文字 `T` または小文字 `t` の後に `h`, `e` が続く文字列を表します。

<pre>
"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/2ITLQ4/1)

文字集合内でのピリオドは文字としてのピリオドを表します。
`ar[.]` という正規表現は `a` という文字のあとに `r` が続き、さらに `.` という文字が続く文字列を表します。

<pre>
"ar[.]" => A garage is a good place to park a c<a href="#learn-regex"><strong>ar.</strong></a>
</pre>

[正規表現の動作確認をする](https://regex101.com/r/wL3xtE/1)

### 2.2.1 否定文字集合

通常キャレットは文字列の開始を意味するメタ文字ですが、角括弧内で最初に使用されると
文字集合を否定する意味を持つようになります。
例えば `[^c]ar` という正規表現は `c` 以外の任意の文字列の後に
`a`, `r` が続く文字列を表します。

<pre>
"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/nNNlq3/1)

## 2.3 繰り返し

`+`, `*`, `?` はパターンが何回続くのかを指定するためのメタ文字になります。
これらのメタ文字は異なるシチュエーションで異なる振る舞いをします。

### 2.3.1 アスタリスク

シンボル `*` は直前の文字が 0 個以上続くパターンにマッチします。
`a*` という正規表現は小文字の `a` が 0 個以上続くことを意味します。
しかし文字集合またはクラスの後に現れた場合はその文字集合すべてが続くことを意味します。
例えば `[a-z]*` という正規表現は行内の任意の小文字の列を表します。

<pre>
"[a-z]*" => T<a href="#learn-regex"><strong>he</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/7m8me5/1)

シンボル `*` はメタ文字 `.` と合わせて `.*` のように使用することで
任意の文字列を表現できます。
またスペースを表す `\s` と併用することで空白文字を表現できます。
例えば `\s*cat\s*` という正規表現は 0 個以上のスペースの後に
小文字の `c`, `a`, `t` が続き、その後に 0 個以上のスペースが続きます。

<pre>
"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the <a href="#learn-regex">con<strong>cat</strong>enation</a>.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/gGrwuz/1)

### 2.3.2 プラス記号

シンボル `+` は直前の文字が 1 個以上続くパターンにマッチします。
例えば `c.+t` という正規表現は小文字の `c` の後に
任意の 1 文字以上が続き、さらに `t` が続くことを意味します。
この `t` は、その文における最後の `t` がマッチします。

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/Dzf9Aa/1)

### 2.3.3 疑問符

正規表現におけるメタ文字 `?` は直前の文字がオプションであることを意味します。
すなわち直前の文字が 0 個または 1 個現れることを意味します。
例えば `[T]?he` という正規表現は大文字の `T` が 0 個または 1 個出現し、
その後に小文字の `h`, `e` が続くことを意味します。

<pre>
"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/cIg9zm/1)

<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/kPpO2x/1)

## 2.4 括弧
この`t`は、その文における最後の`t`であることが明確である必要があります。

正規表現における括弧は数量子とも呼ばれますが、文字列がいくつ現れるかを示すために使用されます。
例えば、`[0-9]{2,3}` という正規表現は 2 桁以上 3 桁以下の数字
（0 から 9 の数字で表された文字列）にマッチします。

<pre>
"[0-9]{2,3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/juM86s/1)

2つ目の数値は省略できます。
例えば `[0-9]{2,}` という正規表現は 2 桁以上の数字を意味します。
カンマも省略することができ、その場合 `[0-9]{3}` という正規表現はちょうど 3 桁の数字を意味します。

<pre>
"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/Gdy4w5/1)

<pre>
"[0-9]{3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to 10.0.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/Sivu30/1)

## 2.5 文字グループ

文字グループは括弧 `(...)` 内にパターンを記述してグループ分けをするために使用します。
前述の通り、正規表現においては数量子を文字の後に置いた場合は
その直前の文字の繰り返しを意味します。しかし、文字グループの後に数量子を置いた場合は
文字グループ全体が繰り返すことを意味します。
例えば、 `(ab)*` という正規表現は "ab" という文字列の 0 個以上の繰り返しにマッチします。
文字グループ内では選言 `|` も使用することができます。
例えば、`(c|g|p)ar` という正規表現は小文字の `c`, `g`, `p` のいずれかの後に
`a` が続き、さらに `r` が続くことを意味します。

<pre>
"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/tUxrBG/1)

## 2.6 選言

正規表現における縦棒 `|` は選言として使用されます。
選言は複数の正規表現からなる条件式のようなものです。
もしかすると文字集合と選言が同じものと感じるかもしれません。
この 2 つの大きな違いは文字集合は文字単位で評価されるのに対して選言は正規表現単位で評価されます。
例えば `(T|t)he|car` という正規表現は大文字の `T` または小文字の `t` の後に
小文字の `h`, `e` が続くか、または小文字の `c` の後に `a`, `r` が続くことを意味します。

<pre>
"(T|t)he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/fBXyX0/1)

## 2.7 特殊文字をエスケープする

バックスラッシュ `\` は正規表現内で次に来る文字をエスケープするために使用されます。
これを使うと予約語 `{ } [ ] / \ + * . $ ^ | ?` を
記号として指定できるようになります。
例えば `.` という正規表現は改行を除く任意の文字として使用されますが、
`(f|c|m)at\.?` という正規表現では `.` 自体にマッチします。
この正規表現は小文字の `f`, `c` または `m` の後に小文字の `a`, `t` が続き、
さらに `.` が 0 個または 1 個続きます。

<pre>
"(f|c|m)at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[正規表現の動作確認をする](https://regex101.com/r/DOc5Nu/1)

## 2.8 アンカー

正規表現内でマッチング文字列の開始または終了であることをチェックするために
アンカーを使うことができます。
アンカーには 2 種類あり、1 つ目が開始を表すキャレット `^`、
2 つ目が終了を表すドル記号 `$` です。

### 2.8.1 キャレット

キャレット `^` は文字列の開始かどうかを調べるために使用します。
次の正規表現 `^a` は入力文字列 `abc` に対して（a が開始文字列なら）`a` にマッチします。
しかし `^b` という正規表現は前の文字列に対してはどれにもマッチしません。
"b" は `abc` という入力文字列の開始ではないからです。
他の例を見てみます。`^(T|t)he` は大文字の `T` または小文字の `t` から始まる文字列で
その後に小文字の `h`, `e` が続くことを意味します。

<pre>
"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/5ljjgB/1)

<pre>
"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/jXrKne/1)

### 2.8.2 ドル記号

ドル記号 `$` は文字列の終了かどうかを調べるために使用します。
例えば `(at\.)$` という正規表現は小文字の `a` の後に
小文字の `t` が続き、最後は `.` で終わることを意味しています。

<pre>
"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[正規表現の動作確認をする](https://regex101.com/r/y4Au4D/1)

<pre>
"(at\.)$" => The fat cat. sat. on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[正規表現の動作確認をする](https://regex101.com/r/t0AkOd/1)

##  3. 文字集合の短縮表記

正規表現ではよく使われる文字集合に対して短縮表記が提供されており、
便利なショートカットとして使用できます。
短縮表記には次のようなものがあります。

|短縮表記|説明                               |
|:------:|-----------------------------------|
|.       |改行を除く任意の文字               |
|\w      |英数字にマッチ: `[a-zA-Z0-9_]`     |
|\W      |英数字以外にマッチ: `[^\w]`        |
|\d      |数字にマッチ: `[0-9]`              |
|\D      |数字以外にマッチ: `[^\d]`          |
|\s      |スペースにマッチ: `[\t\n\f\r\p{Z}]`|
|\S      |スペース以外にマッチ: `[^\s]`      |

## 4. 前後参照

先読みと後読み（前後参照とも呼ばれます）は **非キャプチャグループ**
（パターンのマッチングはするがマッチングリストには含まれない）という
特殊な扱いがなされる機能です。
前後参照はあるパターンが別のあるパターンよりも先行または後続して現れることを示すために使用されます。
例えば入力文字列 `$4.44 and $10.88` に対して `$` に続く全ての数字を取得することを考えます。
そのためには `(?<=\$)[0-9\.]*` という正規表現を使用します。
これは `$` に続き `.` を含む全ての数字を指すことになります。
次のような前後参照が正規表現で使用されます。

|記号  |説明          |
|:----:|--------------|
|?=    |肯定的な先読み|
|?!    |否定的な先読み|
|?<=   |肯定的な後読み|
|?<!   |否定的な後読み|

### 4.1 肯定的な先読み

肯定的な先読みはあるパターンが注目しているパターンよりも後続していることを示すための機能です。
マッチングの結果には注目しているパターンだけが含まれます。
肯定的な先読みを定義するには括弧を使用します。
その括弧の中で疑問符と等号を合わせて `(?=...)` のようにします。
先読みのパターンは括弧の中の等号の後に記述します。
例えば `(T|t)he(?=\sfat)` という正規表現は小文字の `t` か大文字の `T` のどちらかの後に `h`, `e` が続きます。
括弧内で肯定的な先読みを定義していますが、これは `The` または `the` の後に
`fat` が続くことを表しています。

<pre>
"(T|t)he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/IDDARt/1)

### 4.2 否定的な先読み

否定的な先読みはあるパターンが後続しない全てのマッチング文字列を取得するために使用します。
否定的な先読みは肯定的な先読みと同じように定義しますが、 `=` の代わりに
`!` を使うところが唯一の違いで、`(?!...)` と記述します。
次の正規表現 `(T|t)he(?!\sfat)` について考えてみます。
これはスペースを挟んで `fat` が後続することがない全ての `The` または `the` を得ることができます。

<pre>
"(T|t)he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/V32Npg/1)

### 4.3 肯定的な後読み

肯定的な後読みは特定のパターンが先行するような文字列を得るために使用します。
定義の仕方は `(?<=...)` とします。
例えば `(?<=(T|t)he\s)(fat|mat)` という正規表現は
`The` または `the` の後に続く全ての `fat` または `mat` が取得できます。

<pre>
"(?<=(T|t)he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/avH165/1)

### 4.4 否定的な後読み

否定的な後読みは特定のパターンが先行しない全ての文字列を得るために使用します。
定義の仕方は `(?<!...>)` とします。
例えば `(?<!(T|t)he\s)(cat)` は `The` または `the` に続いていない全ての `cat` が取得できます。

<pre>
"(?&lt;!(T|t)he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/8Efx5G/1)

## 5. フラグ

フラグは修飾子とも呼ばれ、正規表現の結果を修正するために使用されます。
フラグは任意の順序・組み合わせで使用でき、正規表現では必要不可欠な機能です。

|フラグ|説明                                                                    |
|:----:|------------------------------------------------------------------------|
|i     |大文字・小文字を区別しない: マッチングで大文字・小文字が区別されなくなる|
|g     |グローバル検索: 入力文字列の全マッチ列を検索する                        |
|m     |複数行: 複数行をマッチさせるためのアンカー                              |

### 5.1 大文字・小文字を区別しない

修飾子 `i` は大文字・小文字を区別したくないときに使用します。
例えば `/The/gi` という正規表現は大文字の `T` の後に小文字の `h`, `e` が続くという意味ですが、
最後の `i` で大文字・小文字を区別しない設定にしています。
文字列内の全マッチ列を検索したいのでフラグ `g` も渡しています。

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/dpQyf9/1)

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/ahfiuh/1)

### 5.2 グローバル検索

修飾子 `g` はグローバル検索（最初のマッチ列を検索する代わりに全マッチ列を検索する）を
行うために使用します。
例えば `/.(at)/g` という正規表現は、改行を除く任意の文字列の後に
小文字の `a`, `t` が続きます。正規表現の最後にフラグ `g` を渡すことで、
最初のマッチだけではなく（これがデフォルトの動作です）、入力文字列内の全マッチ列を検索するようにしています。

<pre>
"/.(at)/" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/jnk6gM/1)

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[正規表現の動作確認をする](https://regex101.com/r/dO1nef/1)

### 5.3 複数行

修飾子 `m` は複数行でマッチさせたいときに使用します。
前述で `(^, $)` という入力文字列の開始と終了を示すためのアンカーについて説明しましたが、
フラグ `m` は複数行でマッチさせるためのアンカーとして使用できます。
例えば `/at(.)?$/gm` という正規表現は小文字の `a`, `t` に続き、改行を除く
任意の文字が 0 個または 1 個続くという意味ですが、
フラグ `m` を渡すことで入力文字列の各行でパターンを検索させることができます。

<pre>
"/.at(.)?$/" => The fat
                cat sat
                on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[正規表現の動作確認をする](https://regex101.com/r/hoGMkP/1)

<pre>
"/.at(.)?$/gm" => The <a href="#learn-regex"><strong>fat</strong></a>
                  cat <a href="#learn-regex"><strong>sat</strong></a>
                  on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[正規表現の動作確認をする](https://regex101.com/r/E88WE2/1)

## 貢献する

* イシューを発行する
* 修正をプルリクエストする
* ドキュメントを普及させる
* 作者に直接連絡を取る: ziishaned@gmail.com または [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/ziishaned.svg?style=social&label=Follow%20%40ziishaned)](https://twitter.com/ziishaned)

## ライセンス

MIT &copy; [Zeeshan Ahmad](https://twitter.com/ziishaned)
