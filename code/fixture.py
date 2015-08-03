from sys import argv, exit
import json
import imp


def usage():
    print 'usage: {} <solution> [case]'.format(argv[0])
    exit(-1)

if len(argv) < 2 or len(argv) > 3:
    usage()

fn = argv[1]
n = int(argv[2]) if len(argv) == 3 else None

solution = imp.load_module(
    fn, *imp.find_module(
        fn, ['implementations']
    )).solution

with open('cases.json') as casesfile:
    cases = json.load(casesfile)


def try_case(i):

    print '-' * 80
    print 'trying case {}'.format(i)
    print

    case = cases[i]
    pirates = case['pirates']
    answer = case['answer']
    myanswer = solution(pirates)

    print
    print 'my answer: {}. correct answer: {}'.format(
        myanswer,
        answer
    )
    print

print
for i in [n] if n is not None else range(len(cases)):
    try_case(i)
