# Using Ubuntu 23.04 as the base image
FROM embedder-base

# Set the working directory to /app
WORKDIR /app
COPY ./requirements.txt .


# # Install the requirements
RUN pip install --trusted-host pypi.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Start a bash shell and source the CHATBOT_NAME value from /etc/bash.bashrc
CMD ["/bin/bash", "-c", "source /etc/bash.bashrc; trap : TERM INT; sleep infinity & wait"]

