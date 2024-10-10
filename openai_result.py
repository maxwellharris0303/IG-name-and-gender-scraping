import os
from openai import OpenAI
import base64
import mimetypes
import json

client = OpenAI()

def load_json_schema(schema_file: str) -> dict:
    with open(schema_file, 'r') as file:
        return json.load(file)

def image_to_base64(image_path):
    # Guess the MIME type of the image
    mime_type, _ = mimetypes.guess_type(image_path)
    
    if not mime_type or not mime_type.startswith('image'):
        raise ValueError("The file type is not recognized as an image")
    
    # Read the image binary data
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Format the result with the appropriate prefix
    image_base64 = f"data:{mime_type};base64,{encoded_string}"
    
    return image_base64



def transcribe_image(image_path, caption):
    json_schema = load_json_schema('result_format.json')

    base64_string = image_to_base64(image_path)
    # Make an API call to submit the image for transcription
    response_1 = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Manually transcribe all the text including this handwriting. Use this JSON schema" + 
                     json.dumps(json_schema)},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": base64_string
                        }
                    },
                ],
            }
        ],
        max_tokens=4000,
    )

    result_1 = response_1.choices[0].message.content
    print(result_1)

    response_2 = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": f"Manually transcribe all the text including this handwriting. provide JSON file by text from this image. Description (scraper should generate 2 paragraphs with the following criteria and total sentences should be between 2 and 3): -Description should answer 3 key Ws: what is happening, when is it happening, where is it happening. -The description should include other important information about the event. -The description should have fun, good energy and light humor. -Description can include relevant emojis. But maximum of 5. Don't start the description with 'Get ready' and make it different each time. -write the descriptions in 3rd person and the description don't have to include word 'us', 'Tapestry', 'Embark', 'Perfect', 'Ultimate', 'Unforgettable', 'Most'.  But it should use both info from image and caption to generate description. The caption is '{caption}'. Music Policy - name of the DJs from the event information. If there is price information in the image or caption but no free information, display “invest” and display the price information next to “invest.” If there is free information in the image or caption or no price information, display “free”. Event date format is “year-month-day”. Use this JSON schema" + 
                     json.dumps(json_schema)},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": base64_string
                        }
                    },
                ],
            }
        ],
        max_tokens=4000,
    )

    # Print the transcription result
    result_2 = response_2.choices[0].message.content
    print(result_2)
   

    return result_1, result_2
    
# Example usage
image_path = 'image.jpg'
caption = "sdfsdfwerwer"
transcribe_image(image_path, caption)