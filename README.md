# ai_piping_test
# Simple Travel Recommendations API

Welcome to the Simple Travel Recommendations API! This FastAPI application provides travel recommendations for a specified country during a particular season by consulting the OpenAI API. It's a quick and easy way to discover exciting things to do in your desired travel destination.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following requirements met:

- **Python**: Make sure you have Python installed on your machine.

### Installation

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

`git clone <repository-url>`

Create a Virtual Environment: Set up a Python virtual environment inside the project folder to manage dependencies.

`python -m venv venv`

### Activate the Virtual Environment:

On Windows:
`venv\Scripts\activate`

On macOS and Linux:
`source venv/bin/activate`

Install Dependencies: Install the required libraries using pip:
`pip install -r requirements.txt`

Obtain an OpenAI API Key: To use this application, you need an API key from OpenAI. If you don't have one, request it from OpenAI.

### Configuration
Make a .env file and write your OPEN_AI_APIKEY there, and the code will automatically pick it up.

### Usage
Now that you have set up the application, here's how to use it:

### Running the Application
Start the FastAPI application with the following command:
`uvicorn main:app --reload`

The application will run locally at http://localhost:3000.

### Accessing the API
You can access the API using your preferred tool, such as curl, httpie, or Postman.

### Request Format:

To get travel recommendations, make a GET request to the following URL, replacing <country> and <season> with your desired values:

`http://localhost:3000/recommendations/?country=<country>&season=<season>`

Example: http://localhost:3000/recommendations/?country=Canada&season=winter

Response Format:

The API will return recommendations for the specified country and season in the following format:

{
  "country": "Canada",
  "season": "winter",
  "recommendations": [
    "Go skiing in Whistler.",
    "Experience the Northern Lights in Yukon.",
    "Visit the Quebec Winter Carnival."
  ]
}

### Troubleshooting
If you encounter any issues or errors, ensure that you've correctly configured your OpenAI API key in the main.py file and that the FastAPI application is running.
