def solution(pirates):

  spoken = reduce(lambda spoken, dummy: (
                    spoken + [pirates[spoken[-1]]]
                    if pirates[spoken[-1]] not in spoken
                    else spoken),
                  pirates,
                  [0]
                 )

  return len(spoken) - spoken.index(pirates[spoken[-1]])
