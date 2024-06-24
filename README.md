# FastAPI REST API with Authentication, CORS, and SQLite

This repository contains an implementation of a REST API using FastAPI, featuring user authentication, CORS support, and SQLite database integration. It serves as a quick-start template for building secure RESTful services with Python.

## Features

- User registration and authentication with JWT tokens
- CRUD operations for a simple "Item" resource
- User-specific item management
- SQLite database for persistent storage
- CORS middleware to allow cross-origin requests
- Pydantic models for request and response validation
- Automatic API documentation with Swagger UI
- Database viewer CLI tool

## Project Structure

```
.
├── main.py
├── view_db.py
├── test.db (created when you run the application)
└── README.md
```

## What is a REST API?

REST (Representational State Transfer) is an architectural style for designing networked applications. A REST API (Application Programming Interface) is a way of accessing web services using HTTP protocols.

Key characteristics of a REST API include:

1. **Client-Server Architecture**: Separation of concerns between the user interface and data storage.
2. **Statelessness**: Each request from client to server must contain all the information needed to understand and process the request.
3. **Cacheability**: Responses must define themselves as cacheable or non-cacheable.
4. **Uniform Interface**: A consistent way of interacting with a given server irrespective of device or type of application.
5. **Layered System**: Client cannot tell whether it is connected directly to the end server or to an intermediary along the way.

REST APIs typically use HTTP methods to perform CRUD (Create, Read, Update, Delete) operations:

- POST: Create a new resource
- GET: Read a resource
- PUT: Update an existing resource
- DELETE: Delete a resource

## How to Run

1. Install the required packages:
   ```
   pip install fastapi uvicorn sqlalchemy passlib python-jose[cryptography] python-multipart python-dotenv
   ```

2. Create a `.env` file in the project root and add a secret key:
   ```
   SECRET_KEY=your_secret_key_here
   ```

3. Run the server:
   ```
   python main.py
   ```

   Or use uvicorn directly:
   ```
   uvicorn main:app --reload
   ```

4. Open your browser and go to `http://localhost:8000/docs` to see the Swagger UI documentation and test the API.

## API Endpoints

### Authentication
- `POST /register`: Register a new user
- `POST /token`: Login and receive an access token

### Items (protected, require authentication)
- `POST /items/`: Create a new item
- `GET /items/`: Get all items for the authenticated user
- `GET /items/{item_id}`: Get a specific item by ID
- `PUT /items/{item_id}`: Update an item
- `DELETE /items/{item_id}`: Delete an item

## Database Viewer

The `view_db.py` script provides a CLI tool to view the contents of the database. This improved version provides a command-line interface with several options:

1. View all tables in the database
2. View all items
3. View all users (without showing hashed passwords)
4. View items belonging to a specific user

To use this tool, you can run it from the command line with different arguments. Here are some example commands:

1. To view all tables:
   ```
   python view_db.py tables
   ```

2. To view all items:
   ```
   python view_db.py items
   ```

3. To view all users:
   ```
   python view_db.py users
   ```

4. To view items belonging to a user with ID 1:
   ```
   python view_db.py user_items --user_id 1
   ```

## CORS Configuration

CORS is enabled for all origins, methods, and headers. In a production environment, you should restrict these to only the necessary origins, methods, and headers.

## Database

The application uses SQLite, a lightweight, file-based database. The database file (`test.db`) will be created in the same directory as `main.py` when you run the application for the first time.

## Security Notes

- The SECRET_KEY in the .env file should be kept secret and not shared or committed to version control.
- In a production environment, consider using a more robust database like PostgreSQL.
- Implement additional security measures such as rate limiting and more granular permissions as needed.

## Next Steps

While this implementation provides a solid foundation, consider the following enhancements for a production environment:

1. Implement refresh tokens for better security
2. Add email verification for user registration
3. Implement password reset functionality
4. Add more complex validation and error handling
5. Implement pagination for large datasets
6. Add unit and integration tests
7. Containerize the application with Docker
8. Implement logging for better debugging and monitoring
9. Consider using asynchronous database queries for improved performance

This template provides a robust starting point for building secure, authenticated REST APIs with FastAPI. Feel free to extend and modify it to suit your specific project needs!