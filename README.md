# URL Shortener Project

A URL shortener service built using Django 3+ and Python 3.6+.

## Overview

This project implements a URL shortener service exposed via a REST API. It allows users to shorten long URLs and retrieve the original URLs using the shortened versions. The project also includes validation for URLs and stores the shortened URLs using the Django ORM.

## Installation

Follow these steps to set up the project:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/url-shortener.git
    cd url-shortener
    ```

2. Set up a virtual environment:

    ```bash
    python3 -m venv env
    source env/bin/activate  # For Linux/Mac
    env\Scripts\activate  # For Windows
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the SQLite database:

    ```bash
    python manage.py migrate
    ```

## Usage

1. Start the Django server:

    ```bash
    python manage.py runserver 0.0.0.0:3000
    ```

2. Access the URL shortener service in your web browser at `http://localhost:3000/shorten/`.

![Alt text](/static/pics/homescreen.png)

3. Access the Django REST service at `http://localhost:3000/api/shortenedurls/` to interact with the URL shortener data.

![Alt text](/static/pics/djangoRest.png/)

## API Endpoints

- `POST /shorten`: Use this endpoint to create a shortened URL. Provide the original URL in the request body.

![Alt text](/static/pics/successfulShorten.png)

- `<short_url>`: Access the shortened URL to be redirected to the original URL.

![Alt text](/static/pics/redirectToLongUrl.png)

- `GET /api/shortenedurls/`: Retrieve a list of all shortened URLs in the database.

## Requirements

- Python 3.6+
- Django 3+
- Other dependencies are listed in the `requirements.txt` file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
