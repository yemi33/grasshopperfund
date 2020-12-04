[Pull Request](https://github.com/grasshopperfund/grasshopperfund/pull/40)


## Changes: 

**Steve:**
Hey guys I finalized my code and pushed all the updates on the Github. Here's a summary of what I changed and updated:

Created Donation model/model forms

* able to donate to a campaign and if you already donated, the system won't let you donate again (as Caitlyn requested)

* Updated browse_organizations.html because previously, I found that although I am logged in as "steveck", I am able to view the organization made by "steve" (different user) and basically make posts and create campaigns although I am not the owner of the campaign. Updated it so that only the owner can make such actions

* Added a full list of donations made by the user in their profile

* Updated the campaign.current_money property function so that it correctly returns the total of all donations made

* currently when the current money exceeds the goal, the system doesn't do anything in terms of whether to no longer show the campaign, etc. I am guessing we should talk about this during a meeting later this week and ask what everyone else thinks we should do once this occurs.

Thank you all for your patience! I know it isn't much but all the changes should be present on Github.
