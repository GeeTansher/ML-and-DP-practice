import re

if __name__ == '__main__':
    str = '''hicu j ijwokddw wkkd@gmail.com ehd
          wedhdiwnend
          dncnwnncnjwndwnd wndnw@gmail.com
          hiwdjd@jed.mdw.d
          hwde wej@wijedj.com'''
    # email = re.findall(r'[0-9a-zA-z+_%$!]+@[0-9a-zA-z+_%$!]+.[0-9a-zA-z+_%$!.]+',str)
    # or
    email = re.findall(r"\w+@\S+.\w+", str)
    print(email)
