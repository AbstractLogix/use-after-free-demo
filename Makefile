# Define variables for Docker image name and container name
IMAGE_NAME := use-after-free-demo:latest
CONTAINER_NAME := use-after-free-demo-container

# Define the default make target
.PHONY: help
help:
	@echo "Available commands:"
	@echo "	 setup			  - Setting up project directories for storing graphs"
	@echo "  build            - Building Docker image $(IMAGE_NAME)"
	@echo "  run              - Running $(CONTAINER_NAME) with volume mapping for graph output"
	@echo "  clean-container  - Stopping and removing the Docker container $(CONTAINER_NAME) (if running)"
	@echo "  clean-image      - Removing the Docker image $(IMAGE_NAME)"
	@echo "  clean            - Clean up all artifacts created by this Makefile, including generated graphs"

# Creates project directory for storying graphs
.PHONY: setup
setup:
	@echo "Setting up project directories..."
	mkdir -p graphs

# Build the Docker image
.PHONY: build
build:
	@echo "Building Docker image $(IMAGE_NAME)..."
	docker build -t $(IMAGE_NAME) .

# Run the Docker container with volume mapping for graph output
.PHONY: run
run:
	@echo "Running $(CONTAINER_NAME)..."
	docker run --rm --name $(CONTAINER_NAME) \
	-v $(PWD)/graphs:/app/graphs \
	$(IMAGE_NAME)

# Stop and remove the Docker container (if running)
.PHONY: clean-container
clean-container:
	@echo "Stopping and removing $(CONTAINER_NAME)..."
	-docker stop $(CONTAINER_NAME)
	-docker rm $(CONTAINER_NAME)

# Remove the Docker image
.PHONY: clean-image
clean-image:
	@echo "Removing Docker image $(IMAGE_NAME)..."
	-docker rmi $(IMAGE_NAME)

# Clean up all artifacts created by this Makefile
.PHONY: clean
clean: clean-container clean-image
	@echo "Removing generated graphs..."
	rm -rf graphs
	@echo "Cleanup complete."
