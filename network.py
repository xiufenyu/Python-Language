from urllib.parse import urlparse
from publicsuffix2 import PublicSuffixList

import socket
import validators

psl = PublicSuffixList()

'''
   get hostname from url
   url MUST start with "http://" or "https://"
'''
def get_hostname(url):
    return urlparse(url).hostname


'''
   get domain from url
   url MUST start with "http://" or "https://"
'''
def get_domain(url):
    hostname = urlparse(url).hostname
    domain = psl.get_public_suffix(host)
    return domain


# test if domain is valid
result = validators.domain("www.google.com")
print(f"result={result}")


'''
* Get host name by ip address
'''
def get_host_by_addr(ipaddr):
    host = None
    try:
        host, alias, addr_list = socket.gethostbyaddr(ipaddr)
    except socket.error:
        print(f"Exception:::look up host failure for {ipaddr}")
    return host


if __name__ == "__main__":
    url = "https://wiki.google.com/news/latest"
    host = get_hostname(url)
    print(host)
    domain = get_domain(url)
    print(domain)

    get_host_by_addr("www.google.com")