# Thera AI
## Project Description
With rising stress, anxiety, and depression among high school students, many face challenges that impact their academic performance and overall well-being. However, the reality is that many schools lack the necessary resources to effectively address these issues, and students often face barriers to accessing available resources, particularly due to financial constraints. The need for accessible, scalable solutions has never been more urgent. So, to tackle this issue, we introduce to you, **Thera**.

## Agents Introduction

- **Weather Agent**: This agent uses your latitude, longitude, and current hour to query the Weather API and provide accurate weather updates.

- **Therapy Agents**: A collaborative system of two agents designed to process and analyze journal entries. The input, consisting of unorganized or potentially multilingual journal content, is first sent to the Translation Agent to ensure it is in a single language. The translated text is then forwarded to the OpenAI Agent, equipped with prompts tailored for teenage therapy scenarios, to generate thoughtful and empathetic responses.
    - **Translator Agent**: Utilizes the high-performing Hugging Face model `Helsinki-NLP/opus-mt-zh-en` to ensure all input is translated into coherent English.
    - **OpenAI Agent**: Leverages OpenAI's GPT-4o-mini Large Language Model, fine-tuned for teenage therapy prompts, to generate thoughtful and empathetic responses.

- **Dashboard Agent**: Processes dashboard data, including mood counts and emotion categories, and performs in-depth analysis with other chronological datasets for actionable insights.

## Roadmap and Future Plans

### Multilingual Models Switch
- Each Hugging Face model works best for a specific pair of languages.
- The frontend includes an interface for language/country selection, which determines the appropriate model to import.

### Proposed Tech Stack 
Due to the scope of the hackathon, we have implemented the key features. However, we also have a systemic plan to ensure scalability and efficiency:

#### Application and Data
- **Backend Framework**: Flask
  - A lightweight WSGI web application framework in Python, suitable for small to medium applications like the journal app.
- **Database**: MongoDB Atlas
  - A fully-managed cloud database service to handle all MongoDB infrastructure.

#### Frontend Development
- **Frontend Framework**: Dart
  - Building a cross-platform mobile application to ensure seamless performance and consistent styling across platforms.

#### Development Tools
- **Source Control**: GitHub
  - Hosting code and managing changes using GitHub’s robust version control capabilities.
- **Continuous Integration/Continuous Deployment (CI/CD)**: GitHub Actions
  - Automating development workflows, including testing and deployment.

#### Hosting and Deployment
- **Application Hosting**: AWS Elastic Beanstalk
  - Deploying applications with automated setup for services like EC2, RDS, and ELB.
- **Static File Storage**: Amazon S3
  - Storing static files or media associated with the application.
- **Domain Management**: Amazon Route 53
  - Managing DNS records and routing end users to the application.

#### Security and Compliance
- **Authentication**: Google OAuth
  - Securely managing user authentication and permissions.

#### Monitoring and Operations
- **Application Monitoring**: AWS Elastic Beanstalk Monitoring Tools
  - Tracking application health and performance through Elastic Beanstalk’s dashboard.
- **Database Monitoring**: MongoDB Atlas Monitoring Tools
  - Monitoring database performance and setting up alerts through Atlas’s built-in tools.
