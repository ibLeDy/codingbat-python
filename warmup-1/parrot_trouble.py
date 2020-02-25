def parrot_trouble(talking, hour):
  trouble = False
  if talking is True:
    if hour < 7:
      trouble = True
    elif hour > 20:
      trouble = True

  return trouble