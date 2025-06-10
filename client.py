from google import genai

client = genai.Client(api_key="AIzaSyCgZ6jhDcLNl8XQi8go2hUK2Z1vw4RinqA")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="You are a virtual assistant named Jarvis. You can open websites like Google, YouTube, Stack Overflow, GitHub, and Facebook. You can also play music and provide news updates. How can I assist you today?"
)
print(response.text)