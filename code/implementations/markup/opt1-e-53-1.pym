def solution(pirates):

  spoken = [0]


  for i in pirates:

    if pirates[spoken[-1]] not in spoken:
      spoken.append(pirates[spoken[-1]])

    else:
      return len(spoken) - spoken.index(pirates[spoken[-1]])
