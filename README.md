# web-app-django

## Project Overview
MySite is a Django web application that showcases an "About Me" page, along with a portfolio and blog section. It allows users to learn more about me, explore my work, and read my blog posts.

## Getting Started

### Prerequisites
- Python 3.x
- Django

### Installation
1. Clone the repository:
https://github.com/cipobt/web-app-django

2. Change into the project directory:

cd mySite2

3. Install the project dependencies:

pip install -r requirements.txt

### Rendering Templates and Mapping URLs
1. Templates: 
- The main template for the "About Me" page is located at `personal/templates/about_me.html`.
- Additional templates for the portfolio and blog sections can be created in the `personal/templates/` directory.

2. URL Mapping:
- Open `personal/urls.py` to map URLs for the different sections.
- Example URL mappings are already provided for the "About Me", portfolio, and blog sections.



### Run the Application
1. Apply database migrations:

python manage.py migrate

2. Start the development server:

python manage.py runserver


3. Access the application in your browser at `http://localhost:8000/`.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request.

## License
This project is licensed under the MIT License.


