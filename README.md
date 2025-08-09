# Django Tweet App

This is a simple Django web application that allows users to post tweets with optional images. It includes a custom form validation to filter out prohibited words.

## Features

* **Tweet Creation:** Post new tweets with text content.

* **Image Upload:** Include an image with your tweet.

* **Profanity Filter:** Automatically prohibits tweets containing the words 'shit', 'fuck', or 'bobo'.

* **Tweet Feed:** Displays all recent tweets in a reverse chronological order.

## Prerequisites

* Python 3.8 or higher

* pip (Python package installer)

* Pillow, required for image uploads

## Installation

Follow these steps to get the project up and running on your local machine.

1. **Clone the repository:**

   ```
   git clone <your-repository-url>
   cd my_tweet_project
   
   ```

2. **Create and activate a virtual environment:**

   ```
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   ```

3. **Install the required packages:**

   ```
   pip install -r requirements.txt
   
   ```

## Usage

1. **Apply database migrations:**

   ```
   python manage.py makemigrations
   python manage.py migrate
   
   ```

2. **Start the development server:**

   ```
   python manage.py runserver
   
   ```

3. **Open the application:**

   * Navigate to `http://127.0.0.1:8000/` in your web browser.

4. **Create a tweet:**

   * Type your tweet content into the text area.

   * (Optional) Click on "Choose File" to upload an image.

   * Click the "Post Tweet" button.

   * If your tweet contains a prohibited word, you will see an error message. Otherwise, your tweet will be posted and appear below the form.

## Repository Structure

Your project should have the following structure after you have created the files and directories as per the instructions:

```
my_tweet_project/
├── my_tweet_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tweets/
│   ├── migrations/
│   ├── templates/
│   │   └── tweets/
│   │       └── tweet_list_create.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py         # <-- We created this
│   ├── models.py
│   ├── urls.py          # <-- We created this
│   └── views.py
├── media/               # <-- Created by Django for image uploads
├── .gitignore           # <-- You should create this
├── requirements.txt
└── manage.py

```

## Contributing

Feel free to submit pull requests or open issues for any improvements or bug fixes.
