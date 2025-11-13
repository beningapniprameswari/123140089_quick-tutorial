from setuptools import setup

# List of dependencies installed via `pip install -e .`
# by virtue of the Setuptools `install_requires` value below.
requires = [
    'pyramid',
    'waitress',
]

setup(
    name='tutorial',
    install_requires=requires,
)
from setuptools import setup

requires = [
    'pyramid',
    'waitress',
]

setup(
    name='tutorial',
    install_requires=requires,
    # --- TAMBAHKAN BLOK INI ---
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main'
        ],
    },
    # ---------------------------
)