## Added Tags

## ✅ Demo of the Campaigns with Tags

Below are demos of Tags.

###🔶 Campaigns without existing tags

![campaign_without_existing_tags](https://user-images.githubusercontent.com/32473119/99199793-7a739d00-2756-11eb-9dfe-add8801d2341.gif)

### 🔷 Campaigns with existing tags

![campaign_with_existing_tags](https://user-images.githubusercontent.com/32473119/99199808-95461180-2756-11eb-9c86-1a01a28ac0c1.gif)

## How to run makemigrations command with Campaigns and Tags

If the migrations for campaigns and / or tags got deleted or want to delete those two migrations, use this command:

```
python manage.py makemigrations campaigns tags
```

[Please see this link that describes about "No changes detected" prompt for makemigrations](https://stackoverflow.com/questions/36153748/django-makemigrations-no-changes-detected)

Where it talks about this problem:

![image](https://user-images.githubusercontent.com/32473119/99199965-86139380-2757-11eb-8fef-e6fc82ec2610.png)

This will solve the issue if you got a CircularDependencyError error issue when running this command

```
python manage.py migrate
```

[Please see this link that describes about the CircularDependencyError error issue](https://stackoverflow.com/questions/30981578/django-1-8-migrations-circulardependencyerror/32575954)

## 🔵 Testing for Tags app

In case if you have tests.py in the tags app (as shown in the image below):

![image](https://user-images.githubusercontent.com/32473119/99200154-86f8f500-2758-11eb-8c81-106fca30c2a3.png)

Delete the tests.py and you should have a folder name tags\tests folder that looks something like this (as shown in the image below):

![image](https://user-images.githubusercontent.com/32473119/99200227-f2db5d80-2758-11eb-9fb0-ee4d1ef18503.png)

Use this command to run the test cases for tags:

```
python manage.py test startsmart.tags
```

## 🎁 What contains the folder of Tags app?

The Tags folder contains __init__.py, admin.py, apps.py, forms.py, models.py, urls.py, and view.py (as shown in the image below):

![image](https://user-images.githubusercontent.com/32473119/99200388-d2f86980-2759-11eb-97c9-9454a905e259.png)

The Tags folder also contains migrations and tests under these two files (as shown below):

`startsmart/tags/tests` and `startsmart/tags/migrations`

You can see all of the contents of Tags folder under the name: `startsmart/tags`

You should see `'startsmart.tags.apps.TagsConfig'` in the `settings.py`

You should see the templates about Tags under this folder: `startsmart/templates/tags`  

## 💾 URLs for Tags

You should only see this url: `filter/<tagname>`
Note that I will add additional urls for Tags later on as I'm experimenting on it.

## 🏃‍♂️ Next steps

- I will continue to work with Tags and Organizations to create an Organization with Tags and move forward with Adding Campaigns in the Organizations once I get familiar with the concept interface testing interactions between Organizations and Tags.
- I will also continue to add other command lines such as this one as an example: `python manage.py makemigrations campaigns tags organizations` , more on that later on.
- I will be working on the search bar for Campaigns once when I configure testing interactions between Organizations and Campaigns with / without Tags.
- I will try to come up with a way to perform makemigrations on each seperate models, such as this one as an example:
`python manage.py makemigrations campaigns` but for now on you can write this command line if a Tags app needs to be added in the Campaigns app. `python manage.py makemigrations campaigns tags`

Thanks for understanding!
