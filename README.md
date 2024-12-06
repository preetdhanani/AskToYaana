# AskToYaana

**AskToYaana** is an AI-powered beauty recommendation app that offers personalized skincare advice, product recommendations, and nutritional tips based on user input.
- [Demo Video of Project](https://drive.google.com/file/d/1ZhRqnPzsUK8WUvx9WybhMFwsxcTRHaLg/view)
- [Website Link](https://asktoyaanarendor.onrender.com)
## Features

- Personalized skincare recommendations
- Product suggestions tailored to skin type and concerns
- Daily usage instructions for recommended products
- Nutritional advice to support skin health

## Prerequisites

Ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (3.x)
- [pip](https://pip.pypa.io/en/stable/)

## Setup

1. **Clone the repository**:
   ```
   git clone https://github.com/yourusername/asktoyaana.git
   cd asktoyaana
   ```
2. **Create a virtual environment (optional but recommended)**:
  ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```
   
4. **Apply database migrations**:
   ```
   python manage.py migrate
   ```
5. **Create a superuser (for admin access)**:
   ```
   python manage.py createsuperuser
   ```
6. **Run the development server**:
   ```
   python manage.py runserver
   ```
7. **Access the application: Open your browser and go to http://127.0.0.1:8000/ to view the application.**
   
# Usage
1. Input your skin tone and concerns into the app.
2. Receive personalized skincare advice, including product recommendations.
3. Follow the provided instructions on how to use the products and adjust your diet for optimal skin health.



