# Superheroes API

A Flask REST API for tracking superheroes and their superpowers. This application allows you to manage heroes, powers, and their relationships through a comprehensive set of API endpoints.

## Author

**Your Name**
Contact: your-email@example.com
GitHub: [@yourusername](https://github.com/yourusername)

## Description

The Superheroes API is a Flask-based RESTful web service that enables CRUD operations on heroes, powers, and their associations. The API features:

- Complete hero management (view all heroes, get individual hero details)
- Power management (view, update powers)
- Hero-Power associations with strength ratings
- Data validation and error handling
- Email functionality using Flask-Mail
- SQLite database with SQLAlchemy ORM

## Features

- **RESTful API Design**: Clean, intuitive endpoints following REST conventions
- **Data Relationships**: Many-to-many relationship between Heroes and Powers through HeroPower
- **Validation**: Built-in validation for data integrity
  - Power descriptions must be at least 20 characters
  - HeroPower strength must be 'Strong', 'Weak', or 'Average'
- **Cascading Deletes**: Automatic cleanup of associations when heroes or powers are deleted
- **Email Support**: Integrated Flask-Mail for sending notifications
- **Serialization**: Efficient data serialization with depth control to prevent recursion
- **Error Handling**: Comprehensive error responses with appropriate HTTP status codes

## Technology Stack

- **Python 3.8+**
- **Flask 3.0.0** - Web framework
- **Flask-SQLAlchemy 3.1.1** - ORM
- **Flask-Migrate 4.0.5** - Database migrations
- **Flask-Mail 0.9.1** - Email support
- **SQLite** - Database

## Database Schema

### Models

#### Hero
- `id`: Integer (Primary Key)
- `name`: String - Hero's real name
- `super_name`: String - Hero's superhero alias

#### Power
- `id`: Integer (Primary Key)
- `name`: String - Power name
- `description`: String - Power description (min 20 characters)

#### HeroPower
- `id`: Integer (Primary Key)
- `strength`: String - Must be 'Strong', 'Weak', or 'Average'
- `hero_id`: Integer (Foreign Key)
- `power_id`: Integer (Foreign Key)

### Relationships

- A Hero has many Powers through HeroPower
- A Power has many Heroes through HeroPower
- A HeroPower belongs to a Hero and a Power

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd code-challenge
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```

   Edit the `.env` file with your configuration:
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   DATABASE_URI=sqlite:///app.db
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   MAIL_DEFAULT_SENDER=your-email@gmail.com
   ```

5. **Initialize the database**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. **Seed the database**
   ```bash
   python seed.py
   ```

7. **Run the application**
   ```bash
   python app.py
   ```

   The API will be available at `http://localhost:5555`


## Testing with Postman

1. Import the provided `challenge-2-superheroes.postman_collection.json` file into Postman
2. The collection contains pre-configured requests for all endpoints
3. Start the Flask server before testing
4. Run the requests in the collection to verify functionality

## Email Configuration

To enable email functionality:

1. **For Gmail:**
   - Enable 2-Factor Authentication on your Google account
   - Generate an App Password: Google Account → Security → 2-Step Verification → App passwords
   - Use the generated app password in your `.env` file

2. **For other email providers:**
   - Update `MAIL_SERVER`, `MAIL_PORT`, and TLS settings accordingly
   - Consult your email provider's SMTP documentation

3. **Test the email functionality:**
   ```bash
   curl -X POST http://localhost:5555/send-test-email \
     -H "Content-Type: application/json" \
     -d '{"recipient": "your-email@example.com"}'
   ```

## Project Structure

```
code-challenge/
├── app.py                 # Main Flask application
├── models.py             # Database models
├── config.py             # Configuration settings
├── seed.py               # Database seeding script
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Development

### Running Migrations

After modifying models:

```bash
flask db migrate -m "Description of changes"
flask db upgrade
```

### Resetting the Database

```bash
rm -rf migrations/
rm app.db
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python seed.py
```

## Error Handling

The API provides clear error messages and appropriate HTTP status codes:

- `200 OK` - Successful GET/PATCH requests
- `201 Created` - Successful POST requests
- `400 Bad Request` - Validation errors
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server errors

## Validation Rules

1. **Power Description:**
   - Must be present
   - Minimum length: 20 characters

2. **HeroPower Strength:**
   - Must be one of: 'Strong', 'Weak', 'Average'
   - Case-sensitive

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

For issues, questions, or contributions:

- **Email**: your-kevrith@gmail.com
- **GitHub Issues**: [Create an issue](https://github.com/yourusername/repository/issues)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built as part of Phase 4 Code Challenge
- Flask documentation and community
- SQLAlchemy ORM documentation

---

**Note**: Remember to update the author information, repository URL, and contact details before submission.
