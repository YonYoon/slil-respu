# slil-respu
#### Vide Demo: https://youtu.be/LZYLYmY-mMw
#### Description: Website with motivatinal advices for everyone who 'slil respu'.
* Virtual environment is used to install packages like Flask and so on.
* `slilrespu` directory contains the whole project. All files and directories described later are located there.
* `app.py` file is the main file of the project. It handles initializing database, storing current quote text and image name, defines various app routes.
* `database.db` is the file containing SQL table `quotes`. There are two columns in this table: `id` and `content`, and 19 rows.
* `schema.sql` contains SQL code that runs on database initialization to create table `quotes` if it is not created yet.
* `templates` directory contains html files that rendered when requested by URLs defined in `app.py`.
* `templates/index.html` is the template rendered on root URL `/`. It shows motivational advices. Advice can be replaced by another one 
* `templates/about.html` is the template rendered on `/about` URL. It shows the page describing the purpose of the project.
* `templates/layout.html` is the boilerplate template that used in other templates. It contains the header, links to css and Google font.
* `static` directory contains files used for styling.
* `static/styles.css` is the main and only css file.
* `static/script.js` used for adding background image to page when loaded for the first time.
* `static/github-mark-white.png` is GitHub's white logo. It is placed with the link for this project's GitHub page.
* `static/image` contains background images that change with the quote on every click.