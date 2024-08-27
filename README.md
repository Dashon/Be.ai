# AAVE Translation App

This project provides a platform for translating between multiple languages and African American Vernacular English (AAVE).

## Structure

- **backend/**: Contains the FastAPI application, model integration, and MongoDB interactions.
- **frontend/**: Contains the React.js user interface.

## Deployment

### Prerequisites

- Python 3.10 or higher
- Node.js and npm

### Steps

1. **Set Up the Backend**

   Navigate to the `backend` directory and create a virtual environment:

   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   Start the FastAPI server:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

   The backend API will be accessible at `http://localhost:8000`.

2. **Set Up the Frontend**

   Navigate to the `frontend` directory:

   ```bash
   cd frontend
   ```

   Install the required Node.js packages:

   ```bash
   npm install
   ```

   Start the React development server:

   ```bash
   npm start
   ```

   The frontend will be accessible at `http://localhost:3000`.

3. **Access the Application**

   - The backend API will be accessible at `http://localhost:8000`.
   - The frontend will be accessible at `http://localhost:3000`.

4. **Stopping the Application**

   To stop the backend, deactivate the virtual environment and stop the server.
   To stop the frontend, terminate the running process in the terminal.

### Prerequisites

- Python 3.10 or higher
- Node.js and npm

### Steps

1. **Set Up the Backend**

   Navigate to the `backend` directory and create a virtual environment:

   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

   The backend API will be accessible at `http://localhost:8000`.

2. **Set Up the Frontend**

   Navigate to the `frontend` directory:

   ```bash
   cd frontend
   ```

   Install the required Node.js packages:

   ```bash
   npm install
   ```

   Start the React development server:

   ```bash
   npm start
   ```

   The frontend will be accessible at `http://localhost:3000`.

3. **Access the Application**

   - The backend API will be accessible at `http://localhost:8000`.
   - The frontend will be accessible at `http://localhost:3000`.

4. **Stopping the Application**

   To stop the backend, deactivate the virtual environment and stop the server.
   To stop the frontend, terminate the running process in the terminal.

## API Endpoints

- `/translate/`: Translate text from the source language to the target language.
- `/vocab/`: Add new vocabulary items to the dynamic vocabulary management system.
