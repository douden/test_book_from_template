# Iframe stuff

## Introduction

This extension provides an interface to include iframes with relative ease, but does try to provide manners to interact with the various options. This rests purely by setting default CSS values, that the user can overwrite if preferred. In general, each `iframe` is embedded within a `div` element, which eases sizing. 

::::{note}
Using CSS is complicated and error prone, so always check and never expect that you get what you want.
::::

## Configuration choices

The extension provides some configuration values, which can be added to:

```yaml
sphinx: 
    config:
        .
        .
        .
        iframe_blend_all: true # default value
        iframe_saturation: 1.5 # default value
        iframe_h5p_autoresize: true # default value
        iframe_background: #ffffff # default value
        .
        .
        .
```

- `iframe_blend_all`: `true` (_default_) or `false`:
  - if `true` all iframes are by default blended with the background and in dark-mode also inverted.
  - if `false` all non-blended iframes will have background a (by default) white background and no inversion for dark-mode are applied.
  - there's no need to set the blend for individual iframes if it's set in the `_config.yml`, unless you want to deviate from the setting set there.
- `iframe_saturation`: `1.5` (_default_) or **float**:
  - Blended iframes are inverted in darkmode using the CSS filter `invert(1) hue-rotate(180deg) saturation(iframe_saturation)`.
- `iframe_h5p_autoresize`: `true` (_default_) or `false`:
  - if `true` all h5p iframes are automagically resized to fit the element in which the iframe is loaded.
  - if `false` no h5p iframes are automagically resized to fit the element in which the iframe is loaded.
- `iframe_background`: `#ffffff` (_default_) or **color string**:
  - sets the background color of non-blended iframes.
  - Any CSS accepted color string can be used.


## General directive

To clearly show the blending and sizing, we showcase everthing in a general titled admonition.

### Default behavior

For use inline or in other directives and admonitions, iframes can be added using the following syntax:

````md
```{iframe} <link_to_webpage_to_embed>
```
````

By default, the following is chosen (which can be adapted):
- `width` to `100% - 2.8rem` of the element in which the iframe is loaded;
- `aspect-ratio` to `auto 2 / 1`.

For example:

`````md
````{admonition} Default
```{iframe} ./some_content/element_pdf_and_cdf.html
```
````
`````

````{admonition} Default
```{iframe} ./some_content/element_pdf_and_cdf.html
```
````

### Blending

Blending can be enable or disable by using the classes `blend` and `no-blend`:

`````md
````{admonition} Enable blending
```{iframe} ./some_content/element_pdf_and_cdf.html
:class: blend
```
````
`````

````{admonition} Enable blending
```{iframe} ./some_content/element_pdf_and_cdf.html
:class: blend
```
````

`````md
````{admonition} Disable blending
```{iframe} ./some_content/element_pdf_and_cdf.html
:class: no-blend
```
````
`````

````{admonition} Disable blending
```{iframe} ./some_content/element_pdf_and_cdf.html
:class: no-blend
```
````

### Sizing aspects

The size of the shown iframe can be controlled with atmost two out the following three options:

- `width`: Sets the width of the iframe. Use CSS compatible strings.
- `height`: Sets the height of the iframe. Use CSS compatible strings.
- `aspectratio`: Sets the aspect ratio of the iframe. Use CSS compatible strings.

These options will be applied to the encapsulating `div` element.

::::{note}
Using CSS is complicated and error prone, so always check and never expect that you get what you want.
::::

::::{warning}
This extension does not check the validity of the given options, nor checks whether at most two options are entered.
::::

`````md
````{admonition} Width and height
```{iframe} ./some_content/element_pdf_and_cdf.html
:width: 600px
:height: 200px
```
````
`````

````{admonition} Width and height
```{iframe} ./some_content/element_pdf_and_cdf.html
:width: 600px
:height: 200px
```
````

`````md
````{admonition} Width and aspect ratio
```{iframe} ./some_content/element_pdf_and_cdf.html
:width: 600px
:aspectratio: 2 / 3
```
````
`````

````{admonition} Width and aspect ratio
```{iframe} ./some_content/element_pdf_and_cdf.html
:width: 200px
:aspectratio: 2 / 3
```
````

`````md
````{admonition} Height and aspect ratio
```{iframe} ./some_content/element_pdf_and_cdf.html
:height: 150px
:aspectratio: 2 / 2
```
````
`````

````{admonition} Height and aspect ratio
```{iframe} ./some_content/element_pdf_and_cdf.html
:height: 150px
:aspectratio: 2 / 2
```
````

### Styling aspects

The style of the shown iframe can be controlled with two options:

- `styleframe`: Sets the style of the iframe. Use CSS compatible strings. Include surround with `" "`.
- `stylediv`: Sets the style of surrounding div. Use CSS compatible strings. Include surround with `" "`.

::::{note}
Using CSS is complicated and error prone, so always check and never expect that you get what you want.
::::

::::{warning}
This extension does not check the validity of the given option.
::::

`````md
````{admonition} iframe styling
```{iframe} ./some_content/element_pdf_and_cdf.html
:styleframe: "border-style: dotted;border-color: #0047AB;border-width:5px;"
```
````
`````

````{admonition} iframe styling
```{iframe} ./some_content/element_pdf_and_cdf.html
:styleframe: "border-style: dotted;border-color: #0047AB;border-width:5px;"
```
````

`````md
````{admonition} div styling
```{iframe} ./some_content/element_pdf_and_cdf.html
:stylediv: "border-style: dashed;border-color: olive;border-width:20px;"
```
````
`````

````{admonition} div styling
```{iframe} ./some_content/element_pdf_and_cdf.html
:stylediv: "border-style: dashed;border-color: olive;border-width:20px;"
```
````

`````md
````{admonition} iframe and div styling
```{iframe} ./some_content/element_pdf_and_cdf.html
:styleframe: "border-style: dotted;border-color: #0047AB;border-width:5px;"
:stylediv: "border-style: dashed;border-color: olive;border-width:20px;"
```
````
`````

````{admonition} iframe and div styling
```{iframe} ./some_content/element_pdf_and_cdf.html
:styleframe: "border-style: dotted;border-color: #0047AB;border-width:5px;"
:stylediv: "border-style: dashed;border-color: olive;border-width:20px;"
```
````


## Special directives

### h5p

For iframes intended for h5p elements, the code

`````md
````{admonition} h5p example
```{iframe} https://tudelft.h5p.com/content/1292011179114024347/embed
:class: blend
:aspectratio: auto
```
````
`````

can be reduced to

`````md
````{admonition} h5p example
```{h5p} https://tudelft.h5p.com/content/1292011179114024347/embed
```
````
`````

resulting in

````{admonition} h5p example
```{h5p} https://tudelft.h5p.com/content/1292011179114024347/embed
```
````

### video

For iframes intended for videos, the code

`````md
````{admonition} video example
```{iframe} https://www.youtube.com/embed/B1J6Ou4q8vE?si=XZDT83fcR6W3Dxut
:class: no-blend
:styleframe: "background: transparent;"
:aspectratio: auto 16 / 9
```
````
`````

can be reduced to

`````md
````{admonition} video example
```{video} https://www.youtube.com/embed/B1J6Ou4q8vE?si=XZDT83fcR6W3Dxut
```
````
`````

resulting in

````{admonition} video example
```{video} https://www.youtube.com/embed/B1J6Ou4q8vE?si=XZDT83fcR6W3Dxut
```
````
