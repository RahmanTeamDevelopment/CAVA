from setuptools import setup

setup(
    name='Cava',
    version='1.2',
    description='Annotation of genetic variants',
    url='https://github.com/RahmanTeamDevelopment/CAVA',
    author='Marton Munz',
    author_email='munzmarci@gmail.com',
    license='MIT',
    packages=['cava'],
    scripts=[
        'bin/CAVA.py',
        'bin/dbsnp_prep.py',
        'bin/ensembl_prep.py'
    ],
    zip_safe=False
)