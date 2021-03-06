# Onboarding

This is meant to help onboard frontend developers.

Our Project Structure:

```
└───grasshopperfund
    ├───grasshopperfund        <-- Django-related files are here
    │   ├───organizations      <-- Django models and views for organizations
    │   ├───campaigns          <-- Django models and views for campaigns
    │   ├───users              <-- Django models and views for users
    │   ├───tags               <-- Django models and views for tags
    │   └───templates          <-- Django HTML templates
    │       ├───organizations
    │       ├───campaigns
    │       ├───users
    │       └───tags
    │    
    └───static <--- images used for the website.
```

## What do I need to know?

Simply follow the links under "Getting Started". I suggest this order:

1. [Installation](/installation)
2. [Git Workflow](/Git-Workflow)
3. [Django](/Django)

## Simple assignment

**[Read this on how to use Git](https://www.notion.so/Git-With-The-Flow-1c62521d9fb747a1ae9ce0f4ecf6bcdb)**

The point of this assignment is to get you familiar with Git, Django, and our project. Please follow the [installation guide](/installation) before attempting this. 

1. `git clone` the repository
2. make your own branch and publish it.
3. Make a simple edit to `startsmart/templates/main.html`. Add a comment, button, whatever
4. `git add` the changed file
5. `git commit` that edit
6. `git push` that edit
7. Make a pull request explaining your edit.
