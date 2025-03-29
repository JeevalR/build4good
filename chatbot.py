from google import genai

client = genai.Client(api_key='AIzaSyADnTi4z1CzS8oZGSAyDgLIaLZtWx43n4s')

def chat(prompt):
    response = client.models.generate_content(model='gemini-2.0-flash', contents='prompt')
    return response
