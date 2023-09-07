import openai

def split_text(text):
    # token_count = 2000 
    token_count = 6000 
    # https://platform.openai.com/tokenizer
    # This translates to roughly ¾ of a word (so 100 tokens ~= 75 words) 
    texts = text.split()
    output = [' '.join(texts[i:i+token_count]) for i in range((len(texts)+token_count-1)//token_count)]
    return output 

def summarize(text_to_summarize, api_key):
    openai.api_key = api_key
    
    text = split_text(text_to_summarize)
    
    response = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        model="gpt-3.5-turbo-16k",
        messages=[ 
            {"role": "user", "content": f"Summarize this research article into one sentence: {text[0]}"},
        ],
    )
    summary = response["choices"][0]["message"]["content"] 
    return summary
