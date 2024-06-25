# Use the official Python image from the Docker Hub
FROM python:3.12.3

# Install necessary packages for Tkinter and Xvfb
RUN apt-get update && apt-get install -y \
    python3-tk \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the display environment variable
ENV DISPLAY=:99

# Run Xvfb in the background and then run the Tkinter app
CMD ["sh", "-c", "xvfb-run -a python app.py"]