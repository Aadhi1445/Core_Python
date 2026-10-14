# with open('data.txt','w') as f:
#     f.write('My  hi name is G.Aditya\n')
#     f.write("I'm 22 year's Old\n")
#     f.write("At current I'm taking course of Python Full stack Development\n")
#     f.write("I have Completed 4 months \n")
#     f.write("I am Learnt hi hi hi  Python,SQL,HTML,CSS \n")
#     f.write("I am currently Learning DSA\n")
#     f.write("I am Good at Communication\n")
#     f.write('I can say self-introduction   hi hi\n')
#
# with open('data.txt','r') as o,open('chunk.txt','w') as c:
#     ct=0
#     for line in o:
#         # print(line)
#         ct+=1
#         line=line.replace('\n','')
#         if ct==2:
#             c.write(f"{line}{p_line}\n")
#             c.flush()
#             ct=0
#         else:
#             p_line=line

def ask_question(question):
    max_score=0
    mrc=""
    with open('chunk.txt', 'r') as file:
        for word in question.split():
            score=0
            for chunk in file:
                if word.lower() in chunk.lower():
                    score+=1
            if score>max_score:
                max_score=score
                mrc=chunk
        # for chunk in file:
        #     score=0
        #     for word in question.split():
        #         if word.lower() in chunk.lower():
        #             score+=1
        #     if score>max_score:
        #         max_score=score
        #         mrc=chunk
    print(mrc)
ask_question(input("What is your question ?: "))


