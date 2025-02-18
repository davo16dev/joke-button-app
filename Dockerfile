# ====== Frontend Build ======
FROM node:20 AS frontend-builder

WORKDIR /app

# Copy frontend files
COPY frontend/react-app /app

# Install dependencies and build the application
RUN npm install && npm run build

# ====== Backend Build ======
FROM python:3.11 AS backend

WORKDIR /app

# Copy backend files
COPY backend/app /app

# Copy requirements.txt from the backend folder
COPY backend/requirements.txt /app/requirements.txt

# Install backend dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the frontend build to the backend in the correct folder
COPY --from=frontend-builder /app/dist /app/static/

# ====== Lightweight Final Image ======
FROM python:3.11-slim AS final

WORKDIR /app

# Copy only the necessary backend files
COPY --from=backend /app /app

# ✅ Install dependencies in the final image (to ensure Uvicorn is available)
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port
EXPOSE 8080

# Define the execution command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
