from setuptools import setup, find_packages

setup(
    name='nlp_pos_tagger',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'nltk',
    ],
    author='AMNA AROOJ',
    author_email='amnaarooj5577@gmail.com',
    description='An NLP library for POS tagging',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Amna541/nlp_pos_tagger',
)
