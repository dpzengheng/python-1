#coding=utf-8

import urllib2

from bs4 import BeautifulSoup


url = "https://baike.baidu.com/item/Python/407313"

response1 = urllib2.urlopen(url)
# print response1.getcode()
# print len(response1.read())

req = urllib2.Request(url)
req.add_header("user-agent", "Mozilla/5.0")

res2 = urllib2.urlopen(req)
# print res2.getcode()
# print len(res2.read())

# print res2.read()
print '我们'
soup = BeautifulSoup(res2.read(),'html.parser',from_encoding='utf-8')
print '获取所有连接'
links = soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()
    
# print '获取某个连接'
# link_node = soup.find('a',href='http://news.baidu.com')
# print link_node.name,link_node['href'],link_node.get_text()

# print '正则匹配连接'
# link_node = soup.find('a', href=re.compile(r'新闻'))
# print link_node.name,link_node['href'],link_node.get_text()