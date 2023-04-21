import openai
import urllib.request
from PIL import Image
import os


def get_API_key():
    key = str()
    try:
        with open('Authentication.txt', mode='r') as my_file:
            key = my_file.read()
    except FileNotFoundError as err:
        print('File does not exit: ', err)
    except IOError as err:
        print('IO Error: ', err)
    return key


def chat_completion(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": query},
         ]
        )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    print(result)


def display_image(img):
    result = []
    for data in img.data:
        result.append(data.url)
    new_path = r'.\Images'
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    for i, url in enumerate(result):
        urllib.request.urlretrieve(url, './Images/image' + str(i) + '.png')
        img = Image.open('./Images/image' + str(i) + '.png')
        img.show()


def image_create(query):
    try:
        response = openai.Image.create(
            prompt=query,
            n=2,
            size="1024x1024",
            response_format='url'
        )
        display_image(response)
        return 'Image Generated Successfully'
    except:
        print('Some error has been encountered, Check your API Key')


CHOICE = {'1': chat_completion,
          '2': image_create
          }
openai.api_key = get_API_key()
print('Running your script')
x = input('For Chat press 1: \nFor Image press 2: ')
y = input('Input your query: ')
(CHOICE.get(x))(y)
input('Press any key to exit')
