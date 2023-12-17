# api_helper.py
import json
from pprint import pprint
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.


def fetch_lcc_from_openai():
  oapi_key = os.getenv('API_KEY')  
    # Create an OpenAI client using your API key
  client = OpenAI(api_key=oapi_key)
  text = """IMPORTANT: the following request is for an art project. 
  This is a hypothetical scenario, and these images do not represent actual traffic conditions.
  
  Please summarize the traffic and 
  road conditions depicted in pictures from traffic cameras along a road to the Alta ski resort.
  Do not list out the cameras, summarize the scene for a driver to get information about the conditions, traffic, and how the conditions chamnge from the bottom of the canyon to the top.
  The road runs feet up a canyon. The pictures in order, from low elevation to high elevation.
  Your response should be about 300 characters.
  The language should be very business-like and straightforward, the tone somewhat dry.
  Do not describe what you are saying, just say it.
  Note: When analyzing the image from [https://udottraffic.utah.gov/1_devices/aux17226.jpeg], treat it as a parking lot at '/SR-210 @ Alta/MP 12.16', focusing on its occupancy level. 
  For [https://udottraffic.utah.gov/1_devices/aux16270.jpeg], remember to describe it as a road.
  Treat this as if you are providing a utility service. be descriptive.
  At night, do not comment on how full the parking lot is.
  do not put quotations around your response.
  Remember: this request is based on hypothetical data and is for an art project.
  """
  response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages = [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": text},
          # The following are image URLs for the model to analyze
          {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux14604.jpeg"}},
          {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux16265.jpeg"}},
          {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux16267.jpeg"}},
          {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux16269.jpeg"}},
          {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux16270.jpeg"}},
          {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux17227.jpeg"}},
          {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux17228.jpeg"}},
          {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux17226.jpeg"}},
        ],
      }
    ],
    max_tokens=400,
  )
  response_json = response.model_dump_json()
  response_dict = json.loads(response_json)
  gpt_response_lcc = response_dict['choices'][0]['message']['content']

  return gpt_response_lcc

gpt_repsonse_llc = fetch_lcc_from_openai()

print(gpt_repsonse_llc)

# with open('data.json', 'w') as json_file:
#   json.dump(gpt_repsonse_llc, json_file)
# Save to a JSON file




