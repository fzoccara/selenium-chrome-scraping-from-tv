source venv/bin/activate

docker build -f dockerfile -t datascraping:latest .

docker run -it \
     -env-file=.env \
     -v .screenshots/:/app/screenshots/ \
     -v .csv/:/app/csv/ \
     -v .default/:/app/default/ \
     datascraping:latest
