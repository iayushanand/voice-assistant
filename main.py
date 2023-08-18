import asyncio
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
import browser_cookie3, json
from elevenlabs import generate, play
import re
import speech_recognition as sr
import openai

# configs
BING_WAKE_WORD = ""
GPT_WAKE_WORD = ""
openai.api_key = ""
gpt_model = ""
system_content = ""


recognizer = sr.Recognizer()


def getCookies(url):
    browsers = [
        # browser_cookie3.chrome,
        # browser_cookie3.chromium,
        # browser_cookie3.opera,
        # browser_cookie3.opera_gx,
        # browser_cookie3.brave,
        browser_cookie3.edge,
        # browser_cookie3.vivaldi,
        # browser_cookie3.firefox,
        # browser_cookie3.librewolf,
        # browser_cookie3.safari,
    ]
    for browser_fn in browsers:
        # if browser isn't installed browser_cookie3 raises exception
        # hence we need to ignore it and try to find the right one
        try:
            cookies = []
            cj = browser_fn(domain_name=url)
            for cookie in cj:
                cookies.append(cookie.__dict__)
            return cookies
        except:
            continue


def gpt_prompt(user_prompt):
    response = openai.ChatCompletion.create(
    model = gpt_model,
    messages=[
        {
        "role": "system",
        "content": system_content
        },
        {
        "role": "user",
        "content": user_prompt
        }
    ],
    temperature=0.9,
    max_tokens=100,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response["choices"][0]["message"]["content"]

async def bing_prompt(user_prompt):
    bot = await Chatbot.create(cookies=getCookies('.bing.com')) # Passing cookies is "optional", as explained above
    response = await bot.ask(prompt=user_prompt, conversation_style=ConversationStyle.creative, simplify_response=True)
    response = response['text']
    # Regex
    response = re.sub('\[\^\d+\^\]', '', response)
    response = re.sub('\*', '', response)


    """
    {
        "text": str,
        "author": str,
        "sources": list[dict],
        "sources_text": str,
        "suggestions": list[str],
        "messages_left": int
    }
    """

    await bot.close()
    return response

async def play_response(text: str):
    audio = generate(
        text=text,
        voice="Elli",
        model="eleven_monolingual_v1"
    )
    play(audio)

async def voice_input() -> str:
    try:
        with sr.Microphone() as source:
            print("Listening to your voice...")
            recognizer.adjust_for_ambient_noise(source=source, duration=0.2)
            audio = recognizer.listen(source=source)
            raw = recognizer.recognize_vosk(audio_data=audio)
            raw_json = json.loads(raw)
            text = raw_json['text']
            text = text.lower()
            return text
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None
         
    except sr.UnknownValueError:
        print("unknown error occurred")
        return None

async def main():
    while True:
        print()
        response = await voice_input()
        print(response)
        if not response: continue
        elif BING_WAKE_WORD in response:
            print()
            await play_response("Hey there, what do do you me want to ask with Bing AI?")
            text = await voice_input()
            ai_response = await bing_prompt(text)
            print(ai_response)
            await play_response(ai_response)
        elif GPT_WAKE_WORD in response:
            print()
            ai_response = gpt_prompt(response)
            print(ai_response)
            await play_response(ai_response)
            
if __name__ == "__main__":
    asyncio.run(main())
