import openai
from app.core.config import settings



class GPTService():
    
    openai.api_key=settings.OPEN_API_KEY
    
    def get_response(self,texts):
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= texts,
        temperature=0,
        max_tokens=750,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop = (";", "/*", "</code>")
        )
        x = response.choices[0].text 
        return x

gpt_service = GPTService()