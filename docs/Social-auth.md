# Social Authentication

uses `allauth` library.
## Two methods
There are two methods to setting up Social Authentication using apps like Google and Facebook.
* **Default**: Environmental Variables (complex but automates the process)
* Django Admin (Simple but time consuming)

## Environmental Variables
You can configure your API credentials as environmental variables, which are defined in `config.py`.

Be sure to have your python virtual environment activated.


## Django admin
Be sure to comment out the 'APP' key-value pair in `startsmart.settings.py` within the dictionary `SOCIALACCOUNT_PROVIDERS`.

Log into `domain/admin` (probably `localhost:8000/admin`) with the superuser you created.
