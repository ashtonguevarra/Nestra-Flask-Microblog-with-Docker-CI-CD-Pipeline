rm app.db
rm -rf migrations
flask db init
flask db migrate -m "init"
flask db upgrade