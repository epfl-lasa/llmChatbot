# LLM Chatbot

## Pre-requisites

### GPT api
You need to create an account, a api key and provision your account with tokens.
- Go to the [API signup page](https://platform.openai.com/signup)
- Create an account if you don't have one or login
- Go to the [API keys page](https://platform.openai.com/account/api-keys) and create a new API key
- Make sure to save your secret key.
- This module expects the secret key to be in environment variables. Simplest way it to modify your `.bashrc` and add:
    ```bash
    # GPT api
    export GPT_API_KEY=<secret_key>
    ```
- Go to the [API tokens page](https://platform.openai.com/account/billing/overview) and provision your account with a bit of money

### Others
- Make sure you have python 3.9 available
- If you don't have venv install using `pip install virtualenv`


## Usage
```bash
source setup_env.bash
python scripts/example_gpt_chat.py  # Starts a chatbot using GPT... it costs tokens
# ... chat ...
# At any time type "exit" to exit
```

You can chang the model in `python scripts/example_gpt_chat.py`