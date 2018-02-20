# Use the following container img
FROM python:3-alpine

# Copy the Contents of the  CWD on the host to the container
RUN mkdir /hanzo-python

# Set the CWD to /hanzo-python
WORKDIR /hanzo-python

# Make this our new volume
VOLUME /hanzo-python

# Copy shit over to the docker container to be run
COPY . /hanzo-python

# Add GIT so code can be pulled from GitHub
RUN apk update
RUN apk upgrade
RUN apk add htop

# Run Some Commands!
RUN pip3 install -r requrements.txt

# Expose port 9022 for kafka and 443 for datadingle
EXPOSE 443
EXPOSE 9092

# Run the Following Command Once Launched
CMD [ "python3", "/hanzo-python/dd-events.py" ]