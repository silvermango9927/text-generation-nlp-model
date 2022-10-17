# An NLP Text Generation Model

## Problem Statement
Say you have a question. You then decide to search on Google. Scrolling on and on, brings you to an obscure website that seems to be the only one having your answer. You click on it and find it to be filled with unnecessary text to the brim with a small portion of it being what you actually want. 

## My solution
This model and porject can take in basically a query of any sort which is processed by the [GPT3 OpenAI algorithm](https://openai.com/api/) to give a succint description and solution to the question posed. \
Along with this, the additional information section comprises of scraped content from websites using [JSON Custon Search API](https://developers.google.com/custom-search/v1/overview). The required content is scraped from a list of websites that have been fetched. The content received and cleaned amounts to millions of characters. To shorten and condense this information into a succint format, [Bidirectional Encoder Representations](https://github.com/google-research/bert) (BERT) and [Generative Pre-trained Transformer](https://huggingface.co/gpt2) (GPT) have been used to get different summarisation styles and techniques.

## Further development
> Success is not a destination, but rather a journey which does not end
This project has a lot more scope and I'm going to be investing my time and effort into:
* Optimising the speeds and performance of the model and its processes
* Creating an optimal web interface for people to easily interact with it
* Expanding search criteria and generalising scrape techniques
* Getting information from YouTube videos too
