#!/bin/bash

# Example: Deploying with kubectl to a Kubernetes cluster
# Update this section according to your deployment setup

# Set Kubernetes context
kubectl config use-context my-kubernetes-staging

# Apply the Kubernetes manifests
kubectl apply -f manifests/k8s/deployment.yaml
kubectl apply -f manifests/k8s/service.yaml

echo "Deployment to staging has been completed."
