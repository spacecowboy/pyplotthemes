# -*- coding: utf-8 -*-

import matplotlib as mpl
from matplotlib import pyplot as plt
import os


class BaseTheme(object):
    '''
    A theme wraps plotting methods and sets appropriate properties
    on the axis produced.

    Valid keyword arguments are anything that is accepted
    by matplotlib.rcParams. These values can be overridden
    for each seperate function call as well.

    Some additional convenience arguments/properties have also been defined:
    - latex : False/True, Force LaTeX and Computer Modern (font) everywhere
    - colors: [list of colors], The color cycle to use when plotting
    '''

    def __init__(self, latex=False, colors=None, **kwargs):
        # Matplotlib defaults
        cadd(kwargs, 'lines.linewidth', 1.0)
        cadd(kwargs, 'lines.linestyle', '-')
        cadd(kwargs, 'lines.color', 'blue')
        cadd(kwargs, 'lines.marker', 'None')
        cadd(kwargs, 'lines.markeredgewidth', 0.5)
        cadd(kwargs, 'lines.markersize', 6)
        cadd(kwargs, 'lines.dash_joinstyle', 'miter')
        cadd(kwargs, 'lines.dash_capstyle', 'butt')
        cadd(kwargs, 'lines.solid_joinstyle', 'miter')
        cadd(kwargs, 'lines.solid_capstyle', 'projecting')
        cadd(kwargs, 'lines.antialiased', True)

        cadd(kwargs, 'patch.linewidth', 1.0)
        cadd(kwargs, 'patch.facecolor', 'blue')
        cadd(kwargs, 'patch.antialiased', True)

        cadd(kwargs, 'font.family', 'sans-serif')
        cadd(kwargs, 'font.variant', 'normal')
        cadd(kwargs, 'font.stretch', 'normal')
        cadd(kwargs, 'font.serif', 'Bitstream Vera Serif, New Century Schoolbook, Century Schoolbook L, Utopia, ITC Bookman, Bookman, Nimbus Roman No9 L, Times New Roman, Times, Palatino, Charter, serif'.split(", "))
        cadd(kwargs, 'font.cursive', 'Apple Chancery, Textile, Zapf Chancery, Sand, cursive'.split(", "))
        cadd(kwargs, 'font.monospace', 'Bitstream Vera Sans Mono, Andale Mono, Nimbus Mono L, Courier New, Courier, Fixed, Terminal, monospace'.split(", "))

        cadd(kwargs, 'text.usetex', False)
        cadd(kwargs, 'text.latex.unicode', False)
        cadd(kwargs, 'text.latex.preamble', '')
        cadd(kwargs, 'text.dvipnghack', 'None')
        cadd(kwargs, 'text.hinting', 'auto')
        cadd(kwargs, 'text.hinting_factor', 8)
        cadd(kwargs, 'text.antialiased', True)

        cadd(kwargs, 'mathtext.cal', 'cursive')
        cadd(kwargs, 'mathtext.tt', 'monospace')
        cadd(kwargs, 'mathtext.bf', 'serif:bold')
        cadd(kwargs, 'mathtext.fontset', 'cm')
        cadd(kwargs, 'mathtext.fallback_to_cm', True)
        cadd(kwargs, 'mathtext.default', 'it')

        cadd(kwargs, 'axes.hold', True)
        cadd(kwargs, 'axes.facecolor', 'white')
        cadd(kwargs, 'axes.edgecolor', 'black')
        cadd(kwargs, 'axes.linewidth', 1.0)
        cadd(kwargs, 'axes.grid', False)
        cadd(kwargs, 'axes.titlesize', 'large')
        cadd(kwargs, 'axes.labelsize', 'medium')
        cadd(kwargs, 'axes.labelweight', 'normal')
        cadd(kwargs, 'axes.labelcolor', 'black')
        cadd(kwargs, 'axes.formatter.limits', (-7, 7))
        cadd(kwargs, 'axes.formatter.use_locale', False)
        cadd(kwargs, 'axes.formatter.use_mathtext', False)
        #cadd(kwargs, 'axes.formatter.useoffset', True)
        cadd(kwargs, 'axes.unicode_minus', True)
        cadd(kwargs, 'axes.color_cycle', 'b, g, r, c, m, y, k'.split(", "))
        cadd(kwargs, 'axes.xmargin', 0)
        cadd(kwargs, 'axes.ymargin', 0)

        cadd(kwargs, 'polaraxes.grid', True)
        cadd(kwargs, 'axes3d.grid', True)

        cadd(kwargs, 'xtick.major.size', 4)
        cadd(kwargs, 'xtick.minor.size', 2)
        cadd(kwargs, 'xtick.major.width', 0.5)
        cadd(kwargs, 'xtick.minor.width', 0.5)
        cadd(kwargs, 'xtick.major.pad', 4)
        cadd(kwargs, 'xtick.minor.pad', 4)
        cadd(kwargs, 'xtick.color', 'k')
        cadd(kwargs, 'xtick.labelsize', 'medium')
        cadd(kwargs, 'xtick.direction', 'in')

        cadd(kwargs, 'ytick.major.size', 4)
        cadd(kwargs, 'ytick.minor.size', 2)
        cadd(kwargs, 'ytick.major.width', 0.5)
        cadd(kwargs, 'ytick.minor.width', 0.5)
        cadd(kwargs, 'ytick.major.pad', 4)
        cadd(kwargs, 'ytick.minor.pad', 4)
        cadd(kwargs, 'ytick.color', 'k')
        cadd(kwargs, 'ytick.labelsize', 'medium')
        cadd(kwargs, 'ytick.direction', 'in')

        cadd(kwargs, 'grid.color', 'black')
        cadd(kwargs, 'grid.linestyle', ':')
        cadd(kwargs, 'grid.linewidth', 0.5)
        cadd(kwargs, 'grid.alpha', 1.0)

        cadd(kwargs, 'legend.fancybox', False)
        cadd(kwargs, 'legend.isaxes', True)
        cadd(kwargs, 'legend.fontsize', 'large')
        cadd(kwargs, 'legend.markerscale', 1.0)
        cadd(kwargs, 'legend.labelspacing', 0.5)
        cadd(kwargs, 'legend.handlelength', 2.)
        cadd(kwargs, 'legend.handleheight', 0.7)
        cadd(kwargs, 'legend.handletextpad', 0.8)
        cadd(kwargs, 'legend.borderaxespad', 0.5)
        cadd(kwargs, 'legend.columnspacing', 2.0)
        cadd(kwargs, 'legend.shadow', False)
        #cadd(kwargs, 'legend.framealpha', 1.0)
        cadd(kwargs, 'legend.scatterpoints', 3)

        cadd(kwargs, 'figure.figsize', (8, 6))
        cadd(kwargs, 'figure.dpi', 80)
        cadd(kwargs, 'figure.facecolor', '0.75')
        cadd(kwargs, 'figure.edgecolor', 'white')
        cadd(kwargs, 'figure.autolayout', False)
        cadd(kwargs, 'figure.subplot.left', 0.125)
        cadd(kwargs, 'figure.subplot.right', 0.9)
        cadd(kwargs, 'figure.subplot.bottom', 0.1)
        cadd(kwargs, 'figure.subplot.top', 0.9)
        cadd(kwargs, 'figure.subplot.wspace', 0.2)
        cadd(kwargs, 'figure.subplot.hspace', 0.2)

        cadd(kwargs, 'image.aspect', 'equal')
        cadd(kwargs, 'image.interpolation', 'bilinear')
        cadd(kwargs, 'image.cmap', 'jet')
        cadd(kwargs, 'image.lut', 256)
        cadd(kwargs, 'image.origin', 'upper')
        cadd(kwargs, 'image.resample', False)

        cadd(kwargs, 'path.simplify', True)
        cadd(kwargs, 'path.simplify_threshold', 0.1)
        cadd(kwargs, 'path.snap', True)
        cadd(kwargs, 'path.sketch', 'None')

        cadd(kwargs, 'savefig.dpi', 100)
        cadd(kwargs, 'savefig.facecolor', 'white')
        cadd(kwargs, 'savefig.edgecolor', 'white')
        cadd(kwargs, 'savefig.format', 'png')
        cadd(kwargs, 'savefig.bbox', 'standard')

        cadd(kwargs, 'savefig.pad_inches', 0.1)
        cadd(kwargs, 'savefig.directory', '~')
        #cadd(kwargs, 'savefig.transparent', False)

        self.rcParams = kwargs
        # Should be last to override rcParams properly
        self.latex = latex
        self.colors = colors

    @property
    def latex(self):
        return self._latex

    @latex.setter
    def latex(self, val):
        self._latex = val
        if (self._latex):
            self.rcParams['text.usetex'] = True
            self.rcParams['text.latex.unicode'] = True
            # Use Latex font always
            self.rcParams['font.family'] = 'serif'
            self.rcParams['font.serif'] = 'Computer Modern'
        else:
            self.rcParams['text.usetex'] = False
            # Use Latex font always
            self.rcParams['font.family'] = 'sans-serif'
            self.rcParams['font.serif'] = 'Bitstream Vera Serif, New Century Schoolbook, Century Schoolbook L, Utopia, ITC Bookman, Bookman, Nimbus Roman No9 L, Times New Roman, Times, Palatino, Charter, serif'.split(", ")

    @property
    def colors(self):
        return self.rcParams['axes.color_cycle']

    @colors.setter
    def colors(self, cl):
        if cl is not None:
            self.rcParams['axes.color_cycle'] = self._colorcycle

    def __getattr__(self, name):
        '''
        This method is called last in the getattribute chain and will
        only be called if an attribute with that name does not exist
        on this or any child classes. In that case, it will try to call
        the corresponding method/property from the pyplot module.

        If successful, the theme's rcParams are set before returning.
        '''
        plt_attr = getattr(plt, name)
        # Set style first
        self.setstyle()
        return plt_attr

    def setstyle(self, **kwargs):
        '''
        Set the theme's rcParams on matplotlib, as well as any
        additional parameters specified.
        '''
        # Set internal first
        for k, v in self.rcParams.items():
            mpl.rcParams[k] = v
        # Allow kwargs to override
        for k, v in kwargs.items():
            mpl.rcParams[k] = v


def cadd(d, key, value):
    '''
    Conditional add. Adds key with value in dict d if
    such a key is not already present.
    '''
    if key not in d:
        d[key] = value


def get_ax(kwargs):
    '''
    Return the specified axis, or if None, the current axis.
    '''
    ax = kwargs.pop('ax') if 'ax' in kwargs else None
    if ax is None:
        ax = plt.gca()
    return ax


def remove_spines(ax, sides=None):
    '''
    Remove spines of axis. Default: 'top' and 'right'

    Examples:
    removespines(ax)
    removespines(ax, ['top'])
    removespines(ax, ['top', 'bottom', 'right', 'left'])
    '''
    if sides is None:
        sides = ['top', 'right']
    for side in sides:
        ax.spines[side].set_visible(False)


def axes_is_polar(ax):
    '''
    Returns true if the axes has a polar projection.
    '''
    try:
        ax.spines['polar']
        # Yes it's polar
        return True
    except KeyError:
        # Not polar
        return False


def set_spines(ax, color='black', lw=0.5, sides=None):
    '''
    Set properties of spines. By default: 'top', 'bottom', 'right', 'left',
    unless axes is polar, in which case the default is 'polar'.

    Examples:
    set_spines(ax)
    set_spines(ax, ['top'])
    set_spines(ax, sides=['left', 'bottom'], color='k')
    set_spines(ax, '#FFFFFF', sides=['right'], lw=1.0)
    '''
    if sides is None:
        # See if it is polar
        if axes_is_polar(ax):
            sides = ['polar']
        else:
            sides = ['top', 'bottom', 'right', 'left']
    for side in sides:
        ax.spines[side].set_linewidth(lw)
        ax.spines[side].set_color(color)


def move_spines(ax, sides, dists):
    '''
    Move the entire spine relative to the figure.
    Examples:
    move_spines(ax, sides=['left', 'bottom'], dists=[-0.02, 0.1])
    '''
    for side, dist in zip(sides, dists):
        ax.spines[side].set_position(('axes', dist))


def set_axiscolors(ax, color, xy=None):
    '''
    Set colors on axis, 'x' and/or 'y'. Default is both.

    Examples:
    set_axiscolors(ax, 'red')
    set_axiscolors(ax, '#FFFFFF', ['x'])
    set_axiscolors(ax, 'k', ['y', 'x'])
    '''
    if xy is None:
        xy = ['x', 'y']
    if 'x' in xy:
        ax.xaxis.label.set_color(color)
    if 'y' in xy:
        ax.yaxis.label.set_color(color)


def remove_ticks(ax, xy=None):
    '''
    Remove ticks from axis. Default: 'x' and 'y'

    Examples:
    removeticks(ax)
    removeticks(ax, ['x'])
    removeticks(ax, ['y', 'x'])
    '''
    if xy is None:
        xy = ['x', 'y']
    if 'x' in xy:
        ax.xaxis.set_ticks_position('none')
    if 'y' in xy:
        ax.yaxis.set_ticks_position('none')


def set_ticks_position(ax, x=None, y=None):
    '''
    Set position of ticks.
    Defaults are x = ['bottom', 'top'], y = ['left', 'right']
    '''
    if x is None:
        x = ['top', 'bottom']
    if y is None:
        y = ['right', 'left']
    ax.yaxis.set_ticks_position(y)
    ax.xaxis.set_ticks_position(x)


def get_savefig(savedir, prefix=None, filename=None, extensions=None):
    '''
    Returns a function which saves the current matplotlib figure
    when called. Will set suitable values for bbox_inches.
    Files are saved with specified extensions in the
    designated directory and prefixed with the specified
    prefix as "prefix_filename.extension"

    DPI defaults to 300 to get high resolution png files.

    Keyword arguments:
    savedir - Folder in which to save figures

    prefix - Optional prefix for files.

    filename - Optional default filename for figures

    extensions - An iterable of file-extensions. If None,
                 defaults to [png]. For publication, try
                 [pdf, png]. Always put eps last since it
                 crashes for large images.
    '''
    # First make sure savedir exists
    if not os.path.exists(savedir):
        os.mkdir(savedir)

    if extensions is None:
        extensions = ['png']

    # Define function which saves figures there
    def savefig(*args, **kwargs):
        # Make sure we use bbox_inches
        if 'bbox_inches' not in kwargs:
            kwargs['bbox_inches'] = 'tight'

        # Make the images high resolution if not otherwise specified
        if 'dpi' not in kwargs:
            kwargs['dpi'] = 300

        # Default filename
        fname = filename
        if args is None or len(args) == 0:
            args = []  # Just make sure it's a list
        else:
            args = list(args)
            fname, ext = os.path.splitext(args.pop(0))
            # prefixing with path and prefix
            fileprefix = prefix
            if prefix is None:
                fileprefix = ''
            elif not prefix.endswith("_"):
                fileprefix += "_"
            fname = fileprefix + fname
            fname = os.path.join(savedir, fname)

        if fname is None:
            raise ValueError("A filename must be specified!")

        for ext in extensions:
            plt.savefig(*([fname + '.' + ext] + args), **kwargs)

    savefig.__doc__ = '''
        Use as plt.savefig. File extension will be ignored, and saved
        as {ext} in {savedir}
        Should only be given a raw file name, not an entire path.

        Use as savefig(filename) or savefig() if a default filename
        has been defined.

        Accepts any arguments that plt.savefig accepts:

        {pltdoc}
        '''.format(ext=extensions, savedir=savedir,
                   pltdoc=plt.savefig.__doc__[plt.savefig.__doc__.find("Keyword arguments:"):])

    return savefig
