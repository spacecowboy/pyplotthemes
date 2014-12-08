
from .base import *
import matplotlib as mpl
from matplotlib import pyplot as plt
from functools import wraps



class ClassicTheme(BaseTheme):
    '''
    A classically looking theme with enclosing boxes and a no-frills
    approach. Suitable for publications.
    '''
    def __init__(self, **kwargs):
        # Colors
        # Colorbrewer 9-class Set1 (minus yellow), print-friendly
        cadd(kwargs, 'axes.color_cycle',
             "#e41a1c #377eb8 #4daf4a #984ea3 #ff7f00 #a65628 #f781bf #999999".split(" "))
        # Axes
        cadd(kwargs, 'axes.linewidth', 0.5)
        cadd(kwargs, 'axes.labelsize', 'large')
        cadd(kwargs, 'axes.labelcolor', "black")
        cadd(kwargs, 'axes.facecolor', 'white')
        cadd(kwargs, 'axes.edgecolor', 'white')
        # Ticks
        cadd(kwargs, 'xtick.direction', 'in')
        cadd(kwargs, 'ytick.direction', 'in')
        cadd(kwargs, 'xtick.color', "black")
        cadd(kwargs, 'ytick.color', "black")
        # Grid
        cadd(kwargs, 'grid.color', 'white')
        cadd(kwargs, 'grid.linestyle', '-')
        cadd(kwargs, 'axes.axisbelow', True)
        cadd(kwargs, 'axes.grid', False)
        # Legend
        cadd(kwargs, 'legend.numpoints', 1)
        cadd(kwargs, 'legend.fancybox', False)
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
        
        lg = plt.legend(*args, **kwargs)
        # Set black border
        lg.get_frame().set_edgecolor('black')
        return lg


    @wraps(plt.plot)
    def plot(self, *args, **kwargs):
        self.setstyle()
        ax = get_ax(kwargs)

        set_spines(ax, "black")
        
        return plt.plot(*args, **kwargs)
        
    @wraps(plt.semilogx)
    def semilogx(self, *args, **kwargs):
        self.setstyle()
        ax = get_ax(kwargs)
        
        set_spines(ax, "black")
        
        return plt.semilogx(*args, **kwargs)
        
    @wraps(plt.semilogy)
    def semilogy(self, *args, **kwargs):
        self.setstyle()
        ax = get_ax(kwargs)

        set_spines(ax, "black")
        
        return plt.semilogy(*args, **kwargs)
        
    @wraps(plt.loglog)
    def loglog(self, *args, **kwargs):
        self.setstyle()
        ax = get_ax(kwargs)

        set_spines(ax, "black")
        
        return plt.loglog(*args, **kwargs)

    @wraps(plt.hist)
    def hist(self, *args, **kwargs):
        self.setstyle(**{'axes.grid' : False,
                         'axes.axisbelow' : False})
        ax = get_ax(kwargs)
        cadd(kwargs, 'edgecolor', 'white')
        remove_ticks(ax, ['x'])
        set_spines(ax, "black")
        ax.grid(axis='y', color='white', linestyle='-', linewidth=0.5)
        
        return plt.hist(*args, **kwargs)
        
        
        # TODO
        # boxplot
        # scatter
        