import threading
import urllib2
import time

start = time.time()
urls = ["https://www.google.com","https://www.Apple.com"]
def chama_url(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print("'%s\' carregando em %ss" % (url, (time.time() - start())))
    #print(the_page)

threads = [threading.Thread(target=chama_url, args=(url,)) for url in urls]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Elapsed time %s" % (time.time() - start))