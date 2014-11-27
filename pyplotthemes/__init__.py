
from .base import BaseTheme
from .pretty import PrettyTheme


# Themes in namespace
base = BaseTheme()
pretty = PrettyTheme()

# Also keep a dict of themes
themes = dict(base=base,
              pretty=pretty)