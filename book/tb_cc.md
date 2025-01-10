# Sphinx extension: Named colors

## Introduction

This extensions provides a simple solution to use [CSS named colors](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color) and ___custom named colors___ in:
- $\LaTeX$;
- HTML text;
- Admonitions.

## What does it do?

This extension defines, based on the CSS named color and custom named colors (provided by the user), several new
- $\LaTeX$ commands;
- Sphinx roles;
- Sphinx admonitions;
- Sphinx admonition classes;
that are styled by a generated CSS file.

If specified, each color will have a different value in the light and dark data-theme. 

## Installation
To use this extenstion, follow these steps:

**Step 1: Install the Package**

Install the `sphinx-named-colors` package using `pip`:
```
pip install sphinx-named-colors
```

**Step 2: Add to `requirements.txt`**

Make sure that the package is included in your project's `requirements.txt` to track the dependency:
```
sphinx-named-colors
```

**Step 3: Enable in `_config.yml`**

In your `_config.yml` file, add the extension to the list of Sphinx extra extensions (**important**: underscore, not dash this time):
```
sphinx: 
    extra_extensions:
        .
        .
        .
        - sphinx_named_colors
        .
        .
        .
```

## Configuration

This extension provides the following configuration values:

```yaml
named_colors_include_CSS: true # default value
```

- If set to _true_ all [CSS named colors](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color) will be included in the extension.
- If set to _false_ no [CSS named colors](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color) will be included in the extension. If no custom named colors are defined, this extension will do nothing.

```yaml
named_colors_dark_and_light: true # default value
```

- _true_: for all [CSS named colors](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color) and all custom named colors a secondary value will be generated for use in the dark data-theme, unless otherwise specifed for custom colors. The generated colors emulate the same as the CSS filter `invert(1) hue_rotate(180) saturate(<val>);` where `<val>` is the value set by `named_colors_saturation`.
- _false_: This disables the use of different colors in the dark data-theme, even if specified for custom colors.

```yaml
named_colors_saturation: 1.5 # default value
```

- _number_: The saturation value used in the generation of the dark data-theme colors.

```yaml
named_colors_custom_colors: None
```

- _None_: No custom named colors will be included.
- _dictionary_: A Python dictionary where each `key` defines a custom name and the `value` is a list of 3 or 6 integers, with each integer at minimum 0 and at maximum 255.
  - If 3 integers are provided, these are the RGB values of the custom named color and, if specified, the dark data-theme color will be generated.
  - If 6 integers are provided, the first set of 3 integers form the RGB values of the custom named color and the second set of 3 integers form the RGB values of the dark data-theme color.

## Provided code

### Textual elements

::::{note}
In the next part, replace `namedcolor` by the name of the CSS/custom named color.
::::

```latex
\namedcolor{...}
```

- Only use in $\LaTeX$ code.
- This will typeset `...` in the color _namedcolor_.

```md
{namedcolor}`...`
```

- Only use in _inline_ code.
- This will typeset `...` in the color _namedcolor_.

### Admonitions

Colored admonitions can be generated in two ways, explained below.

**1. By adding a class to an existing admonition**

```md
::::{type} Title (optional or required, depending on type)
:class: namedcolor
Content
::::
```

**2. By using a new admonition**

```md
::::{namedcolor} Title (optional)
Content
::::
```

In both cases extra classes can be added to the admonition to apply other styling.

::::{warning}
Note that, because of the use of CSS, sometimes results may differ from the expected result.
::::

## Examples

To see examples of usage visit the [TeachBooks manual](https://teachbooks.io/manual/intro.html).

## Contribute

This tool's repository is stored on [GitHub](https://github.com/TeachBooks/Sphinx-TUDelft-theme). The `README.md` of the branch `Manual` is also part of the [TeachBooks manual](https://teachbooks.io/manual/intro.html) as a submodule. If you'd like to contribute, you can create a fork and open a pull request on the [GitHub repository](https://github.com/TeachBooks/Sphinx-TUDelft-theme). To update the `README.md` shown in the TeachBooks manual, create a fork and open a merge request for the [GitHub repository of the manual](https://github.com/TeachBooks/manual). If you intent to clone the manual including its submodules, clone using: `git clone --recurse-submodulesgit@github.com:TeachBooks/manual.git`.  

## Code in `_config.yml`

```yaml
sphinx:
  config:
    tb_cc_list: {'purplepink':[165,21,160],'greenorange':[45,180,117,204,158,110]}
```

## Code inserted in `_config.yml`

```yaml
sphinx:
  config:
    mathjax3_config:
      tex:
        macros:
          'purplepink': ['\class{purplepink}{#1}', 1]
          'greenorange': ['\class{greenorange}{#1}', 1]
```

## CSS generated

```css
/* (light/default mode) colors */
:root {
	--purplepink: #a515a0;
	--purplepink-mid: #a515a020;
	--purplepink-min: #a515a005;
	--greenorange: #2db475;
	--greenorange-mid: #2db47520;
	--greenorange-min: #2db47505;
}

/* dark mode colors */
html[data-theme="dark"] {
	--purplepink: #ff8aff;
	--purplepink-mid: #ff8aff20;
	--purplepink-min: #ff8aff05;
	--greenorange: #cc9e6e;
	--greenorange-mid: #cc9e6e20;
	--greenorange-min: #cc9e6e05;
}

/* LaTeX classes */
.purplepink {color: var(--purplepink);}
.greenorange {color: var(--greenorange);}


/* Admonitions */
/* purplepink admonition */
div.admonition.purplepink {
	border-color: var(--purplepink);
	background-color: var(--purplepink-min);
}
div.admonition.purplepink > .admonition-title {
	color: var(--pst-color-text-base);
	background-color: var(--purplepink-mid);
}
div.admonition.purplepink > .admonition-title::after {
	color: var(--purplepink);
}
div.admonition.purplepink > p{
	color: var(--pst-color-text-base);
}
/* greenorange admonition */
div.admonition.greenorange {
	border-color: var(--greenorange);
	background-color: var(--greenorange-min);
}
div.admonition.greenorange > .admonition-title {
	color: var(--pst-color-text-base);
	background-color: var(--greenorange-mid);
}
div.admonition.greenorange > .admonition-title::after {
	color: var(--greenorange);
}
div.admonition.greenorange > p{
	color: var(--pst-color-text-base);
}
```

## New stuff in action

### $\LaTeX$ colors

$$
\purplepink{\int_a^bf(x)dx} = \greenorange{F(b)-F(a)}.
$$

```latex
$$
\purplepink{\int_a^bf(x)dx} = \greenorange{F(b)-F(a)}.
$$
```

### Color admonitions

::::{admonition} Title of the admonition
:class: purplepink
Content of the admonition
::::

```
::::{admonition} Title of the admonition
:class: purplepink
Content of the admonition
::::
```

::::{greenorange}
Correct color?
::::

```
::::{greenorange}
Correct color?
::::
```

::::{greenorange} with title?
Correct color?
::::

```
::::{greenorange} with title?
Correct color?
::::
```

::::{warning}
:class: greenorange
Content of the admonition
::::

```
::::{warning}
:class: greenorange
Content of the admonition
::::
```

::::{prf:theorem}
:class: purplepink
Content of the admonition
::::

```
::::{prf:theorem}
:class: greenorange
Content of the admonition
::::
```

::::{exercise}
:class: greenorange
Content of the admonition
::::

```
::::{exercise}
:class: greenorange
Content of the admonition
::::
```

::::{greenorange} with title?
:class: definition
Correct color? Just an other icon?
::::

```
::::{greenorange} with title?
:class: definition
Correct color? Just an other icon?
::::
```

### Text in color

{greenorange}`Sphinx`

```
{greenorange}`Sphinx`
```

_{purplepink}`Sphinx`_

```
_{purplepink}`Sphinx`_
```

**{purplepink}`Sphinx`**

```
**{purplepink}`Sphinx`**
```

_**{greenorange}`Sphinx`**_

```
_**{greenorange}`Sphinx`**_
```

