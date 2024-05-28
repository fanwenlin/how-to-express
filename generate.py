import argparse
import os


# todo check if openai ins installed
# if not installed, give a warning response and install


from openai import OpenAI
import sys

from util import cache_data, write_status

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_HOST"),
)

def generage(term: str):
    chat_model = "gpt-3.5-turbo"
    if os.environ.get('MODEL_NAME'):
        chat_model = os.environ.get('MODEL_NAME')

    # Set up assistant settings
    messages = [
        {"role": "system",
         "content": f"You are a translator assistant that translates terms into English native expression."
                    f"Don't give extra response, be strict in format, each line for a suggestion, English expression and explanation are seperated by a '|' character."
                    f"For example:"
                    f"Apple|苹果，一种水果"
                    f"Language of explanation should depend on the language of the term. In this case, explanation is in Chinese language."
                    f"Please give several suggestions"
                    f""},
        {"role": "user", "content": f"How to express '{term}' to English?"},
    ]
    stream = client.chat.completions.create(
        model=chat_model,
        messages=messages,
        stream=True,
    )
    all_content = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            all_content = all_content + chunk.choices[0].delta.content
            # print(chunk.choices[0].delta.content, end="")
            cache_data(taskname, all_content)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--term', type=str, help='Input file name')
    parser.add_argument('--taskname', type=str, help='Input file name')
    cfg = parser.parse_args()

    term = cfg.term
    taskname = cfg.taskname

    write_status(cfg.taskname, 'running')
    try:     
        generage(term)
    except Exception as e:
        print(e)
    write_status(cfg.taskname, 'end')


