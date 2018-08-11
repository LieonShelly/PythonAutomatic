import random

'''
创建 35 份不同的测验试卷。
为每份试卷创建 50 个多重选择题，次序随机。
为每个问题提供一个正确答案和 3 个随机的错误答案，次序随机。
将测验试卷写到 35 个文本文件中。
将答案写到 35 个文本文件中。
这意味着代码需要做下面的事: 将州和它们的首府保存在一个字典中。 针对测验文本文件和答案文本文件，调用 open()、write()和 close()。 利用 random.shuffle()随机调整问题和多重选项的次序
'''
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
            'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for quizNnum in range(35):
    quzeFile = open('captitalsquiz%s.txt' % (quizNnum + 1), 'w')
    anserKeyFile = open('capitalsquize_answers%s.txt' % (quizNnum + 1), 'w')
    # writer a header for the quiz
    quzeFile.write('Name:\n\n Date:\n\n Period:\n\n')
    quzeFile.write((' ' * 20) + 'State Capitals Quiz (From %s)' % (quizNnum + 1))
    quzeFile.write('\n\n')

    #shuffle the order of the state
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnsers = list(capitals.values())
        del wrongAnsers[wrongAnsers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnsers, 3)
        answeroptions = wrongAnswers + [correctAnswer]
        random.shuffle(answeroptions)

        quzeFile.write('%s. What is the captial of %s?\n' % (questionNum + 1, states[questionNum]))

        for i in range(4):
            quzeFile.write('%s. %s\n' % ('ABCD'[i], answeroptions[i]))
            anserKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answeroptions.index(correctAnswer)]))
        quzeFile.write('\n')
    quzeFile.close()
    anserKeyFile.close()