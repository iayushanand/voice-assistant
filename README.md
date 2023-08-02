# Virtual Assistant
## Made by [AyuItz](https://youtube.com/ayuitz) inspired by [Ai-Austin](https://github.com/Ai-Austin/Bing-GPT-Voice-Assistant)
**A Bing AI/Chat GPT powered virtual assistant in your terminal**



### How to setup?

#### 1. Install all requirements
In order to use this voice assistant, you have to install the requirements through pip so we will do
```sh
python -m pip install -r requirements.txt
```

#### 2. Fill up config variables
```python
BING_WAKE_WORD = "word to trigger Bing AI"
GPT_WAKE_WORD = "word to trigger gpt, usually your voice assistant name"
openai.api_key = "your openai api key"
# you can get this key from OpenAI Dashboard (https://platform.openai.com/account/api-keys)
gpt_model = "your chat gpt model"
# read about it at https://platform.openai.com/docs/api-reference/models
system_content = "role for your voice assistant"
# read the docs at https://platform.openai.com/docs/api-reference/chat/create#chat/create-role
```

<!-- #### 3. Get cookies
To get the cookies for Bing AI to work follow the steps below:

- Open Edge Web Browser

    ![Edge](/readmeassest/Edge.png)

- Open Extensions

    ![Extenstions](/readmeassest/extension.png)

- Click on Manage Extension

    ![Manage Extension](/readmeassest/manage.png)

- Install Extension named Cookie Editor

    ![cookie-editor](/readmeassest/cookie.png)

- Go to Bing AI chat

    ![Bing AI](/readmeassest/Chat.png)

- Click on the Cookie Editor extension

    ![Cookie Editor](/readmeassest/cookie2.png)

- Click on the Export Button

    ![Export Cookie](/readmeassest/export.png)

- Paste the content in the file named cookies.json

    ![cookie-json](/readmeassest/cookiejson.png) -->

#### 3. Run the file
Run the following command in your terminal to start your virtual assistant

```sh
python main.py
```

> To use the Bing AI you have to manually chat with the Bing once on their site
