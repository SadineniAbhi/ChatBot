# Use Ubuntu as a parent image
FROM ubuntu:latest

# Set environment variables
ENV OPENAI_API_KEY=""
ENV DefaultLangchainUserAgent=""

# Update package index and install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git

# Set the working directory inside the container
WORKDIR /ChatBot

# Copy ChatBot directory into the container at /ChatBot
COPY ChatBot /ChatBot

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

# Copy context.txt into the container (adjust path if needed)
COPY context.txt /ChatBot/rag/content.txt

# Expose the Flask port (if using Flask)
EXPOSE 5000

# Command to run the Flask application (adjust as needed)
CMD ["python3", "app.py"]
