FROM python:3.5


#adding code
ADD . /code
WORKDIR /code

#install pip deps
RUN pip install -r req.txt

#start app
CMD ["python","-u","index.py"]