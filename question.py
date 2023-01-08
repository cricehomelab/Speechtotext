import openai
import apikeys
import json


class ArtificialIntelligence:
    def __init__(self):
        self.apikey = apikeys.OPENAI_APIKEY
        self.url = "https://api.openai.com/v1/models/chatgpt/versions/1/infer"

    def post_chatgpt_question(self, question):
        try:
            openai.api_key = self.apikey
            full_response = openai.Completion.create(
                model="text-davinci-003",
                prompt=question,
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
            )
            return (True, full_response)
        except Exception as err:
            print("error")
            return (False, err)

    def get_text(self, full_response):
        print("trimming down response...")
        print("converting to Json")
        answer_json = json.dumps(full_response)
        answer_json = json.loads(answer_json)
        print(f"answer_json is a: {type(answer_json)}")
        print("*********full answer**********")
        print(answer_json)
        print("************choices*************")
        text = answer_json["choices"][0]["text"]
        return text



