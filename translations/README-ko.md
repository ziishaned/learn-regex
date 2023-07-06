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


## 번역:

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

## 정규표현식이란 무엇인가?

[![](https://img.shields.io/badge/-Download%20PDF%20-0a0a0a.svg?style=flat&colorA=0a0a0a)](https://gum.co/learn-regex)

> 정규표현식은 텍스트에서 특정 패턴을 찾아내는데 사용되는 문자 혹은 기호들의 집합이다.

정규표현식(Regular expression)은 대상 문자열에 왼쪽에서 오른쪽 방향으로 매칭되는 하나의 패턴이다. "Regular expression"이라고 매번 발음하기 어렵기 때문에, 보통 약어로 "regex" 혹은 "regexp", "정규식"으로 축약되어 사용된다. 정규 표현식은 문자열 내부의 텍스트 대체, 포맷의 유효성 검사, 패턴 매칭을 기반으로한 문자열에서 일부 텍스트를 추출, 그리고 그 외에 다양한 목적을 위해 사용된다.

당신이 하나의 어플리케이션을 작성하고 있고 사용자가 사용자명을 선택할 때 사용되는 규칙들을 정하고 싶다고 상상해보자. 예를 들어, 우리는 사용자명에 문자, 숫자, 밑줄 문자(\_), 그리고 하이픈이 포함되는 것은 허용하고 싶다. 또한, 사용자명의 글자수를 제한해서 사용자명이 지저분해보이지 않도록 하고 싶다. 이때 아래 정규표현식을 사용해 입력된 사용자명이 해당 규칙에 맞는지 검사할 수 있다.

<br/><br/>
<p align="center">
  <img src="../img/regexp-en.png" alt="Regular expression">
</p>

위의 정규 표현식은 `john_doe`, `jo-hn_doe`, 그리고 `john12_as` 문자열을 받아들일 수 있다. `Jo`는 대문자를 포함하고 있고 길이가 너무 짧기 때문에 위의 정규표현식과 매칭되지 않는다.


## 목차

- [기본 매쳐](#1-기본-매쳐)
- [메타 문자](#2-메타-문자)
  - [마침표](#21-마침표)
  - [문자 집합](#22-문자-집합)
    - [부정 문자 집합](#221-부정-문자-집합)
  - [반복](#23-반복)
    - [별 부호](#231-별-부호)
    - [덧셈 부호](#232-덧셈-부호)
    - [물음표](#233-물음표)
  - [중괄호](#24-중괄호)
  - [캡쳐링 그룹](#25-캡쳐-그룹)
    - [논-캡쳐링 그룹](#251-논-캡쳐링-그룹)
  - [대안 부호](#26-대안-부호)
  - [특수 문자 이스케이핑](#27-특수-문자-이스케이핑)
  - [앵커 부호](#28-앵커-부호)
    - [캐럿 부호](#281-캐럿-부호)
    - [달러 부호](#282-달러-부호)
- [단축형 문자열 집합](#3-단축형-문자열-집합)
- [전후방탐색](#4-전후방탐색)
  - [긍정형 전방탐색](#41-긍정형-전방탐색)
  - [부정형 전방탐색](#42-부정형-전방탐색)
  - [긍정형 후방탐색](#43-긍정형-후방탐색)
  - [부정형 후방탐색](#44-부정형-후방탐색)
- [플래그](#5-플래그)
  - [대소문자 구분없음](#51-대소문자-구분없음)
  - [전체 검색](#52-전체-검색)
  - [멀티 라인](#53-멀티-라인)
- [탐욕적 vs 게으른 매칭](#6-탐욕적-vs-게으른-매칭)

## 1. 기본 매쳐

하나의 정규 표현식은 단지 텍스트 내부의 검색을 수행하기 위한 문자열의 패턴이다. 예를 들어, 정규 표현식 `the`는 문자 `t` 다음에 문자 `h`, 그 다음에 문자 `e`가 나오는 것을 의미한다.

<pre>
"the" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Test the regular expression](https://regex101.com/r/dmRygT/1)

정규 표현식 `123`은 문자열 `123`에 매칭된다. 정규 표현식은 정규 표현식의 각 문자(Character)와 입력된 문자열의 각 문자(Character)를 비교함으로써 해당 문자열과 매칭된다. 정규 표현식들은 일반적으로 대소문자를 구분하기 때문에, 정규 표현식 `The`는 문자열 `the`와 매칭되지 않는다.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Test the regular expression](https://regex101.com/r/1paXsy/1)

## 2. 메타 문자

메타 문자들은 정규 표현식의 빌딩 블락들이다. 메타 문자들은 자체적인 의미를 가지지 않고 특별한 방식으로 해석되어진다. 어떤 메타 문자열들은 특별한 의미를 가지며 대괄호안에서 쓰인다. 아래는 이러한 메타 문자열들이다:

|메타 문자|설명|
|:----:| ----|
|.|온점(Period)는 줄바꿈을 제외한 어떤 종류의 단일 문자와 매치.|
|[ ]|문자 클래스. 대괄호 사이에 있는 문자들로 매치.|
|[^ ]|부정 문자 클래스. 대괄호 안에 포함되지 않은 모든 문자들로 매치.|
|\*|이 메타 문자의 바로 앞에 있는 심볼이 0번 이상 반복된 문자들과 매치.|
|+|이 메타 문자의 바로 앞에 있는 심볼이 한번 이상 반복된 문자들과 매치.|
|?|이 메타 문자의 바로 앞에 있는 심볼을 선택적(optional)으로 만듬.|
|{n,m}|중괄호. 이 메타 문자의 바로 앞에 위치한 심볼이 최소 n번 최대 m번의 반복된 문자들과 매치.|
|(xyz)|문자 그룹. 문자열 xyz와 정확히 같은 순서를 가진 문자들과 매치.|
|&#124;|대안. 문자가 이 메타 문자의 앞에 있는 심볼이거나 뒤에 있는 심볼이면 매치.|
|&#92;|다음 문자 이스케이프(Escape). 예약된 문자열들 <code>[ ] ( ) { } . \* + ? ^ \$ \ &#124;</code>을 이스케이핑함으로써 그 자체와 매칭되는 것을 허용.|
|^|입력의 시작과 매치.|
|\$|입력의 끝과 매치.|

## 2.1 마침표

마침표(`.`)는 메타 문자의 가장 간단한 예다. 메타 문자 `.`는 어떠한 단일 문자와도 매치되지만 리턴 혹은 개행 문자와는 매치되지 않는다. 예를 들어, 정규 표현식 `.ar`은 어떠한 단일 문자 다음에 문자 `a`가 오고, 그 다음에 문자 `r`이 오는 패턴을 의미한다.

<pre>
".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Test the regular expression](https://regex101.com/r/xc9GkU/1)

## 2.2 문자 집합

문자 집합은 문자 클래스라고도 불린다. 대괄호는 이 문자 집합을 명시하기 위해 사용된다. 문자열 집합내에 사용된 하이픈은 문자들의 범위를 지정하는데 사용된다. 대괄호 내부에 명시된 문자들의 순서는 중요하지 않다. 예를 들어, 정규 표현식 `[Tt]he`는 대문자 `T` 혹은 소문자 `t`가 나온 다음에, 문자 `h`가 나오고 그 뒤에 문자 `e`가 나오는 패턴을 의미한다.

<pre>
"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Test the regular expression](https://regex101.com/r/2ITLQ4/1)

하지만, 문자 집합 내부에서 사용되는 온점(Period)은 온점 그 자체를 의미한다. 정규 표현식 `ar[.]`은 소문자 `a` 다음에 문자 `r`이 오고 그 뒤에 문자 `.`이 오는 패턴을 의미한다.

<pre>
"ar[.]" => A garage is a good place to park a c<a href="#learn-regex"><strong>ar.</strong></a>
</pre>

[Test the regular expression](https://regex101.com/r/wL3xtE/1)

### 2.2.1 부정 문자 집합

일반적으로, 캐럿 기호(^)는 문자열의 시작지점을 나타내지만, 왼쪽 대괄호 바로 뒤에 위치했을때는 해당 문자 집합의 부정(negation)을 나타낸다. 예를 들어, 정규 표현식 `[^c]ar`은 문자 `c`를 제외한 어떠한 문자뒤에 문자 `a`가 오고, 그 뒤에 문자 `r`이 오는 패턴을 의미한다.

<pre>
"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Test the regular expression](https://regex101.com/r/nNNlq3/1)

## 2.3 반복

메타 문자 `+`, `*` 또는 `?`은 하위패턴(subpattern)이 몇 번 발생하는지 지정하는데 사용된다. 이러한 메타 문자들은 상황에 따라 다르게 동작한다.

### 2.3.1 별 부호

`*` 부호는 부호 앞에 위치한 매처(matcher)가 0번 이상 반복된 문자열과 매치된다. 정규 표현식 `a*`은 소문자 `a`가 0번 이상 반복되는 패턴을 의미한다. 하지만, 만약 이 별 부호가 문자 집합(character set) 직후에 나오는 경우에는 문자 집합 전체의 반복을 찾게된다. 예를 들어, 정규 표현식 `[a-z]*`은 소문자들이 갯수와 상관없이 연속으로 반복되는 패턴을 의미한다.

<pre>
"[a-z]*" => T<a href="#learn-regex"><strong>he</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.
</pre>

[Test the regular expression](https://regex101.com/r/7m8me5/1)

`*` 부호는 메타 문자 `.`와 함께 모든 문자열과 매치되는 패턴을 만드는데 사용될 수 있다. 또한, `*` 부호는 공백 문자 `\s`와 함께 공백 문자들로 이루어진 문자열과 매치되는 패턴을 만드는데 사용될 수 있다. 예를 들어, 정규 표현식 `\s*cat\s*`는 0번 이상 공백문자가 나온 이후에 소문자 `c`, 소문자 `a`, 소문자 `t`가 자체로 나오고 그 뒤에 다시 0번 이상의 공백문자가 나오는 패턴을 의미한다.

<pre>
"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the <a href="#learn-regex">con<strong>cat</strong>enation</a>.
</pre>

[Test the regular expression](https://regex101.com/r/gGrwuz/1)

### 2.3.2 덧셈 부호

`+` 부호는 부호 앞에 위치한 문자가 한번 이상 반복되는 패턴을 만드는데 사용된다. 예를 들어, 정규 표현식 `c.+t`는 소문자 `c`가 나오고, 그 뒤에 한개 이상의 문자가 나온 후, 소문자 `t`가 나오는 패턴을 의미한다. 여기서 문자 `t`는 해당 문장의 제일 마지막 글자 `t`라는것을 명확히할 필요가 있다.

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

[Test the regular expression](https://regex101.com/r/Dzf9Aa/1)

### 2.3.3 물음표

정규 표현식에서 메타 문자 `?`는 선행 문자를 선택적으로 만드는 역할을 한다. 물음표는 부호 앞에 쓰여진 문자가 선택적으로 나오는 패턴을 나타내는데 사용된다. 예를 들어, 정규 표현식 `[T]?he`는 대문자 `T`가 선택적으로 나온 이후에, 그 뒤에 소문자 `h`, 그 뒤에 소문자 `e`가 나오는 패턴을 의미한다.

<pre>
"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Test the regular expression](https://regex101.com/r/cIg9zm/1)

<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

[Test the regular expression](https://regex101.com/r/kPpO2x/1)

## 2.4 중괄호

정규 표현식에서 정량자(quantifier)라고도 불리는 중괄호는 하나의 문자 혹은 문자 집합으로 표시된 문자가 몇번 반복되는지 명시하는데 사용된다. 예를 들어, 정규 표현식 `[0-9]{2,3}`은 숫자 문자(0부터 9사이의 문자)가 최소 2번, 최대 3번 연속해서 나오는 문자열 패턴을 의미한다.

<pre>
"[0-9]{2,3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Test the regular expression](https://regex101.com/r/juM86s/1)

두번째 숫자를 생략하는 것이 가능하다. 예를 들어, 정규 표현식 `[0-9]{2,}`는 2번 이상의 숫자가 연속으로 나오는 패턴을 의미한다. 만약 여기서 쉼표를 삭제하는 경우, 정규 표현식 `[0-9]{3}`은 숫자가 정확히 3번 연속해서 나오는 패턴을 의미한다.

<pre>
"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Test the regular expression](https://regex101.com/r/Gdy4w5/1)

<pre>
"[0-9]{3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to 10.0.
</pre>

[Test the regular expression](https://regex101.com/r/Sivu30/1)

## 2.5 캡쳐링 그룹

캡쳐링 그룹은 괄호 `(...)` 안에 쓰여진 하위 패턴들의 그룹이다. 위에서 논의했듯이, 정규 표현식에서 하나의 문자 뒤에 정량자(quantifier)를 넣는 경우에는 해당 문자의 반복을 나타낸다. 하지만, 만약 하나의 캡쳐링 그룹 뒤에 정량자를 넣는 경우에는 캡쳐링 그룹 전체의 반복을 나타내게 된다. 예를 들어, 정규 표현식 `(ab)*`는 문자 "ab"가 0번 이상 반복되는 패턴을 의미한다. 대안 부호인 `|` 또한 문자 그룹 내부에서 사용할 수 있다. 예를 들어, 정규 표현식 `(c|g|p)ar`은 소문자 `c`, `g` 혹은 `p`가 나온 이후에 문자 `a`가 나오고 그 뒤에 문자 `r`이 나오는 패턴을 의미한다.

<pre>
"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Test the regular expression](https://regex101.com/r/tUxrBG/1)

캡처링 그룹은 부모 언어에서 사용하기 위해 문자를 일치시킬뿐만 아니라 문자를 캡처한다는 점에 유의해야 한다. 부모 언어는 파이썬이나 자바 스크립트 또는 함수 정의에서 정규 표현식을 구현하는 거의 모든 언어가 될 수 있다.

### 2.5.1 논-캡쳐링 그룹

논-캡쳐링 그룹은 오직 문자열에 매칭되지만, 그룹을 캡쳐하지 않는 캡쳐링 그룹이다. 논-캡쳐링 그룹은 `(...)` 괄호안에 `?:` 로 표시된다. 예를 들어 정규식 `(?:c|g|p)ar` 는 `(c|g|p)ar`와 같은 문자열을 매칭하는 것에서 유사하지만, 캡쳐링 그룹을 만들지 않는다.

<pre>
"(?:c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Test the regular expression](https://regex101.com/r/Rm7Me8/1)

논-캡처링 그룹은 찾기 및 변경 기능에서 사용하거나 캡처 그룹 함께 사용하여 다른 종류의 출력 생성시 overview를 유지할 때 유용하다. 또한 [4. 전후방탐색](#4-전후방탐색)를 보아라.

## 2.6 대안 부호

정규 표현식에서 수직 막대 부호 `|`는 대안을 정의하는데 사용된다. 대안 부호는 여러개의 표현식들 사이의 조건과도 같다. 지금쯤 당신은 문자 집합(Character set)과 대안 부호가 동일하게 동작한다고 생각하고 있을 것이다. 하지만, 문자 집합과 대안 부호 사이의 가장 큰 차이점은 문자 집합은 문자 수준에서 동작하는 반면, 대안 부호는 표현식 수준에서 동작한다는 것이다. 예를 들어, 정규 표현식 `(T|t)he|car`는 대문자 `T` 혹은 소문자 `t`가 나오고 문자 `h`, 문자 `e`가 차례로 나오거나 문자 `c`, 문자 `a`, 문자 `r`이 차례로 나오는 패턴을 의미한다.

<pre>
"(T|t)he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Test the regular expression](https://regex101.com/r/fBXyX0/1)

## 2.7 특수 문자 이스케이핑

백 슬래시 `\`는 정규 표현식에서 다음에 나오는 부호를 이스케이핑하는데 사용된다. 백 슬래시는 예약 문자들인 `{ } [ ] / \ + * . $ ^ | ?`를 메타 부호가 아닌 문자 그 자체로 매칭되도록 명시한다. 특수 문자를 매칭 캐릭터로 사용하기 위해서는 백 슬래시 `\`를 해당 특수 문자 앞에 붙이면 된다. 예를 들어, 정규 표현식 `.`은 개행을 제외한 어떤 문자와 매칭된다. 입력 문자열에 포함된 `.` 문자를 매치시키는 정규 표현식 `(f|c|m)at\.?`은 소문자 `f`, `c` 또는 `m` 이후에 소문자 `a`와 `t`가 차례로 등장하고 이후에 문자 `.`가 선택적으로 나타나는 패턴을 의미한다.

<pre>
"(f|c|m)at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Test the regular expression](https://regex101.com/r/DOc5Nu/1)

## 2.8 앵커 부호

정규 표현식에서 앵커는 매칭 문자가 표현식의 시작 문자인지 혹은 끝 문자인지 명시하는데 사용된다. 앵커는 두가지 종류가 있다: 첫번째 종류인 캐럿 부호 `^`는 매칭 문자가 입력 문자열의 첫 시작 문자인지 나타내는데 사용되며 두번째 종류인 달러 부호 `$`는 해당 매칭 문자가 입력 문자의 마지막 문자라는 것을 명시하는데 사용된다.

### 2.8.1 캐럿 부호

캐럿 부호 `^`는 매칭 문자가 표현식의 시작이라는 것을 명시하는데 사용된다. 만약 (a가 시작 문자인지 확인하는) 정규 표현식 `^a`를 입력 문자열 `abc`에 적용하면, 이 정규 표현식은 `a`를 매칭 결과값으로 내보낸다. 반면, 정규 표현식 `^b`를 위의 입력 문자열에 적용하면, 아무런 매칭도 일어나지 않는다. 왜냐하면 입력 문자열 `abc`에서 "b"는 처음 시작 문자가 아니기 때문이다. 또 다른 정규 표현식인 `^(T|t)he`를 살펴보자. 이 정규 표현식은 대문자 `T` 또는 소문자 `t`가 입력 문자열의 시작으로 나오고, 그 뒤에 문자 `h`와 문자 `e`가 차례로 나오는 패턴을 의미한다.

<pre>
"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Test the regular expression](https://regex101.com/r/5ljjgB/1)

<pre>
"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Test the regular expression](https://regex101.com/r/jXrKne/1)

### 2.8.2 달러 부호

달러 부호 `$`는 입력 문자열의 마지막 문자가 매칭 문자로 끝나는지 확인하는데 사용된다. 예를 들어, 정규 표현식 `(at\.)$`는 소문자 `a`와 `t` 그리고 문자 `.`가 순서대로 입력 문자열의 맨 마지막에 나오는지 확인하는 패턴을 의미한다.

<pre>
"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Test the regular expression](https://regex101.com/r/y4Au4D/1)

<pre>
"(at\.)$" => The fat cat. sat. on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Test the regular expression](https://regex101.com/r/t0AkOd/1)

## 3. 단축형 문자열 집합

정규 표현식은 일반적으로 사용되는 문자열 집합들을 간편하게 사용할 수 있도록 여러 단축형들을 제공한다. 단축형 문자열 집합은 아래와 같다.

|단축형|설명|
|:----:|----|
|.|개행을 제외한 모든 문자|
|\w|영숫자 문자와 매치: `[a-zA-Z0-9_]`|
|\W|영숫자 문자가 아닌 문자와 매치: `[^\w]`|
|\d|숫자와 매치: `[0-9]`|
|\D|숫자가 아닌 문자와 매치: `[^\d]`|
|\s|공백 문자와 매치: `[\t\n\f\r\p{Z}]`|
|\S|공백 문자가 아닌 문자와 매치: `[^\s]`|

## 4. 전후방탐색

때때로 전후방탐색<sub>Lookaround</sub>이라고 알려진 후방탐색<sub>Lookbehind</sub>과 전방탐색<sub>Lookahead</sub>은 (패턴 매칭을 위해서 사용되지만 매칭된 리스트에는 포함되지 않는) **_넌-캡쳐링 그룹_** 의 특정 종류들이다. 전후방탐색은 하나의 패턴이 다른 특정 패턴 전이나 후에 나타나는 조건을 가지고 있을때 사용한다. 예를 들어, 우리가 입력 문자열 `$4.44 and $10.88`에 대해서 달러 부호 `$`이후에 나오는 모든 숫자를 매칭시키고 싶다고 하자. 이때 정규 표현식 `(?<=\$)[0-9\.]*`를 사용할 수 있다. 이 정규 표현식은 `$` 문자 뒤에 나오는 문자 `.`을 포함한 모든 숫자 문자를 의미한다. 다음은 정규 표현식에서 사용되는 전후방탐색들이다.

|부호|설명|
|:----:|----|
|?=|긍정형 전방탐색|
|?!|부정형 전방탐색|
|?<=|긍정형 후방탐색|
|?<!|부정형 후방탐색|

### 4.1 긍정형 전방탐색

긍정형 전방탐색는 표현식의 첫 부분뒤에 전방탐색 표현식이 뒤따라 나오는지 확인하는데 사용된다. 매칭의 결과값은 표현식의 첫 부분과 매칭된 텍스트만이 포함된다. 긍정형 전방탐색를 정의하기 위해서는 괄호가 사용된다. 이 괄호 안에서, 물음표 부호 `?`와 등호 `=`가 다음과 같이 사용된다: `(?=...)`. 전방탐색 표현식은 괄호 내부의 등호 `=` 부호 뒤에 쓰면된다. 예를 들어, 정규 표현식 `[T|t]he(?=\sfat)`는 대문자 `T` 혹은 소문자 `t` 뒤에 문자 `h`, 문자 `e`가 나오는 패턴을 의미한다. 괄호 안에서 우리는 정규 표현식 엔진에게 바로 뒤에 공백문자와 문자열 `fat`이 나오는 `The` 또는 `the`만 매치하도록 알리는 긍정형 전방탐색를 정의하였다.

<pre>
"[T|t]he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Test the regular expression](https://regex101.com/r/IDDARt/1)

### 4.2 부정형 전방탐색

부정형 전방탐색는 입력 문자열로부터 특정 패턴이 뒤에 나오지 않기를 바라는 상황에서 사용된다. 부정형 전방탐색는 우리가 긍정형 전방탐색를 정의하는 방식과 동일하게 정의된다. 하지만, 유일한 차이점은 등호 부호 `=` 대신 부정 부호 `!` 문자를 사용한다는 것이다, 즉 `(?!...)`. 정규 표현식 `[T|t]he(?!\sfat)`를 살펴보도록 하자. 이 정규 표현식은 공백 문자와 `fat` 문자열이 연속으로 나오지 않는 모든 `The` 혹은 `the` 문자열과 매치된다.

<pre>
"[T|t]he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Test the regular expression](https://regex101.com/r/V32Npg/1)

### 4.3 긍정형 후방탐색

긍정형 후방탐색는 특정 패턴뒤에 나오는 문자열 매치를 가져오기 위해서 사용된다. 긍정형 후방탐색는 `(?<=...)`로 표시된다. 예를 들어, 정규 표현식 `(?<=[T|t]he\s)(fat|mat)`는 입력 문자열에서 `The` 혹은 `the` 뒤에 공백이 나오고, 그 뒤에 `fat` 또는 `mat`이 나오는 패턴을 의미한다.

<pre>
"(?<=[T|t]he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Test the regular expression](https://regex101.com/r/avH165/1)

### 4.4 부정형 후방탐색

부정형 후방탐색는 특정 패턴이 뒤에 나오지 않기를 바라는 상황에서 사용된다. 부정형 후방탐색는 `(?<!...)`로 표시된다. 예를 들어, 정규 표현식 `(?<!(T|t)he\s)(cat)`은 앞에 `The` 혹은 `the` 가 위치하지 않는 모든 `cat` 문자열을 의미한다.

<pre>
"(?&lt;![T|t]he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

[Test the regular expression](https://regex101.com/r/8Efx5G/1)

## 5. 플래그

플래그는 정규표현식의 출력값을 수정하기 때문에 수정자(modifier)라고도 불린다. 이러한 플래그들은 어떤 순서 혹은 조합으로 사용 가능하며 정규 표현식의 일부분이다.

|플래그|설명|
|:----:|----|
|i|대소문자 구분없음: 매칭이 대소문자를 구분하지 않도록 설정.|
|g|전체 검색: 입력 문자열 전체를 대상으로 패턴을 검색.|
|m|멀티 라인: 앵터 메타 문자가 각 줄마다 동작하도록 설정.|

### 5.1 대소문자 구분없음

수정자 `i`는 대소문자 구분없는 매칭을 수행하는데 사용된다. 예를 들어, 정규 표현식 `/The/gi`는 대문자 `T`, 소문자 `h`, 소문자 `e`가 차례로 나오는 패턴을 의미한다. 여기서 정규 표현식 마지막에 있는 `i` 플래그가 정규 표현식 엔진에게 대소문자를 구분하지 않도록 알려준다. `g` 플래그는 전체 입력 문자열 내부에서 패턴을 검색하기 위해 설정되었다.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Test the regular expression](https://regex101.com/r/dpQyf9/1)

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Test the regular expression](https://regex101.com/r/ahfiuh/1)

### 5.2 전체 검색

수정자 `g`는 첫번째 매칭후에 멈추지 않고 계속해서 모든 매칭을 검색하는 전체 검색을 수행하는데 사용된다. 예를 들어, 정규 표현식 `/.(at)/g`는 개행을 제외한 문자가 나오고, 그 뒤에 소문자 `a`, 소문자 `t`가 나오는 패턴을 의미한다. 여기에서 `g` 플래그를 정규 표현식의 마지막에 설정했기 때문에, 이 패턴은 입력 문자열 전체에서 나타나는 모든 패턴을 찾아낸다.

<pre>
"/.(at)/" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

[Test the regular expression](https://regex101.com/r/jnk6gM/1)

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Test the regular expression](https://regex101.com/r/dO1nef/1)

### 5.3 멀티 라인

수정자 `m`은 멀티 라인 매치를 수행하는데 사용된다. 이전에 이야기 했던 것처럼, 앵커 `(^, $)`는 패턴의 시작과 끝을 확인하는데 사용된다. 하지만 만약 우리가 각 라인마다 이 앵커가 동작하게하고 싶으면 `m` 플래그를 설정하면된다. 예를 들어, 정규 표현식 `/at(.)?$/gm`은 소문자 `a`와 소문자 `t`가 차례로 나오고, 선택적으로 개행을 제외한 문자가 나오는 패턴을 의미한다. 여기서 플래그 `m`으로 인해서 정규 표현식 엔진은 입력 문자열의 각 라인에 대해서 해당 패턴을 매칭하게 된다.

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

## 6. 탐욕적 vs 게으른 매칭
기본적으로 정규 표현식은 탐욕적(greedy) 매칭을 수행하는데, 이는 가능한 한 길게 매칭하는 것을 의미한다. 우리는 `?`를 사용하여 게으른(lazy) 방법 매칭할 수 있으며, 가능한 한 짧게 매칭하는 것을 의미한다.

<pre>
"/(.*at)/" => <a href="#learn-regex"><strong>The fat cat sat on the mat</strong></a>. 
</pre>

[Test the regular expression](https://regex101.com/r/AyAdgJ/1)

<pre>
"/(.*?at)/" => <a href="#learn-regex"><strong>The fat</strong></a> cat sat on the mat. 
</pre>

[Test the regular expression](https://regex101.com/r/AyAdgJ/2)

## 기여 방법

* 이슈 리포팅
* 코드 개선해서 풀 리퀘스트 열기
* 소문내기
* ziishaned@gmail.com 메일로 직접 연락하기 또는 [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/ziishaned.svg?style=social&label=Follow%20%40ziishaned)](https://twitter.com/ziishaned)

## 라이센스

MIT &copy; [Zeeshan Ahmad](https://twitter.com/ziishaned)
