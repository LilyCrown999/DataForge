# DataForge

DataForge is a web application for generating synthetic data from predefined models. It allows users to create data in various formats, such as CSV, JSON, SQL import files, or XML, based on the specified models. 
The application is built using Django, HTML, and Python.

## Features

- Model-based data generation: Create data based on predefined models and attributes.
- Multiple file format support: Generate data in CSV, JSON, SQL import files, or XML formats.
- Easy data retrieval: Retrieve data from the database using specific IDs or search for attributes.

## Installation

1. Clone the repository:

git clone https://github.com/LilyCrown999/Dataforge.git

2. Install the dependencies:

pip install -r requirements.txt

3. Run the application:

python manage.py runserver

4. Access the application in your web browser at `http://localhost:8000`.

## Architecture

The user interacts with the frontend built using Django, HTML, which communicates with the backend built using Python, Django, and Django Rest Framework. 
The frontend serves the models to the backend, and it creates the data from the models and returns it to the frontend in the requested format (CSV, JSON, SQL import files, or XML).

## APIs and Methods

### API Routes for Web Client

- `/generate`: 
 - GET: Returns all documents in the database (Not yet configured)
 - POST: Creates new data from given model using input and stores the data in the database

    i.e 
    request data like
        var Data = {
        "id" : "id",
        "age" : "number (12-16)",
        "amount": "number (100 - 20000)",
        "city" : "city",
        "state" : "state",
        "country" : "country",
        "First name":  "name",
        "Last name": "name",
        "Gender": "gender"
    }

    var jsonData = JSON.stringify(Data);

    var headers = {
        'Content-Type': 'application/json',
        'mode': 'csv',
        'line': 1000
    };

    // Make POST request to the API
    fetch(apiUrl, {
        method: "POST",
        body: jsonData,
        headers: headers
    })
    .then(response => response.json())
    .then(data => {
        // API response handling
        console.log(data);
    })
    .catch(error => console.error(error));

### API Endpoints for Other Clients

N/A

### 3rd Party APIs

N/A

## About

DataForge was inspired by the need for a flexible and customizable data generation tool. It was developed as a Portfolio Project for Holberton School, showcasing the team's skills in web development and data processing. This project is part of the curriculum at Holberton School.

## Team Members

- Adesoye Michael Ademola - [LinkedIn](https://www.linkedin.com/in/johndoe) | [GitHub](https://github.com/LilyCrown999) | [Twitter](https://twitter.com/nichael_crown)

## Repository

Visit the [DataForge GitHub repository](https://github.com/LilyCrown999/Dataforge) for more information, documentation, and to contribute to the project.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
