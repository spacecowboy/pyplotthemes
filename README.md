
# pyplotthemes

A wrapper around matplotlib with themes.

## Usage:
Instead of doing the typical

```python
    from matplotlib import pyplot as plt
```

you instead import the theme you want


```python
    from pyplotthemes import classic as plt
```

Every method/attribute in pyplot is available in the themes so this can be
a one line replacement to get away from the default settings.

## Why another theme package?
There are several packages available that try to change the way your plots look.
Most change the matplotlib *rcParams*, but go no further. In addition, they
assume
you have not messed up your *rcParams* file, and it's not trivial to use many
different
themes in the same program.

This package tries to achieve the following:

* Every plotting call assumes nothing about styles, and will reset the
*rcParams* before every call. This makes it possible to use several themes in
one program and ensures consistency even if you've screwed up your *rcParams*
file.
* Tweak things that can't be tweaked with *rcParams*, like axes positioning,
legend alpha, etc.
* Allow everything to be customized. You can override all *rcParam* values in
the theme constructor.

# Examples


    %matplotlib inline
    %load_ext autoreload
    %autoreload 2
    import numpy as np
    
    from pyplotthemes import themes

## Logarithmic plots


    def logtest(theme):
        theme.figure(figsize=(15,5))
    
        for sub in range(3):
            # Set the random seed for consistency
            np.random.seed(12)
            theme.subplot(131 + sub)
            # Show the whole color range
            for i in range(8):
                y = 1 + np.random.uniform(size=10).cumsum()
                x = np.arange(10)
    
                if sub == 0:
                    theme.semilogx(x, y, label=str(i), marker='o')
                elif sub == 1:
                    theme.semilogy(x, y, label=str(i), marker='o')
                else:
                    theme.loglog(x, y, label=str(i), marker='o')
                    
                theme.legend(loc='best', ncol=3)
        
    
    for name, theme in themes.items():
        if name != "base":
            theme.latex = True
        logtest(theme)
        theme.gcf().suptitle(name)


![png](README_files/README_3_0.png)



![png](README_files/README_3_1.png)



![png](README_files/README_3_2.png)



    def histtest(theme):
        # Set the random seed for consistency
        np.random.seed(12)
        
        theme.figure(figsize=(5,4))
        
        x = np.random.normal(size=1000)
        
        theme.hist(x, label='A label')
        theme.legend(loc='best')
        
    for name, theme in themes.items():
        if name != "base":
            theme.latex = True
        histtest(theme)
        theme.title(name)


![png](README_files/README_4_0.png)



![png](README_files/README_4_1.png)



![png](README_files/README_4_2.png)



    def plottest(theme):
        # Set the random seed for consistency
        np.random.seed(12)
    
        theme.figure(figsize=(5,4))
    
        # Show the whole color range
        for i in range(8):
            y = np.random.normal(size=1000).cumsum()
            x = np.arange(1000)
    
            theme.plot(x, y, label=str(i))
    
        theme.legend(loc='best', ncol=3)
        
    
    for name, theme in themes.items():
        if name != "base":
            theme.latex = True
        plottest(theme)
        theme.title(name)


![png](README_files/README_5_0.png)



![png](README_files/README_5_1.png)



![png](README_files/README_5_2.png)

