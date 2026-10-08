**Self-Healing & Scalable REST API Platform using Red Hat OpenShift and Podman**

A containerized Flask REST API deployed on Red Hat OpenShift with automated health monitoring, self-healing, horizontal scaling, Prometheus metrics, and GitHub Actions CI/CD. The project demonstrates how containerized applications can automatically recover from failures and how new application versions can be built, pushed, and deployed automatically through a CI/CD pipeline.

**Problem Statement :**
Containerized applications can experience failures due to application crashes, unhealthy processes, resource constraints, or other runtime issues. Manually detecting and restarting failed services can increase downtime and require continuous monitoring.
This project addresses the problem by deploying a REST API on OpenShift with:

Health checks using Kubernetes/OpenShift probes
Automatic container recovery
Multiple application replicas
Horizontal scaling
Application-level monitoring metrics
Container security using a non-root user
Automated CI/CD using GitHub Actions
Container image management through Quay.io

**Objectives :** 
The main objectives of this project are to:

Containerize a Flask REST API using Podman.
Store container images in Quay.io.
Deploy the application on Red Hat OpenShift.
Maintain multiple application replicas for availability.
Automatically detect unhealthy containers.
Automatically restart failed containers.
Demonstrate horizontal scaling.
Expose application monitoring metrics.
Run the application as a non-root user.
Automate build and deployment using GitHub Actions.
       
**Tech Stack :**

**Application Development**

Python 3.13 — Backend programming language
Flask 3.1.3 — REST API framework
Prometheus Client — Application metrics and monitoring
REST API / JSON — API communication and data format

**Containerization**

Podman — Build, run, and manage OCI containers
Containerfile — Container image definition
Python Slim Base Image — Lightweight container base image

**Container Registry**

Quay.io — Container image storage and distribution

**Container Orchestration & Deployment**

Red Hat OpenShift — Container orchestration and application deployment
Kubernetes Deployments — Replica management and self-healing
Pods — Application runtime instances
Services — Internal service discovery and load balancing
OpenShift Routes — External application access
ConfigMaps — Non-sensitive configuration management
Secrets — Sensitive configuration management
Liveness & Readiness Probes — Health monitoring and automated recovery
Resource Requests & Limits — CPU and memory management

**Monitoring**

Prometheus-compatible Metrics — Application and health metrics
/metrics endpoint — Metrics exposure
/uptime endpoint — Application uptime monitoring
CI/CD & Version Control
Git — Version control
GitHub — Source-code hosting
GitHub Actions — CI/CD automation
OpenShift CLI (oc) — OpenShift management and automated deployment

Development Environment
WSL2 + Ubuntu — Linux development environment on Windows
Python Virtual Environment (venv) — Isolated Python dependencies
The OpenShift Service distributes requests among healthy application Pods.

