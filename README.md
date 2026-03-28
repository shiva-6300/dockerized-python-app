# End-to-End CI/CD Pipeline for Python Flask Application

---

## 1. Project Overview
This project demonstrates an End-to-End CI/CD pipeline for a Python Flask web application using Jenkins, Docker, AWS EC2, and Nginx.

The pipeline automatically builds and deploys the application whenever new code is pushed to the GitHub repository. The application is containerized using Docker and deployed on an AWS EC2 instance with Nginx acting as a reverse proxy.

This project simulates a real-world DevOps deployment workflow including Continuous Integration, Continuous Deployment, containerization, and cloud deployment.

---

## 2. Architecture Diagram
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


---

## 3. Technologies Used

| Technology | Purpose |
|------------|---------|
| Python (Flask) | Backend Web Application |
| Docker | Containerization |
| Jenkins | CI/CD Automation |
| GitHub | Source Code Repository |
| AWS EC2 | Cloud Hosting |
| Nginx | Reverse Proxy |
| Linux (Ubuntu) | Deployment Server |

---

## 4. CI/CD Pipeline Flow

The CI/CD pipeline automates the deployment process whenever new code is pushed to GitHub.

### Pipeline Workflow:
1. Developer pushes code to GitHub repository  
2. GitHub webhook triggers Jenkins pipeline  
3. Jenkins pulls latest source code  
4. Jenkins builds Docker image  
5. Jenkins stops old running container  
6. Jenkins removes old container  
7. Jenkins runs new container  
8. Application deployed on AWS EC2  
9. Nginx routes traffic to Flask container  
10. Updated application goes live  

---

## 5. Jenkins Pipeline Stages

The Jenkins pipeline consists of the following stages:

1. Clone GitHub Repository  
2. Build Docker Image  
3. Stop Running Container  
4. Remove Old Container  
5. Run New Container  
6. Deploy Application  

---

## 6. Setup Instructions

### Connect to AWS EC2
```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
Install Docker
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker

Install Jenkins
sudo apt install openjdk-21-jdk -y
sudo apt install jenkins -y
sudo systemctl start jenkins
sudo systemctl enable jenkins

Access Jenkins:
http://EC2-PUBLIC-IP:8080

Install Nginx
sudo apt install nginx -y
sudo systemctl start nginx

7. Docker Commands
Build Docker Image
docker build -t flask-app .
Run Docker Container
docker run -d -p 5000:5000 flask-app
List Running Containers
docker ps
Stop Container
docker stop <container_id>

8. Nginx Configuration
Edit Nginx configuration file:
sudo nano /etc/nginx/sites-available/default
Add the following configuration:

server {
    listen 80;
    location / {
        proxy_pass http://localhost:5000;
    }
}

Restart Nginx:

sudo systemctl restart nginx
```
  
9. Future Improvements
1.Deploy application using Kubernetes
2.Use Terraform for AWS infrastructure
3.Push Docker images to AWS ECR
4.Implement Prometheus monitoring
5.Create Grafana dashboards
6.Add automated testing stage
7.Implement Blue-Green Deployment

10. Author
Shiva
Aspiring DevOps Engineer
GitHub: https://github.com/shiva-6300
