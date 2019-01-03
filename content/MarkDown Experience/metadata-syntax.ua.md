---
title: MarkDown
date: 2018-06-24
modified: 2018-06-24
category: Різне
tags: pelican, learning, markdown
slug: cool-cafe
#additional urls
aliases: test1, test2
#audio:
description: Markdown metadata feature testing
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
authors: Oleg Kmechak
lang: ua  
draft : true  
---

# Headers
---

These statements:

`# This is an <h1> tag`   
`## This is an <h2> tag`   
`###### This is an <h6> tag`   

will give:

# This is an `<h1>` tag
## This is an `<h2>` tag
###### This is an `<h6>` tag



# Emphasis
---

`*This text will be italic*`  
`_This will also be italic_`  
`**This text will be bold**`  
`__This will also be bold__`  
`_You **can** combine them_`  
`~~This will striked throug~~`  


*This text will be italic*  
_This will also be italic_  
**This text will be bold**  
__This will also be bold__  
_You **can** combine them_  
~~This will striked throug~~  

# Line
--- 

this statetment `---` or this `___` , will give line

---



# Lists
___
(In this example, leading and trailing spaces are shown with with dots: ⋅)
#### Unordered

1. First ordered list item
2. Another item
⋅⋅* Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
⋅⋅1. Ordered sub-list
4. And another item.

⋅⋅⋅You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

⋅⋅⋅To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
⋅⋅⋅Note that this line is separate, but within the same paragraph.⋅⋅
⋅⋅⋅(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks
- Or minuses
+ Or pluses

# Images
---
You can use this statement
`![Avatar](/avatar.png)`
but html `<img>` tag provides more control, so:
`<img width ="50%" src="/avatar.png"/>`  
<img width ="50%" src="/avatar.png"/>
Quotes
---
>quote  

> > quote of quote   

> > > quote of quote of quote



# Inline code
---
Simply put your text into next quotes &#96; `<addr>` &#96;  
`<addr>`

# Syntax Highlight
---

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

python code:
```python
def foo():
    if not bar:
        return True
```
# Task List
---

For some reason don't work

`- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported  `  
`- [x] list syntax required (any unordered or ordered list supported)  `  
`- [x] this is a complete item  `  
`- [ ] this is an incomplete item  `  


- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported  
- [x] list syntax required (any unordered or ordered list supported)  
- [x] this is a complete item  
- [ ] this is an incomplete item  



# Table 
---


`First Header | Second Header`  
`------------ | -------------`  
`Content from cell 1 | Content from cell 2`  
`Content in the first column | Content in the second column`  



First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

# Emojies
---
At first you should enable it in config.toml file by putting
```
enableEmoji = true
```

after that you can use standard codes of smiley &#58;smile&#58; will give:
:smile:

# HTML addons
---

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
    <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>   



lala
