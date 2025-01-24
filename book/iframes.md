# Iframe stuff

## Introduction

This extension provides an interface to include iframes with relative ease, but does try to provide manners to interact with the various options. This rests purely by setting default CSS values, that the user can overwrite if preferred. In general, each `iframe` is embedded within a `div` element, which eases sizing. 

::::{note}
Using CSS is complicated and error prone, so always check and never expect that you get what you want.
::::

## Configuration choices

- `iframe_blend_all`: `true` (_default_) or `false`:
  - if `true` all iframes are by default blended with the background and in dark-mode also inverted.
  - if `false` all non-blended iframes will have background a (by default) white background and no inversion for dark-mode are applied.
- `iframe_saturation`: `1.5` (_default_) or **float**:
  - Blended iframes are inverted in darkmode using the CSS filter `invert(1) hue-rotate(180deg) saturation(iframe_saturation)`.
- `iframe_h5p_autoresize`: `true` (_default_) or `false`:
  - if `true` all h5p iframes are automagically resized to fit the element in which the iframe is loaded.
  - if `false` no h5p iframes are automagically resized to fit the element in which the iframe is loaded.
- `iframe_background`: `#ffffff` or **color string**:
  - sets the background color of non-blended iframes.
  - Any CSS accepted color string can be used.


## General directive

For use inline or in other directives and admonitions.

To clearly show the blending and sizing, we showcase everthing in a general titled admonition.

### Default behavior

General directive sets by default

- `width` to `80%` of the element in which the iframe is loaded;
- `aspect-ratio` to `2 / 1`.
- blending with the background to the chosen default.

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

The style of the shown iframe can be controlled with the option:

- `style`: Sets the style of the iframe. Use CSS compatible strings. Include surround with `" "`.

This option will be applied to the `iframe` element.

::::{note}
Using CSS is complicated and error prone, so always check and never expect that you get what you want.
::::

::::{warning}
This extension does not check the validity of the given option.
::::

`````md
````{admonition} Height and aspect ratio
```{iframe} ./some_content/element_pdf_and_cdf.html
:style: "border-style: dotted !important;border-color: #0047AB !important;border-width:5px !important;"
```
````
`````

````{admonition} Height and aspect ratio
```{iframe} ./some_content/element_pdf_and_cdf.html
:style: "border-style: dotted !important;border-color: #0047AB !important;border-width:5px !important;"
```
````


## Special directives

**h5p**

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

**video**

For iframes intended for videos, the code

`````md
````{admonition} video example
```{iframe} https://www.youtube.com/embed/B1J6Ou4q8vE?si=XZDT83fcR6W3Dxut
:class: no-blend
:aspectratio: 16 / 9
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