![GitHub License](https://img.shields.io/github/license/shiro46mt/tableau-colormap)
[![PyPI - Version](https://img.shields.io/pypi/v/tableau-colormap)](https://pypi.org/project/tableau-colormap/)
[![PyPI Downloads](https://static.pepy.tech/badge/tableau-colormap)](https://pepy.tech/projects/tableau-colormap)

# tableau-colormap
Applies Tableau's new color maps with only an import statement

## Usage

After importing `matplotlib`, import `tableau_colormap`.

```python
import matplotlib.pyplot as plt
import tableau_colormap

x = [i+1 for i in range(10)]
y = [i+10 for i in range(10)]
c = [f'C{i}' for i in range(10)]
plt.bar(x, y, color=c)
plt.show()
```

![demo](https://raw.githubusercontent.com/shiro46mt/tableau-colormap/master/demo.png)

## Installation

```sh
# Using pip
pip install tableau-colormap

# Using uv
uv add tableau-colormap
```

## FAQ

### I get a linter warning / My formatter removes `import tableau_colormap`

Since the imported `tableau_colormap` is not explicitly used, it's mistakenly identified as an unnecessary import. You can prevent it from being flagged as unused by explicitly calling `tableau_colormap.set_colormap()` as shown below. Although this execution is functionally **meaningless** (*no-op*), run it immediately after the import, or wherever necessary.

```python
import tableau_colormap

tableau_colormap.set_colormap()
```

## Legal Disclaimer / Note on Copyright

This library aims to replicate the color palettes used in Tableau products for use with Matplotlib in Python.

**Important Notice:**
This project is **unofficial** and is **not affiliated with, endorsed by, or sponsored by Tableau Software, LLC or Salesforce, Inc.**

This library is released under the MIT License, see LICENSE.
