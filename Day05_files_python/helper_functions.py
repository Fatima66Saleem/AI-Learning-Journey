import os
from google import genai
from config import gemini_api_key

# Set up the Gemini client
client = genai.Client(api_key=gemini_api_key)


def get_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to Google's Gemini model. The function then saves the response of the model as
    a string.
    """
    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")
        completion = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        response = completion.text
        return response
    except TypeError as e:
        print("Error:", str(e))


def print_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to Google's Gemini model. The function then prints the response of the model.
    """
    llm_response = get_llm_response(prompt)
    print(llm_response)


def files_in_directory():
    """This function lists all the files in the current working directory
    (the folder where your notebook/script is running from).
    """
    files = os.listdir()
    for file in files:
        print(file)


def upload_text_file():
    """This function asks the user to type the name of a text file
    that is already placed in the current working directory, and
    returns the file's content as a string.

    (Note: unlike the course's browser-based upload button, this local
    version expects you to manually copy your file into the working
    directory first, then type its name when asked.)
    """
    filename = input("Enter the name of the text file (e.g. myfile.txt): ")
    if filename not in os.listdir():
        print(f"'{filename}' not found in the current working directory.")
        return None
    f = open(filename, "r")
    content = f.read()
    f.close()
    return content