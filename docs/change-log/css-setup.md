[Pull Request](https://github.com/grasshopperfund/grasshopperfund/pull/48)

## Summary of my changes
Created a css folder for all stylesheets (static/css). Created and initialized a global stylesheet (static/css/style.css) and loaded it into main.html. Created and loaded an [empty] stylesheet for register.html (static/css/users/register.css).

**frontend documentation below❗ ❗ ❗**

## Introduction
This is a brief introduction on the frontend structure of Grasshopperfund. We will be using vanilla Django templates (for now) and a responsive CSS framework (Materialize) to make styling easier.

As mentioned above, the CSS framework we will be using is [Materialize CSS](https://materializecss.com/), based on Google's Material Design. We will also be utilizing [Google Fonts](https://fonts.google.com/) and [Material Icons](https://materializecss.com/icons.html).

## Folder setup
All css files for this project are found in `static/css`.
The global stylesheet, `style.css`, is responsible for the app's main styles. style.css is by default loaded into main.html, meaning that all other templates automatically inherit style.css's styles. If you are working on a page other than main.html and want to override a style in style.css, you need to create a new css file for that page.

## main.html
main.html is the main (haha) template that all of the other templates will be extending. It can be found in `grasshopperfund/templates`. main.html contains:
- The navigation bar
- The footer
- All global styles in style.css

## Creating & naming a new css file
If you are formatting a template (other than main.html) and want to override a style in style.css, you need to create a new css file for that template. Name the css file similarly to the template that will be using it. For example, if I wanted to create a stylesheet for the user registration template (`grasshopperfund/templates/users/register.html`), I would name the stylesheet `register.css` and place it in `static/css/users/`. You may have to create additional subfolders in the css folder depending on the templates you want to edit.

## Loading a new css file into a template
Once you create a new css file and place it in the correct folder, you must correctly insert it into a template in order for it to work properly. To do so, follow these steps in your _template_:

1. Insert `{% load static %}` tag at the top so that Django knows that your stylesheet is in /static/. Also double-check that your file contains `{% extends 'main.html' %}`.
2. Create a style block by adding `{% block styles %}` and `{% endblock %}`tags. All of your page content should go between these tags.
3. Load your stylesheet immediately after the opening `{% block styles %}` tag: `<link rel='stylesheet' href="{% static 'css/users/register.css' %}">`

As an example, [this is what register.html looks like](https://prnt.sc/vmh9vn) after loading register.css stylesheet into it.
Note that once you load another css file into your template, you can override global styles!

## Design guidelines
The design guidelines for this project can be found [here](https://www.figma.com/file/fEJlgeYxgEMve45zMURP4H/Design-Guidelines?node-id=0%3A1).

## Global stylesheet (style.css)
style.css contains a basic implementation of all of the [design guidelines](https://www.figma.com/file/fEJlgeYxgEMve45zMURP4H/Design-Guidelines?node-id=0%3A1) outlined in our Figma folder.
The current components included are:
- **Colors**: all 5 primary colors (lightgreen, green, darkgreen, lightgrey, and yellow) are listed as variables in the :root pseudoclass. Note that these variables only work in style.css and cannot be used in other css files.
- **Fonts**: Poppins and Lato are both loaded into main.html and can be used in any stylesheet, not just style.css. Poppins has been set to the default font.
- **Buttons**: 3 different button classes have been initialized: `.btn`, `.btn-flat`, and `.btn-yellow`. `.btn` is a default green button, `.btn-flat` is a white button with green text, and `.btn-yellow` is a, you guessed it, yellow button. Buttons can also be large (.btn-large) or small (.btn-small) - see [Materialize documentation](https://materializecss.com/buttons.html) for more info
- **Brand logo**: The brand logo (.brand-logo) has been set as per the design guidelines.

Other styles that should be in style.css but are not yet initialized include .navbar, .card, and .carousel.
