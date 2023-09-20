import openai

def split_text(text, token_count=6000):
    # https://platform.openai.com/tokenizer
    # This translates to roughly ¾ of a word (so 100 tokens ~= 75 words) 
    # Removing newline is important
    assert (type(text) == str)
    texts = text.split()
    output = [' '.join(texts[i:i+token_count]) for i in range((len(texts)+token_count-1)//token_count)]
    return output

def summarize(text_to_summarize, api_key):
    assert (type(text_to_summarize) == str)
    print("text length: ", len(text_to_summarize))
    try:
        return _summarize(split_text(text_to_summarize, token_count=6000), api_key)
    except openai.error.InvalidRequestError as e:
        print("reducing text length")
        try: 
            return _summarize(split_text(text_to_summarize, token_count=5000), api_key)
        except: 
            return _summarize(split_text(text_to_summarize, token_count=4000), api_key)

def _summarize(text, api_key):
    assert (type(text) == list)
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        model="gpt-3.5-turbo-16k", # This model's maximum context length is 16385 tokens.
        messages=[ 
            #{"role": "user", "content": f"Summarize this research article into one sentence: {text[0]}"},
            #{"role": "user", "content": f"We are trying to summarize key findings and references from a research paper. Please read following article carefully. : \n[start of article]\n {text[0]}\n[end of article]\nInstruction:\nSummarize this research article into one sentence. And then, make a list of key findings and important references."},
            {"role": "user", "content": f"We are trying to summarize key findings, and references from a research paper. Please read following article carefully. Mathematical formulae are presented in LaTeX format. : \n[start of article]\n {text[0]}\n[end of article]\nInstruction:\nSummarize this research article into one sentence. And then, make a list of key findings, LaTeX formulae and important references."},
        ],
    )
    summary = response["choices"][0]["message"]["content"] 
    print("created", response["created"])
    print("prompt tokens:", response["usage"]["prompt_tokens"])
    print("total tokens:", response["usage"]["total_tokens"])
    return summary
