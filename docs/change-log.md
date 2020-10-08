# Change Log

## 🔒 Removing vulnerabilities
### Removed API secrets
Instead of using Django Admin to store Social App developer secrets, they are now stored in `startsmart/settings.py`. Facebook and Google API secrets have been **publicly exposed 😬** -- I suggest the owner refresh their secrets.

There are two methods for providing your Facebook and Google API secrets.
* **Default**: Environmental Variables
* **Old / easier way**: Django admin

More info [here](https://nananananate.github.io/startsmart-backend-version/Social-auth/)

### Removed user information
The SQLite database was included in the commit -- this would allow anyone to obtain user information. I removed it and wrote documentation on how to initialize it.

## 📝 Documentation
A simple readme to install dependencies, initialize the database, and run the server.
In-depth documentation [hosted on the web](https://nananananate.github.io/startsmart-backend-version/).

**TO DO**: *Elaborate on developing locally*

## 📈 Scalability
Project restructured for scalability. Since this project is titled as a **backend-version**, this new structure allows for easier implementation of Web API endpoints such as REST or GraphQL. With that django-powered Web-API, this structure allows for an addition of a front-end framework such as React or Vue.js.

### Structure guidelines
Here are some points to follow when contributing:
* Initialize database with each new clone using `python manage.py migrate`
* Use packages and keep them within the `startsmart` directory
* Use environmental variables for sensitive information, which you can configure in *config.py*
* Don't commit private information such as a database or profile pictures (these are already included in `.gitignore`).

**Example**: Let's say you want to implement Campaigns. You'll need a new set of routes/models for `campaigns`.
* Create a new folder within `startsmart` called `campaigns`, and create an `apps.py` within `startsmart.campaigns` (see `startsmart.users` for an example structure and `apps.py`).
* Define your URL routes within `startsmart.campaigns.urls` instead of `startsmart.urls`.
* Register this app within `startsmart.settings.INSTALLED-APPS` as `startsmart.campaigns`

This project restructure is based on [this popular Django cookiecutter](https://github.com/pydanny/cookiecutter-django)

### Url routing
Now URL routes are no longer defined `startsmart.urls`. Routes are now each defined in their respective directory, which is currently only `startsmart.users.urls`. Those routes are then imported into `startsmart.url` with `INSTALLED-APPS` registered in `startsmart.settings`
