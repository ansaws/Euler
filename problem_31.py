"""t = 0
onep = 0
twop= 0
fivep=0
tenp = 0
twentp = 0
oneE = 0

for onep in range(0, 201):
  if onep+twop+fivep+tenp+twentp+oneE ==200:
    t+=1
    break
  elif onep+twop+fivep+tenp+twentp+oneE>200:
    break
  else:
    for twop in range(0,201,2):
      if onep+twop+fivep+tenp+twentp+oneE ==200:
        t+=1
        break
      elif onep+twop+fivep+tenp+twentp+oneE>200:
        break
      else:
        for fivep in range(0, 201,5):
          if onep+twop+fivep+tenp+twentp+oneE ==200:
            t+=1
            break
          elif onep+twop+fivep+tenp+twentp+oneE>200:
            continue
          else:
            for tenp in range(0,201,10):
              if onep+twop+fivep+tenp+twentp+oneE ==200:
                t+=1
                break
              elif onep+twop+fivep+tenp+twentp+oneE >200:
                break
              else:
                for twentp in range(0,201,20):
                  if onep+twop+fivep+tenp+twentp+oneE ==200:
                    t+=1
                    break
                  elif onep+twop+fivep+tenp+twentp+oneE >200:
                    break
                  else:
                    for oneE in range(0, 201,100):
                      if onep+twop+fivep+tenp+twentp+oneE ==200:
                        t+=1
                        break
                      if onep+twop+fivep+tenp+twentp+oneE>200:
                        break
print(t+1)"""


