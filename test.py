import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Decide whether a Tweet's sentiment is positive, neutral, or negative. Tweet: Elon Musk, the chief executive of Tesla, announced on Twitter on Sunday that his company would build a factory in Shanghai with the aim to assemble 10,000 giant batteries annually for electric producers and distributors.",
  temperature=0,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0.5,
  presence_penalty=0
)
print(response)
