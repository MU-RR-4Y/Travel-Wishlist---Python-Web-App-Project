# Travel Wishlist - Python/Flask App

Travel Wishlist is an app made in Python using Flask.

The app uses PostgreSQL for a backend database and implements CRUD functionality.

The frontend was created using HTML and CSS.

The app allows users to add destinations to their own wishlist and then update them as visited. A user may select from the existing destinations or add a new destination to their wishlist. The app also includes a leaderboard to track which users have visited the most destinations.

Technologies used:
Python 3
Flask
HTML/CSS
psycopg2
PostgreSQL

## Run Locally

Install dependencies

```bash
pip3 install psycopg2
pip3 install Flask
```

Create a 'travel' database using PostgreSQL

```bash
createdb travel
```
Initiate database table setup
```bash
psql -d travel -f db/travel.sql
```

Run seed data

```bash
python3 seeds.py
```

Run app

```bash
flask run
```


The app will be available on localhost 5000 : http://127.0.0.1:5000
```bash
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
