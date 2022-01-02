def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
with open('Quiz.txt', "r") as qs:
    qs = qs.read()
    qs = qs.split(',')
    quiz = Convert(qs)
'''for i in quiz.keys():
 print(i,'\n',j+1)'''
'''with open('Exp.txt','w') as exp:
    exp.write('Hello')'''
i=0
for qno in quiz:
    with open('q%s.txt' % (i+1), 'w') as qf:
        qf.write('Qno %s)\n' % (i+1))
        qf.write(str(qno))
    with open('a%s.txt' % (i+1), 'w') as af:
        af.write(str(quiz[qno]))
    i+=1