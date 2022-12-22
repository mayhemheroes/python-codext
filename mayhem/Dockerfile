FROM fuzzers/atheris:2.0.7-python3.9

RUN apt-get update

ADD . /src
WORKDIR /src

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install codext
RUN chmod +x /src/mayhem/fuzz-codext.py

CMD ["/src/mayhem/fuzz-codext.py"]
