# AI Learning Journey

This repository contains my practice code and assignments from the **DeepLearning.AI - AI Python for Beginners** course, along with additional Python practice exercises.

## Setting up Gemini API (to run notebooks locally)

The course notebooks are normally designed to run on Coursera's hosted environment. If you want to run them on your own machine, you'll need to connect the `helper_functions.py` file to a free LLM API. This project uses **Google's Gemini API**, since it offers a free tier.

### Step 1: Get a free Gemini API key

1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Click **"Create API key"**
4. Copy the generated key (it will look something like `AIzaSy...`)

### Step 2: Install the required package

```bash
pip install google-generativeai
```

### Step 3: Set up `helper_functions.py`

Add your API key and configure the client like this:

```python
import google.generativeai as genai

# Add your Gemini API key as a string here
gemini_api_key = "YOUR_API_KEY_HERE"

# Set up the Gemini client
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-2.5-flash")   # free-tier model


def get_llm_response(prompt):
    """Takes a prompt (string) and returns the LLM's response as a string."""
    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")
        completion = model.generate_content(prompt)
        return completion.text
    except TypeError as e:
        print("Error:", str(e))


def print_llm_response(prompt):
    """Takes a prompt (string) and prints the LLM's response."""
    llm_response = get_llm_response(prompt)
    print(llm_response)
```

### Step 4: Restart your kernel and test

In Jupyter/VS Code, restart the kernel, then run:

```python
from helper_functions import print_llm_response
print_llm_response("What is the capital of France?")
```

If you see a response printed, the setup is working.

## ⚠️ Important Note on API Keys

- **Never commit your real API key to a public repository.**
- Keep your key private — anyone with it can make requests using your account.
- Consider adding `helper_functions.py` (or a separate config file with your key) to `.gitignore` if it contains your real key.

## Notes

- `gemini-2.5-flash` was used because older models like `gemini-1.5-flash` have since been deprecated. Check [Gemini's model list](https://ai.google.dev/gemini-api/docs/models) if you run into a "model not found" error.
- If you don't want to set up a local API key at all, you can simply run the notebooks directly in Coursera's hosted "Code" environment — no setup needed there.
