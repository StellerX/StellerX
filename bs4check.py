import requests                                              
from bs4 import BeautifulSoup
def getPost(link):
        # Make a request            
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        # Extract title of page
        page_title = soup.title                                                                 # print the result
        a=soup.find_all('p')
        return a[1].get_text()

data=getPost('https://stellerxserver.wordpress.com/stellerx')
data=data.split('[new]')
data=data[1]
with open('__.steller','w') as f :
    f.write(data)