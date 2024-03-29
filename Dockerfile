FROM ubuntu:24.04

# Install system dependencies
RUN apt-get update && \
    apt-get install -y python3.11 python3-pip python3.11-venv python3.11-dev build-essential libffi-dev libasan5 && \
    # Clean up
    rm -rf /var/lib/apt/lists/*

# Create and activate virtual env
RUN python3.11 -m venv /opt/venv

# Setting the PATH environment variable for the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Copying requirements
COPY requirements.txt /app/requirements.txt

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt

# Add source code to the container
COPY ./src /app

# Compile C/C++ code with AddressSanitizer
WORKDIR /app
RUN gcc -g -fsanitize=address -shared -o vuln_demo.so vuln_demo.c -fPIC -static-libasan

ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libasan.so.5

# Activate virtual environment and set the command to run Python script
CMD ["bash", "-c", "source /opt/venv/bin/activate && exec python /app/server.py"]