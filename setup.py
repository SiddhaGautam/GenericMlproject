#this file helps us whatever the machine learning algorith or project we made that will get converted as a package and later we can use it as importing the package..also we can deploy it in pypi

from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->list[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[val.replace("\n","") for val in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


setup(
    name="GenericMlproject",
    version="0.0.1",
    author="Gautam",
    author_email="gautamtiwari0258@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")

)