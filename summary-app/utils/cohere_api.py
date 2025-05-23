from cohere import Client
import os

co = Client(os.getenv("COHERE_API_KEY"))

def summarize_text(text, length="medium"):
    
    response = co.summarize(
        text=text,
        length=length,
        format="paragraph",
        model="summarize-xlarge",
    )
    return response.summary
