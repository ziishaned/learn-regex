<a href="https://www.buymeacoffee.com/ziishaned" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<p align="center">
    <br/>
    <a href="https://github.com/ziishaned/learn-regex">	
        <img src="https://i.imgur.com/bYwl7Vf.png" alt="Learn Regex">
    </a>
</p>


## Terjemahan:

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
* [Bahasa Indonesia](translations/README-id.md)

## Apakah Ekspresi Reguler Itu?

<p>
    <a href="https://gum.co/learn-regex">
        <img src="https://img.shields.io/badge/-Download%20PDF%20-0a0a0a.svg?style=flat&colorA=0a0a0a" alt="Download PDF">
    </a>
</p>

> Ekspresi reguler adalah sekumpulan karakter atau simbol yang digunakan untuk mencari pola tertentu dalam teks.

Ekspresi reguler merupakan pola yang dicocokkan dengan string subjek dari kiri ke kanan. Ekspresi reguler digunakan untuk mengganti teks dalam string, memvalidasi formulir, mengekstrak substring dari string berdasarkan kecocokan pola, dan masih banyak lagi. Istilah "ekspresi reguler" terdengar panjang, sehingga Anda biasanya akan menemukan istilah ini disingkat menjadi "regex" atau "regexp".

Bayangkan Anda sedang menulis aplikasi dan ingin membuat aturan ketika pengguna memilih nama pengguna. Kita ingin mengizinkan nama pengguna berisi huruf, angka, garis bawah, dan tanda hubung. Kita juga ingin membatasi jumlah karakter dalam nama pengguna agar tidak terlihat buruk. Kita dapat menggunakan ekspresi reguler berikut untuk memvalidasi nama pengguna:
<br/><br/>
<p align="center">
  <img src="./img/regexp-id.png" alt="Regular expression">
</p>
Ekspresi reguler di atas dapat menerima string `john_doe`, `jo-hn_doe`, dan `john12_as`. Pola ini tidak cocok dengan `Jo` karena string tersebut mengandung huruf besar dan terlalu pendek.

## Daftar Isi :

- [Pencocokan Dasar](#1-basic-matchers)
- [Karakter Meta](#2-meta-characters)
  - [Titik](#21-the-full-stops)
  - [Set Karakter](#22-character-sets)
    - [Set Karakter yang dinegasikan](#221-negated-character-sets)
  - [Perulangan](#23-repetitions)
    - [Tanda Bintang](#231-the-star)
    - [Tanda Tambah](#232-the-plus)
    - [Tanda Tanya](#233-the-question-mark)
  - [Tanda Kurung](#24-braces)
  - [Kelompok Penangkapan](#25-capturing-groups)
      - [Kelompok non-Penangkapan](#251-non-capturing-groups)
  - [Alternasi](#26-alternation)
  - [Meloloskan Karakter khusus](#27-escaping-special-characters)
  - [Penanda Posisi](#28-anchors)
    - [Tanda Karat (Caret)](#281-the-caret)
    - [Tanda Dolar](#282-the-dollar-sign)
- [Set Karakter Singkatan](#3-shorthand-character-sets)
- [Lookarounds](#4-lookarounds)
  - [Positif Lookahead](#41-positive-lookahead)
  - [Negatif Lookahead](#42-negative-lookahead)
  - [Positif Lookbehind](#43-positive-lookbehind)
  - [Negatif Lookbehind](#44-negative-lookbehind)
- [Flags](#5-flags)
  - [Sensitivitas Huruf (besar/kecil)](#51-case-insensitive)
  - [Pencarian Global](#52-global-search)
  - [Baris Berganda](#53-multiline)
- [Pencocokan Serakah vs Malas](#6-greedy-vs-lazy-matching)

## 1. Pencocokan Dasar

Ekspresi reguler hanyalah pola karakter yang kita gunakan untuk melakukan pencarian dalam teks. Sebagai contoh, ekspresi reguler `the` berarti: huruf `t`, diikuti oleh huruf `h`, diikuti oleh huruf `e`.
<pre>
"the" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/dmRygT/1)

Ekspresi reguler `123` akan cocok dengan string `123`. Ekspresi reguler dicocokkan dengan string masukan dengan membandingkan setiap karakter dalam ekspresi reguler dengan setiap karakter dalam string masukan, satu per satu. Biasanya, ekspresi reguler bersifat peka terhadap huruf besar/kecil (case-sensitive), sehingga ekspresi reguler `The` tidak akan cocok dengan string `the`.

Ini berarti huruf besar dan huruf kecil dianggap berbeda dalam pencocokan pola menggunakan ekspresi reguler, kecuali jika diatur untuk mengabaikan perbedaan tersebut.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/1paXsy/1)

## 2. Karakter Meta

Karakter meta adalah blok bangunan dari ekspresi reguler. Karakter meta tidak berdiri sendiri tetapi diinterpretasikan dengan cara khusus. Beberapa karakter meta memiliki makna khusus dan ditulis di dalam tanda kurung siku. Berikut adalah karakter meta yang tersedia:

|Karakter Meta|Deskripsi|
|:----:|----|
|.|Titik mencocokkan karakter tunggal apa pun kecuali jeda baris.|
|[ ]|Kelas karakter. Mencocokkan karakter apa pun yang terkandung di antara tanda kurung siku.|
|[^ ]|Kelas karakter yang dinegasikan. Mencocokkan karakter apa pun yang tidak terkandung di antara tanda kurung siku|
|*|Mencocokkan 0 atau lebih pengulangan dari simbol sebelumnya.|
|+|Mencocokkan 1 atau lebih pengulangan dari simbol sebelumnya.|
|?|Membuat simbol sebelumnya opsional.|
|{n,m}|Tanda kurung kurawal. Mencocokkan setidaknya "n" tetapi tidak lebih dari "m" pengulangan dari simbol sebelumnya.|
|(xyz)|Kelompok karakter. Mencocokkan karakter xyz dalam urutan yang tepat.|
|&#124;|Alternasi. Mencocokkan karakter sebelum atau karakter setelah simbol.|
|&#92;|Meloloskan karakter berikutnya. Ini memungkinkan Anda mencocokkan karakter yang dipesan <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>|
|^|Mencocokkan awal dari input.|
|$|Mencocokkan akhir dari input.|

## 2.1 Titik

Titik `.` adalah contoh paling sederhana dari karakter meta. Karakter meta `.`
mencocokkan karakter tunggal apa pun. Ini tidak akan mencocokkan karakter return atau newline.
Sebagai contoh, ekspresi reguler `.ar` berarti: karakter apa pun, diikuti oleh
huruf `a`, diikuti oleh huruf `r`.

<pre>
".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/xc9GkU/1)

## 2.2 Set Karakter

Set karakter juga disebut kelas karakter. Tanda kurung siku digunakan untuk
menentukan set karakter. Gunakan tanda hubung di dalam set karakter untuk menentukan
rentang karakter. Urutan rentang karakter di dalam tanda kurung siku
tidak masalah. Sebagai contoh, ekspresi reguler `[Tt]he` berarti: huruf besar
`T` atau huruf kecil `t`, diikuti oleh huruf `h`, diikuti oleh huruf `e`.

<pre>
"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/2ITLQ4/1)

Namun, titik di dalam set karakter berarti titik literal. Ekspresi reguler
`ar[.]` berarti: karakter huruf kecil `a`, diikuti oleh huruf `r`,
diikuti oleh karakter titik `.`.

<pre>
"ar[.]" => A garage is a good place to park a c<a href="#learn-regex"><strong>ar.</strong></a>
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/wL3xtE/1)

### 2.2.1 Set Karakter yang Dinegasikan

Secara umum, simbol caret mewakili awal dari string, tetapi ketika ditulis
setelah tanda kurung siku pembuka, itu menegasikan set karakter. Sebagai
contoh, ekspresi reguler `[^c]ar` berarti: karakter apa pun kecuali `c`,
diikuti oleh karakter `a`, diikuti oleh huruf `r`.

<pre>
"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/nNNlq3/1)

## 2.3 Perulangan

Karakter meta `+`, `*` atau `?` digunakan untuk menentukan berapa kali
subpola dapat terjadi. Karakter meta ini bertindak berbeda dalam situasi
yang berbeda.

### 2.3.1 Tanda Bintang

Simbol `*` mencocokkan nol atau lebih pengulangan dari pencocok sebelumnya. Ekspresi reguler
`a*` berarti: nol atau lebih pengulangan dari karakter huruf kecil sebelumnya
`a`. Namun, jika muncul setelah set karakter atau kelas, maka itu menemukan
pengulangan dari seluruh set karakter. Sebagai contoh, ekspresi reguler
`[a-z]*` berarti: sejumlah huruf kecil dalam barisan.

<pre>
"[a-z]*" => T<a href="#learn-regex"><strong>he</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/7m8me5/1)

Simbol `*` dapat digunakan dengan karakter meta `.` untuk mencocokkan string karakter apa pun
`.*`. Simbol `*` juga dapat digunakan dengan karakter spasi `\s`
untuk mencocokkan string karakter spasi. Sebagai contoh, ekspresi
`\s*cat\s*` berarti: nol atau lebih spasi, diikuti oleh huruf kecil `c`,
diikuti oleh huruf kecil `a`, diikuti oleh huruf kecil `t`,
diikuti oleh nol atau lebih spasi.

<pre>
"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the con<a href="#learn-regex"><strong>cat</strong></a>enation.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/gGrwuz/1)

### 2.3.2 Tanda Tambah

Simbol `+` mencocokkan satu atau lebih pengulangan dari karakter sebelumnya. Sebagai
contoh, ekspresi reguler `c.+t` berarti: huruf kecil `c`, diikuti oleh
setidaknya satu karakter, diikuti oleh huruf kecil `t`. Perlu
dijelaskan bahwa `t` adalah `t` terakhir dalam kalimat.

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/Dzf9Aa/1)

### 2.3.3 Tanda Tanya

Dalam ekspresi reguler, karakter meta `?` membuat karakter sebelumnya
opsional. Simbol ini mencocokkan nol atau satu instance dari karakter sebelumnya.
Sebagai contoh, ekspresi reguler `[T]?he` berarti: Opsional huruf besar
`T`, diikuti oleh huruf kecil `h`, diikuti oleh huruf kecil `e`.

<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/cIg9zm/1)

<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/kPpO2x/1)

## 2.4 Tanda Kurung Kurawal

Dalam ekspresi reguler, tanda kurung kurawal (juga disebut quantifier) digunakan untuk
menentukan berapa kali karakter atau kelompok karakter dapat
diulang. Sebagai contoh, ekspresi reguler `[0-9]{2,3}` berarti: Cocokkan setidaknya
2 digit, tetapi tidak lebih dari 3, berkisar dari 0 hingga 9.

<pre>
"[0-9]{2,3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/juM86s/1)

Kita dapat menghilangkan angka kedua. Sebagai contoh, ekspresi reguler
`[0-9]{2,}` berarti: Cocokkan 2 atau lebih digit. Jika kita juga menghapus koma, ekspresi reguler
`[0-9]{3}` berarti: Cocokkan tepat 3 digit.

<pre>
"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/Gdy4w5/1)

<pre>
"[0-9]{3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to 10.0.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/Sivu30/1)

## 2.5 Kelompok Penangkapan

Kelompok penangkapan adalah kelompok subpola yang ditulis di dalam tanda kurung 
`(...)`. Seperti yang dibahas sebelumnya, dalam ekspresi reguler, jika kita meletakkan quantifier 
setelah karakter maka itu akan mengulang karakter sebelumnya. Namun, jika kita meletakkan quantifier
setelah kelompok penangkapan maka itu mengulang seluruh kelompok penangkapan. Sebagai contoh,
ekspresi reguler `(ab)*` mencocokkan nol atau lebih pengulangan dari karakter
"ab". Kita juga dapat menggunakan alternasi `|` karakter meta di dalam kelompok penangkapan.
Sebagai contoh, ekspresi reguler `(c|g|p)ar` berarti: huruf kecil `c`,
`g` atau `p`, diikuti oleh `a`, diikuti oleh `r`.

<pre>
"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/tUxrBG/1)

Perhatikan bahwa kelompok penangkapan tidak hanya mencocokkan, tetapi juga menangkap karakter untuk digunakan dalam 
bahasa induk. Bahasa induk dapat berupa Python, JavaScript, atau hampir semua
bahasa yang mengimplementasikan ekspresi reguler dalam definisi fungsi.

### 2.5.1 Kelompok Non-Penangkapan

Kelompok non-penangkapan adalah kelompok penangkapan yang mencocokkan karakter tetapi 
tidak menangkap kelompok. Kelompok non-penangkapan dilambangkan dengan `?` diikuti oleh `:` 
di dalam tanda kurung `(...)`. Sebagai contoh, ekspresi reguler `(?:c|g|p)ar` mirip dengan 
`(c|g|p)ar` dalam hal itu mencocokkan karakter yang sama tetapi tidak akan membuat kelompok penangkapan.

<pre>
"(?:c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/Rm7Me8/1)

Kelompok non-penangkapan dapat berguna ketika digunakan dalam fungsionalitas find-and-replace atau 
ketika dicampur dengan kelompok penangkapan untuk menjaga gambaran ketika menghasilkan jenis output lainnya. 
Lihat juga [4. Lookaround](#4-lookaround).

## 2.6 Alternasi

Dalam ekspresi reguler, batang vertikal `|` digunakan untuk mendefinisikan alternasi.
Alternasi seperti pernyataan OR antara beberapa ekspresi. Sekarang, Anda mungkin
berpikir bahwa set karakter dan alternasi bekerja dengan cara yang sama. Namun, perbedaan besar
antara set karakter dan alternasi adalah bahwa set karakter bekerja pada
tingkat karakter tetapi alternasi bekerja pada tingkat ekspresi. Sebagai contoh, ekspresi reguler
`(T|t)he|car` berarti: baik (huruf besar `T` atau huruf kecil
`t`, diikuti oleh huruf kecil `h`, diikuti oleh huruf kecil `e`) ATAU
(huruf kecil `c`, diikuti oleh huruf kecil `a`, diikuti oleh
huruf kecil `r`). Perhatikan bahwa saya menyertakan tanda kurung untuk kejelasan, untuk menunjukkan bahwa ekspresi mana pun
dalam tanda kurung dapat dipenuhi dan itu akan cocok.

<pre>
"(T|t)he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/fBXyX0/1)

## 2.7 Meloloskan Karakter Khusus

Backslash `\` digunakan dalam ekspresi reguler untuk meloloskan karakter berikutnya. Ini
memungkinkan kita untuk menyertakan karakter yang dipesan seperti `{ } [ ] / \ + * . $ ^ | ?` sebagai karakter pencocokan. Untuk menggunakan salah satu karakter khusus ini sebagai karakter pencocokan, tambahkan `\` di depannya.

Sebagai contoh, ekspresi reguler `.` digunakan untuk mencocokkan karakter apa pun kecuali
newline. Sekarang, untuk mencocokkan `.` dalam string input, ekspresi reguler
`(f|c|m)at\.?` berarti: huruf kecil `f`, `c` atau `m`, diikuti oleh huruf kecil
`a`, diikuti oleh huruf kecil `t`, diikuti oleh opsional `.`
karakter.

<pre>
"(f|c|m)at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/DOc5Nu/1)

## 2.8 Penanda Posisi

Dalam ekspresi reguler, kita menggunakan penanda posisi untuk memeriksa apakah simbol pencocokan adalah
simbol awal atau simbol akhir dari string input. Penanda posisi terdiri dari dua jenis:
Jenis pertama adalah caret `^` yang memeriksa apakah karakter pencocokan adalah karakter pertama
dari input dan jenis kedua adalah tanda dolar `$` yang memeriksa apakah karakter pencocokan
adalah karakter terakhir dari string input.

### 2.8.1 Tanda Karat (Caret)

Simbol caret `^` digunakan untuk memeriksa apakah karakter pencocokan adalah karakter pertama
dari string input. Jika kita menerapkan ekspresi reguler berikut `^a` (berarti 'a' harus
menjadi karakter awal) ke string `abc`, itu akan mencocokkan `a`. Namun, jika kita menerapkan
ekspresi reguler `^b` ke string di atas, itu tidak akan mencocokkan apa pun.
Karena dalam string `abc`, "b" bukan karakter awal. Mari kita lihat
ekspresi reguler lain `^(T|t)he` yang berarti: huruf besar `T` atau
huruf kecil `t` harus menjadi karakter pertama dalam string, diikuti oleh
huruf kecil `h`, diikuti oleh huruf kecil `e`.

<pre>
"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/5ljjgB/1)

<pre>
"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/jXrKne/1)

### 2.8.2 Tanda Dolar

Tanda dolar `$` digunakan untuk memeriksa apakah karakter pencocokan adalah karakter terakhir
dalam string. Sebagai contoh, ekspresi reguler `(at\.)$` berarti: huruf kecil
`a`, diikuti oleh huruf kecil `t`, diikuti oleh karakter
`.` dan pencocok harus berada di akhir string.

<pre>
"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/y4Au4D/1)

<pre>
"(at\.)$" => The fat cat. sat. on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/t0AkOd/1)

## 3. Set Karakter Singkatan

Ada sejumlah singkatan yang nyaman untuk set karakter yang umum digunakan/
ekspresi reguler:

|Singkatan|Deskripsi|
|:----:|----|
|.|Karakter apa pun kecuali baris baru|
|\w|Mencocokkan karakter alfanumerik: `[a-zA-Z0-9_]`|
|\W|Mencocokkan karakter non-alfanumerik: `[^\w]`|
|\d|Mencocokkan digit: `[0-9]`|
|\D|Mencocokkan non-digit: `[^\d]`|
|\s|Mencocokkan karakter spasi: `[\t\n\f\r\p{Z}]`|
|\S|Mencocokkan karakter non-spasi: `[^\s]`|

## 4. Lookarounds

Lookbehinds dan lookaheads (juga disebut lookarounds) adalah jenis khusus dari
***kelompok non-penangkapan*** (digunakan untuk mencocokkan pola tetapi tanpa menyertakannya dalam daftar
pencocokan). Lookarounds digunakan ketika pola harus
didahului atau diikuti oleh pola lain. Sebagai contoh, bayangkan kita ingin mendapatkan semua
angka yang didahului oleh karakter `$` dari string
`$4.44 and $10.88`. Kita akan menggunakan ekspresi reguler berikut `(?<=\$)[0-9\.]*`
yang berarti: dapatkan semua angka yang mengandung karakter `.` dan didahului
oleh karakter `$`. Berikut adalah lookarounds yang digunakan dalam ekspresi
reguler:

|Simbol|Deskripsi|
|:----:|----|
|?=|Positif Lookahead|
|?!|Negatif Lookahead|
|?<=|Positif Lookbehind|
|?<!|Negatif Lookbehind|

### 4.1 Positif Lookahead

Positif lookahead menegaskan bahwa bagian pertama dari ekspresi harus
diikuti oleh ekspresi lookahead. Pencocokan yang dikembalikan hanya berisi teks
yang dicocokkan oleh bagian pertama dari ekspresi. Untuk mendefinisikan positif
lookahead, tanda kurung digunakan. Di dalam tanda kurung tersebut, tanda tanya dengan
tanda sama dengan digunakan seperti ini: `(?=...)`. Ekspresi lookahead ditulis setelah
tanda sama dengan di dalam tanda kurung. Sebagai contoh, ekspresi reguler
`(T|t)he(?=\sfat)` berarti: cocokkan huruf kecil `t` atau huruf besar
 `T`, diikuti oleh huruf `h`, diikuti oleh huruf `e`. Dalam tanda kurung kita
mendefinisikan positif lookahead yang memberitahu mesin ekspresi reguler untuk mencocokkan `The`
atau `the` hanya jika diikuti oleh kata `fat`.

<pre>
"(T|t)he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/IDDARt/1)

### 4.2 Negatif Lookahead

Negatif lookahead digunakan ketika kita perlu mendapatkan semua pencocokan dari string input
yang tidak diikuti oleh pola tertentu. Negatif lookahead ditulis dengan cara yang sama seperti
positif lookahead. Satu-satunya perbedaan adalah, alih-alih tanda sama dengan `=`, kita
menggunakan tanda seru `!` untuk menunjukkan negasi yaitu `(?!...)`. Mari kita lihat ekspresi reguler berikut
`(T|t)he(?!\sfat)` yang berarti: dapatkan semua kata `The` atau `the`
dari string input yang tidak diikuti oleh karakter spasi dan kata `fat`.

<pre>
"(T|t)he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/V32Npg/1)

### 4.3 Positif Lookbehind

Positif lookbehind digunakan untuk mendapatkan semua pencocokan yang didahului oleh
pola tertentu. Positif lookbehind ditulis `(?<=...)`. Sebagai contoh, ekspresi reguler
`(?<=(T|t)he\s)(fat|mat)` berarti: dapatkan semua kata `fat` atau `mat`
dari string input yang datang setelah kata `The` atau `the`.

<pre>
"(?<=(T|t)he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/avH165/1)

### 4.4 Negatif Lookbehind

Negatif lookbehind digunakan untuk mendapatkan semua pencocokan yang tidak didahului oleh
pola tertentu. Negatif lookbehind ditulis `(?<!...)`. Sebagai contoh, ekspresi reguler
`(?<!(T|t)he\s)(cat)` berarti: dapatkan semua kata `cat` dari string input
yang tidak setelah kata `The` atau `the`.

<pre>
"(?<!(T|t)he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/8Efx5G/1)

## 5. Flags

Flags juga disebut modifier karena mereka memodifikasi output dari ekspresi
reguler. Flags ini dapat digunakan dalam urutan atau kombinasi apa pun, dan merupakan
bagian integral dari RegExp.

|Flag|Deskripsi|
|:----:|----|
|i|Tidak peka huruf: Pencocokan akan tidak peka terhadap huruf besar/kecil.|
|g|Pencarian Global: Cocokkan semua instance, bukan hanya yang pertama.|
|m|Multiline: Karakter meta anchor bekerja pada setiap baris.|

### 5.1 Tidak Peka Huruf

Modifier `i` digunakan untuk melakukan pencocokan yang tidak peka terhadap huruf. Sebagai contoh, ekspresi reguler
`/The/gi` berarti: huruf besar `T`, diikuti oleh huruf kecil
`h`, diikuti oleh `e`. Dan di akhir ekspresi reguler
flag `i` memberitahu mesin ekspresi reguler untuk mengabaikan huruf besar/kecil. Seperti yang Anda bisa
lihat, kita juga menyediakan flag `g` karena kita ingin mencari pola dalam
seluruh string input.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/dpQyf9/1)

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/ahfiuh/1)

### 5.2 Pencarian Global

Modifier `g` digunakan untuk melakukan pencocokan global (menemukan semua pencocokan daripada
berhenti setelah pencocokan pertama). Sebagai contoh, ekspresi reguler `/.(at)/g`
berarti: karakter apa pun kecuali baris baru, diikuti oleh huruf kecil `a`,
diikuti oleh huruf kecil `t`. Karena kita menyediakan flag `g` di akhir
ekspresi reguler, sekarang akan menemukan semua pencocokan dalam string input, bukan hanya yang pertama (yang merupakan perilaku default).

<pre>
"/.(at)/" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/jnk6gM/1)

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/dO1nef/1)

### 5.3 Baris Berganda

Modifier `m` digunakan untuk melakukan pencocokan multi-baris. Seperti yang kita bahas sebelumnya,
anchor `(^, $)` digunakan untuk memeriksa apakah pola berada di awal input atau
di akhir. Tetapi jika kita ingin anchor bekerja pada setiap baris, kita menggunakan
flag `m`. Sebagai contoh, ekspresi reguler `/at(.)?$/gm` berarti: huruf kecil
`a`, diikuti oleh huruf kecil `t` dan, secara opsional, apa pun kecuali
baris baru. Dan karena flag `m`, mesin ekspresi reguler sekarang mencocokkan pola
di akhir setiap baris dalam string.

<pre>
"/.at(.)?$/" => The fat
                cat sat
                on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/hoGMkP/1)

<pre>
"/.at(.)?$/gm" => The <a href="#learn-regex"><strong>fat</strong></a>
                  cat <a href="#learn-regex"><strong>sat</strong></a>
                  on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Uji Ekspresi Reguler](https://regex101.com/r/E88WE2/1)

## 6. Pencocokan Serakah vs Malas
Secara default, regex akan melakukan pencocokan serakah (greedy), yang berarti pencocokan akan selama
mungkin. Kita dapat menggunakan `?` untuk mencocokkan dengan cara malas (lazy), yang berarti pencocokan harus sesingkat mungkin.

<pre>
"/(.*at)/" => <a href="#learn-regex"><strong>The fat cat sat on the mat</strong></a>. </pre>


[Uji Ekspresi Reguler](https://regex101.com/r/AyAdgJ/1)

<pre>
"/(.*?at)/" => <a href="#learn-regex"><strong>The fat</strong></a> cat sat on the mat. </pre>


[Uji Ekspresi Reguler](https://regex101.com/r/AyAdgJ/2)


## Kontribusi

* Buka pull request dengan perbaikan
* Diskusikan ide dalam issues
* Sebarkan informasi
* Hubungi dengan feedback apa pun [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/ziishaned.svg?style=social&label=Follow%20%40ziishaned)](https://twitter.com/ziishaned)

## Lisensi

MIT &copy; [Zeeshan Ahmad](https://twitter.com/ziishaned)
