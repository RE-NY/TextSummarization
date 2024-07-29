# Text Summarizer Application
---
## Project Overview
The Text Summarizer Application is a robust, production-grade application designed for efficient text summarization. By leveraging the principles of modular coding, this project ensures scalability, maintainability, and ease of deployment.

## Key Features
- **Modular Coding**: Adopts a modular approach to coding, ensuring that the application is structured, maintainable, and scalable.
- **Logging and Exception Handling**: Includes comprehensive logging and exception handling modules to enhance the reliability and debuggability of the application.
- **Deployable Docker Image**: Provides a Docker image for seamless deployment, ensuring consistency across different environments.
- **CI/CD Pipeline**: Implements a GitHub workflow CI/CD pipeline for automated testing, building, and deployment.
- **Text Summarization**: Utilizes the Google Pegasus model from the Hugging Face Transformers library, fine-tuned on the Samsun dataset, to generate high-quality text summaries.
- **Web Application**: Features a simple web app built using Flask as the backend framework for easy user interaction.

## Technologies Used
- Hugging Face Transformers: For the Google Pegasus text summarization model.
- Samsun Dataset: For fine-tuning the model.
- Flask: For the backend framework of the web application.
- Docker: For containerizing the application.
- GitHub Actions: For setting up the CI/CD pipeline.


The main.py acts as training pipeline and src/TextSummarizer/pipeline/prediction.py acts as prediction pipeline.
