# Custom colors (v2)

## Code in `_config.yml`

```yml
sphinx:
  config:
    tb_cc_list: {'purplepink':[165,21,160],'greenorange':[45,180,117,204,158,110]}
```

## Code inserted in `_config.yml`

```yml
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

### Color admonotions

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