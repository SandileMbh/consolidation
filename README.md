# My Band

Welcome to the official website of the Misfit Band!
This README file will guide you through navigating our website and setting up the application using a virtual environment and Docker.

## Table of Contents

1. Website Navigation 
2. Building and Running the Application

    - Using venv
    - Using Docker

## Website Navigation

Our website is designed to be user-friendly and intuitive. Here are the main sections you can explore:

    * Home: Get the latest news, tour dates, and updates about the Misfits Band.
    * About: Learn more about the band members, their history, and their musical journey.
    * Music: Listen to our latest tracks, albums, and playlists.
    * Gallery: Browse through photos and videos from our concerts and behind-the-scenes moments. 
    * Contact: Reach out to us for inquires, bookings, or fan mail.


## Building and Running the Application

### Using venv

    1. Clone the repository:
        
        git clone https://github.com/username/the-misfits-band.git
        cd the-misfits-band

    2. Create a virtual environment:

        python3 -m venv venv

    3. Activate the virtual environment:

        * On Windows:
            
            venv/Scripts/activate

        * On macOS and Linux:

            source venv/bin/activate

    4. Install the dependencies:

        pip install -r requirements.txt

    5. Run the application:

        python app.py


### Using Docker

    1. Clone the repository: 

        git clone https://github.com/username/the-misfits-band.git
        cd the-misfits-band

    2. Build the Docker Image:

        docker build -t misfits-band-app .

    3. Run the Docker container:

        docker run -p 8000:8000 misfits-band-app

    4. Access the application: Open your web browser and go to http://localhost:8000.

    