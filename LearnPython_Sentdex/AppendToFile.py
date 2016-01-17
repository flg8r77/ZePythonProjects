__author__ = 'flg8r77'

StuffToAppend = '\nThis is the new line of text added to an existing file'

TargetFile = open('Output.txt', 'a')
TargetFile.write(StuffToAppend)
TargetFile.close()
