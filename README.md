# ChatBot

Build custom Chatbot based on LLMs by providing coustom context for context-specific retrival.

for getting started follow the steps below:-

clone the github repositry 
```git clone https://github.com/SadineniAbhi/CustomChatbot.git```

change directory 
`cd CustomChatbot`

clone the Chatbot directory

`git clone https://github.com/SadineniAbhi/ChatBot.git`

build the docker image 
`docker build -t docker_image_name .`

run your docker image 
`docker run -d -p 5000:5000 -e OPENAI_API_KEY="your_openai_api_key" docker_image_name`

you can now access your service through localhost at port 5000




