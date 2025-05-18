FROM --platform=linux/amd64 python:3.13-slim AS builder

# Avoids python buffering
ENV PYTHONUNBUFFERED=1

#Install system dependencies
RUN apt-get update && apt-get install -y curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


RUN python -m pip install --upgrade pip

# Adds non-root user
RUN useradd --create-home django-user

# Set the working directory
WORKDIR /core

# Copy dependency files from backend/
COPY backend/requirements.txt /core/requirements.txt
COPY backend/dev-requirements.txt /core/dev-requirements.txt

# Copy the backend application code
COPY backend/ /core/

RUN mkdir -p /core/staticfiles

RUN chown -R django-user:django-user /core
# Switch to non-root user
USER django-user

