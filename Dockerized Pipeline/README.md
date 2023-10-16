# Using Docker for Running the Python Script

This project provides a Dockerized environment for running a Python script. The script, `pipeline.py`, contains your print statement with dynamic variables, and Docker ensures that the necessary dependencies are available within the isolated container. This README will guide you through the process of running the script using Docker.

## Prerequisites

Before you begin, ensure that you have Docker installed on your system. You can download and install Docker from the official [Docker website](https://www.docker.com/get-started).

## Project Structure

The project directory should have the following structure:

```
docker-python-script/
│
├── Dockerfile          # The Dockerfile for building the Docker image
├── pipeline.py         # Python script containing the print statement
├── screenshot          # Screenshot of the terminal showing results
├── README.md           # Project README file

```

## Building the Docker Image

1. Clone this project repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/docker-python-script.git
   ```

2. Change your working directory to the project folder:

   ```bash
   cd docker-python-script
   ```

3. Build the Docker image using the provided Dockerfile. Run the following command from the project directory:

   ```bash
   docker build -t python-script .
   ```

   This command tells Docker to build an image named `python-script` from the current directory (`.`) using the Dockerfile.

## Running the Docker Container

After building the Docker image, you can run the Python script in a container with the following command:

```bash
docker run -it python-script
```

The `docker run` command creates a new container from the `python-script` image and runs it interactively (`-it`). This will execute the `pipeline.py` script and print the formatted text using the dynamic variables you mentioned.

## Cleaning Up

After running the script, you can exit the Docker container. To stop and remove the container, use the following command:

```bash
docker stop $(docker ps -aq)
docker system prune -a
```

This will stop all running containers and remove any unused images.

## Contribution and Feedback

Contributions are welcomed to help uncover more insights into the data and deepen my knowledge of Postgre SQL. Feel free traise issues, or provide feedback to help us improve the project.


## Github profile
https://github.com/mujjeeb

Enjoy running your Python script in a Docker container!
