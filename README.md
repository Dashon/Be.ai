# AAVE Translation App

This project provides a platform for translating between multiple languages and African American Vernacular English (AAVE).

## Structure

- **backend/**: Contains the FastAPI application, model integration, and MongoDB interactions.
- **frontend/**: Contains the React.js user interface.

## Running the Project

### Backend

1. Navigate to the `backend` directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the FastAPI server: `uvicorn app.main:app --reload`
4. or export PYTHONPATH=./backend  
   uvicorn app.main:app --reload --app-dir backend/app

### Frontend

1. Navigate to the `frontend` directory.
2. Install dependencies: `npm install`
3. Start the React app: `npm start`

## API Endpoints

- `/translate/`: Translate text from the source language to the target language.
- `/vocab/`: Add new vocabulary items to the dynamic vocabulary management system.
