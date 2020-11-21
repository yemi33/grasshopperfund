[Pull Request](https://github.com/grasshopperfund/grasshopperfund/pull/50)

## Organizations + Posts Implemented

Organizations and posts basic implementation. You can now create, edit, delete, and view organizations and posts. Tests have also been implemented, providing over 90% coverage over `grasshopper/organizations` and `grasshopper/posts`.

This covers issues #13 and #38.

### Organizations

All python files related to organizations can be found under `grasshopper/organizations`. HTML templates can be found under `grasshopper/templates/organizations`.

New organization URLs are under `/organizations`:

* `/organization/browse` Browse an unordered list of Organizations. Buttons to view are available publicly, and buttons to edit/delete are available to owners.
* `/organization/view/<organization_name>` View an organization, its posts, and campaigns.  Buttons to view posts are available publicly, and buttons to edit/delete posts/organization are available to owners. Form to create a new post is available to owners. Button to create a campaign is available to owners.
* `/organization/update/<organization_name>` Edit an organization.
* `/organization/delete/<organization_name>` Delete an organization.
* `/organization/create` Create an organization.

To reiterate, you must go to `/organization/view/<organization_name>` to create a campaign. A different flow to create a campaign can be implemented, but this is the short term solution to enforce that an `Organization` must be created before a `Campaign` is created. If an attempt to create a `Campaign` without a parent `Organization` specified, it will cause an `Internal Server Error`.

![demo org](https://gifs.tisuela.com/grasshopperfund/new_organization_demo.gif)

### Posts

All python files related to posts can be found under `grasshopper/posts`. HTML templates can be found under `grasshopper/templates/posts`. I've added a simple template called `templates/posts/post.html` which is a **simple Materialize card, from which all posts are displayed.**  In other words, `templates/organizations/view_organization.html`, `templates/posts/view_post.html`, and other templates which display a post include the template `templates/posts/post.html`.

To view an Organization's feed of posts, see `organization/view/<organization_name>`.

All post URLS are under `/posts`. Note that currently, all URLs must take the name of an Organization as a parameter -- this helps the backend process requests.  

* `/posts/view/<organization_name>/<post_id>` View a single post.
* `/posts/update/<organization_name>/<post_id>` Edit a post.
* `/posts/delete/<organization_name>/<post_id>` Delete a post.
* `/posts/create/<organization_name>` Create a post.

![demo posts](https://gifs.tisuela.com/grasshopperfund/posts_demo.gif)

Side note: Posts `views.py` uses class-based Django views. Previously, we have been using function-based Django views. Class-based Django views allow for more control, and we can use built-in generic views that make implementation quicker and simpler. Read more about class-based Django views [here](https://docs.djangoproject.com/en/3.1/topics/class-based-views/).
