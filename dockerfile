# Use a smaller base image
FROM python:3.11-slim AS builder

# Set environment variables
ENV OPENAI_API_KEY=""
ENV DefaultLangchainUserAgent=""

RUN git clone https://github.com/SadineniAbhi/ChatBot.git
# Set working directory
WORKDIR /ChatBot

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Copy only necessary files
COPY requirements.txt ./
RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt

# Copy the ChatBot directory
COPY ChatBot /ChatBot
COPY mycontent.txt /ChatBot/rag/content.txt

# Set the PATH to include the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
