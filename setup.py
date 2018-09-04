from setuptools import setup


setup(name='corella',
      version='0.1',
      description='correlation matrix plots on the terminal',
      url='http://github.com/nk412/corella',
      author='Nagarjuna Kumarappan',
      author_email='nagarjuna.412@gmail.com',
      license='MIT',
      packages=['corella'],
      install_requires=[
          'pandas', 'colored'
      ],
      entry_points={
        'console_scripts': ['corella=corella.cli:main']
      },
      zip_safe=False)
