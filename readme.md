source venv/bin/activate

docker build -f dockerfile -t datascraping:latest .

docker run -it \
     -env-file=.env \
     -v /Users/fzoccara/www/liscivia/datascraping/screenshots/:/app/screenshots/ \
     -v /Users/fzoccara/www/liscivia/datascraping/csv/:/app/csv/ \
     -v /Users/fzoccara/www/liscivia/datascraping/default/:/app/default/ \
     datascraping:latest
