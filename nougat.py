from gradio_client import Client
#client = Client("http://0.0.0.0:7860")
client = Client("http://nougat:7860")

import uuid 
import requests

def get_pdf(pdf_link):
  # Generate a unique filename
  unique_filename = f"input/downloaded_paper_{uuid.uuid4().hex}.pdf"

  # Send a GET request to the PDF link
  response = requests.get(pdf_link)

  if response.status_code == 200:
      # Save the PDF content to a local file
      with open(unique_filename, 'wb') as pdf_file:
          pdf_file.write(response.content)
      print("PDF downloaded successfully.")
  else:
      print("Failed to download the PDF.")
  return unique_filename #.split('/')[-1][:-4]

def get_text(url):
    return client.predict(get_pdf(url),url  , fn_index=0)


