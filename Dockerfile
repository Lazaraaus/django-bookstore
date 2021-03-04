# Pull base image
From python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /bookstore

# Install dependencies
COPY Pipfile Pipfile.lock /bookstore/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /bookstore/ 
