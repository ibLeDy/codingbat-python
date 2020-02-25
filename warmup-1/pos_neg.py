def pos_neg(a, b, negative):
  if negative is True:
    if abs(a) != a and abs(b) != b:
      return True
  else:
    if abs(a) != a and abs(b) == b or abs(a) == a and abs(b) != b:
      return True
  return False
