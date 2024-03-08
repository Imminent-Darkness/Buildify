from setuptools import setup, find_packages

setup(
    name='buildify',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python project to generate a Shopify store using AI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/buildify',
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
        'requests',
        'beautifulsoup4',
        'Pillow',
        'torchvision',
        'transformers',
        'scikit-learn',
        'nltk',
        # etc.
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
