# Healthcare Translation Backend

## Overview
The Healthcare Translation Backend is a robust API service built with FastAPI and Python that powers medical translation capabilities. It leverages OpenAI's language models to provide accurate translations of medical terminology, enhancing communication between healthcare providers and patients who speak different languages.

## Features
- **Medical Translation API**: Translates medical terms and phrases with clinical precision
- **Language Support**: Handles multiple languages including Spanish, French, German, Bengali, and more
- **Enhanced Medical Terminology**: Improves translations with precise clinical terminology
- **CORS Support**: Enables secure cross-origin requests from the frontend
- **Error Handling**: Comprehensive error management and logging
- **Docker Support**: Easy containerization for deployment

## Prerequisites
- Python 3.9+
- OpenAI API Key
- Docker (optional)

## Installation

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/healthcare-translation-backend.git
   cd healthcare-translation-backend
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY = "your-openai-api-key"
   MODEL_ID = "gpt-4" # or your preferred model
   ```

5. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at http://localhost:8000

### Docker Setup

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```
   The API will be available at http://localhost:8000

## API Documentation

### Endpoints

#### `GET /`
- **Description**: Root endpoint that returns a welcome message
- **Response**: 
  ```json
  {"message": "Welcome to the Healthcare Translation API"}
  ```

#### `GET /_status`
- **Description**: Health check endpoint
- **Response**: 
  ```json
  {"status": "ok"}
  ```

#### `POST /ai/translate`
- **Description**: Translates medical text to the specified language
- **Request Body**:
  ```json
  {
    "query": "The patient is experiencing chest pain and shortness of breath",
    "preferred_language": "Spanish"
  }
  ```
- **Response**:
  ```json
  {
    "translated_text": "El paciente está experimentando dolor torácico (angina de pecho) y dificultad para respirar (disnea)"
  }
  ```

### Request Schema

#### `AskRequest`
- `query` (string, required): The text to translate
- `preferred_language` (string, required): The target language for translation

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `MODEL_ID` | OpenAI model ID (e.g., "gpt-4") | Yes |
| `PORT` | Server port (default: 8000) | No |

## Deployment

### Railway Deployment

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**
   ```bash
   railway login
   ```

3. **Initialize Railway project**
   ```bash
   railway init
   ```

4. **Deploy to Railway**
   ```bash
   railway up
   ```

5. **Set environment variables in Railway dashboard**
   - `OPENAI_API_KEY`
   - `MODEL_ID`

### Other Deployment Options

- **Heroku**: Use the Procfile included in the repository
- **AWS**: Deploy as a container using ECS or as a Lambda function
- **GCP**: Deploy using Cloud Run or App Engine

## Development

### Adding New Features

1. **Create new route files** in `app/api/routes/`
2. **Define schemas** in `app/schemas/`
3. **Implement business logic** in appropriate modules
4. **Update main.py** to include new routers

## Troubleshooting

### Common Issues

1. **API Key Issues**
   - Ensure your OpenAI API key is valid and has sufficient credits
   - Check that the key is properly set in the `.env` file

2. **CORS Errors**
   - If experiencing CORS issues, update the `origins` list in `main.py`
   - For development, you can use `origins = ["*"]`

3. **Model Errors**
   - Verify that the specified `MODEL_ID` is available in your OpenAI account
   - Check OpenAI's documentation for model availability

4. **Deployment Issues**
   - Ensure all environment variables are properly set in your deployment platform
   - Check logs for any runtime errors

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- OpenAI for providing the language models
- FastAPI for the web framework
- All contributors who have helped improve this project

---

*For questions or support, please open an issue on the GitHub repository.*
