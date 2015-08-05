def solution(pirates):

  def new_spoken(spoken, dummy=None):
    return spoken + [(pirates[spoken[-1]])] \
               if pirates[spoken[-1]] not in spoken \
               else spoken

  spoken = reduce(new_spoken, pirates, [0])

  return len(spoken) - spoken.index(pirates[spoken[-1]])
