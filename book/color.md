# Tabel stuff

|  | GitHub   | TU Delft GitLab      |
|--|----------|-------------|
| Book url  | GitHub pages (`<organization/username>.github.io/<book>`), for TU Delft books a custom URL (`oit.tudelft.nl/<book>`), for private books on TU Delft GitHub Enterprise with SSO a random URL (`<random>.github.io/<book>`), or custom url `<anything>.<anything>/<book>`> 🌐         | TU Delft OIT (`interactivetextbooks.tudelft.nl/<book>`) 🎓 |
| Real-time book editing | Automated and flexible (multiple version of the book, building error insights, fast, custom urls)  🚀   | Automated but simplistic (not easily adaptable, no caching environments, no visual summaries, no parallel processes) 🛵 For TU Delft OIT: restricted adaptations because of copyright checks 🚫   |
| Setting up book website | Immediate and automated with [template](../external/template/README.md) ⚡️         | Manual setup on personal webserver, or access required by TeachBooks or TU Delft OIT  🚧    |
| Book access with SSO | Only available for GitHub pages on GitHub Enterprise of TU Delft 🎓, optional with custom URL  ✅ | Optional  ✅          |
| Access to source code | Private (if part of organization linked to educational account) /public / internally TU Delft (on GitHub Enterprise of TU Delft) 👥   | Private / public (read-only) / internally TU Delft, editing requires requires SSO login  👥  👀 |
| Book size limits | 1 GB for all branches 📚 | 150 MB per book 📕 |
| GitHub Desktop | Well integrated 😎 | Basic integration 🙂 |
| Utteranc.es | Can be linked to same repository 🏷️ | Requires GitHub repository next to GitLab repository 🏷️🏷️|

# Iframe stuff

## Inline

**Default**
::::{iframe} https://tudelft.h5p.com/content/1292011179114024347/embed
::::

**Force blend**
::::{iframe} https://tudelft.h5p.com/content/1292011179114024347/embed
:class: blend
::::

**Force no-blend**
::::{iframe} https://tudelft.h5p.com/content/1292011179114024347/embed
:class: no-blend
::::

## Admonition

:::{exercise} Default
::::{iframe} https://tudelft.h5p.com/content/1292011179114024347/embed
::::
:::

:::{exercise} Force blend
::::{iframe} https://tudelft.h5p.com/content/1292011179114024347/embed
:class: blend
::::
:::

:::{exercise} Force no-blend
::::{iframe} https://tudelft.h5p.com/content/1292011179114024347/embed
:class: no-blend
::::
:::