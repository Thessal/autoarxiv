# # app.py
# from flask import Flask
# 
# app = Flask(__name__)
# 
# @app.route('/')
# def hello():
#     return "Hello, World!"
# 
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=3000)


from flask import Flask, render_template, request
import json 
import nougat
import chatgpt
import arxiv

app = Flask(__name__, template_folder='template')

@app.route("/", methods=["GET", "POST"])
def index():
    with open("config.json", 'rt') as f:
        config = json.load(f)
    apikey = config["api_key"]

    query = """(cat:"physics.soc-ph") OR ((cat:"math.PR" OR cat:"math.ST" OR cat:"math.CO" OR cat:"stat.ML" OR cat:"physics.data-an") AND abs:"complex network") OR (abs:"complex network" AND abs:"soci")"""
    data = ""
    if request.method == "POST":
        # Retrieve form data
        query = request.form.get("query")
        apikey = request.form.get("apikey")

        # You can process the form data here
        # For now, let's just print it
        # print(f"Name: {name}, Email: {email}")

        # data = f"<p>{str(config)}</p>"
        print("arxiv running")
        arxiv_item = arxiv.get_arxiv(query)
        if arxiv_item:
            header = '\n\n'.join([f'{x} : {arxiv_item[x]}' for x in ['id','title', 'author']])
            pdf_url = arxiv_item["pdf"]
            print("arxiv finished")
            # url = "https://arxiv.org/pdf/2308.08316.pdf"
            print("nougat running")
            data = nougat.get_text(pdf_url)
            print("nougat finished")
            print("chatgpt running")
            data = chatgpt.summarize(data, apikey)
            print("chatgpt finished")
            data = header + '\n\n' + data
        else:
            data = "arxiv item does not contain pdf"

    return render_template("form.html", query=query, apikey=apikey, data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
