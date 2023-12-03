import os
import urllib.request
from urllib.parse import urlparse, urlunparse
import re

src = input()
parsed_url = urlparse(src)

# Trích xuất tên file từ phần đường dẫn của URL
image_name = os.path.basename(parsed_url.path)

# Tạo URL mới với cấu trúc đã chỉ định
new_url = urlunparse(('https', 'i3.hhentai.net', '/images/2023/09v2/01/' + image_name + '?imgmax=1200','', '', ''))
print(new_url)