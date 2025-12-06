from ollama import ChatResponse, chat
import requests

def location():
    url = "http://ip-api.com/json/"
    response = requests.get(url).json() 

    loc = f"City: {response['city']} -- Country: {response['country']}"
    return loc

def ai(query, location):
    response: ChatResponse = chat(
        model="phi",
        messages=[
            {
                "role": "user",
                "content": f"""
                Answer limit is 50 words.
                Based on query: {query}
                Based on location: {location}
                """
            }
        ]
    )
    return response.message.content

location_info = location()
print(location_info)

while True:
    query = input("Question: ")
    answer = ai(query, location_info)
    print(answer)
