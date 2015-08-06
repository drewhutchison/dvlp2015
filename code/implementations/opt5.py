solution = lambda pirates: \
  (lambda spoken: len(spoken) - spoken.index(pirates[spoken[-1]])
  )(reduce(lambda spoken, dummy: spoken + [(pirates[spoken[-1]])] \
                   if pirates[spoken[-1]] not in spoken \
                   else spoken,
                  pirates, [0]))
