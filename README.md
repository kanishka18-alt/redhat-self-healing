**Self-Healing & Scalable REST API Platform using Red Hat OpenShift and Podman**

A containerized Flask REST API deployed on Red Hat OpenShift with automated health monitoring, self-healing, horizontal scaling, Prometheus metrics, and GitHub Actions CI/CD. The project demonstrates how containerized applications can automatically recover from failures and how new application versions can be built, pushed, and deployed automatically through a CI/CD pipeline.

**Problem Statement :**
Containerized applications can experience failures due to application crashes, unhealthy processes, resource constraints, or other runtime issues. Manually detecting and restarting failed services can increase downtime and require continuous monitoring. This project addresses the problem by deploying a REST API on OpenShift with:

1. Health checks using Kubernetes/OpenShift probes

2. Automatic container recovery

3. Multiple application replicas

4. Horizontal scaling
   
5. Application-level monitoring metrics
   
6. Container security using a non-root user

7. Automated CI/CD using GitHub Actions
 
8. Container image management through Quay.io

**Objectives :** 

The main objectives of this project are to:

1. Containerize a Flask REST API using Podman.

2. Store container images in Quay.io.

3. Deploy the application on Red Hat OpenShift.

4. Maintain multiple application replicas for availability.
   
5. Automatically detect unhealthy containers.

6. Automatically restart failed containers.

7. Demonstrate horizontal scaling.

8. Expose application monitoring metrics.

9. Run the application as a non-root user.

10. Automate build and deployment using GitHub Actions.

**Project Structure :**
```text
redhat-self-healing/
│
├── .github/
│   └── workflows/
│       └── cicd.yml
│
├── openshift/
│   ├── configmap.yaml
│   ├── deployment.yaml
│   ├── route.yaml
│   ├── secret.yaml
│   └── service.yaml
│
├── app.py
├── Containerfile
├── requirements.txt
├── .gitignore
└── README.md

**Tech Stack :**

**Application Development**

1. Python 3.13 — Backend programming language

2. Flask 3.1.3 — REST API framework

3. Prometheus Client — Application metrics and monitoring

4. REST API / JSON — API communication and data format

**Containerization**

1. Podman — Build, run, and manage OCI containers

2. Containerfile — Container image definition

3. Python Slim Base Image — Lightweight container base image

**Container Registry**

1. Quay.io — Container image storage and distribution

**Container Orchestration & Deployment**

1. Red Hat OpenShift — Container orchestration and application deployment

2. Kubernetes Deployments — Replica management and self-healing

3. Pods — Application runtime instances

4. Services — Internal service discovery and load balancing
   
5. OpenShift Routes — External application access

6. ConfigMaps — Non-sensitive configuration management

7. Secrets — Sensitive configuration management

8. Liveness & Readiness Probes — Health monitoring and automated recovery

9. Resource Requests & Limits — CPU and memory management

**Monitoring**

1. Prometheus-compatible Metrics — Application and health metrics
  
2. /metrics endpoint — Metrics exposure

3. /uptime endpoint — Application uptime monitoring

4. CI/CD & Version Control

5. Git — Version control

6. GitHub — Source-code hosting

7. GitHub Actions — CI/CD automation

8. OpenShift CLI (oc) — OpenShift management and automated deployment

**Development Environment**

1. WSL2 + Ubuntu — Linux development environment on Windows

2. Python Virtual Environment (venv) — Isolated Python dependencies

3. The OpenShift Service distributes requests among healthy application Pods.

**Author : **

Kanishka Sharma

B.E. Computer Science, B.M.S College of Engineering

GitHub: https://github.com/kanishka18-alt LinkedIn: https://linkedin.com/in/kanishka-sharma-3aab79279

