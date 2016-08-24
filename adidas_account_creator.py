#!/usr/bin/env python
import requests
import time
from BeautifulSoup import BeautifulSoup
from GmailDotEmailGenerator import GmailDotEmailGenerator

def account_successfully_created(response):
  try:
    return False if BeautifulSoup(response.text).find('input',
        { 'id': 'resumeURL' }).get('value') == \
            'https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MyAccount-CreateOrLogin'\
             else True
  except:
    return True

# CHANGE :30 TO HOWEVER MANY U WANT TO MAKE
for email in \
    (GmailDotEmailGenerator('YOUR_EMAIL_HERE').generate())[:30]:

  headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
      'Accept-Encoding': 'gzip, deflate, sdch, br',
      'Accept-Language': 'en-US,en;q=0.8',
      'Upgrade-Insecure-Requests': 1
      }

  s = requests.Session()
  s.headers.update(headers)

  r = s.get('https://cp.adidas.com/web/eCom/en_US/loadcreateaccount')
  csrftoken = BeautifulSoup(r.text).find('input',
      { 'name': 'CSRFToken' }).get('value')

  print "** Found CSRFToken: {0}".format(csrftoken)

  s.headers.update({
    'Origin': 'https://cp.adidas.com',
    'Referer': 'https://cp.adidas.com/web/eCom/en_US/loadcreateaccount',
    })

  password = 'A_PASSWORD'

  r = s.post('https://cp.adidas.com/web/eCom/en_US/accountcreate',
      data = {
        'firstName': 'YOUR_FIRST_NAME',
        'lastName': 'Sarmiento',
        'minAgeCheck': 'true',
        '_minAgeCheck': 'on',
        'email': email,
        'password': password,
        'confirmPassword': password,
        '_amf': 'on',
        'terms': 'true',
        '_terms': 'on',
        'metaAttrs[pageLoadedEarlier]': 'true',
        'app': 'eCom',
        'locale': 'en_US',
        'domain': '',
        'consentData1': 'Sign me up for adidas emails, featuring exclusive offers, featuring latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.com/us/help-topics-privacy_policy.html">Policy Policy</a> for details.',
        'consentData2': '',
        'consentData3': '',
        'CSRFToken': csrftoken
        } )


  print "Username = {0}, Password = {1}, Account created? {2}".format(email, password, account_successfully_created(r))

  time.sleep(5)
# print dir(r)
