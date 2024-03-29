FROM ubuntu:latest

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.11 python3-pip \
    build-essential libffi-dev \
    # Clean up
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies in a virtual environment
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install virtualenv \
    && virtualenv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Add source code to the container
COPY ./src /app

# Compile C/C++ code with AddressSanitizer
WORKDIR /app
RUN gcc -g -fsanitize=address -o vuln_demo vuln_demo.c

# Activate virtual environment and set the command to run Python demonstration script
CMD ["/bin/bash", "-c", "source /opt/venv/bin/activate && python /app/server.py"]
