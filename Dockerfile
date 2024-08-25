FROM python:3.12

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install python3-tk -y \
    && apt-get install -y libxrender-dev libx11-6 libxext-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev libxtst-dev tk-dev && rm -rf /var/lib/apt/lists/* 

RUN mkdir -p usr/app
WORKDIR /usr/app
COPY . /usr/app/

RUN pip3 install -r requirements/dependencies.txt

CMD ["python3", "src/main.py"]
