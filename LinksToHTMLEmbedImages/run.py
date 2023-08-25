import sys
from os.path import join
input_file = join(sys.path[0], "input.txt")
output_file = join(sys.path[0], "output.txt")
with open(input_file,'r',encoding="utf-8") as i:
    images = i.readlines()
print(" ")  
print("Hãy đảm bảo rằng đã đưa dữ liệu đầu vào ở file input.txt")
print(" ")
print("********************")
print(" ")

params = str(input("Các cú pháp phụ cho thẻ img (title, alt, style,..)? - Y/N: "))
if params == "Y":
    print(f"Nếu không muốn cú pháp đó, hãy gõ \"N/A\"")
    title = str(input("title?: "))
    alt = str(input("alt?: "))
    style = str(input("style?: "))
else:
    for t in range(len(images)):
        html = f'<img src={images[t]} id="{t}"/>\n'
        with open(output_file,'a',encoding="utf-8") as o:
            o.write(str(html))

html = [f"<img src=\"{images[t]}\"",f"title=\"{title}\"",f"alt=\"{alt}\"",f"style=\"{style}\"",f"id=\"{t}\"","/>"]






    
