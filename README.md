# Use-after free vulnerability demonstration

## How to setup project

Requires Docker.

Project was built on windows using WSL: Ubuntu.

## How to Us Makefile

*Building the Docker Image:* Run `make build` to build the Docker image for the project.

*Running the Docker Container:* Execute `make run` to start the Docker container.

*Cleaning Up:* Use make clean to remove both the Docker container and the image. You can also individually clean the container (make clean-container) or the image (make clean-image).
