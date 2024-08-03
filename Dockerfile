#base image
FROM python:3.10.1

#maintainer
LABEL Author="Alberto e AJ"

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONBUFFERED 1

#directory to store app source code
RUN mkdir /indicadores_esus

#switch to /app directory so that everything runs from here
WORKDIR /indicadores_esus

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .