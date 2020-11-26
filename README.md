# STATSBOMB ETL TASK

The aim of this project is to take the full names of employees attending a social separated by commas as CLI arguments and return valid venues to visit and also the reasons why remaining venues are invalid for the attendees. The venues.json file contain the menu of all potential venues, the users.json file contains what all employees would like to drink and will not eat. These files are pulled from a public GCS (Google Cloud Storage) bucket.

The aim of this project is to ingest NYC yellow taxi data from the following URL: (https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) and load into a MySQL database and perform analysis on the data. The ETL task, MySQL connection, and Start/End date range of files to ingest are specified in config.py. 

The application is run on a Google Cloud Platform Virtual machine with the following specs:
* Region: eu-west2-c
* Type: n2-standard-4 (4vCPU, 16GB memory)
* OS: Ubuntu 18.04 LTS
* Persistant disk: 700GB

INSTRUCTIONS:

- SSH into Virtual machine
- Ensure Python3 is installed
- Create a Python3.6 virtual environment and activate
- Clone the 'timeout-task' repository locally through the terminal via HTTPS or SSH e.g:
  'git clone https://github.com/Josephabiy/statsbomb.git'
- Navigate into the package:
  'cd statsbomb'
- Install the package dependencies, run the following in the terminal:
  'python setup.py develop'
- Install MySQL
- Update the MySQL connection variables as per your requirements in the config.py file
- Copy the create the table commands specified in the sql_vars.py file
- Copy the Dimension data insert statments specified in sql_vars.py file
- Execute the programme, run the following in the terminal:
  'python src/main.py'
- Detach from the terminal:
  'ctrl+a' followed by 'ctrl+d'
- Reconnect to the session when required:
  'screen -r'

UNIT TESTS:

- Tests if 'test_date_range_by_month' function successfully generates a list of dates between START_DATE and END_DATE
- Execute the unit tests in the terminal:
  'pytest -v'
  
SQL TASK:

- TBC

TO DO:

- Improve unit test converage
- Improve Exception handling to catch specific errors
- Apply specific data validy checks
- Move logging to separate config file
