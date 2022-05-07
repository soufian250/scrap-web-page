import requests
from bs4 import BeautifulSoup
import shutil # to save it locally

# Making a GET request
r = requests.get('https://www.monaloc.ma/en/our-cars/2')


# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')


for tr in soup.find_all('div',class_='featured-car-img'):

   
    values = [data for data in tr.find_all('img',class_='img-responsive')]
    for value in values:
        
        ## Set up the image URL and filename
        image_url = value.get('src')
        ext = image_url.split(".")[-1]
        filename = value.get('alt')
        

        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(image_url, stream = True)

        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            
            filename = filename+'.'+ext
            # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
               shutil.copyfileobj(r.raw, f)
                
            print('Image sucessfully Downloaded: ',filename)
        else:
            print('Image Couldn\'t be retreived')
    print()
