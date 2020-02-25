def string_splosion(str):
  result = ''
  for i, _ in enumerate(str):
    result += str[:i + 1]
  return result
