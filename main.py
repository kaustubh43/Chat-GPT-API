import openai
import urllib.request
from PIL import Image


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


def chat_completion():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": "Why should DevOps engineer learn kubernetes?"},
        ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    return result


def display_image(img):
    result = []
    for data in img.data:
        result.append(data.url)
    print(result)
    for i, url in enumerate(result):
        urllib.request.urlretrieve(url, '.\Images\image' + str(i) + '.png')
        img = Image.open('.\Images\image' + str(i) + '.png')
        img.show()


def image_create():
    response = openai.Image.create(
        prompt="Cat sitting on a chair",
        n=2,
        size="1024x1024",
        response_format='url'
    )
    display_image(response)
    return 'Image Generated Successfully'


openai.api_key = get_API_key()
print('Running your script')
print(image_create())
