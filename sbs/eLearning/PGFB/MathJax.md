*Contents*:

- [MathML](#mathml)
- [MathJax LIBRARY](#mathjax-library)
    + [CONFIG Options](#config-options)
    + [REMOTE Inclusion](#remote-inclusion)
    + [LOCAL Inclusion](#local-inclusion)
- [EXAMPLE (of default/STATIC rendering)](#example-of-defaultstatic-rendering)
- ['DYNAMIC Rendering'...](#dynamic-rendering)
    + [Example](#example)
    + [Method](#method)

----

## MathML

- http://caniuse.com/#search=math

    - Only 2 (mainstream) web-browsers have _built-in_ **MathML**: *Firefox* and *Safari*.

    - (The others need the **_MathJax_** library to render MathML.)

----

## MathJax Library

#### CONFIG Options

- Loading and Configuring MathJax: http://docs.mathjax.org/en/latest/configuration.html#loading-and-configuring-mathjax

```
config=TeX-AMS-MML_HTMLorMML
```

:mag:  ``mathjax  contrib/a11y/accessibility-menu.js``

- https://github.com/mathjax/MathJax-a11y/tree/master/docs
    - http://docs.mathjax.org/en/latest/options/ThirdParty.html#mathjax-third-party-extension-repository

> MathJax.js?config=...&noContrib

```
noContrib
```

- Hence, append ``?config=TeX-AMS-MML_HTMLorMML&noContrib``

#### REMOTE Inclusion

- Main/init file: ``https://cdn.mathjax.org/mathjax/latest/MathJax.js``

```html
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML&noContrib" type="text/javascript"></script>
```

#### LOCAL Inclusion

- https://github.com/mathjax/MathJax/releases
    - https://github.com/mathjax/MathJax/archive/2.7.0.zip

For v2.7.0, when ``MathJax-2.7.0.zip`` is extracted, the (32000!) files are approx. **60MB** in size.

These (26!) files are the **bare minimum** for my purposes: (determined by 'trial & error')


```
__LIB__/mathjax/MathJax.js
                config/TeX-AMS-MML_HTMLorMML.js
                extensions/MathMenu.js
                           MathZoom.js
                fonts/HTML-CSS/TeX/woff/*
                jax/output/HTML-CSS/jax.js
                                    fonts/TeX/fontdata.js
```


- Main/init file: ``MathJax.js``

```html
<script src="__LIB__/mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML&noContrib" type="text/javascript"></script>
```

----

## Example (of default/STATIC rendering)

- http://jsfiddle.net/9BCGx/36/

----

## 'DYNAMIC Rendering'...

:mag:  ``mathjax  DYNAMIC RENDERING``

- http://stackoverflow.com/questions/22442611/render-mathjax-dynamically

- https://cdn.mathjax.org/mathjax/latest/test/sample-dynamic-2.html
> `` MathJax.Hub.Queue``


:mag:  ``MathJax.Hub.Queue``

- http://stackoverflow.com/questions/7926233/display-mathjax-dynamically-only-when-there-are-delimiters
    - http://jsfiddle.net/Zky72/2/

> `` MathJax.Hub.Queue(["Typeset", MathJax.Hub, "MathOutput"]); ``

#### Example

- http://jsfiddle.net/Zky72/209/

Either **TeX** or **MathML** can be typed.

(**TeX** needs to be enclosed in ``$``, e.g. ``$ x^2 + y^3 $``) 

#### Method

```javascript
$(document).ready(function() {

  // get HTML elements/tags ('DIV's whose id starts with "fb" and have a MATH elt/tag)
  // !! :has() is succinct, but NOT portable ~ https://api.jquery.com/has-selector/
  var elts = $('div[id^="fb"]:has(math)');
  
  // RENDER the elements, each of which must have an id
  for (var i = 0; i < elts.length; i++) {
    MathJax.Hub.Queue(["Typeset", MathJax.Hub, $(elts[i]).attr('id')]);
  }

});
```
