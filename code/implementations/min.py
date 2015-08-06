solution=lambda p:(lambda s:len(s)-s.index(p[s[-1]]))(reduce(lambda s,d:s+[(p[s[-1]])] if p[s[-1]] not in s else s,p,[0]))

