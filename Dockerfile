# Use an official Python runtime as a parent image
FROM python:3.8
# Set the working directory in the container 
WORKDIR /MyBand
# Copy the current directory contents into the container at /MyBand
COPY . /MyBand
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Make port 80 available to the world outside this container 
EXPOSE 8000
# Define environment variable
ENV NAME World
# Run MyBand.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
