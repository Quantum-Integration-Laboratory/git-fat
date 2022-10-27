
from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()
    #print(requirements)
  
long_description = 'QIL fork of git-fat, for handling our large data files. Mostly an attempt to port to python 3 and windows\
    fork largely deals with porting to windows and cleaning up usage somewhat'
#print(find_packages())
setup(
        name ='qil_git_fat',
        version ='1.0.0',
        author ='Ben Field',
        author_email ='bfie3543@uni.sydney.edu.au',
        url ='https://github.com/Quantum-Integration-Laboratory/git-fat/tree/master',
        description ='QIL fork of git-fat, for handling our large data files. Mostly an attempt to port to python 3 and windows',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='BSD-2',
        packages = find_packages(),
        scripts=['git_fat/git-fat'],
        classifiers =[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: BSD-2 License",
            "Operating System :: OS Independent",
        ],
        keywords ='git',
        install_requires = requirements,
        zip_safe = False
)