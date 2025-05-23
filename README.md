# Bookbot

Программа для подсчета общего количества слов и каждого алфавитного символа.

## Зависимости

- Python 3.9+

## Установка

### Репозиторий

Скачайте и распакуйте ZIP
или
```shell
git clone https://github.com/Daniablos/bookbot.git
```

### Poetry

```shell
poetry add git+https://github.com/Daniablos/bookbot.git
```

### PIP

```shell
pip install git+https://github.com/Daniablos/bookbot.git
```

##  Использование

В корне проекта через терминал вводите команду 
```shell
python3 -m bookbot <filename>`
```

Флаг `--words` выводит только кол-во слов

```
=====================BOOKBOT======================
Analyzing book found at books/frankenstein.txt
====================Word Count====================
Found 75767 total words
=================Character Count==================
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
=======================END========================
```
