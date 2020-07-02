# Rp5CleanupWorker
Selenium-based worker for cleanup old launches from EPAM ReportPortal (Workaround for RP5.0.0 bug with cleanup old reports cronjobs)

1. Install Python (&pip)

2. Install all dependencies for the project:
a) pip3 install -r requirements.txt - UNIX
b) pip install -r requirements.txt - Windows:

3. Put valid values into properties.py
a) username, password - credentials for RP user
b) filter url - url to filter, which contains items you want to delete (for example, filter for launches > 1 month ago)

4. run python start_app.py
