#! C:/Python27/python.exe
# -*- coding: utf-8 -*- 

# これはコメントです

import test_class

if __name__ == "__main__":
  classList = []
  classList.append(test_class.test_class(1, u"テスト1"))
  classList.append(test_class.test_class(2, u"テスト2"))

  for value in classList:
    print "===== class ====="
    print "code --> " + str(value.code)
    print "name --> " + value.name
