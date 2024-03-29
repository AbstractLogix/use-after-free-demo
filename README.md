# Use-after free vulnerability demonstration

## How to setup project

Requires *Python 3.12*

- __Create python virtual environment__

```bash
python -m venv venv
```

- __Activate virtual environment__

On windows e.g.:

```bash
venv\Scripts\activate
```

- __Install python dependencies__

```bash
pip install -r requirements.txt
```

- __Compile C program for specific host system:__

On Linux:

```bash
gcc -shared -fPIC -o libvuln_demo.so vuln_demo.c
```

On macOS:

```bash
gcc -shared -o libvuln_demo.dylib vuln_demo.c
```

On Windows (using MinGW):

```bash
gcc -shared -o vuln_demo.dll vuln_demo.c
```

## How to run the project

```bash
python
```

## How to Us Makefile

*Building the Docker Image:* Run make build to build the Docker image for the project.

*Running the Docker Container:* Execute make run to start the Docker container. This will automatically build the image if it hasn't been built.

*Cleaning Up:* Use make clean to remove both the Docker container and the image. You can also individually clean the container (make clean-container) or the image (make clean-image).
