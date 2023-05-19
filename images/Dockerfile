# Using Ubuntu 23.04 as the base image
FROM python:3.11-slim-bullseye
# FROM chrisgatt/cpp-python-dev
# needs c++ 11 to work with pytorch

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
# needs c++ 11 to work with pytorch and chroma so installing build-essential
    apt-get install -y --no-install-recommends --allow-change-held-packages build-essential \
        wget \
        python3-full \
        python3-pip \
        python3-dev \
        git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    pip install --trusted-host pypi.org torch && \
    pip install chromadb && \
    pip install tiktoken && \
    pip install --no-cache-dir --upgrade pip setuptools 

    # docker build -t embedder-base .