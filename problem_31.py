count = 0
for onep in range(0, 201,100):
  if onep ==200:
    count+=1
    break
  if onep >200:
    break
  for twop in range(0,201,50):
    if onep+twop ==200:
      count+=1
      break
    if onep+twop>200:
      break
    for fivep in range(0, 201,20):
      if onep+twop+fivep==200:
        count+=1
        break
      if onep+twop+fivep >200:
        break
      for tenp in range(0,201,10):
        if onep+twop+fivep+tenp ==200:
          count+=1
          break
        if onep+twop+fivep+tenp >200:
          break
        for twentp in range(0,201,5):
          if onep+twop+fivep+tenp+twentp ==200:
            count+=1
            break
          if onep+twop+fivep+tenp+twentp >200:
            break
          for oneE in range(0, 201,2):
            if onep+twop+fivep+tenp+twentp+oneE ==200:
              count+=1
              break
            if onep+twop+fivep+tenp+twentp+oneE >200:
              break
            for yeet in range(0, 201,1):            
              if onep+twop+fivep+tenp+twentp+oneE +yeet ==200:
                count+=1
                break
              if onep+twop+fivep+tenp+twentp+oneE +yeet >200:
                break
print(count+1)




