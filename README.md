# Prometheus-R2
## Description
---
A simple web application that provides login and signup functionality made with flask. Users can sign up using their email, username, and password. After registration, they can log in to view their email and user ID on the dashboard.

## Getting Started
---
1. Clone this repository to your local machine.

2. Ensure you have Python, Flask, and SQLite installed.

3. Run the Flask app using the following command:

```bash
python app.py
```
4. Open http://127.0.0.1:5000 URL to launch the app


## File Description
---
The project contains the following files and directories:

### `static/`

This folder contains the CSS file used for styling the web app's HTML templates.

- `style.css`: The stylesheet used to style the web app's pages.

### `templates/`

This folder contains the HTML templates used for the web app's pages.

- `signup.html`: Sign up page template with a form to register a new user.
- `login.html`: Login page template with a form to authenticate users.
- `dashboard.html`: Dashboard page template to display the user's email and user ID after login.

### `app.py`

The main Flask application file that defines the routes and handles user authentication. It connects to the SQLite database and manages user login and signup functionality.

### `database.db`

The SQLite database file where user information is stored. The 'users' table contains columns for `id`, `email`, `username`, and `password`.

### `README.md`

The Markdown file you are currently reading, providing project information, instructions, and descriptions.

