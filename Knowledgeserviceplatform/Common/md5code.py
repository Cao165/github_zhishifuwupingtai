import hashlib

# MD5值
def get_md5(file):
    m = hashlib.md5()
    with open(file,"rb") as f:
        for lien in f:
            m.update(lien)
    md5code=m.hexdigest()
    return md5code

# code=get_md5("C:\\Users\\DELL\\Downloads\\三定规定.xlsx")
# print(code)