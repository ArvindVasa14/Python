def score_sorter(array, top_score):
  # Write your code here
  outputlst = []
  while len(array)>0:
    temp = float('inf')
    highest = 0
    for item in range(len(array)):
      if top - array[item] < temp:
        temp = top-array[item]
        highest = array[item]
    outputlst.append(highest)
    array.remove(highest)
  return outputlst
    

score_list = [1, 2, 3, 9999, 13]
top = 10000

print(score_sorter(score_list, top))