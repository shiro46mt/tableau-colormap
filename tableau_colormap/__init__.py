__version__ = '0.1.0'

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from cycler import cycler

tableau = [
    "#4e79a7",
    "#f28e2b",
    "#e15759",
    "#76b7b2",
    "#59a14f",
    "#edc948",
    "#b07aa1",
    "#ff9da7",
    "#9c755f",
    "#bab0ac",
]


def set_colormap():
    """ListedColormapを作成して登録"""
    cmap_tableau = ListedColormap(tableau, name='Tableau10')
    plt.rcParams['axes.prop_cycle'] = cycler(color=cmap_tableau.colors)

set_colormap()
