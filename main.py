from bs4 import BeautifulSoup
import urllib.request
import urllib
import random
import string
import os

url_base = 'https://prnt.sc/'

def get_html(url_len):
    global url_last3
    url_last3 = str(''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(url_len)))
    req = str(url_base + url_first3 + url_last3)
    html = urllib.request.urlopen(req).read()
    return html

def main():
    count = input('How many pictures I must download? ')
    pic_count = int(count)
    successfully = 0
    global url_first3
    url_first3 = input('Enter first 1 digit (recommendation 1-3): ')
    url_len = int(input('Enter link generation length (recommendation 5-6): '))
    print('OK! Now I`ll download ' + count + ' pictures with the "' + url_first3 + '" first digits!')
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    for counter in range(pic_count):
        html = get_html(url_len)
        soup = BeautifulSoup(html, 'html.parser')
        picture_url = soup.find(id='screenshot-image')['src']
        if picture_url[40:] == '':
            with urllib.request.urlopen(picture_url) as urll:
                out = open("download/"+picture_url[-11:], 'wb')
                out.write(urll.read())
                out.close()
            count = counter + 1
            successfully += 1
            print(str(count) + '   [' + str(url_first3) + str(url_last3) + '] - [' + picture_url + f'] - OK ! successful - {successfully}')
        else:
            count = counter + 1
            print (str(count) + '   [' + str(url_first3) + str(url_last3) + '] - [' + picture_url + '] - PASS !')




if __name__ == '__main__':
    if os.path.exists('download') == False:
        os.mkdir('download')
    main()
