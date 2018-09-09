from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='corella',
      version='0.0.2',
      description='correlation matrix plots on the terminal',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/nk412/corella',
      author='Nagarjuna Kumarappan',
      author_email='nagarjuna.412@gmail.com',
      license='MIT',
      packages=['corella'],
      install_requires=[
          'pandas>=0.23.4', 'colored>=1.3.93'
      ],
      entry_points={
        'console_scripts': ['corella=corella.cli:main']
      },
      zip_safe=False)
