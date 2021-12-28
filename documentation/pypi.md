# PyPi

## How to build a version and push it to PyPi ?
1. Update the version in [**setup.cfg**](./../setup.cfg)
2. Execute the command to build the project
> py -m build
3. Execute the command to push the project.
> py -m twine upload --repository pypi dist/*
> 
> (You will need to give your username/password of your PyPi account)

*[Full Tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)*
