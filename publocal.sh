TARGET=/var/www/django/rpiact/

rsync -avz . $TARGET --exclude '*.pyc' --exclude '.idea' --exclude '.git' --exclude 'db.sqlite3'

chown www-data.www-data -R /var/www/django/rpiact

