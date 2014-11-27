
from .base import *
import matplotlib as mpl
from matplotlib import pyplot as plt
from functools import wraps


_almost_black = '#262626'
_light_grey = '#fafafa'


class PrettyTheme(BaseTheme):
    '''
    A minimalist theme with ticks and axes only where
    required. More suitable for web publication than print.
    '''
    def __init__(self, **kwargs):
        # TODO PLOT COLORS
        # Axes
        cadd(kwargs, 'axes.linewidth', 0.5)
        cadd(kwargs, 'axes.labelsize', 'large')
        cadd(kwargs, 'axes.labelcolor', _almost_black)
        cadd(kwargs, 'axes.facecolor', 'white')
        # Ticks
        cadd(kwargs, 'xtick.direction', 'out')
        cadd(kwargs, 'ytick.direction', 'out')
        cadd(kwargs, 'xtick.color', _almost_black)
        cadd(kwargs, 'ytick.color', _almost_black)
        # Grid
        cadd(kwargs, 'grid.color', 'white')
        cadd(kwargs, 'grid.linestyle', '-')
        cadd(kwargs, 'axes.axisbelow', True)
        cadd(kwargs, 'axes.grid', False)
        # Legend
        cadd(kwargs, 'legend.numpoints', 1)
        cadd(kwargs, 'legend.fancybox', True)
        # Figure
        cadd(kwargs, 'figure.figsize', (5, 4))
        cadd(kwargs, 'figure.facecolor', 'white')
        cadd(kwargs, 'figure.edgecolor', '0.50')
        cadd(kwargs, 'figure.subplot.bottom', 0.15)
        cadd(kwargs, 'figure.subplot.top', 0.85)
        cadd(kwargs, 'figure.subplot.hspace', 0.5)
        # Quality
        cadd(kwargs, 'figure.dpi', 100)
        cadd(kwargs, 'savefig.dpi', 100)

        super().__init__(**kwargs)
        
    @wraps(plt.legend)
    def legend(self, *args, **kwargs):
        self.setstyle()
        cadd(kwargs, 'framealpha', 0.5)
        plt.legend(*args, **kwargs)

    @wraps(plt.plot)
    def plot(self, *args, **kwargs):
        self.setstyle()
        plt.plot(*args, **kwargs)

        ax = get_ax(**kwargs)
        remove_ticks(ax)
        remove_spines(ax)
        set_spines(ax, _almost_black)

        # TODO
        # hist
        # boxplot
        # semilogx
        # semilogy
        # loglog
        # scatter
        