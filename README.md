
# Cloud Flight Search ✈️

A Python-based flight search application that integrates a flight API with AWS Secrets Manager and Amazon DynamoDB to securely manage API credentials and destination data. The application uses AWS Lambda and Amazon API Gateway for serverless deployment.

## 🚀 Features

- **Flight Search:** Retrieve flight itineraries and pricing through an external flight API.
- **Secure API Credentials:** Store and retrieve API keys using AWS Secrets Manager.
- **Destination Management:** Store and retrieve destination data using Amazon DynamoDB.
- **Python OOP:** Organise application logic using reusable classes and methods.
- **Serverless Architecture:** Use AWS Lambda to run flight-search logic and API Gateway to expose HTTP endpoints.

## 🛠️ Tech Stack

- **Language:** Python
- **Cloud Provider:** Amazon Web Services (AWS)
- **Database:** Amazon DynamoDB
- **Secrets Management:** AWS Secrets Manager
- **Serverless Compute:** AWS Lambda
- **API Management:** Amazon API Gateway
- **Libraries:** Boto3, Requests

## 📁 Project Structure

```text
cloud-flight-search/
├── main.py
├── flight_details.py
├── secrets_manager.py
├── destination_service.py
├── seed_destinations.py
├── .gitignore
└── README.md
```

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/cloud-flight-search.git
cd cloud-flight-search
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install boto3 requests
```

### 4. Configure AWS credentials

Configure a local AWS CLI profile named `flight-dev` with the required permissions to access your DynamoDB table and Secrets Manager secret.

```bash
aws configure --profile flight-dev
```

Use your own AWS credentials locally. Never commit access keys or API secrets to GitHub.

### 5. Configure the flight API

Store your flight API key in AWS Secrets Manager. Configure your application to retrieve it securely rather than hardcoding it in your source code.

### 6. Set up DynamoDB

Create a DynamoDB table named `FlightDestinations` in your configured AWS region, with `iataCode` as a String partition key.

Run the destination seeding script when you need to populate the initial destination data:

```bash
python seed_destinations.py
```

### 7. Run the application

```bash
python main.py
```

## ☁️ Cloud Architecture

The planned serverless architecture uses:

1. **Amazon API Gateway** to receive HTTP requests.
2. **AWS Lambda** to execute the flight-search application logic.
3. **Amazon DynamoDB** to store destination data.
4. **AWS Secrets Manager** to manage flight API credentials.
5. **External Flight API** to retrieve flight-search results.

## 🔐 Security

- Never commit API keys, AWS access keys, or secret values.
- Use IAM policies that grant only the permissions required.
- Use an IAM execution role when running the application on AWS Lambda.
- Keep local credentials and environment files out of version control.

## 🗺️ Roadmap

- [ ] Complete flight-search API integration.
- [ ] Retrieve and manage destination data using DynamoDB.
- [ ] Deploy the flight-search logic to AWS Lambda.
- [ ] Expose flight-search endpoints through API Gateway.
- [ ] Add input validation and error handling.
- [ ] Add automated tests.
- [ ] Improve flight-price comparison and tracking.

## 👨‍💻 Author

**PROMISE EKHOSUEHI**

---

Built to explore Python backend development, AWS cloud services, and serverless application architecture.
