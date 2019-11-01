import datetime
import urllib.request


today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
url = f"http://10.216.72.145:8080/rest/download/ceph/autobackup?id=9531&appid=15429332&taskid=10008355&batchid={yesterday}-"
print(f"请求的url是： {url}")
response = urllib.request.urlopen(url)
result = response.read()
print(f"返回的response是： {result}")
