import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, Response, send_file


ENDPOINT = 'http://talkobamato.me'

app = Flask(__name__)


def get_fact():
    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")
    return facts[0].getText().strip()


@app.route('/')
def home():
    data = {
        'input_text': get_fact(),
    }
    r = requests.post(url='/'.join([ENDPOINT, 'synthesize.py']),
                      data=data,
                      allow_redirects=False)
    return r.headers['Location']


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
