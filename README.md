# OpenPedia

This application is an encyclopedia where users
can visit pages about certain topics, search
for specific pages and create new pages.


## Getting Started
This application requires installing **django** and
**markdown2** using ```pip3 install Django``` and
```pip3 install markdown2``` 
respectively.

## Design Document
To add new pages to the website, the *urls.py* and the *views.py*
files need to be changed to save the new url patterns and to load the
HTML of the new page the url references. Of course, this means that a 
new HTML file has to be created for the new page.

The HTML pages can be categorized:
* The homepage (index)
* Subject pages
* Search pages
* Error page
* Create page

The homepage has a link to every page, except the error page.
This page can only be accessed by editing the current page
in the search bar. All pages have a sidebar with a link to the homepage, 
a search bar and the create page.

The search pages include a page with succesful search results and
a page where the search resulted in no results.

The create page lets users create a page in markdown text.
If the page does not exist yet and is saved, the new page is 
created and the user is brought to that page. If it does,
the user gets an error message and the page is not saved.

## UI Sketch
![UI_Sketch](/images/pages.png)

This image shows a rough idea of what each page is going to look
like. References to other pages are shown using color coding,
where each colored circle is a reference to the circled page
(header) of the same color.

## Workflow Diagram
![workflow_diagram](/images/flowdiagram.png)

This image depicts the application workflow diagram. The arrows
show where from what page the user can navigate to another.
Note that most arrows where the sidebar would have been used
are not shown, since every page has this sidebar and this would
clutter the diagram. The dotted lines show some of those
initial sidebar connections. The dashed arrow with a plus sign
shows the new subject page being added to the site. The error page 
can not be accessed in an intended way.
## Authors

- [Finn Peranovic](https://github.com/LignumVerus)


## Acknowledgements

This website was made for the minor "programmeren" at the
University of Amsterdam (2021-2022).