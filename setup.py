from setuptools import setup, find_packages

setup(
    name='moonlib', 
    version='0.1.0', 
    author='Lunar',
    description='Un module pour les couleurs et les emojis',
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown',
    url='https://github.com/Luunarr/moonlib', 
    packages=find_packages(where='src'), 
    package_dir={'': 'src'},  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)