from setuptools import find_packages,setup
from typing import List

HYPER_E_DOT = '-e .'

def get_requirements(file_patrh)->List[str]:
    '''
    this function returns a list of requirementscls
    
    '''
    
    requirements=[]
    
    with open(file_patrh) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPER_E_DOT in requirements:
            requirements.remove(HYPER_E_DOT)
            
        return requirements
    command:python.viewOutput
    
setup(
    name='House_price_predictions',
    version='0.0.1',
    author='kunal patil',
    author_email='kunal15cr@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
    