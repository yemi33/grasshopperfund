# [StartSmart Django Backend](https://docs.startsmart.tisuela.com/)
[![Coverage Status](https://coveralls.io/repos/github/PeterOR2D2/startsmart-backend-version/badge.svg?branch=master)](https://coveralls.io/github/PeterOR2D2/startsmart-backend-version?branch=master) [![CodeFactor](https://www.codefactor.io/repository/github/peteror2d2/startsmart-backend-version/badge)](https://www.codefactor.io/repository/github/peteror2d2/startsmart-backend-version)
## Installation

**Clone repository**
```
git clone https://github.com/nananananate/startsmart-backend-version
```

**Navigate into repository**
```
cd startsmart-backend-version
```

**🐍 Create Python virtual environment**

There are a good amount of depencies for this project -- it will be good practice to use a virtual environment, albeit not necessary.

On macOS and Linux:
```
python3 -m virtualenv env
```

On Windows:
```
python -m venv env
```
The second argument is the location to create the virtual environment. Generally, you can just create this in your project and call it env.


**✅ Activate virtual environment**

On macOS and Linux:
```
source env/bin/activate
```

On Windows Command Line:
```
.\env\Scripts\activate.bat
```

One Windows Powershell
```
.\env\Scripts\activate.ps1
```

**Install dependencies**
```
python -m pip install -r requirements.txt
```

**Initialize database**
```
python manage.py migrate
```

**Run Django app**
```
python manage.py runserver
```


## Quick Start
Be sure that the Django app is **NOT** running for these steps

### Creating a super user
This allows access to `/admin`
```
python manage.py createsuperuser
```
