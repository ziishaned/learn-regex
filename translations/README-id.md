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
* [Bahasa Indonesia](translations/README-id.md)
* [فارسی](translations/README-fa.md)
* [עברית](translations/README-he.md)


## Apa itu Ekspresi Reguler?

<p>
    <a href="https://gum.co/learn-regex">
        <img src="https://img.shields.io/badge/-Download%20PDF%20-0a0a0a.svg?style=flat&colorA=0a0a0a" alt="Download PDF">
    </a>
</p>

> Ekspresi reguler adalah sekelompok karakter atau simbol yang digunakan untuk menemukan pola tertentu dalam sebuah teks.

Ekspresi reguler adalah pola yang dicocokkan dengan string subjek dari
kiri ke kanan. Ekspresi reguler digunakan untuk mengganti teks dalam string,
memvalidasi formulir, mengekstrak substring dari string berdasarkan kecocokan pola,
dan masih banyak lagi. Istilah "ekspresi reguler" adalah suap, jadi kamu biasanya akan
temukan istilah yang disingkat "regex" atau "regexp". 

Bayangkan Anda sedang menulis aplikasi dan Anda ingin menetapkan aturan kapan a
pengguna memilih nama pengguna mereka. Kami ingin mengizinkan nama pengguna berisi huruf,
angka, garis bawah, dan tanda hubung. Kami juga ingin membatasi jumlah karakter
di username agar tidak terlihat jelek. Kita dapat menggunakan ekspresi reguler berikut untuk
memvalidasi nama pengguna:

<br/><br/>
<p align="center">
  <img src="./img/regexp-en.png" alt="Regular expression">
</p>

Ekspresi reguler di atas dapat menerima string `john_doe`, `jo-hn_doe` dan
`john12_as`. Itu tidak cocok dengan `Jo` karena string itu berisi huruf besar
surat dan juga terlalu pendek.

## Table of Contents

- [Pencocokan Dasar](#1-basic-matchers)
- [Karakter Meta](#2-meta-characters)
  - [Perhentian Penuh](#21-the-full-stop)
  - [Set Karakter](#22-character-sets)
    - [Set Karakter yang Dinegasikan](#221-negated-character-sets)
  - [Pengulangan](#23-repetitions)
    - [Tanda Bintang](#231-the-star)
    - [Tanda Tambah](#232-the-plus)
    - [Tanda Tanya](#233-the-question-mark)
  - [Kurung Kurawal](#24-braces)
  - [Menangkap Grup](#25-capturing-groups)
      - [Grup yang Tidak Menangkap](#251-non-capturing-groups)
  - [Alternasi](#26-alternation)
  - [Karakter Spesial](#27-escaping-special-characters)
  - [Anchor Text](#28-anchors)
    - [Tanda Sisipan](#281-the-caret)
    - [Tanda Dollar](#282-the-dollar-sign)
- [Set Karakter Singkatan](#3-shorthand-character-sets)
- [Melihat](#4-lookarounds)
  - [Pandangan ke Depan Positif](#41-positive-lookahead)
  - [Pandangan ke Depan Negatif](#42-negative-lookahead)
  - [Pandangan Positif ke Belakang](#43-positive-lookbehind)
  - [Pandangan negatif ke belakang](#44-negative-lookbehind)
- [Bendera](#5-flags)
  - [Tidak peka huruf besar/kecil](#51-case-insensitive)
  - [Pencarian Global](#52-global-search)
  - [Multiline](#53-multiline)
- [Greedy vs Lazy Matching](#6-greedy-vs-lazy-matching)

## 1. Pencocokan Dasar

Ekspresi reguler hanyalah pola karakter yang kita gunakan untuk melakukan
pencarian dalam sebuah teks. Misalnya, ekspresi reguler `the` berarti: huruf
`t`, diikuti huruf `h`, diikuti huruf `e`.

<pre>
"the" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/dmRygT/1)

Ekspresi reguler `123` cocok dengan string `123`. Ekspresi reguler adalah
dicocokkan dengan string input dengan membandingkan setiap karakter di reguler
ekspresi ke setiap karakter dalam string input, satu demi satu. Reguler
ekspresi biasanya peka huruf besar/kecil sehingga ekspresi reguler `The` akan
tidak cocok dengan string `the`.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/1paXsy/1)

## 2. Karakter Meta

Karakter meta adalah blok bangunan ekspresi reguler. Meta
karakter tidak berdiri sendiri tetapi sebaliknya ditafsirkan dalam beberapa
cara spesial. Beberapa karakter meta memiliki arti khusus dan tertulis di dalamnya
tanda kurung siku. Karakter metanya adalah sebagai berikut:

|Meta karakter|Deskripsi|
|:----:|----|
|.|Titik cocok dengan karakter tunggal apa pun kecuali jeda baris.|
|[ ]|Kelas karakter. Mencocokkan karakter apa pun yang ada di antara tanda kurung siku.|
|[^ ]|Kelas karakter yang dinegasikan. Cocok dengan karakter apa pun yang tidak ada di antara tanda kurung siku|
|*|Mencocokkan dengan 0 atau lebih pengulangan dari simbol sebelumnya.|
|+|Mencocokkan 1 atau lebih pengulangan dari simbol sebelumnya.|
|?|Jadikan simbol sebelumnya opsional.|
|{n,m}|Kurung Kurawal. Mencocokkan setidaknya "n" tetapi tidak lebih dari "m" pengulangan simbol sebelumnya.|
|(xyz)|Kelompok karakter. Mencocokkan karakter xyz dalam urutan yang tepat.|
|&#124;|Alternasi. Mencocokkan dengan karakter sebelum atau karakter setelah simbol.|
|&#92;|Meloloskan dari karakter berikutnya. Ini memungkinkan Anda untuk mencocokkan karakter yang dipesan <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>|
|^|Mencocokkan dengan awal input.|
|$|Mencocokkan dengan akhir input.|

## 2.1 Perhentian Penuh

Tanda titik `.` adalah contoh paling sederhana dari karakter meta. Karakter meta `.`
cocok dengan karakter tunggal apa pun. Itu tidak akan cocok dengan karakter kembali atau baris baru.
Misalnya, ekspresi reguler `.ar` berarti: karakter apa pun, diikuti oleh
huruf `a`, diikuti dengan huruf `r`.

<pre>
".ar" => The <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/xc9GkU/1)

## 2.2 Set Karakter

Kumpulan karakter juga disebut kelas karakter. Tanda kurung siku digunakan untuk
menentukan set karakter. Gunakan tanda hubung di dalam set karakter untuk menentukan
jangkauan karakter. Urutan rentang karakter di dalam tanda kurung siku
tidak masalah. Misalnya, ekspresi reguler `[Tt]he` berarti: huruf besar
`T` atau huruf kecil `t`, diikuti huruf `h`, diikuti huruf `e`.

<pre>
"[Tt]he" => <a href="#learn-regex"><strong>The</strong></a> car parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/2ITLQ4/1)

Sebuah periode di dalam set karakter, bagaimanapun, berarti periode literal. yang biasa
ekspresi `ar[.]` berarti: karakter huruf kecil `a`, diikuti dengan huruf `r`,
diikuti dengan karakter titik `.`.

<pre>
"ar[.]" => A garage is a good place to park a c<a href="#learn-regex"><strong>ar.</strong></a>
</pre>

[Uji ekspresi reguler](https://regex101.com/r/wL3xtE/1)

### 2.2.1 Set Karakter yang Dinegasikan

Secara umum, simbol tanda sisipan mewakili awal string, tetapi ketika itu
diketik setelah kurung siku pembuka itu meniadakan set karakter. Untuk
contoh, ekspresi reguler `[^c]ar` berarti: karakter apa pun kecuali `c`,
diikuti dengan karakter `a`, diikuti dengan huruf `r`.

<pre>
"[^c]ar" => The car <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/nNNlq3/1)

## 2.3 Pengulangan

Karakter meta `+`, `*` atau `?` digunakan untuk menentukan berapa kali a
subpola dapat terjadi. Karakter meta ini bertindak secara berbeda di berbagai
situasi.

### 2.3.1 Tanda Bintang

Simbol `*` cocok dengan nol atau lebih pengulangan dari pencocokan sebelumnya. Itu
ekspresi reguler `a*` berarti: nol atau lebih pengulangan dari huruf kecil sebelumnya
karakter `a`. Tetapi jika itu muncul setelah set karakter atau kelas maka ia menemukan
pengulangan seluruh set karakter. Misalnya, ekspresi reguler
`[a-z]*` artinya: sejumlah huruf kecil dalam satu baris.

<pre>
"[a-z]*" => T<a href="#learn-regex"><strong>he</strong></a> <a href="#learn-regex"><strong>car</strong></a> <a href="#learn-regex"><strong>parked</strong></a> <a href="#learn-regex"><strong>in</strong></a> <a href="#learn-regex"><strong>the</strong></a> <a href="#learn-regex"><strong>garage</strong></a> #21.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/7m8me5/1)

Simbol `*` dapat digunakan dengan karakter meta `.` untuk mencocokkan string apa pun dari
karakter `.*`. Simbol `*` dapat digunakan dengan karakter spasi putih `\s`
untuk mencocokkan string karakter spasi. Misalnya, ungkapan
`\s*cat\s*` artinya: nol spasi atau lebih, diikuti dengan huruf kecil `c`,
diikuti dengan huruf kecil `a`, diikuti dengan huruf kecil `t`,
diikuti oleh nol atau lebih spasi.

<pre>
"\s*cat\s*" => The fat<a href="#learn-regex"><strong> cat </strong></a>sat on the con<a href="#learn-regex"><strong>cat</strong></a>enation.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/gGrwuz/1)

### 2.3.2 Tanda Tambah

Simbol `+` cocok dengan satu atau lebih pengulangan karakter sebelumnya. Untuk
contoh, ekspresi reguler `c.+t` berarti: huruf kecil `c`, diikuti oleh
setidaknya satu karakter, diikuti dengan huruf kecil `t`. Itu perlu
mengklarifikasi bahwa `t` adalah `t` terakhir dalam kalimat.

<pre>
"c.+t" => The fat <a href="#learn-regex"><strong>cat sat on the mat</strong></a>.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/Dzf9Aa/1)

### 2.3.3 Tanda Tanya

Dalam ekspresi reguler, karakter meta `?` membuat karakter sebelumnya
opsional. Simbol ini cocok dengan nol atau satu contoh karakter sebelumnya.
Misalnya, ekspresi reguler `[T]?he` artinya: Huruf besar opsional
`T`, diikuti dengan huruf kecil `h`, diikuti dengan huruf kecil `e`.

<pre>
"[T]he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/cIg9zm/1)

<pre>
"[T]?he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in t<a href="#learn-regex"><strong>he</strong></a> garage.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/kPpO2x/1)

## 2.4 Braces

Dalam ekspresi reguler, kurung kurawal (juga disebut quantifier) ​​digunakan untuk
tentukan berapa kali karakter atau sekelompok karakter dapat
ulang. Misalnya, ekspresi reguler `[0-9]{2,3}` berarti: Setidaknya cocok
2 digit, tetapi tidak lebih dari 3, mulai dari 0 hingga 9.

<pre>
"[0-9]{2,3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/juM86s/1)

Kita bisa meninggalkan nomor kedua. Misalnya, ekspresi reguler
`[0-9]{2,}` berarti: Mencocokkan 2 digit atau lebih. Jika kita juga menghapus koma,
ekspresi reguler `[0-9]{3}` berarti: Sama persis dengan 3 digit.

<pre>
"[0-9]{2,}" => The number was 9.<a href="#learn-regex"><strong>9997</strong></a> but we rounded it off to <a href="#learn-regex"><strong>10</strong></a>.0.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/Gdy4w5/1)

<pre>
"[0-9]{3}" => The number was 9.<a href="#learn-regex"><strong>999</strong></a>7 but we rounded it off to 10.0.
</pre>

[Test the regular expression](https://regex101.com/r/Sivu30/1)

## 2.5 Menangkap Grup

Grup penangkap adalah grup subpola yang ditulis di dalam tanda kurung
`(...)`. Seperti yang dibahas sebelumnya, dalam ekspresi reguler, jika kita menempatkan quantifier
setelah karakter maka akan mengulangi karakter sebelumnya. Tetapi jika kita menempatkan quantifier
setelah grup penangkap kemudian mengulangi seluruh grup penangkap. Sebagai contoh,
ekspresi reguler `(ab)*` cocok dengan nol atau lebih pengulangan karakter
"ab". Kita juga dapat menggunakan karakter meta `|` bergantian di dalam grup penangkap.
Misalnya, ekspresi reguler `(c|g|p)ar` berarti: huruf kecil `c`,
`g` atau `p`, diikuti oleh `a`, diikuti oleh `r`.

<pre>
"(c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/tUxrBG/1)

Perhatikan bahwa menangkap grup tidak hanya cocok, tetapi juga menangkap, karakter untuk digunakan dalam
bahasa induk. Bahasa induk bisa berupa Python atau JavaScript atau hampir semua
bahasa yang mengimplementasikan ekspresi reguler dalam definisi fungsi.

### 2.5.1 Grup yang Tidak Menangkap

Grup yang tidak menangkap adalah grup yang cocok dengan karakter tetapi
tidak menangkap kelompok. Grup yang tidak menangkap dilambangkan dengan `?` diikuti oleh `:`
dalam tanda kurung `(...)`. Misalnya, ekspresi reguler `(?:c|g|p)ar` mirip dengan
`(c|g|p)ar` karena cocok dengan karakter yang sama tetapi tidak akan membuat grup tangkapan.

<pre>
"(?:c|g|p)ar" => The <a href="#learn-regex"><strong>car</strong></a> is <a href="#learn-regex"><strong>par</strong></a>ked in the <a href="#learn-regex"><strong>gar</strong></a>age.
</pre>

[Test the regular expression](https://regex101.com/r/Rm7Me8/1)

Grup yang tidak menangkap dapat berguna saat digunakan dalam fungsi temukan-dan-ganti atau
ketika dicampur dengan grup penangkap untuk menjaga gambaran umum saat memproduksi jenis keluaran lainnya.
Lihat juga [4. Melihat-lihat](#4-lookaround).

## 2.6 Alternasi

Dalam ekspresi reguler, bilah vertikal `|` digunakan untuk mendefinisikan pergantian.
Pergantian seperti pernyataan OR antara beberapa ekspresi. Sekarang, Anda mungkin
berpikir bahwa set karakter dan pergantian bekerja dengan cara yang sama. Tapi yang besar
perbedaan antara set karakter dan pergantian adalah bahwa set karakter bekerja di
tingkat karakter tetapi pergantian bekerja pada tingkat ekspresi. Misalnya,
ekspresi reguler `(T|t)he|car` berarti: baik (huruf besar `T` atau huruf kecil
`t`, diikuti dengan huruf kecil `h`, diikuti dengan huruf kecil `e`) ATAU
(huruf kecil `c`, diikuti dengan huruf kecil `a`, diikuti oleh
huruf kecil `r`). Perhatikan bahwa saya menyertakan tanda kurung untuk kejelasan, untuk menunjukkan bahwa salah satu ekspresi
dalam tanda kurung dapat dipenuhi dan itu akan cocok.

<pre>
"(T|t)he|car" => <a href="#learn-regex"><strong>The</strong></a> <a href="#learn-regex"><strong>car</strong></a> is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/fBXyX0/1)

## 2.7 Karakter Spesial

Garis miring terbalik `\` digunakan dalam ekspresi reguler untuk keluar dari karakter berikutnya. Ini
memungkinkan kita untuk menyertakan karakter yang dicadangkan seperti `{ } [ ] / \ + * . $ ^ | ?` sebagai karakter yang cocok. Untuk menggunakan salah satu karakter khusus ini sebagai karakter yang cocok, awali dengan `\`.

Misalnya, ekspresi reguler `.` digunakan untuk mencocokkan karakter apa pun kecuali a
garis baru. Sekarang, untuk mencocokkan `.` dalam string input, ekspresi reguler
`(f|c|m)at\.?` artinya: huruf kecil `f`, `c` atau `m`, diikuti dengan huruf kecil
`a`, diikuti dengan huruf kecil `t`, diikuti dengan `.` . opsional
karakter.

<pre>
"(f|c|m)at\.?" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> sat on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Test the regular expression](https://regex101.com/r/DOc5Nu/1)

## 2.8 Anchor Text

Dalam ekspresi reguler, kami menggunakan jangkar untuk memeriksa apakah simbol yang cocok adalah
simbol awal atau simbol akhir dari string input. Jangkar terdiri dari dua jenis:
Tipe pertama adalah tanda sisipan `^` yang memeriksa apakah karakter yang cocok adalah yang pertama
karakter input dan tipe kedua adalah tanda dolar `$` yang memeriksa apakah cocok
karakter adalah karakter terakhir dari string input.

### 2.8.1 Tanda Sisipan

Simbol tanda sisipan `^` digunakan untuk memeriksa apakah karakter yang cocok adalah karakter pertama
dari string masukan. Jika kita menerapkan ekspresi reguler berikut `^a` (artinya 'a' harus
karakter awal) ke string `abc`, itu akan cocok dengan `a`. Tapi jika kita melamar
ekspresi reguler `^b` ke string di atas, itu tidak akan cocok dengan apa pun.
Karena dalam string `abc`, "b" bukanlah karakter awal. Mari lihat
di ekspresi reguler lain `^(T|t)he` yang artinya: huruf besar `T` atau
huruf kecil `t` harus menjadi karakter pertama dalam string, diikuti oleh a
huruf kecil `h`, diikuti dengan huruf kecil `e`.

<pre>
"(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in <a href="#learn-regex"><strong>the</strong></a> garage.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/5ljjgB/1)

<pre>
"^(T|t)he" => <a href="#learn-regex"><strong>The</strong></a> car is parked in the garage.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/jXrKne/1)

### 2.8.2 Tanda Dolar

Tanda dolar `$` digunakan untuk memeriksa apakah karakter yang cocok adalah karakter terakhir
dalam tali. Misalnya, ekspresi reguler `(at\.)$` berarti: a
huruf kecil `a`, diikuti dengan huruf kecil `t`, diikuti oleh `.`
karakter dan matcher harus berada di akhir string.

<pre>
"(at\.)" => The fat c<a href="#learn-regex"><strong>at.</strong></a> s<a href="#learn-regex"><strong>at.</strong></a> on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Uji ekspresi reguler](https://regex101.com/r/y4Au4D/1)

<pre>
"(at\.)$" => The fat cat. sat. on the m<a href="#learn-regex"><strong>at.</strong></a>
</pre>

[Uji ekspresi reguler](https://regex101.com/r/t0AkOd/1)

##  3. Set Karakter Singkatan

Ada sejumlah singkatan yang mudah digunakan untuk set karakter yang umum digunakan/
ekspresi reguler:

|Singkatan|Deskripsi|
|:----:|----|
|.|Karakter apa pun kecuali baris baru|
|\w|Mencocokkan karakter alfanumerik: `[a-zA-Z0-9_]`|
|\W|Mencocokkan karakter non-alfanumerik: `[^\w]`|
|\d|Mencocokkan digit: `[0-9]`|
|\D|Mencocokkan non-digit: `[^\d]`|
|\s|Mencocokkan karakter spasi putih: `[\t\n\f\r\p{Z}]`|
|\S|Mencocokkan karakter non-spasi: `[^\s]`|

## 4. Melihat-lihat

Melihat ke belakang dan melihat ke depan (juga disebut melihat sekeliling) adalah jenis tertentu dari
***grup non-penangkapan*** (digunakan untuk mencocokkan pola tetapi tanpa menyertakannya dalam pencocokan
daftar). Lookarounds digunakan ketika sebuah pola harus
didahului atau diikuti oleh pola lain. Misalnya, bayangkan kita ingin mendapatkan semua
angka yang didahului oleh karakter `$` dari string
`$4,44 dan $10,88`. Kami akan menggunakan ekspresi reguler berikut `(?<=\$)[0-9\.]*`
yang artinya: dapatkan semua angka yang mengandung karakter `.` dan didahului
oleh karakter `$`. Ini adalah lookaround yang biasa digunakan
ekspresi:

|Simbol|Deskripsi|
|:----:|----|
|?=|Pandangan ke Depan Positif|
|?!|Melihat ke Depan Negatif|
|?<=|Tampilan Positif di Belakang|
|?<!|Tampilan Negatif di Belakang|

### 4.1 Pandangan ke Depan Positif

Pandangan ke depan positif menegaskan bahwa bagian pertama dari ekspresi harus
diikuti oleh ekspresi lookahead. Pertandingan yang dikembalikan hanya berisi teks
yang dicocokkan dengan bagian pertama dari ekspresi. Untuk mendefinisikan positif
lookahead, tanda kurung digunakan. Di dalam tanda kurung itu, tanda tanya dengan
tanda sama dengan digunakan seperti ini: `(?=...)`. Ekspresi lookahead ditulis setelah
tanda sama dengan di dalam kurung. Misalnya, ekspresi reguler
`(T|t)he(?=\sfat)` artinya: cocok dengan huruf kecil `t` atau huruf besar
 `T`, diikuti huruf `h`, diikuti huruf `e`. Dalam tanda kurung kita
mendefinisikan lookahead positif yang memberitahu mesin ekspresi reguler untuk mencocokkan `The`
atau `the` hanya jika diikuti oleh kata `fat`.

<pre>
"(T|t)he(?=\sfat)" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/IDDARt/1)

### 4.2 Pandangan ke Depan Negatif

Pandangan negatif ke depan digunakan ketika kita perlu mendapatkan semua kecocokan dari string input
yang tidak mengikuti pola tertentu. Sebuah lookahead negatif ditulis dengan cara yang sama seperti a
pandangan positif ke depan. Satu-satunya perbedaan adalah, alih-alih tanda sama dengan `=`, kami
gunakan tanda seru `!` untuk menunjukkan negasi yaitu `(?!...)`. Yuk simak berikut ini
ekspresi reguler `(T|t)he(?!\sfat)` yang artinya: dapatkan semua kata `The` atau `the`
dari string input yang tidak diikuti oleh karakter spasi dan kata `fat`.

<pre>
"(T|t)he(?!\sfat)" => The fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Test the regular expression](https://regex101.com/r/V32Npg/1)

### 4.3 Pandangan Positif ke Belakang

Positif melihat ke belakang digunakan untuk mendapatkan semua kecocokan yang didahului oleh a
pola tertentu. Positif lookbehinds ditulis `(?<=...)`. Misalnya,
ekspresi reguler `(?<=(T|t)he\s)(fat|mat)` artinya: dapatkan semua kata `fat` atau `mat`
dari string input yang datang setelah kata `The` atau `the`.

<pre>
"(?<=(T|t)he\s)(fat|mat)" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Test the regular expression](https://regex101.com/r/avH165/1)

### 4.4 Pandangan negatif ke belakang

Pandangan belakang negatif digunakan untuk mendapatkan semua kecocokan yang tidak didahului oleh a
pola tertentu. Tampilan negatif di belakang ditulis `(?<!...)`. Misalnya,
ekspresi reguler `(?<!(T|t)he\s)(cat)` artinya: dapatkan semua kata `cat` dari input
string yang tidak setelah kata `The` atau `the`.

<pre>
"(?&lt;!(T|t)he\s)(cat)" => The cat sat on <a href="#learn-regex"><strong>cat</strong></a>.
</pre>

[Test the regular expression](https://regex101.com/r/8Efx5G/1)

## 5. Bendera

Bendera juga disebut pengubah karena mereka memodifikasi output dari regular
ekspresi. Bendera ini dapat digunakan dalam urutan atau kombinasi apa pun, dan merupakan
bagian integral dari RegExp.

|Bendera|Deskripsi|
|:----:|----|
|i|Tidak peka huruf besar/kecil: Pencocokan tidak peka huruf besar/kecil.|
|g|Penelusuran Global: Cocokkan semua instance, bukan hanya yang pertama.|
|m|Multiline: Karakter meta jangkar bekerja di setiap baris.|

### 5.1 Tidak peka huruf besar/kecil

Pengubah `i` digunakan untuk melakukan pencocokan case-insensitive. Misalnya,
ekspresi reguler `/The/gi` berarti: huruf besar `T`, diikuti dengan huruf kecil
`h`, diikuti oleh `e`. Dan di akhir ekspresi reguler
flag `i` memberitahu mesin ekspresi reguler untuk mengabaikan kasus ini. Sebisa kamu
lihat, kami juga menyediakan flag `g` karena kami ingin mencari pola di
seluruh string masukan.

<pre>
"The" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on the mat.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/dpQyf9/1)

<pre>
"/The/gi" => <a href="#learn-regex"><strong>The</strong></a> fat cat sat on <a href="#learn-regex"><strong>the</strong></a> mat.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/ahfiuh/1)

### 5.2 Pencarian Global

Pengubah `g` digunakan untuk melakukan kecocokan global (menemukan semua kecocokan daripada
berhenti setelah pertandingan pertama). Misalnya, ekspresi reguler`/.(at)/g`
berarti: karakter apa pun kecuali baris baru, diikuti dengan huruf kecil `a`,
diikuti dengan huruf kecil `t`. Karena kami menyediakan flag `g` di akhir
ekspresi reguler, sekarang akan menemukan semua kecocokan dalam string input, bukan hanya yang pertama (yang merupakan perilaku default).

<pre>
"/.(at)/" => The <a href="#learn-regex"><strong>fat</strong></a> cat sat on the mat.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/jnk6gM/1)

<pre>
"/.(at)/g" => The <a href="#learn-regex"><strong>fat</strong></a> <a href="#learn-regex"><strong>cat</strong></a> <a href="#learn-regex"><strong>sat</strong></a> on the <a href="#learn-regex"><strong>mat</strong></a>.
</pre>

[Uji ekspresi reguler](https://regex101.com/r/dO1nef/1)

### 5.3 Multiline

Pengubah `m` digunakan untuk melakukan pencocokan multi-baris. Seperti yang telah kita bahas sebelumnya,
jangkar `(^, $)` digunakan untuk memeriksa apakah suatu pola ada di awal input atau
tamat. Tetapi jika kita ingin jangkar bekerja pada setiap baris, kita menggunakan
bendera `m`. Misalnya, ekspresi reguler `/at(.)?$/gm` berarti: huruf kecil
`a`, diikuti dengan huruf kecil `t` dan, opsional, apa pun kecuali
baris baru. Dan karena flag `m`, mesin ekspresi reguler sekarang cocok dengan pola
di akhir setiap baris dalam sebuah string.

<pre>
"/.at(.)?$/" => The fat
                cat sat
                on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Uji ekspresi reguler](https://regex101.com/r/hoGMkP/1)

<pre>
"/.at(.)?$/gm" => The <a href="#learn-regex"><strong>fat</strong></a>
                  cat <a href="#learn-regex"><strong>sat</strong></a>
                  on the <a href="#learn-regex"><strong>mat.</strong></a>
</pre>

[Uji ekspresi reguler](https://regex101.com/r/E88WE2/1)

## 6. Greedy vs Lazy Matching
Secara default, regex akan melakukan kecocokan greedy, yang berarti kecocokan akan berlangsung selama
mungkin. Kita dapat menggunakan `?` untuk mencocokkan dengan cara yang lazy, yang berarti pencocokan harus sesingkat mungkin.

<pre>
"/(.*at)/" => <a href="#learn-regex"><strong>The fat cat sat on the mat</strong></a>. </pre>


[Uji ekspresi reguler](https://regex101.com/r/AyAdgJ/1)

<pre>
"/(.*?at)/" => <a href="#learn-regex"><strong>The fat</strong></a> cat sat on the mat. </pre>


[Uji ekspresi reguler](https://regex101.com/r/AyAdgJ/2)


## Kontribusi

* Buka pull request dengan peningkatan
* Diskusikan ide dalam issue
* Sebarkan materinya
* Jangkau dengan umpan balik apa pun [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/ziishaned.svg?style=social&label=Follow%20%40ziishaned)](https://twitter.com/ziishaned)

## Lisensi

MIT &copy; [Zeeshan Ahmad](https://twitter.com/ziishaned)
