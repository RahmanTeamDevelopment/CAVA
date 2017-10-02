from setuptools import setup

setup(
    name='CAVA',
    version='1.3.0',
    description='Annotation of genetic variants',
    url='https://github.com/RahmanTeamDevelopment/CAVA',
    author='Marton Munz',
    author_email='munzmarci@gmail.com',
    license='MIT',
    packages=['cava'],
    scripts=[
        'bin/CAVA.py',
        'bin/cava',
        'bin/dbsnp_prep.py',
        'bin/ensembl_prep.py'
    ],
    zip_safe=False
)
