#! C:/Python27/python.exe
# -*- coding: utf-8 -*- 

# これはコメントです

print u"helloモジュールのロード"

multiline = u"""
aaa
bbb
ccc
吾輩は猫である
"""

def say_hello():
  print u"hello, python world."

if __name__ == "__main__":

  print u"main関数内" + u"ああああああああああ"
  say_hello()
  print multiline

  print str(100 + 20) + u"円"
