# Suggestions

## Additional Database Models
**💾 Models needed for a working prototype**

* Campaign Tags
* Donation
* Membership Type

### More suggested models
Not necessary, but may be useful

* User roles (creator, team member, investor/backer, beneficiary)
* Comments


## Social Authentication
**👯‍♂️ With Social Authentication already implemented, there's a lot more that can be done with it**

* Invite friends to StartSmart
* Prepopulate profiles based on Social media accounts
* Share campaigns 


## Campaign Search Engine
**🔍 Search campaigns via tags, description, creator, and title from one simple search bar.**

* Implementation via [ElasticSearch](https://django-elasticsearch-dsl.readthedocs.io/en/latest/quickstart.html)
* Feasible to implement within the next few weeks
* Improve UX for finding causes to support


## Template forms
**📝 Offer prefilled forms made by us and other users based on the type of campaign.**

* Works with `crispy-forms`.
* Gives non-technical users a quick way to create a campaign.

## Web API
**🌐 Most likely a REST API, but [implementation of](https://docs.graphene-python.org/projects/django/en/latest/tutorial-plain/) [GraphQL](https://graphql.org/) would be nice.**

### Mobile App Development
📱 Allows the reusability for many backend features in the creation of an iOS or Android app.

* Authentication (Session, login, Social Authentication, etc.)
* Registration
* Campaigns
* etc. (basically, anything in the backend can be reused as long as the Web API is properly implemented)

Easy to implement while developing the prototype via the [Django REST Framework](https://www.django-rest-framework.org/)

### Separation of Backend and Frontend
🤝 While Django is a complete framework for fullstack web development, it does have limitations in UI/UX due to it's template-based pages. A fully implemented Web API would allow work to be cleanly separated with a Django backend and some frontend framework (Vue.js, React.js, etc.).

* Opens up to the creation of an SPA website.
* Potential to vastly improve UI/UX with increased reactivity and quicker loading times

### HTML Widgets
⚙ GoFundMe has a nice [HTML widget](https://support.gofundme.com/hc/en-us/articles/203604554-Adding-a-GoFundMe-Widget-to-a-Blog-or-Website) for donations. A Web API would make it easier to create this.

### Control to the user
👑 Allow campaign creators and their team to do more with fundraising data (incorporating current funds and donation button on their website or app)
