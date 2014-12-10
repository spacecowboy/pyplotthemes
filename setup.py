from distutils.core import setup, Extension


setup(name = 'pyplotthemes',
      version = '0.1',
      description = 'A wrapper around matplotlib with themes',
      author = 'Jonas Kalderstam',
      author_email = 'jonas@kalderstam.se',
      url = 'https://github.com/spacecowboy/pyplotthemes',
      packages = ['pyplotthemes'],
      package_dir = {'pyplotthemes': 'pyplotthemes'},
      install_requires = ['matplotlib>=1.3'],
     )
