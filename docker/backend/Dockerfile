# Use a modern Ubuntu base
FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies and Python 3.11
RUN apt-get update && \
    apt-get install -y software-properties-common wget build-essential \
                       python3.11 python3.11-dev python3.11-venv python3-pip \
                       git curl && \
    rm -rf /var/lib/apt/lists/*

# Set Python 3.11 as default
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install gunicorn==20.1.0  # updated gunicorn version

# Copy project files
COPY ./backend /app/backend
COPY ./docker /app/docker
COPY ./research /app/research

# Ensure static folder exists
RUN mkdir -p /app/backend/server/static

# Expose port (if your app runs on 8000)
EXPOSE 8000

# Default command (adjust if needed)
CMD ["gunicorn", "--chdir", "backend/server", "server.wsgi:application", "--bind", "0.0.0.0:8000"]
