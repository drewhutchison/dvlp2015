def solution(pirates):

  spoken = [0]

  for i in pirates:

    spoken = spoken + [(pirates[spoken[-1]])] \
               if pirates[spoken[-1]] not in spoken \
               else spoken

  return len(spoken) - spoken.index(pirates[spoken[-1]])
