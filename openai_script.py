import os
import openai
openai.api_type = ""
openai.api_base = ""
openai.api_version = ""
openai.api_key = ""

# read the file question.txt from the local directory
file = open("question.txt", "r")
text = file.read()
file.close()

# for each line in text, create a prompt and get the response from the API and store the response in the document response.txt
file = open("response.txt", "w")
for line in text.splitlines():
  response = openai.ChatCompletion.create(
  engine="gpt-3.5-turbo	",
  messages = [{"role": "system", "content": "You are a helpful assistant that help me"}, 
    {"role": "user", "content": line}],
  temperature=0)

  # write the response to the file by managing the format of the response since there are characters like à è ì ò ù that are not supported by the file
  file.write("##########\n")
  file.write(line)
  file.write(response.choices[0].message.content.replace("à", "a'").replace("è", "e'").replace("ì", "i'").replace("ò", "o'").replace("ù", "u'"))
  file.write("\n")
file.close()