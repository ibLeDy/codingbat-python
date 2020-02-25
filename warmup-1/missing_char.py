def missing_char(str, n):
  return "".join([v for i, v in enumerate(str) if i != n])
