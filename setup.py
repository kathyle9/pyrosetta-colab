from distutils.core import setup
from setuptools import setup
setup(
  name = 'pyrosetta-colab',         # How you named your package folder (MyLib)
  packages = ['pyrosetta-colab'],   # Chose the same as "name"
  entry_points = {
     'console_scripts': [
        'pyrosetta-colab = pyrosetta-colab.__main__:main'
     ]
  },
  version = '0.8',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Contains commands for using PyRosetta in Google Colaboratory',   # Give a short description about your library
  author = 'Kathy Le',                   # Type in your name
  author_email = 'kle16@jhu.edu',      # Type in your E-Mail
  url = 'https://github.com/kathyle9/pyrosetta-colab',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/kathyle9/pyrosetta-colab/archive/v_04.tar.gz',    # I explain this later on
  keywords = ['PyRosetta', 'Google Colaboratory'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
