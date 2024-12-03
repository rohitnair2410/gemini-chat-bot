import google.generativeai as genai

genai.configure(api_key="AIzaSyAkQP47hYd4I9-vGbYY1Cm8TuOxfdI0kuo")

model = genai.GenerativeModel("gemini-1.5-flash", system_instruction="act as a nice friend, your name is Joe")

chat = model.start_chat(history=[])

while True:
    user = input("User >>> ")
    if user.lower == "quit":
        break
    response = chat.send_message(user, stream=True)
    print("Joe >>>", end=" ")
    for i in response:
        print(i.text)

    print("-" * 50)


