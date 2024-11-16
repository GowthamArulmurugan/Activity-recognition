
# Video ML Deployment

This project demonstrates a machine learning model deployment using Docker. The Docker image is available on Docker Hub for easy setup and usage.

## Prerequisites
Make sure you have Docker installed on your system before proceeding. You can download it [here](https://www.docker.com/products/docker-desktop).

## Getting Started

Follow the steps below to pull and run the Docker image.

### Step 1: Pull the Docker Image
To get started, pull the pre-built Docker image from Docker Hub using the following command:

```bash
docker pull gowthama27/myapp:latest
```

### Step 2: Run the Docker Container
After pulling the image, you can run it using:

```bash
docker run -d -p 5000:5000 gowthama27/myapp:latest
```

This command will:
- Run the container in detached mode (`-d`).
- Expose port `5000` (adjust the port as needed).

### Step 3: Access the Application
Open your browser and navigate to:

```
http://localhost:5000
```

You should see the deployed application up and running.

## Useful Docker Commands

- **View Docker images**:
  ```bash
  docker images
  ```
- **Stop a running container**:
  ```bash
  docker stop <container_id>
  ```
- **Remove unused Docker images**:
  ```bash
  docker rmi <image_id>
  ```

## Troubleshooting
If you encounter issues, ensure that:
- Docker is installed and running.
- The ports are not blocked by other services on your system.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Author
Gowthama27
