from setuptools import setup, find_packages
import os
import mapsud

setup(name = 'mapsud',
      version = '1.0.3',
      url='https://github.com/lucea97217/mapsud.git',
      author = 'LUCEA, VALDEYRON, YUAN',
      author_email = 'lenny.lucea@etu.umontpellier.fr',
      maintainer = 'LUCEA, VALDEYRON, YUAN',
      maintainer_email = 'lenny.lucea@etu.umontpellier.fr',
      keywords = 'Tarifs autoroutiers sud France',
      packages = ['mapsud','test'],
      description = 'voir presentation git',
      long_description = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read(),
      license = 'MIT',
      platforms = 'ALL',
     )