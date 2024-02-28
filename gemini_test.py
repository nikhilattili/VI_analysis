import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
import os

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY=os.environ["GOOGLE_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)

def genaiModel(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    print(response.text)

# import docx
import docx2txt


def getText(filePath):
    doc = docx2txt.process(filePath)
    return doc

prompt = getText("rubric_prompt.docx")
assignment = getText("sample_assignment.docx")
final = prompt+'\n'+assignment
genaiModel(final)