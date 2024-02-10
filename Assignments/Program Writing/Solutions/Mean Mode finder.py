def stats_finder(array):
  # Write your code here
  modedict = {}
  outputlst = [sum(array)/len(array)]
  for val in array:
    if val in modedict:
      modedict[val]+= 1
    else:
      modedict[val] = 1
  modes = []
  for valcounts in modedict:
    if modedict[valcounts] == max(modedict.values()):
      modes.append(valcounts)
  outputlst.append(min(modes))
  return outputlst

print(stats_finder([500, 400, 400, 375, 300, 350, 325, 300]))