# Added Organizations
**This is a basic implementation of Organizations for #13 . Not all model attributes have been added**

## 🌟 What's new?

#### Added directories

All models, views, and URLs directly related to Organizations can be found under `startsmart/organizations`.

All templates used for Organizations can be found under `startsmart/templates/organizations`.

#### New Database Models

I have created new models named `Organization` and `Post`. The reason I created `Post` is because it is needed as an attribute of `Organization`, as indicated in our database ER diagram. It should also help whoever will be implementing it.

You can find these new models within `startsmart/organizations/models.py`

#### Organization CRUD
You can now create, view, update, delete, and browse organizations! Much of the functionality is based on the current implementation of Campaigns.

Here are the new URL paths:

* `/organizations/view/<organization_name>`
* `/organizations/update/<organization_name>`
* `/organizations/delete/<organization_name>`
* `/organizations/create`
* `/organizations/browse`

## 😮 What's changed?

Besides `settings.py`, I have limited my changes to existing files to avoid merge conflicts. That being said, the implementation of Organizations has been limited.

## 😢 What's missing?

To avoid merge conflicts, I have not made any edits to `users` or `campaigns`. Because of this, I cannot implement the following:

Organizations

* Followers
* Campaigns
* Tags

Posts

* Likes
* Tags

## 🏃🏽‍♂️ Going forward

Once this is approved, and after checking where you guys are making edits, I'd like to make major changes to `startsmart/campaigns` to be in line with the current requirements and database design. Campaigns are currently made and owned by any registered user. Now, they can only be made and owned by an organization owner, and **every campaign must be associated with an organization**.

The implementation of Organizations will cause cascading changes for campaign models, views, and URL paths. Thus, **organizations cannot be fully implemented until these changes are made**.
