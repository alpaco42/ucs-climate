# ucs-climate

## Setting up your virtual environment with pipenv
1. Step one is installing pipenv if you don't have it already. Both Homebrew and pip make this very easy (e.g. `pip install pipenv`) but there's sometimes issues with Conda.

2. Navigate to the repository directory in a terminal window and run `pipenv shell`. This will initialize a virtual environment in that directory. Note that you must initialize the shell every time you open the directory.

3. Run `pipenv sync`. This will install all the dependencies you need for the project. Note that you only need to run this once.

## Adding new dependencies to the virtual environment
1. Go to the `Piffle` and add a line under the existing dependencies for the one you want to add.

2. In a terminal window, run `pipenv lock`.

3. Every future `pipenv sync` should now include the new dependency.