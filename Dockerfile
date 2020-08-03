FROM python:3.6-slim

# Install dependencies
# Do this first for caching
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy
COPY experiments experiments
COPY image_captioning image_captioning
COPY logging.json logging.json

# Export ports
EXPOSE 5000

# Start app
CMD ["uvicorn", "image_captioning.app:app", "--host", "0.0.0.0", "--port", "5000"]