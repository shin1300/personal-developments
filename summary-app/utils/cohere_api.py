from cohere import Client
import os

co = Client(os.getenv("COHERE_API_KEY"))

def summarize_text(text):
    response = co.summarize(
        text=text,
        length="medium",
        format="paragraph",
        model="summarize-xlarge",
    )
    return response.summary
