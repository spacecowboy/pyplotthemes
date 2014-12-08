
from .base import BaseTheme
from .pretty import PrettyTheme
from .classic import ClassicTheme


# Themes in namespace
base = BaseTheme()
pretty = PrettyTheme()
classic = ClassicTheme()

# Also keep a dict of themes
themes = dict(base=base,
              pretty=pretty,
              classic=classic)