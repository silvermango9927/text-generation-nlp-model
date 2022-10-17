# Importing required models
from base64 import encode
from dotenv import dotenv_values
vals = dotenv_values(".env")
from bs4 import BeautifulSoup

import openai

# import wikipedia as wk

from summarizer import Summarizer, TransformerSummarizer

import requests as rq
from urllib.request import urlopen
import re

# Getting environment variables
api_key = vals['API_KEY']
engine_id= vals['ENGINE_ID']
openai.api_key = vals['OPENAI_API_KEY']


# Sending a request based on parameters
query=str(input('Enter the query: '))

res = rq.get('https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}'.format(key=api_key, cx=engine_id, query=query)).json()

# wiki = wk.search(query)
# page = wk.page(wiki[0])

# summary = page.summary
# print(summary)


# Getting content from websites
text = ''

with open('links.txt', 'w') as file:
        for link in res['items']:
            url = link['link']
            file.write(url)
            source = urlopen(url).read()
            
            soup = BeautifulSoup(source, 'lxml')
            for paragraph in soup.find_all('p'):
                text+=paragraph.text


# Cleaning content into required format
text = re.sub(r'\[.*?\]+', '', text)
text = text.replace('\n', '')
# print(text)


# Using pre-trained models to summarise given paragraphs
bert_model = Summarizer()
bert_summary = ''.join(bert_model(text, num_sentences = 3))

GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
gpt_summary = ''.join(GPT2_model(text, num_sentences=2))

info_para = bert_summary + gpt_summary
# print(info_para)


# Using GPT3 to auto-generate text based on prompt
response = openai.Completion.create(
    model='text-davinci-002',
    prompt=query,
    temperature=0.7,
    frequency_penalty=0.5,
    presence_penalty=0.2,
    max_tokens=1000
)

model_res = ''

for choice in response['choices']:
    model_res+=choice['text']

# print(model_res)


final_response = model_res + '\n' + 'Additional information' + '\n' + info_para
with open('response.txt', 'w') as file:
    file.write(final_response)
