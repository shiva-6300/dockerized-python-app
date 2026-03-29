Here’s a clean, professional **README.md**

---

#  End-to-End CI/CD Pipeline for Python Flask Application

##  Project Overview

This project demonstrates a complete **End-to-End CI/CD pipeline** for a Python Flask web application using modern DevOps tools.

The pipeline automatically builds, tests, and deploys the application whenever new code is pushed to the GitHub repository. The application is containerized using Docker and deployed on an AWS EC2 instance, with Nginx acting as a reverse proxy.

This setup simulates a real-world DevOps workflow including:

* Continuous Integration (CI)
* Continuous Deployment (CD)
* Containerization
* Cloud Deployment

---

##  Architecture Diagram

```
Developer
   │
   │ Push Code
   ▼
GitHub Repository
   │
   │ Webhook Trigger
   ▼
Jenkins Pipeline
   │
   │ Build Docker Image
   ▼
Docker Container
   │
   │ Deploy Container
   ▼
AWS EC2 Instance
   │
   │ Reverse Proxy
   ▼
Nginx Server
   │
   ▼
Flask Web Application
```

---

##  Technologies Used

| Technology     | Purpose                 |
| -------------- | ----------------------- |
| Python (Flask) | Backend Web Application |
| Docker         | Containerization        |
| Jenkins        | CI/CD Automation        |
| GitHub         | Source Code Repository  |
| AWS EC2        | Cloud Hosting           |
| Nginx          | Reverse Proxy           |
| Linux (Ubuntu) | Deployment Server       |

---

##  CI/CD Pipeline Flow

The pipeline automates deployment whenever code is pushed.

### Workflow Steps:

1. Developer pushes code to GitHub
2. GitHub webhook triggers Jenkins
3. Jenkins pulls latest code
4. Docker image is built
5. Old container is stopped
6. Old container is removed
7. New container is started
8. Application is deployed on EC2
9. Nginx routes traffic to container
10. Updated application goes live

---

##  Jenkins Pipeline Stages

* Clone GitHub Repository
* Build Docker Image
* Stop Running Container
* Remove Old Container
* Run New Container
* Deploy Application

---

##  Setup Instructions

###  Connect to AWS EC2

```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

---

###  Install Docker

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

---

###  Install Jenkins

```bash
sudo apt install openjdk-21-jdk -y
sudo apt install jenkins -y
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

Access Jenkins:

```
http://<EC2-PUBLIC-IP>:8080
```

---

###  Install Nginx

```bash
sudo apt install nginx -y
sudo systemctl start nginx
```

---

##  Docker Commands

### Build Image

```bash
docker build -t flask-app .
```

### Run Container

```bash
docker run -d -p 5000:5000 flask-app
```

### List Containers

```bash
docker ps
```

### Stop Container

```bash
docker stop <container_id>
```

---

##  Nginx Configuration

Edit config file:

```bash
sudo nano /etc/nginx/sites-available/default
```

Add:

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://localhost:5000;
    }
}
```

Restart Nginx:

```bash
sudo systemctl restart nginx
```

---

##  Future Improvements

* Deploy using Kubernetes
* Use Terraform for infrastructure
* Push Docker images to AWS ECR
* Add Prometheus monitoring
* Create Grafana dashboards
* Add automated testing stage
* Implement Blue-Green Deployment

---

## 👨‍💻 Author

**Shiva**
Aspiring DevOps Engineer

🔗 GitHub: [https://github.com/shiva-6300](https://github.com/shiva-6300)

---
