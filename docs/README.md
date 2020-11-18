# [Grasshopperfund](https://docs.grasshopperfund.tisuela.com/)

[![Coverage Status](https://coveralls.io/repos/github/grasshopperfund/grasshopperfund/badge.svg?branch=master)](https://coveralls.io/github/grasshopperfund/grasshopperfund?branch=master)
[![CodeFactor](https://www.codefactor.io/repository/github/grasshopperfund/grasshopperfund/badge)](https://www.codefactor.io/repository/github/grasshopperfund/grasshopperfund)

## Installation

**Clone repository**
```
git clone https://github.com/grasshopperfund/grasshopperfund/
```

**Navigate into repository**   
```
cd grasshopperfund
```

**🐍 Create Python virtual environment**

There are a good amount of depencies for this project -- it will be good practice to use a virtual environment, albeit not necessary.

macOS/Linux

```
python3 -m venv env
```

Windows Command Line

```
python -m venv env
```

Windows Powershell

```
python -m venv env
```

The last argument is the location to create the virtual environment. Generally, you can just create this in your project and call it env.


**✅ Activate virtual environment**

macOS/Linux

```
source env/bin/activate
```

Windows Command Line

```
.\env\Scripts\activate.bat
```

Windows Powershell

```
.\env\Scripts\activate.ps1
```


**Install Requirements**

```
python -m pip install -r requirements.txt

```

### Configuration

**🔐 This portion provides API authetnication information. You can skip this**

We use environmental variables to store sensitive information. Anything that is committed to this repository becomes publicly available, and it is difficult to remove. The use of environmental variables is preferred (over, say, manual input via Django Admin) in order to use Github Actions to automate testing.

Environmental variables are configured at [`config.py`](https://raw.githubusercontent.com/PeterOR2D2/startsmart-backend-version/master/config.py)

``` python
import os

class Config:

  SOCIAL_AUTH_FACEBOOK_APP_ID = os.environ.get(
    "SOCIAL_AUTH_FACEBOOK_APP_ID", "")

  SOCIAL_AUTH_FACEBOOK_APP_SECRET = os.environ.get(
    "SOCIAL_AUTH_FACEBOOK_APP_SECRET", "")

  SOCIAL_AUTH_FACEBOOK_APP_KEY = os.environ.get(
      "SOCIAL_AUTH_FACEBOOK_APP_KEY", "")

  SOCIAL_AUTH_GOOGLE_APP_ID = os.environ.get(
      "SOCIAL_AUTH_GOOGLE_APP_ID", "")

  SOCIAL_AUTH_GOOGLE_APP_SECRET = os.environ.get(
      "SOCIAL_AUTH_GOOGLE_APP_SECRET", "")

  SOCIAL_AUTH_GOOGLE_APP_KEY = os.environ.get(
      "SOCIAL_AUTH_GOOGLE_APP_KEY", "")
```


#### Method 1: secrets.json

Currently not implemented.

#### Method 2: Set environmental variables

🌳 If you do not have our json file, or if you cannot use it for some reason, you will need to write environmental variables within your terminal. **These variables must be made in the terminal/shell where your virtual environment is running**

The environmental variables are specified within `config.py`

To set environmental variables, follow these instructions:

**Social Authentication API Tokens**

    Not all of these fields may be required, but please populate as much as you can.

macOS/Linux

``` bash
export SOCIAL_AUTH_FACEBOOK_APP_ID=your_facebook_app_id
export SOCIAL_AUTH_FACEBOOK_APP_SECRET=your_facebook_app_secret
export SOCIAL_AUTH_FACEBOOK_APP_KEY=your_facebook_app_key
export SOCIAL_AUTH_GOOGLE_APP_ID=your_google_app_id
export SOCIAL_AUTH_GOOGLE_APP_SECRET=your_google_app_secret
export SOCIAL_AUTH_GOOGLE_APP_KEY=your_google_app_key
```

Windows Command Line

``` bat
set SOCIAL_AUTH_FACEBOOK_APP_ID=your_facebook_app_id
set SOCIAL_AUTH_FACEBOOK_APP_SECRET=your_facebook_app_secret
set SOCIAL_AUTH_FACEBOOK_APP_KEY=your_facebook_app_key
set SOCIAL_AUTH_GOOGLE_APP_ID=your_google_app_id
set SOCIAL_AUTH_GOOGLE_APP_SECRET=your_google_app_secret
set SOCIAL_AUTH_GOOGLE_APP_KEY=your_google_app_key
```

Windows Powershell

``` powershell
$env:SOCIAL_AUTH_FACEBOOK_APP_ID="your_facebook_app_id"
$env:SOCIAL_AUTH_FACEBOOK_APP_SECRET="your_facebook_app_secret"
$env:SOCIAL_AUTH_FACEBOOK_APP_KEY="your_facebook_app_key"
$env:SOCIAL_AUTH_GOOGLE_APP_ID="your_google_app_id"
$env:SOCIAL_AUTH_GOOGLE_APP_SECRET="your_google_app_secret"
$env:SOCIAL_AUTH_GOOGLE_APP_KEY="your_google_app_key"
```


### Running Django

**Initialize database**

``` console
python manage.py migrate
```



**Run Django app**

```
python manage.py runserver
```



## Utilities


Be sure that the Django app is **NOT** running for these steps

### Creating a super user
This allows access to `/admin`



``` console
python manage.py createsuperuser

// Input the username for superuser login
Username (leave blank to use 'default'): administrator

// You can leave email blank
Email address:

// Password must be at least 8 characters long

Password: ********
Password (again): ********
```
