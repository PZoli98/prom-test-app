# Use official Python image as base
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements and install (if you have a requirements.txt)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Expose port your Flask app listens on
EXPOSE 8000

# Run the app
CMD ["python", "main.py"]
