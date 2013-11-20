#! C:/Python27/python.exe
# -*- coding: utf-8 -*- 

# これはコメントです

if __name__ == "__main__":

  value_1 = "WNOGUCHI"
  value_2 = "PYTHON"
  
  if value_1 == "Python":
    pass
  elif value_1 == "python" and value_2 == "wnoguchi":
    print u"2番目の条件式true"
  elif value_1 == "WNOGUCHI" and value_2 == "PYTHON":
    print u"3番目の条件式true"
  else:
    print "no..."
