# blog-backend
## step1
build docker image using
`docker build -t blog-backend:0.1 .`

## step2:
after successfull building the docker image run the belowe command
`docker run -it -v $(pwd):/usr/src/app -p 8001:8000 blogapp:0.1 bash`

## step3:
`
python manange.py makemigraiton

python manage.py migrate

python manage.py runserver 0:8000`
