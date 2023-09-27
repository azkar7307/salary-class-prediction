from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(filepath: str) -> List[str]:

    requirements = []
    
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace('\n', '') for i in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


setup(name='Salary_Class_Classification',
    version='0.0.1',
    description='Salary Class Classification Pipeline Project',
    author='Mohammad Azkar',
    author_email='azkar7307@gmail.com',
    url='https://github.com/azkar7307/salary-class-prediction.git',
    packages=find_packages(),
    install_reqires = get_requirements('requirements.txt')
)