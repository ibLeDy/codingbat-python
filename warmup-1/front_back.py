def front_back(s):
  if len(s) > 1:
    string = [s[-1]]
    string.extend([i for i in s[1:-1]])
    string.append(s[0])
    return "".join(string)
  else:
    return s