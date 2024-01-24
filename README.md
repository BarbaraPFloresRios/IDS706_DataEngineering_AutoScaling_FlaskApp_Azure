[![Format](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/install.yml)
[![Test](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/test.yml)
[![Lint](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/lint.yml)



IDS706_DataEngineering_BarbaraFlores_Project4
## 📂 Auto Scaling Flask App Using Any Platform As a Service

### Project Overview
In this project, we have created a Translation App using Flask, allowing users to translate English text to Spanish seamlessly. The core functionality is powered by the Helsinki-NLP Opus MT model, showcasing the integration of advanced natural language processing capabilities into a Flask web application.

### Why Auto Scaling?
Auto scaling is a critical aspect of modern web applications, ensuring that the infrastructure adapts dynamically to varying workloads. This project not only demonstrates the translation capabilities of our app but also highlights the implementation of auto-scaling features using Azure App Services. By doing so, we address the need for efficiency, performance, and scalability in a real-world deployment scenario.

### How to Use This README
This README serves as a comprehensive guide for developers, reviewers, and anyone interested in understanding the structure, deployment process, and functionality of the Auto Scaling Flask App. Whether you're here to explore the codebase, run the application locally, or deploy it to the cloud, you'll find detailed instructions and insights to assist you on your journey.


## 🎥 Video Tutorial
The following [YouTube link](https://youtu.be/3oEopPvWFHk) shows a clear, concise walkthrough and demonstration of the project.


## 🌲 Project Structure
The project structure is as follows:

```bash
.
├── Dockerfile
├── Makefile
├── README.md
├── app.py
├── requirements.txt
├── setup.sh
├── templates
│   └── index.html
└── test_main.py

```


## 🛠️ Setup and Running

To get the translation application up and running, follow these simple steps:

1. **Install Dependencies:** Before getting started, make sure you have all the dependencies installed. Execute the following command to install them:

    ```bash
    pip install -r requirements.txt
    ```

2. **Local Execution:**
   - Start the application locally with the following command:

    ```bash
    python app.py
    ```

   - Open your web browser and visit [http://localhost:5000](http://localhost:5000).

   The application should now be up and running in your local environment.

## Deployment

If you prefer to deploy the application in a Docker container, follow these additional steps:

1. **Build Docker Image:**
   - Build the Docker image with the following command:

    ```bash
    docker build -t barbarapfloresrios/translator_app .
    ```

2. **Run Docker Container:**
   - Run the Docker container with the following command:

    ```bash
    docker run -p 5000:5000 barbarapfloresrios/translator_app
    ```

   The application will now be accessible at [http://localhost:5000](http://localhost:5000), similar to the local execution.

These steps will allow you to run the translation application both locally and in a Docker container. Enjoy exploring the functionality of the application!

![00.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/main/images/00.png)

## Dependencies
- Flask: 2.0.0
- transformers: 4.12.0


## ☁️ Azure Web App Deployment

To deploy the application to Azure Web App, follow these steps:

1. **Web App Creation:**
   - Access the [Azure Portal](https://portal.azure.com/).
   - Create a new instance of Azure Web App.
   - Configure the instance with necessary details, such as a unique name, resource group, and service plan.

2. **Docker Configuration in Azure Web App:**
   - In the Configuration section of the Web App, find the "Container Settings" category.
   - Enable the "Container" option.
   - Specify the Docker image, which in this case is `barbarapfloresrios/translator_app`.

3. **Continuous Deployment (Optional):**
   - Consider configuring continuous deployment from DockerHub or your preferred Docker repository. This will facilitate automatic updates when you make changes to your application.

4. **Access the Public Endpoint:**
   - Once the Web App is deployed, obtain the URL of the public endpoint provided by Azure.

![01.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/main/images/01.png)


## 📦 Dependencies
- Flask: 2.0.0
- transformers: 4.12.0

## 🎥 Example of Use
![02.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/main/images/02.png)
![03.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/main/images/03.png)

## 🏁 Conclusion
In summary, this project demonstrates not only the translation capability of the application but also the successful implementation of a scalable Flask application using Azure App Services. For further scalability, consider optimizing containerization and deployment strategies.



