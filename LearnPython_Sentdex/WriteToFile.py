__author__ = 'flg8r77'

TextToWrite = 'Today is a good day to start learning programming!\nThis is another line'

TargetFile = open('Output.txt', 'w')
TargetFile.write(TextToWrite)
TargetFile.close()
