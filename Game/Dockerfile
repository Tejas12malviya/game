FROM python:3.9-slim

# Install required packages
RUN pip install flask pillow

# Set working directory
WORKDIR /app

# Copy the application files
COPY templates/ ./templates/
COPY static/ ./static/
COPY app.py .

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]