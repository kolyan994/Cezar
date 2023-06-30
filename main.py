def cezar(f : str, metod : bool, lengv : bool, k : int):
  if metod == True:
    if lengv == True:
      result = ''
      for i in f:
        if i.isalpha():
          if i.isupper():
            if ord(i) + k > 90:
              result += chr(ord(i) + k - 26)
            else:
              result += chr(ord(i) + k)
          else:
            if ord(i) + k > 122:
              result += chr(ord(i) + k - 26)
            else:
              result += chr(ord(i) + k)
        else:
          result += i
      return result
    else:
      result = ''
      for i in f:
        if i.isalpha():
          if i.isupper():
            if ord(i) + k > 1071:
              result += chr(ord(i) + k - 32)
            else:
              result += chr(ord(i) + k)
          else:
            if ord(i) + k > 1103:
              result += chr(ord(i) + k - 32)
            else:
              result += chr(ord(i) + k)
        else:
          result += i
      return result
  else:
    if lengv == True:
      result = ''
      for i in f:
        if i.isalpha():
          if i.isupper():
            if ord(i) - k < 66:
              result += chr(ord(i) - k + 26)
            else:
              result += chr(ord(i) - k)
          else:
            if ord(i) - k < 96:
              result += chr(ord(i) - k + 26)
            else:
              result += chr(ord(i) - k)
        else:
          result += i
      return result
    else:
      result = ''
      for i in f:
        if i.isalpha():
          if i.isupper():
            if ord(i) - k < 1040:
              result += chr(ord(i) - k + 32)
            else:
              result += chr(ord(i) - k)
          else:
            if ord(i) - k < 1072:
              result += chr(ord(i) - k + 32)
            else:
              result += chr(ord(i) - k)
        else:
          result += i
      return result

stroka = "Hawnj pk swhg xabkna ukq nqj."
print(cezar(stroka, False, True, 22))