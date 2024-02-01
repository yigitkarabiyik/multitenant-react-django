# Project README

## Project Structure

The project is organized into multiple directories, each serving a specific purpose. Below is an overview of the project structure:

### `main/`

The `main/` directory contains the main React frontend application:

- **`frontend/`**: The main React application.
  - **`public/`**: Contains static files like HTML and images.
  - **`src/`**: Holds the React components and assets.
  - **`.dockerignore`**: Specifies files and directories to be ignored by Docker.
  - **`.gitignore`**: Lists files and directories to be ignored by Git.
  - **`Dockerfile`**: Configuration for building the Docker image.
  - **`package-lock.json` and `package.json`**: Node.js package files.
  - **`README.md`**: Documentation for the React frontend.

### `project1/`

The `project1/` directory contains an example project with Django backend and React frontend:

- **`backend/`**: Django backend application.
  - **`config/`**: Configuration files for different environments.
  - **`db.sqlite3`**: SQLite database file.
  - **`Dockerfile`**: Configuration for building the Docker image.
  - **`manage.py`**: Django management script.
  - **`requirements.txt`**: Python dependencies.
- **`frontend/`**: React frontend application.
  - **`public/`**: Contains static files like HTML and images.
  - **`src/`**: Holds the React components and assets.
  - **`.gitignore`**: Lists files and directories to be ignored by Git.
  - **`Dockerfile`**: Configuration for building the Docker image.
  - **`package-lock.json` and `package.json`**: Node.js package files.
  - **`README.md`**: Documentation for the React frontend.
- **`docker-compose.yml`**: Docker Compose configuration file.

### Other Important Files and Directories

- **`ssl_certs/`**: Placeholder for SSL certificates.
- **`docker-compose.yml`**: Docker Compose configuration for the entire project.
- **`nginx.conf`**: Nginx configuration file.
- **`README.md`**: This file providing an overview of the project.
- **`tree.txt`**: Output of the directory tree for reference.

## Project Overview

The project serves as a template for a main frontend page built using React. It includes an example project (`project1`) that combines a Django backend with a React frontend. Developers can use this structure as a foundation for extending the project or creating additional projects.

### Aim of the Project

The primary goal of the project is to provide a template for the main frontend page, implemented using React. Additionally, `project1` demonstrates how to structure a Django backend and a React frontend within the same project. The project emphasizes building Nginx for backend API environments, with separate subdomains for testing and production, along with the main domain.

This is to provide developers with a versatile portfolio template for showcasing their Django and React projects. The project structure includes a main React frontend page and an example project (project1) that combines a Django backend with a React frontend. Developers can use this template as a foundation for extending their portfolio with additional projects.


### Key Objectives

1. **Main Frontend Page:**

    - Implement a clean and dynamic main frontend page using React, serving as the landing page for the portfolio.

2. **Example Project (project1):**

    - Showcase an example project that demonstrates the integration of Django backend and React frontend within a single project.

3. **Nginx Configuration:**

    - Illustrate how to configure Nginx for backend API environments, emphasizing separate subdomains for testing and production alongside the main domain.

4. **Docker Compose Setup:**

    - Simplify project deployment with Docker Compose, allowing developers to easily build, run, and showcase their portfolio projects.

5. **Scalability:**

    - Provide a scalable structure that allows developers to extend the portfolio by adding more projects, each with its own Django backend and React frontend.

### Getting Started

To get started with the project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Build and Run the Project:**
   ```bash
   docker-compose up --build
   ```

   This command initializes and builds the Docker containers for both the main frontend and the example project.

3. **Access the Applications:**
    - The nginx.conf file configures Nginx to manage multiple upstream servers and subdomains. It's designed to route traffic to different backend applications based on subdomain mappings.

    - Subdomain Mapping

      Access the main React frontend at http://localhost.

      Subdomain 1 - Backend API (http://sub1.api.localhost):

      Subdomain 1 - Frontend (http://sub1.localhost):