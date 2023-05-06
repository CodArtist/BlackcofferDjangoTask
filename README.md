# BlackcofferDjangoTask

# Movie Search Webapp

This is a Django webapp that allows you to search for movies and view their cast details. The app uses Neo4j as the backend database to store movie and cast data.

## Getting Started

To run this app locally, you'll need to have Python and Neo4j installed on your system.

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/movie-search-webapp.git
   ```

2. Install the required Python packages:

   ```sh
   pip install django neo4j
   ```

3. Start the Django web server:

   ```sh
   python manage.py runserver
   ```

4. Open the webapp in your browser at http://localhost:8000/.

## Usage

To search for a movie, enter the movie title in the search box on the homepage and click the "Search" button. The app will display a list of matching movies, along with their release year and cast details.

To view the cast details for a movie, hover your cursor on the movie card. The app will display a list of the movie's cast members, along with their roles.

## Credits

This webapp was created by Harsh Jain as a project task for Blackcoffer. The movie data was obtained from neo4j.
