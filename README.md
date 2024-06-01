### Project Overview

This project is designed to demonstrate a complete MLOps lifecycle using Kubeflow, covering all phases from data preprocessing, model training, model evaluation, to serving the model with Kubeflow's serving capabilities. The model focuses on the Iris dataset, predicting flower species based on input features.

### Features

- **Data Preprocessing**: Clean and prepare Iris dataset for training.
- **Model Training**: Train a machine learning model using a RandomForest algorithm.
- **Model Evaluation**: Evaluate the model's performance with standard metrics.
- **Model Serving**: Serve the model using Kubeflow Serving for real-time predictions.

### Prerequisites

- Kubernetes Cluster with Kubeflow installed.
- Docker installed and configured on your machine.
- Access to a Kubernetes cluster (e.g., Minikube, EKS, GKE).
- Python 3.8 or higher.
- pip and virtualenv (optional, but recommended for package management)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/kubeflow-iris-project.git
   cd kubeflow-iris-project
   ```

2. **Install Dependencies**

   Navigate to the project directory and install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Kubernetes and Kubeflow**

   Ensure that your Kubernetes cluster is up and running and that Kubeflow is installed and properly configured.

4. **Build Docker Images**

   Build the Docker images for the preprocessing, training, and serving components:

   ```bash
   docker build -t iris-preprocess:latest -f docker/Dockerfile.preprocess .
   docker build -t iris-train:latest -f docker/Dockerfile.train .
   docker build -t iris-serve:latest -f docker/Dockerfile.serve .
   ```

### Running the Project

1. **Start the Pipeline**

   Deploy the pipeline to Kubeflow Pipelines from the Kubeflow dashboard or using the CLI:

   ```bash
   kfp pipeline upload -p iris_training_pipeline pipelines/pipeline.py
   ```

2. **Monitor the Pipeline**

   Use the Kubeflow dashboard to monitor the pipeline's progress and inspect logs and artifacts generated by each pipeline component.

3. **Access the Model**

   Once the model is deployed, you can access it via the provided endpoint for real-time predictions:

   ```bash
   curl -X POST http://<service-url>/predict -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
   ```

### Additional Resources

- **Kubeflow Documentation**: [Official Kubeflow Documentation](https://www.kubeflow.org/docs/)
- **Kubernetes Documentation**: [Official Kubernetes Documentation](https://kubernetes.io/docs/)

### Contributing

Contributions to this project are welcome! Please refer to our contributing guidelines for more information.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
