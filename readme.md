source venv/bin/activate

docker build -f dockerfile -t datascraping:latest .

docker run -it \
     -env-file=.env \
     -v ${PWD}/screenshots/:/app/screenshots/ \
     -v ${PWD}/csv/:/app/csv/ \
     -v ${PWD}/default/:/app/default/ \
     datascraping:latest
