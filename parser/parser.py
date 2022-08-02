
import re
import requests
from bs4 import BeautifulSoup as bs


from os.path import abspath, split
import sys
dir = split(split(abspath(__file__))[0])[0]
sys.path.append(dir)
from settings import get_url



def get_data():
    # URL = "https://docs.near.org/api/rpc/transactions"
    r = requests.get(get_url())
    soup = bs(r.text, "html.parser")
    data = soup.find('div', class_='docItemContainer_Djhp')
    names = data.findAll('h2', class_='anchor anchorWithStickyNavbar_LWe7')
    method_params = data.findAll('ul')


    res:str = []
    for i in method_params:
        if(re.match(r'<ul><li>method:', str(i))):
            res.append(i)

    result = []
    for name, mp in zip(names, res):

        name.find('a').decompose()
    
        new_mp = mp.findAll('li')
        method = new_mp[0].text.replace('method: ','',1)

        if new_mp[1].find('ul'):
            params = [i.text for i in new_mp[1].find('ul').findAll('li')]
        else:
            params = [new_mp[1].text.replace('params: ','',1)]
        
        x = {"name": name.text,
             "method": method,
             "params": params}
        result.append(x)
    return result


if __name__ == '__main__':
    print (get_data())
