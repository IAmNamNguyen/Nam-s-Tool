import sys
from os.join import path
input_file = join(sys.path[0], input.txt)
output_file = join(sys.path[0], output.txt)
with open(input_file,'r') as i:
    paras = i.readlines()
def out(html):
    with open(output_file,'w') as o:
        o.write(str(html))
print("Hãy đảm bảo rằng đã đưa dữ liệu đầu vào ở file input.txt")
check = str(input("Đã cho dữ liệu vào file input.txt chưa? (yes/no): "))
checknote = str(input("Có note không? (yes/no): "))
if checknote == "yes":
    notes = str(input("Liệt kê các dòng cần note (ngăn cách bởi dấu phẩy, viết liền):"))
    listnote = list(map(int, notes.split(",")))
if check == "yes":
    for t in range(len(paras)):
        if t in listnote:
            print(f'Đã đến dòng chứa note (dòng {t}).')
            notenum = int(input("Ghi tên note: "))
            notetext = str(input("Nội dung note: "))
            html = f'<p id="{t}">{paras[t]}<span id="anchor-note{notenum}" class="tooltip note1"><img src="https://filedn.com/l6Yawa51iDjJ68pgrC3ymCB/WebData/Images/item.png" title="note1"><a href="#note1" title="Xuống dưới">.</a><span class="toolttext">{notetext}</span></span></p>\n'
        else:
            html = f'<p id="{t}">{paras[t]}</p>\n'
        

    
