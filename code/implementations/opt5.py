solution = lambda pirates: \
  len(reduce(lambda spoken, dummy: spoken + [(pirates[spoken[-1]])] \
                   if pirates[spoken[-1]] not in spoken \
                   else spoken,
                   pirates, [0])) - (
    reduce(lambda spoken, dummy: spoken + [(pirates[spoken[-1]])] \
      if pirates[spoken[-1]] not in spoken \
      else spoken,
      pirates, [0])).index(pirates[reduce(lambda spoken, dummy: \
        spoken + [(pirates[spoken[-1]])] \
                   if pirates[spoken[-1]] not in spoken \
                   else spoken,
                  pirates, [0]) [-1]])
