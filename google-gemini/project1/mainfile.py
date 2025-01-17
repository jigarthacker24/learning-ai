import google.generativeai as genai
from dotenv import dotenv_values
import PIL.Image
import time

config = dotenv_values(".env")


genai.configure(api_key=config["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")


def get_response():
    response = model.generate_content("Explain how AI works in 50 words")
    print(response.text)


def analyze_image():
    organ = PIL.Image.open("elephants.jpg")
    response = model.generate_content(["Tell me about this image", organ])
    print(response.text)

def chat_response():
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ]
    )
    response = chat.send_message("I have 2 dogs in my house.")
    print(response.text)
    response2 = chat.send_message("How many paws are in my house?")
    print(response2.text)

def configure_text_generation():
    model1 = genai.GenerativeModel("gemini-1.5-flash")
    response = model1.generate_content(
        "Explain how AI works",
        generation_config = genai.GenerationConfig(
            max_output_tokens=50,
            temperature=0.1,
        )
    )
    print(response.text)




def system_instruction():
    model1 = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction="You are a genz. Your name is luke.")
    
    response = model1.generate_content(
        "Define a genZ",
        generation_config = genai.GenerationConfig(
            max_output_tokens=255,
            temperature=1,
        )
    )
    print(response.text)



def tax_expert():
    model1 = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction="You are a tax expert in india with 25 years of work experience. You can combile all tactice and link all laws. Your name is Mr Jha. All you need to just give in which clause how much amout can be exempted. do not provide any opinion")
    
    response = model1.generate_content(
        "I am a salaried software engineer with 10lacs gross income.. how can I manage my tax most efficient way"
    )
    print(response.text)


def two_person_talking():
    p1model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction="You are a 25 year old monther of a 5 year son in gujarat, india. your name is Malti. You need to talk to your son")

    p2model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction="You are a 5 year old son of 25 year mother in gujarat, india. Your name is Shyam. you need to talk to your mother")


    p1_reply = p1model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
        ]
    )

    p2_reply = p2model.start_chat(
        history=[
            {"role": "user", "parts": "Hello, Beta"},
        ]
    )

    boy = "Hello, mumma"
    
    for i in range(9): 
        time.sleep(1)
        print(i)
        print("\none: "+boy)
        response1 = p1_reply.send_message(boy)
        print("two: "+ response1.text)
        response2 = p2_reply.send_message(response1.text)
        boy = response2.text


def two_person_talking2(charactersInfo):

    P1Name = charactersInfo["name1"]
    P1Age = charactersInfo["age1"]
    P1Gender = charactersInfo["gender1"]
    P2Name = charactersInfo["name2"]
    P2Age = charactersInfo["age2"]
    P2Gender = charactersInfo["gender2"]
    Location = charactersInfo["location"]
    P1Says = charactersInfo["1speaks"]
    extra = charactersInfo["moreinfo"]

    p1SystemInstruction = f'Your name is {P1Name} and you live in {Location}. You are a {P1Age} old {P1Gender} and {P2Name}, who is {P2Age} {P2Gender} and you are talking to {P2Name}. {extra}'
    p2SystemInstruction = f'Your name is {P2Name} and you live in {Location}. You are a {P2Age} old {P2Gender} and {P1Name}, who is {P1Age} {P1Gender} and you are talking to {P1Name}. {extra}'

    print("P1: " +  p1SystemInstruction)
    print("P2: " +  p2SystemInstruction)

    p1model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction=p1SystemInstruction)

    p2model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction=p2SystemInstruction)


    p1_reply = p1model.start_chat(
        history=[
            {"role": "model", "parts": P1Says},
        ]
    )
    p2_reply = p2model.start_chat(
    )

    One = P1Says
    
    for i in range(8): 
        time.sleep(1)
        print(i)
        print(f'\n{P1Name}: {One}')
        response1 = p2_reply.send_message(One)
        print(f'{P2Name}:  {response1.text}')
        response2 = p1_reply.send_message(response1.text)
        One = response2.text



two_person_talking2({
    "name1":"Narendra Modi",
    "age1":"70",
    "gender1":"male",
    "name2":"Pandit Jawaharlal Nehru",
    "age2":"70",
    "gender2":"male",
    "location":"Delhi, India",
    "1speaks":"Namaskar",
    "moreinfo" : "Naredra modi is current prime minister of india and jawaharlal nehru was the first prime minister of india"
    })
