from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(f_path: str)->List[str]:
    '''
    Returns list of requirements
    '''
    requirements = []
    with open(f_path) as f_obj:
        requirements = f_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
 name = 'imageclassification',
version='0.0.1',
author='Harjas',
author_email='hrohra2004@gmaill.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt'),
)