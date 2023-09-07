# Automatic Arxiv summarizer

* Arxiv api
* Nougat
* ChatGPT


# Usage

Requires cuda 12

'''
git clone https://github.com/Thessal/autoarxiv

cd autoarxiv

docker network create auto-arxiv-app

docker run -d \
    --network auto-arxiv-app --network-alias nougat \
    --hostname nougat\
    -p 7860:7860 --platform=linux/amd64 --gpus all \
	registry.hf.space/ysharma-nougat:latest python app.py

docker build -t getting-started .

docker run --network auto-arxiv-app -p 0.0.0.0:3000:3000 getting-started
'''

# Example
![demo](demo.png?raw=true "Demo")
