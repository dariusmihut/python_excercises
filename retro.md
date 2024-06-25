- base programming
- basic python tasks like:
    - running a script
    - installing requirements.txt (pip install -r requirements.txt, alternative install with setup.py "pip install .") / setup.py offers more than requirements.txt as it can define the package and it can be installed as such.
        - A specific version can be pinned in both methods, the setup.py extends the functionality and allows the package to be installed (packaging and distributing the project) and to install all the configured dependencies
        ```python
        # example
        install_requires=[
            'package1>=1.1,<1.7',
            'package2>=2.1'
            ]
        
        # example with complete setup parameters

        setup(
            name='training',
            version='1.0.0',
            packages=find_packages(include=['trainingproject', 'trainingproject.*']),
            install_requires=[
            'package1>=1.1,<1.7',
            'package2>=2.1'
            ],
            entry_points={
               'console_scripts': ['trainme=trainingproject.train:main']
            }
        )
        ```
    - working with format, composing "telegrams", using ljust to get the string to the desired length if the provided string does not meet the required length
    - read a csv file and based on the data (rows and content) generate a json object for each row and write the data in a json file 
    - getting into the main function and how to use the arguments
    - work with exceptions, what means "try > except > else > finally" - throw exceptions
    - work with paths - absolute vs relative
    - work with files
    - functions, define and call them
    - json, how to load string to json (loads) and to dump json object into string (dump)
    - load a json file and read the given properties in form of ex. prop1.subprop1 with the possibility of having multiple levels
    - calling a demo endpoint ("https://dummy.restapiexample.com/api/v1/employees") and printing the response, and printing specific properties from the response

    - connect to oracle DB
    - connect to MongoDB