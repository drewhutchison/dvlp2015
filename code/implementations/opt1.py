def solution(pirates):

  spoken = [0] # pirates we've spoken to
  current_pirate = pirates[0] # pirate we're presently speaking to

  for i in pirates:

    if current_pirate not in spoken:
      # we haven't talked to current_pirate yet
      spoken.append(current_pirate)
      current_pirate = pirates[current_pirate]
    else:
      # otherwise we're done
      return len(spoken) - spoken.index(current_pirate)
