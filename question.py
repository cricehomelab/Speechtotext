import openai
import apikeys
import json


class ArtificialIntelligence:
    def __init__(self):
        self.apikey = apikeys.OPENAI_APIKEY

    def post_chatgpt_question(self, question):
        """Queries the OpenAI API with a question. Returns a response."""
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
        """This cuts the response down from its original OpenAI jsonlike object to just the response we would like."""
        #print("trimming down response...")
        #print("converting to Json")
        answer_json = json.dumps(full_response)
        answer_json = json.loads(answer_json)
        #print(f"answer_json is a: {type(answer_json)}")
        #print("*********full answer**********")
        #print(answer_json)
        #print("************choices*************")
        text = answer_json["choices"][0]["text"]
        return text



