```markdown
# 🚀 End-to-End CI/CD Pipeline for Python Flask Application

## 📌 Project Overview

This project demonstrates a complete **End-to-End CI/CD pipeline** for a Python Flask web application using modern DevOps tools.

The pipeline automatically builds, tests, and deploys the application whenever new code is pushed to the GitHub repository. The application is containerized using Docker and deployed on an AWS EC2 instance, with Nginx acting as a reverse proxy.

### Key Features:
- Continuous Integration (CI)
- Continuous Deployment (CD)
- Containerization using Docker
- Cloud Deployment on AWS

---

## 🏗️ Architecture Diagram

```

Developer
│
▼
GitHub Repository
│
▼
Jenkins Pipeline
│
▼
Docker Image
│
▼
Docker Container
│
▼
AWS EC2 Instance
│
▼
Nginx Server
│
▼
Flask Application

````

---

## 🛠️ Technologies Used

| Technology      | Purpose                  |
|----------------|--------------------------|
| Python (Flask) | Backend Application      |
| Docker         | Containerization         |
| Jenkins        | CI/CD Automation         |
| GitHub         | Source Code              |
| AWS EC2        | Cloud Hosting            |
| Nginx          | Reverse Proxy            |
| Linux (Ubuntu) | Deployment Server        |

---

## 🔄 CI/CD Pipeline Flow

### Workflow Steps:

1. Developer pushes code to GitHub  
2. GitHub triggers Jenkins (Webhook)  
3. Jenkins pulls latest code  
4. Docker image is built  
5. Old container is stopped  
6. Old container is removed  
7. New container is started  
8. Application deployed on EC2  
9. Nginx routes traffic  
10. Application goes live  

---

## ⚙️ Jenkins Pipeline Stages

- Clone Repository  
- Build Docker Image  
- Stop Running Container  
- Remove Old Container  
- Run New Container  
- Deploy Application  

---

## 🖥️ Setup Instructions

### 🔐 Connect to EC2

```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
````

---

### 🐳 Install Docker

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

---

### 🔧 Install Jenkins

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

### 🌐 Install Nginx

```bash
sudo apt install nginx -y
sudo systemctl start nginx
```

---

## 🐳 Docker Commands

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

## 🌍 Nginx Configuration

Edit file:

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

## 🚀 Future Improvements

* Kubernetes Deployment
* Terraform for Infrastructure
* AWS ECR Integration
* Prometheus Monitoring
* Grafana Dashboards
* Automated Testing
* Blue-Green Deployment

---

## 👨‍💻 Author

**Shiva**
Aspiring DevOps Engineer

🔗 GitHub: [https://github.com/shiva-6300](https://github.com/shiva-6300)

---
