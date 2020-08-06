def is_acceptable_password(string):
  str_ = string.lower()
  restr = "password"
  if restr in str_:
    return False
  if str_.isdigit() and len(str_) > 9:
    return True
  elif str_.isdigit():
    return False
  elif len(str_) > 9:
    return True
  for i in str_:
    if i.isdigit():
      if len(str_) > 6:
        return True
      else:
        return False
    else:
      continue
  return False



print(is_acceptable_password("Passwordsdfjsdkj7887"))
