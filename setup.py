from setuptools import setup
import unittest


def get_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('test', pattern='test_*.py')
    return test_suite

setup(
    name='es-bgm',
    version='1.5.1',
    packages=['bgm'],
    url='',
    license='GPL',
    package_data={'bgm': ['bgmconfig.ini']},
    author='DOCK.PI3',
    author_email='DOCK.PI3@gmail.com',
    description='Adaptado para MasOS ,MUSICA DE FONDO PARA EmulationStation',
    requires=['mock', 'pytest'],
    entry_points=
    {'console_scripts':
         ['startbgm = bgm:main']
     },
    test_suite='setup.get_test_suite',
    data_files=[('/lib/systemd/system', ['service/bgm.service']),
                ('/etc', ['cfg/bgmconfig.ini']),
                ('/home/pi/MasOS/roms/music', ['extra/COPIAR_MUSICA_AQUI'])]
)
