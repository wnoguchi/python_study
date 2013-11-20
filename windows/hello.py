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
  
  v = "aaa"
  v += "bbb"
  v += "ccc"
  
  print v

  print 3.141592

  # タプル型
  print "aaaaa-bbbbb-ccccc".split("-")

  print "12".zfill(10)

  print "aaa" in multiline
  print "qq" in multiline
