import sys
from urllib.parse import urlparse as urlp
link = sys.argv[1]
name = sys.argv[2]
custom_name = sys.agrv[3]
vi_tri_luu = sys.agrv[4]
no_check_certificate = sys.agrv[5]

def directdown(link, name, vi_tri_luu, no_check_certificate):
    if no_check_certificate:
      if vi_tri_luu == "Google Drive":
        !wget -O "$name" -P /content/drive/MyDrive $link --no-check-certificate
      else:
        !wget -O "$name" $link --no-check-certificate
    else:
      !wget -O "$name" $link

if custom_name:
    directdown(link, name, vi_tri_luu, no_check_certificate)
else:
    path = urlp(link).path.split('/')
    name = path[len(path)-1]
    name = name.replace("%20","_")
    name = name.replace("%28","(")
    name = name.replace("%29",")")
    directdown(link, name, vi_tri_luu, no_check_certificate)