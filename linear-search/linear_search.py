def linear_search(lst, to_find):
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
  for i in range(0,len(lst)):
    if(lst[i] == to_find):
      print(i)
    else:
      print(-1)