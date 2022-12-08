# How To Run This Test

## Prerequisites 
1. Install Python 3.x your local env
2. Clone this project onto you local env
3. From within the project inside a virtual env(venv) run the command pip install seleniumbase

## Run Test
To run a test use the command
_**pytest -k test_name_**

To generate Reports pass in the _--dashboard_ flag
example pytest -k test_name --dashboard

To Run the test in headless mode pass in --headless flag
example _pytest -k test_name --headless_

To Run the test in headed mode pass in --headed flag
example _pytest -k test_name --headed_