# Custom colors

Within these online books sometimes extra/new colors are wished for. In this page is shown how this can be achieved.

## Using `definecolor`

::::{warning}
This method only works for $\LaTeX$  colors.
::::

::::{warning}
In this case the color remains the same in ligt and dark mode.
::::

### Code in `_config.yml`

```yaml
sphinx:
  config:
    mathjax3_config:
      tex:
        macros:
          "newcolor": ['\definecolor{newcolor}{RGB}{111, 29, 119}{\color{newcolor}#1}',1]
```

### Code in content

```latex
:::{math}
\newcolor{\LaTeX}
:::
```

### Result

:::{math}
\newcolor{\LaTeX}
:::

## Using CSS

In this case one has three options:

1. Light and dark mode the same color
1. Light and dark mode different colors using two color definitions
1. Light and dark mode different colors using a color filter

### Light and dark mode the same color

::::{note}
This method has the benefit that the custom color can be used also within html and css elements.
::::

#### Code in `_static/color.css` 

```css
:root {
    --newcolor: rgb(111, 29, 119);
}

.newcolor {color: var(--newcolor);}
```

#### Code in content

```latex
:::{math}
\class{newcolor}{\LaTeX}
:::
```

```html
<div class="newcolor">HTML text</div>
```

#### Result

:::{math}
\class{newcolor-same}{\LaTeX}
:::

<div class="newcolor-same">HTML text</div>

### Light and dark mode different colors using two color definitions

::::{note}
This method has the benefit that the custom colors can be used also within html and css elements with automatic changes when the mode changes from Light to dark or vice versa. 
::::


#### Code in `_static/color.css` 

```css
:root {
    --newcolor: rgb(111, 29, 119);
}

html[data-theme="dark"] {
    --newcolor: rgb(255, 167, 255)
}

.newcolor {color: var(--newcolor);}
```

#### Code in content

```latex
:::{math}
\class{newcolor}{\LaTeX}
:::
```

```html
<div class="newcolor">HTML text</div>
```

#### Result

:::{math}
\class{newcolor}{\LaTeX}
:::

<div class="newcolor">HTML text</div>

### Light and dark mode different colors using a color filter

::::{warning}
This method has the benefit that the custom colors can only be used as a class.
::::

#### Code in `_static/color.css` 

```css
:root {
    --newcolor: rgb(111, 29, 119);
}

.newcolor {color: var(--newcolor);}

html[data-theme="dark"] .newcolor {
  filter:  invert(1) hue-rotate(180deg) saturate(1.5);
}

```

#### Code in content

```latex
:::{math}
\class{newcolor}{\LaTeX}
:::
```

```html
<div class="newcolor">HTML text</div>
```

#### Result

:::{math}
\class{newcolor-filter}{\LaTeX}
:::

<div class="newcolor-filter">HTML text</div>
