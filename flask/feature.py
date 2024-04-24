import pygoogle
#code for feature extraction
from urllib.parse import urlparse,urlencode
import ipaddress
import re
from bs4 import BeautifulSoup
import whois
import urllib
import urllib.request
from datetime import datetime
import requests
from googlesearch import search
import tldextract
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#link in java script
def has_script_links(url):
    try:
        # Fetch webpage HTML content
        response = requests.get(url)
        if response.status_code == 200:
            # Extract URLs from script tags
            script_urls = re.findall(r'<script.*?src="(.*?)".*?>', response.text)
            if len(script_urls) != 0:
                return 1
    except Exception as e:
        return 0
    return 1

#email info
def has_phishing_email(url):
    try:
        # Fetch webpage HTML content
        response = requests.get(url)
        if response.status_code == 200:
            # Search for potential phishing email patterns in the HTML content
            email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
            if email_pattern.search(response.text):
                return 1
    except Exception as e:
        return 0
    return -1

#server form handling
def has_server_form_handler(url):
    try:
        # Fetch webpage HTML content
        response = requests.get(url)
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find all form tags
            form_tags = soup.find_all('form')
            # Check if any form contains the ServerFormHandler
            for form in form_tags:
                if 'ServerFormHandler' in form.get('action', ''):
                    return 1
    except Exception as e:
        return 0
    return -1

def has_anchor_urls(url):
    try:
        # Fetch webpage HTML content
        response = requests.get(url)
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find all anchor tags
            anchor_tags = soup.find_all('a', href=True)
            if anchor_tags:
                return 1
    except Exception as e:
        return 0
    return -1
#subdomain
def get_favicon_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find favicon link with rel="icon" or rel="shortcut icon"
            favicon_link = soup.find("link", rel="icon") or soup.find("link", rel="shortcut icon")
            if favicon_link:
                favicon_url = favicon_link.get('href')
                # Convert relative URL to absolute URL if necessary
                favicon_url = urljoin(url, favicon_url)
                return 1
    except Exception as e:
        i = 0
    return 0

def is_abnormal_url(url):
    
    # Check for suspicious characters in the URL
    parsed_url = urlparse(url)
    if re.search(r'[@!#$%^&*()_+{}[\]:;<>,.?/\\|~-]', url):
        return 1

    if len(url) > 1000:
        return 1
    
    # Check if domain exists and is reachable
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        response.raise_for_status()
    except Exception as e:
        return 1
    
    # Check SSL certificate expiration date
    if parsed_url.scheme == 'https':
        try:
            ssl_expiry_date = datetime.strptime(response.headers['Expires'], '%a, %d %b %Y %H:%M:%S %Z')
            if ssl_expiry_date < datetime.now():
                return 1
        except KeyError:
            # SSL expiry date not found or invalid
            return 1
    
    return 0


def has_subdomain(url):
    # Extract domain parts
    try:
      extracted = tldextract.extract(url)
    # Check if subdomain exists
      if bool(extracted.subdomain):
       return 1
      else:
       return -1
    except:
      return 0

def SSLfinal_State(url):
    try:
        response = requests.get(url, timeout=10)
        response.status_code == 200 and response.url.startswith('https')
        return 1
    except requests.exceptions.RequestException:
        return -1

#RequestURL

def has_redirected(url):
    try:
        response = requests.head(url, allow_redirects=True)
        final_url = response.url
        if final_url != url:
            return 1
        else:
           return -1
    except Exception as e:
        return 0
    



# 1.Domain of the URL (Domain) 
# 1.Domain of the URL (Domain) 
def getDomain(url):  
  domain = urlparse(url).netloc
  if re.match(r"^www.",domain):
	  domain = domain.replace("www.","")
  return domain

# 2.Checks for IP address in URL (Have_IP)
def havingIP(url):
  try:
    ipaddress.ip_address(url)
    ip = 1
  except:
    ip = 0
  return ip

def uses_non_standard_port(url):
    parsed_url = urlparse(url)
    if parsed_url.port is None:
        return 0  # No port specified, assuming standard port
    elif parsed_url.scheme == 'http' and parsed_url.port == 80:
        return 0  # Standard HTTP port
    elif parsed_url.scheme == 'https' and parsed_url.port == 443:
        return 0  # Standard HTTPS port
    else:
        return 1

# 3.Checks the presence of @ in URL (Have_At)
def haveAtSign(url):
  if "@" in url:
    at = 1    
  else:
    at = 0    
  return at


# 4.Finding the length of URL and categorizing (URL_Length)
def getLength(url):
  if len(url) < 54:
    length = 0            
  else:
    length = 1            
  return length

# 5.Gives number of '/' in URL (URL_Depth) LongURL
def getDepth(url):
  s = urlparse(url).path.split('/')
  depth = 0
  for j in range(len(s)):
    if len(s[j]) != 0:
      depth = depth+1
  if(depths > 10):
     return 1
  return 0


# 6.Checking for redirection '//' in the url (Redirection)
def redirection(url):
  pos = url.rfind('//')
  if pos > 6:
    if pos > 7:
      return 1
    else:
      return 0
  else:
    return 0
  

# 7.Existence of “HTTPS” Token in the Domain Part of the URL (https_Domain)
def httpDomain(url):
  domain = urlparse(url).netloc
  if 'https' in domain:
    return 1
  else:
    return 0
  
#listing shortening services
shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net"


# 8. Checking for Shortening Services in URL (Tiny_URL)
def tinyURL(url):
    match=re.search(shortening_services,url)
    if match:
        return 1
    else:
        return 0


# 9.Checking for Prefix or Suffix Separated by (-) in the Domain (Prefix/Suffix)
def prefixSuffix(url):
    if '-' in urlparse(url).netloc:
        return 1            # phishing
    else:
        return 0            # legitimate
    

#Domain Based Features
    


# 12.Web traffic (Web_Traffic)
def web_traffic(url):
  # try:
  #   #Filling the whitespaces in the URL if any
  #   url = urllib.parse.quote(url)
  #   rank = BeautifulSoup(urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find(
  #       "REACH")['RANK']
  #   rank = int(rank)
  # except TypeError:
  #       return 1
  # if rank <100000:
  #   return 1
  # else:
    return 0
  

# 13.Survival time of domain: The difference between termination time and creation time (Domain_Age)  
def domainAge(domain_name):
  creation_date = domain_name.creation_date
  expiration_date = domain_name.expiration_date
  if (isinstance(creation_date,str) or isinstance(expiration_date,str)):
    try:
      creation_date = datetime.strptime(creation_date,'%Y-%m-%d')
      expiration_date = datetime.strptime(expiration_date,"%Y-%m-%d")
    except:
      return 1
  if ((expiration_date is None) or (creation_date is None)):
      return 1
  elif ((type(expiration_date) is list) or (type(creation_date) is list)):
      return 1
  else:
    ageofdomain = abs((expiration_date - creation_date).days)
    if ((ageofdomain/30) < 6): #less than 6 months then phishing
      age = 1
    else:
      age = 0
  return age

# 14.End time of domain: The difference between termination time and current time (Domain_End) 
#If end period of domain > 6 months, the vlaue of this feature is 1 (phishing) else 0 (legitimate)
def domainEnd(domain_name):
  expiration_date = domain_name.expiration_date
  if isinstance(expiration_date,str):
    try:
      expiration_date = datetime.strptime(expiration_date,"%Y-%m-%d")
    except:
      return 1
  if (expiration_date is None):
      return 1
  elif (type(expiration_date) is list):
      return 1
  else:
    today = datetime.now()
    end = abs((expiration_date - today).days)
    if ((end/30) < 6):
      end = 0
    else:
      end = 1
  return end


# 15. IFrame Redirection (iFrame)
def iframe(response):
  if response == "":
      return 1
  else:
      if re.findall(r"[<iframe>|<frameBorder>]", response.text):
          return 0
      else:
          return 1
      
# 16.Checks the effect of mouse over on status bar (Mouse_Over)
def mouseOver(response): 
  if response == "" :
    return 1
  else:
    if re.findall("<script>.+onmouseover.+</script>", response.text):
      return 1
    else:
      return 0
    
# 17.Checks the status of the right click attribute (Right_Click)
def rightClick(response):
  if response == "":
    return 1
  else:
    if re.findall(r"event.button ?== ?2", response.text):
      return 0
    else:
      return 1

# 18.Checks the number of forwardings (Web_Forwards)    
def forwarding(response):
  if response == "":
    return 1
  else:
    if len(response.history) <= 2:
      return 0
    else:
      return 1
#web traffic
def get_web_traffic(url):
    try:
        api_key = '63d96f060dff4bb48e8a6303c1c5bd75'
        url = f"https://api.similarweb.com/v1/website/{url}/total-traffic-and-engagement/visits"
        params = {'api_key': api_key}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'visits' in data:
                if(int(data['visits']) < 1000):
                   return 1
    except Exception as e:
        return 0
    return 1


#page rank
def get_page_rank(url):
    try:
        pr = pygoogle.get_pr(url)
        return pr
    except Exception as e:
        print("Error:", e)
    return None


#Function to extract features
def featureExtraction(url,label):

  features = []
  #Address bar based features (10)
  features.append(getDomain(url))
  features.append(havingIP(url))
  features.append(haveAtSign(url))
  features.append(getLength(url))
  #features.append(getDepth(url))
  features.append(redirection(url))
  features.append(httpDomain(url))
  features.append(tinyURL(url))
  features.append(prefixSuffix(url))
  features.append(has_subdomain(url))
  
  #Domain based features (4)
  dns = -1
  try:
    domain_name = whois.whois(urlparse(url).netloc)
    dns = 1
  except:
    dns = -1
  #Dnsrecrding
  features.append(dns)
  features.append(web_traffic(url))
  features.append(1 if dns == 1 else domainAge(domain_name))#DomainRegLen
  features.append(1 if dns == 1 else domainEnd(domain_name)) 



  
  # HTML & Javascript based features (4)
  try:
    response = requests.get(url)
  except:
    response = ""
  features.append(iframe(response))
  features.append(mouseOver(response))
  features.append(rightClick(response))
  features.append(forwarding(response))
  features.append(label)
  
  return features



x = featureExtraction("https://erpcustomer.epicor.com/lms/catalog/browse", 0)
print(x)


# importing library


# # enter website name
# website = input('Enter website: ')
# # enter query
# query = input('Enter query: ')
# # initilazing index=0
# index = 0

# # search will return an object containing
# # all url from google search results
# # here, tid is top level domain, 
# # stop means how many search results you want
# # stop=100 means we will get top 100 results from google
# for i in search(query, tld="com", num=10, stop=100, pause=2):
#     # checking website in results
#     if website in i:
#         # printing index of website and url
#         print(index+1, i)
#     index