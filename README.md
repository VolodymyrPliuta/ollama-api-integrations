# Local Python Chatbot Using Ollama and Experimental APIs

This project runs a local chat interface using Ollama + external APIs.
---

## 🚀 Prerequisites

Install the following:

- **Python 3.10+**
- **Ollama** → https://ollama.com/download

Check that Ollama works:

```bash
ollama --version
```

Download a model:
```
ollama pull phi:latest
```

Verify it’s installed:
```
ollama list
```

## External APIs:

- ** Repo with list of public APIs** → ```https://github.com/public-apis/public-apis```

I used the following APIs in my experiments:
- **IP Geolocation API** → http://ip-api.com/json/ - No API key required



## 🛠️ Setup

1. Clone this repository:
   ```
   git clone git@github.com:VolodymyrPliuta/ollama-api-integrations.git
   ```

2. Navigate to the project directory:
   ```
   cd ollama-api-integrations
   ``` 
3. Create and activate a virtual environment:
   ```bash
    python -m venv venv

    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```  

## ▶️ Run the Chatbot
Run the chatbot script:
```bash
python rest_location_ai.py
```
Type your messages and press Enter to chat with the local model based on your APIs data. 
Type `exit` to quit the chat.

Enjoy chatting with your enhanced local AI model!
