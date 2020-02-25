def array123(nums):
  string = ''.join([str(i) for i in nums])
  if '123' in string:
    return True
  return False