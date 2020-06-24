import PyPDF2 as pypdf
import re
object = open('fe-2019-course-11.02.20.pdf', 'rb')
reader = pypdf.PdfFileReader(object)
x=reader.numPages
a=input("Enter your surname: ")
a=a.upper()
abc=[]
name=[]
h=[]
k=[]
for i in range(x):
    page = reader.getPage(i)
    y = (page.extractText())
    res = re.sub(' +', ' ', y)
    l = res.split()
    n=list(l[50:53])
    sgpa = l[l.index('SGPA') + 2]
    if sgpa=='-----':
        abc.append(0.000)
        h.append(0.0)
    else:
        abc.append(float(sgpa))
        h.append(float(sgpa))
    for b in n:
        if b==a:
            ame = (" ".join(n))
            name.append(ame)
            if sgpa=='-----':
                k.append(0.0)
                break
            else:
                k.append(float(sgpa))
                break
abc.sort()
h.sort(reverse=True)
for i in range(len(k)):
    print(name[i])
    print('RANK: ('+str(h.index(k[i]))+"-"+str(781-abc.index(k[i]))+ ')/ 781')




