# Use a small Python base
FROM --platform=linux/amd64 python:3.11-slim

# Install OS deps
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
       gcc  \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy your extractor
COPY main.py .

# Create only the two dirs you actually need

# When container starts, run the extractor
ENTRYPOINT ["python", "main.py"]
