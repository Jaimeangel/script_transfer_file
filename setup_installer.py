from distutils.core import setup
import py2exe
import os
import shutil

# Copiar los binarios de Playwright manualmente
def copy_playwright_binaries():
    playwright_dir = os.path.join(os.path.dirname(__file__), 'playwright')
    destination_dir = os.path.join(os.path.dirname(__file__), 'dist', 'playwright')
    if os.path.exists(playwright_dir):
        shutil.copytree(playwright_dir, destination_dir)

setup(
    console=['your_script.py'],
    options={
        'py2exe': {
            'packages': ['playwright'],
            'bundle_files': 1,
            'compressed': True
        }
    },
    zipfile=None,
    data_files=[
        # Añade aquí cualquier otro archivo necesario
    ],
    cmdclass={
        'build': copy_playwright_binaries
    }
)

# Copiar los binarios de Playwright
copy_playwright_binaries()
