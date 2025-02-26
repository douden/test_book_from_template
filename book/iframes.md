# Sphinx extension: Iframes

```{admonition} User types
:class: tip
This section is useful for user type 3-5.
```
+++
{bdg-primary}`Sphinx Extension`

## Introduction

This extension provides an interface to include iframes with relative ease, but does try to provide manners to interact with the various options. This rests purely by setting default CSS values, that the user can overwrite if preferred for individual iframes, but also globally. In general, each `iframe` is embedded within a `div` element, which eases sizing.

::::{note}
Using CSS is complicated and error prone, so always check and never expect that you get what you want.
::::

## What does it do?

This extension provides several Sphinx directives:

- `iframe`
- `h5p`
- `video`
- `iframe-figure`

 that can be used to quickly insert an iframe with standard sizing and styling.

## Installation
To use this extenstion, follow these steps:

**Step 1: Install the Package**

Install the module `sphinx-iframes` package using `pip`:
```
pip install git+https://github.com/TeachBooks/sphinx-iframes.git
```
    
**Step 2: Add to `requirements.txt`**

Make sure that the package is included in your project's `requirements.txt` to track the dependency:
```
git+https://github.com/TeachBooks/sphinx-iframes.git
```

**Step 3: Enable in `_config.yml`**

In your `_config.yml` file, add the extension to the list of Sphinx extra extensions (**important**: underscore, not dash this time):
```
sphinx: 
    extra_extensions:
        .
        .
        .
        - sphinx_iframes
        .
        .
        .
```

## Configuration

The extension provides several configuration values, which can be added to `_config.yml`:

```yaml
sphinx: 
    config:
        -
        -
        -
        iframe_blend:          true # default value
        iframe_saturation:     1.5 # default value
        iframe_h5p_autoresize: true # default value
        iframe_background:     "#ffffff" # default value
        iframe_width:          calc(100% - 2.8rem) # default value
        iframe_aspectratio:    auto 2 / 1 # default value
        -
        -
        -
```

- `iframe_blend`: `true` (_default_) or `false`:
  - if `true` all iframes are standard blended with the background and in dark-mode also inverted.
  - if `false` all non-blended iframes will have background a colored background and no inversion for dark-mode is applied.
  - there's no need to set the blend or no-blend for individual iframes if it's set in the `_config.yml`, unless you want to deviate from the setting set there.
- `iframe_saturation`: `1.5` (_default_) or **float**:
  - Blended iframes are inverted in darkmode using the CSS filter `invert(1) hue-rotate(180deg) saturation(iframe_saturation)`.
- `iframe_h5p_autoresize`: `true` (_default_) or `false`:
  - if `true` all h5p iframes are automagically resized to fit the element in which the iframe is loaded.
  - if `false` no h5p iframes are automagically resized to fit the element in which the iframe is loaded.
- `iframe_background`: `"#ffffff"` (_default_) or **CSS string**:
  - sets the standard background color of non-blended iframes.
  - Any CSS string defining colors can be used, see [<color> CSS data type](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value).
  - Surround with `" "` for hex strings.
  - Only visible if the content of the iframes has a transparant background. 
- `iframe_width`:  `calc(100% - 2.8rem)` (_default_) or **CSS string**:
  - sets the standard width of the iframe within the parent element;
  - Any CSS string defining a width can be used, see [width CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/width).
- `iframe_aspectratio`: `auto 2 / 1` (_default_) or **CSS string**:
  - sets the standard aspect ration of the iframe within the parent element;
  - Any CSS string defining an aspect ratio can be used, see [aspect-ratio CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/aspect-ratio).

## Provided code

### Directives

The following new directives are provided:

````md
```{iframe} <link_to_webpage_to_embed>
```
````

````md
```{h5p} <link_to_h5p_webpage_to_embed>
```
````

````md
```{video} <link_to_video_to_embed>
```
````

````md
```{iframe-figure} <link_to_webpage_to_embed>
:name: some:label

The caption for the iframe.
```
````

Note that you don't need the full embed code of an iframe. Only the source url should be used.

All of these have the following options:

- `:class:`
  - If further CSS styling is needed, then use this option to append a CSS class name to the rendered iframe.
  - We recommend to only use the classes `blend` and `no-blend`, see [](sec:iframes:examples).
- `:width:`
  - Sets the width of the iframe. Use CSS compatible strings.
- `:height:`
  - Sets the width of the iframe. Use CSS compatible strings.
- `:aspectratio:`
  - Sets the width of the iframe. Use CSS compatible strings.
- `:styleframe:`
  - Sets the style of the iframe. Use CSS compatible strings. Surround with " ".
- `:stylediv:`
  - Sets the style of the surrounding div. Use CSS compatible strings. Surround with " ".

The directive `iframe-figure` also inherits all options from the `figure` directive from Sphinx.

(sec:iframes:examples)=
## Examples and details

### `iframe` directive

To clearly show the blending and sizing, we showcase everthing in a general titled admonition.

#### Default behavior

For use inline or in other directives and admonitions, iframes can be added using the following syntax:

````md
```{iframe} <link_to_webpage_to_embed>
```
````

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

#### Blending

Blending can be enabled or disabled by using the classes `blend` and `no-blend`:

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

#### Sizing aspects

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

#### Styling aspects

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

### `h5p` directive

For iframes intended for H5P elements, the code

`````md
````{admonition} H5P example
```{iframe} https://tudelft.h5p.com/content/1292011179114024347/embed
:class: blend
:aspectratio: auto
```
````
`````

can be reduced to

`````md
````{admonition} H5P example
```{h5p} https://tudelft.h5p.com/content/1292011179114024347/embed
```
````
`````

resulting in

````{admonition} H5P example
```{h5p} https://tudelft.h5p.com/content/1292011179114024347/embed
```
````

Note that you don't need the full embed code as provided by H5P. Only the source url (often with the following syntax `https://<h5p_host_server>/content/<h5p_element_id>/embed`) should be used. This url can be obtained from the url in your H5P application with an addtional `/embed`, or in the html-embed-code.

### `video` directive

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

### `iframe-figure` directive

In {numref}`some:label` you can find the result of the below code. The reference is made using `{numref}` and label behind `:name:`.

`````md
````{iframe-figure} ./some_content/element_pdf_and_cdf.html
:name: some:label

The caption for the iframe.
````
`````

```{iframe-figure} ./some_content/element_pdf_and_cdf.html
:name: some:label
 
The caption for the iframe.
```

## Contribute

This tool's repository is stored on [GitHub](https://github.com/TeachBooks/sphinx-iframes). If you'd like to contribute, you can create a fork and open a pull request on the [GitHub repository](https://github.com/TeachBooks/sphinx-iframes).

The `README.md` of the branch `Manual` is also part of the [TeachBooks manual](https://teachbooks.io/manual/intro.html) as a submodule.
