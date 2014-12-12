# -*- coding: utf-8 -*-

from .base import *
from matplotlib import pyplot as plt
from functools import wraps


_almost_black = '#262626'
_light_grey = '#fafafa'


class PrettyTheme(BaseTheme):
    '''
    A minimalist theme with ticks and axes only where
    required. More suitable for web publication than print.

    '''.format(BaseTheme.__doc__)
    def __init__(self, **kwargs):
        # Colors
        cadd(kwargs, 'axes.color_cycle', ['#E41A1C', '#377EB8', '#4DAF4A',
                                          '#984EA3', '#FF7F00',  '#A65628',
                                          '#F781BF', '#999999'])
        # Axes
        cadd(kwargs, 'axes.linewidth', 0.5)
        cadd(kwargs, 'axes.labelsize', 'large')
        cadd(kwargs, 'axes.labelcolor', _almost_black)
        cadd(kwargs, 'axes.facecolor', 'white')
        cadd(kwargs, 'axes.edgecolor', 'white')
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
        ax = get_ax(kwargs)

        lg = ax.legend(*args, **kwargs)
        # Remove border of box
        lg.get_frame().set_linewidth(0.0)
        return lg

    @wraps(plt.plot)
    def plot(self, *args, **kwargs):
        self.setstyle()
        ax = get_ax(kwargs)

        if axes_is_polar(ax):
            ax.grid(True, color='grey', linestyle=':')
        else:
            remove_ticks(ax)
            remove_spines(ax)

        set_spines(ax, _almost_black)

        return ax.plot(*args, **kwargs)

    @wraps(plt.errorbar)
    def errorbar(self, *args, **kwargs):
        self.setstyle()
        ax = get_ax(kwargs)

        if axes_is_polar(ax):
            ax.grid(True, color='grey', linestyle=':')
        else:
            remove_ticks(ax)
            remove_spines(ax)

        set_spines(ax, _almost_black)

        return ax.errorbar(*args, **kwargs)

    @wraps(plt.semilogx)
    def semilogx(self, *args, **kwargs):
        self.setstyle()
        ax = get_ax(kwargs)

        set_ticks_position(ax, 'bottom', 'left')
        remove_ticks(ax, ['y'])
        remove_spines(ax)
        set_spines(ax, _almost_black)
        move_spines(ax, ['left'], [-0.02])

        return ax.semilogx(*args, **kwargs)

    @wraps(plt.semilogy)
    def semilogy(self, *args, **kwargs):
        self.setstyle()
        ax = get_ax(kwargs)

        set_ticks_position(ax, 'bottom', 'left')
        remove_ticks(ax, ['x'])
        remove_spines(ax)
        set_spines(ax, _almost_black)
        move_spines(ax, ['bottom'], [-0.02])

        return ax.semilogy(*args, **kwargs)

    @wraps(plt.loglog)
    def loglog(self, *args, **kwargs):
        self.setstyle()
        ax = get_ax(kwargs)

        set_ticks_position(ax, 'bottom', 'left')
        remove_spines(ax)
        set_spines(ax, _almost_black)
        move_spines(ax, ['bottom', 'left'], [-0.02, -0.02])

        return ax.loglog(*args, **kwargs)

    @wraps(plt.hist)
    def hist(self, *args, **kwargs):
        self.setstyle(**{'axes.grid': False,
                         'axes.axisbelow': False})
        ax = get_ax(kwargs)
        cadd(kwargs, 'edgecolor', 'white')
        remove_ticks(ax)
        remove_spines(ax)
        set_spines(ax, _almost_black)
        ax.grid(axis='y', color='white', linestyle='-', linewidth=0.5)

        return ax.hist(*args, **kwargs)


        # TODO
        # boxplot
        # scatter
