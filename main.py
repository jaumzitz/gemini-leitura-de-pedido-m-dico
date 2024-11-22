import google.generativeai as genai
from PIL import Image

genai.configure(api_key='')

model = genai.GenerativeModel('gemini-1.5-flash')
img = Image.open('./guia.jpeg')

response = model.generate_content(["Essa é a foto de uma solicitação de exames escrita por um médico. Identifique quais são os exames solicitados. Retorne um objeto JSON com todos os exames, e nada mais.", img])
print (response.text)