# Use the official Python image
FROM python:3.9-slim

# Set environment variables to prevent Python from buffering outputs
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Copy dependencies file and install packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app and data directories to the container
COPY app /app/app
COPY data /app/data

# Expose the port Streamlit runs on
EXPOSE 8501

# Change to the app directory where the Streamlit script is located
WORKDIR /app/app

# Run the Streamlit application
CMD ["streamlit", "run", "dashboard.py", "--server.port=10000", "--server.address=0.0.0.0"]
