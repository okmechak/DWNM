---
title: Тестова Сторінка
date: 2019-01-02
modified: 2019-01-02
#category: Різне
tags: markdown, tex, shortcodes, теми
slug: testova-storinka
#additional urls
aliases: test1, test2
#audio:
description: Перевірка в практиці різних властивостей Markdown, Hugo, метаданих. 
  Також різних модулів підключених ззовні, таких як MatJax і інші можливості HTML, які використовуються на веб-сторінці. 
#expiryDate:
#headless:
#images: used by internal templates
#keywords: key1, key2, key3
#layout: if type isn't specified
#lastmod: last modification date
#linkTitle:
#resources:
#series:
#type:
#url: full path to content from root
#videos: og:video
#can be a lot user defined which will be under params field
author: Олег Кмечак
timeofreading: 10 хв
lang: ua  
draft : true
cover_image: test_page.jpg
---

<!-- dependecie of TeX--->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/contrib/auto-render.min.js"></script>

Після деякого часу пошуків статичного генератора для персональної веб-сторінки, зупинився на [HUGO](https://gohugo.io).  

Кілька ключових моментів, чому саме HUGO:  

1. Надзвичайно швидка генерація(вимірюється в мілісекундах).
2. Написаний на мові GO.
3. Інтерактивний:  
Редагуючи сторінки генератор в реальному часі підтягує зміни, що неймовірно полегшує написання статтей(На відміну від генератора Pelican).
Зміни відслідковуються звідусіль. Чи то файл конфігурації, чи то пост, чи нові файли зображеннь.
4. Не складний в користуванні із детальною документацією.
5. Активна спільнота користувачів.  


Наступний крок - це вибір теми. Серед великого числа [різноматніх тем](https://themes.gohugo.io/), обрав [Material-blog](https://themes.gohugo.io/hugo-material-blog/). Про смаки не судять :wink:

Також є важливою для цього сайту підтримка [TeX](https://uk.wikipedia.org/wiki/TeX) - мова розмітки даних, а в особливості написання математичних формул. Наприклад:
{{< tex display = "e^{i\pi} + 1 = 0" >}}.


Різноманітні HTML вставки з інших вебсайтів використовуючи [`<iframe>`](https://www.w3schools.com/tags/tag_iframe.asp), наприклад:
<iframe src="http://free.timeanddate.com/clock/i6kpbav2/n368/tles/tcf90/pc9f0/ftbi/tt0/th2" frameborder="0" width="100%" height="30"></iframe>


І останній пункт - це **Markdown** і [**shortcodes**](https://gohugo.io/content-management/shortcodes/), які є чудовим доповненням до Markdown і широко використовуються в HUGO.


Наразі це весь перелік використаних технологій на цьому сайті. Що ж, Поїхали!





## Markdown

###### [Першоджерело](https://daringfireball.net/projects/markdown/syntax) специфікації Markdown розмітки.

### Заголовки
---


`# Це є h1 таг`   
`## Це є  h2 таг`   
`###### Це є h6 таг`   

Також таг h1 і р2 можуть бути заданими наступним чином:  
`Це є h1 таг`  
`=============`  

`Це є H2 таг`  
`------------`  


Будь яка кількість "-"/"=" буде працювати.

### Виділення тексту
---

Ввівши наступний текст:

`*Цей текст буде похилим*`  
`_Цей текст також буде похилим_`  
`**Це текст буде жирним**`  
`__Цей текст також буде жирним__`  
`_Ти **можеш** комбінувати їх_`  
`~~Цей текст буде закресленим~~`  

Отримaємо:

*Цей текст буде похилим*  
_Цей текст також буде похилим_  
**Це текст буде жирним**  
__Цей текст також буде жирним__  
_Ти **можеш** комбінувати їх_  
~~Цей текст буде закресленим~~  

### Горизонтальна лінія
--- 

Наступний комбінація `---` або ця `___` , згенерує суцільну горизонтальну лінію(але це також залежить від конфігурації css файлу)

---
___



### Списки
___

Використовуючи таби, а також числа(для нумерованих списків), або один із `*`, `-`, `+` символів, можна сворити списки довільної вкладеності:

```
1. Перший по порядку елемент.  
   - Перший піделемент.  
   - Другий піделемент.  
     - Перший підпіделемент.  
     - Другий підпіделемент.  
   - Третій піделемент.  
2. Наступний елемент.  
   1. Перший.  
      1. Перший  
      2. Другий  
   2. Другий.  
3. Номер елементу не має значення.    
   a. Перший.    
   b. Другий.    
4. Останній елемент.   
```

Згенерує:

1. Перший по порядку елемент.  
   - Перший піделемент.  
   - Другий піделемент.  
     - Перший підпіделемент.  
     - Другий підпіделемент.  
   - Третій піделемент.  
2. Наступний елемент.  
   1. Перший.  
      1. Перший  
      2. Другий  
   2. Другий.  
3. Номер елементу не має значення.    
   a. Перший.    
   b. Другий.    
4. Останній елемент.  


### Зображення
---
Можна використати синтаксис MarkDown
`![Avatar](/avatar.png)`
але html `<img>` таг більше котролю, тож:
`<img width ="50%" src="/avatar.png"/>`  
<img width ="50%" src="/avatar.png"/>


### Цитати
---

```
> цитата  

> > цитата цитати   

> > > цитата цитати цитати
```

Згенерує:

> цитата  

> > цитата цитати   

> > > цитата цитати цитати


### Посилання

Посилання бувають трьох видів:  

  - Одразу в тій же лінійці:  
`[якась назва](example.com)`  
[якась назва](example.com)

  - В кінці
`[якась назва][id]`  
`[id]: example.com`  

[якась назва][id]  
[id]: example.com  

Або і ще варіант
`[Google][]`  
`[Google]: google.com`  

[Google][]  
[Google]: google.com  




### Вбудований код
---
Достатньо лише вписати текст в наступні лапки &#96; `<addr>` &#96;  
`<addr>`

    вбудований код теж задається табом(4и пробіли)

#### Підсвітка синтаксису

Аналогічно до вбудованого коду, але цього разу потрібний текст обгортаємо повністю на скільки потрібно лінійок. Також можемо додати мову програмування в кінці перших потрійних лапок, як це є в прикладі.

TODO: Як повінстю підсвітити синтаксис?  

&#96;&#96;&#96;`javascript`  
`function fancyAlert(arg) {`  
    `if(arg) {`  
        `$.facebox({div:'#foo'})`  
    `}`  
`}`  
&#96;&#96;&#96;


```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```   

python код:  
```python
def foo():
    if not bar:
        return True
```

### Список задач
---

TODO: як написати список задач?  

З невідомих наразі причин, цей приклад розмітки - не працює.

`- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported  `  
`- [x] list syntax required (any unordered or ordered list supported)  `  
`- [x] this is a complete item  `  
`- [ ] this is an incomplete item  `  


- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported  
- [x] list syntax required (any unordered or ordered list supported)  
- [x] this is a complete item  
- [ ] this is an incomplete item  



### Таблиця 
---


`Перший заголовок | Другий заголовок`  
`------------ | -------------`  
`Контент із першої клітинки | Контент із другої клітинки`  
`Контент в першому стопчику | Контент в другому стопчику`  

Згенерує:

Перший заголовок | Другий заголовок  
------------ | -------------  
Контент із першої клітинки | Контент із другої клітинки  
Контент в першому стопчику | Контент в другому стопчику  


#### Прилягання

TУДУ: Прилягання з якоїсь причини не працюють.  

Також з допомогою двокрапки ":", можуть бути задані прилягання:  
- по-центру  
- зліва  
- справа  

`|Перший заголовок|Другий заголовок|`  
`|:------------|:-------------:|`  
`|Контент із першої клітинки | Контент із другої клітинки|`  
`|Контент в першому стопчику | Контент в другому стопчику|`  

Згенeрує:


|Перший заголовок|Другий заголовок|
|:------------|:-------------:|
|Контент із першої клітинки | Контент із другої клітинки|  
|Контент в першому стопчику | Контент в другому стопчику|  


  



### Емотікони
---

Спочатку їх треба активувати у файлі конфігурації config.toml додавши наступний рядок:


```
enableEmoji = true
```

Після цього можна використовувати стандартні коди для емотіконів, наприклда &#58;smile&#58; згенерує:
:smile:


### HTML
---

Наразі це тільки різноманітні вставки з допомогою тегу `<iframe>`, наприклад відео з ютубу:

`<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">`
`    <iframe src="https://www.youtube.com/embed/RavnmzMRrnw" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width:100%;height:100%"/>`
`</div>`   

Зробить звичайну вставку відео:

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
    <iframe src="https://www.youtube.com/embed/RavnmzMRrnw" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>   



## Математичні формули
---

[Хороша стаття](http://www.latkin.org/blog/2016/08/07/better-tex-math-typesetting-in-hugo/) про підключення TeX в HUGO, що власне використовується і на цьому сайті.  

Сума в одному рядку:  
{{< tex "\sum_{n=1}^{\infty} 2^{-n} = 1" >}}.

Режим нового рядка:  
{{< tex display="\int \frac{1}{x} dx = \ln |x|" >}}



## Shortcodes
---
[Документація](https://gohugo.io/templates/shortcode-templates/)
ТУДУ: описати

## Візуальні Теми
---

[Документація](https://gohugo.io/themes/)

ТУДУ: описати різні те як використовувати і писати власні чи модифікувати існуючі теми.






<!-- dependecie of TeX--->
<script>renderMathInElement(document.body);</script>