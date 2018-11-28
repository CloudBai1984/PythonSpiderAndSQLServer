from datetime import datetime


global logFile
logFile = 'D:\\O\\Log\\'


def writeInfoLog(log):
    logInfoFile = logFile + "\\Information\\" + datetime.now().strftime('%Y%m%d') + ".log"
    file = open(logInfoFile,"a")
    log = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + ' - Information:' + log + '\r\n'
    file.writelines(log)
    file.close()

def writeErrorLog(log):
    
    logErrorFile = logFile + "\\Error\\" + datetime.now().strftime('%Y%m%d') + ".log"
    file = open(logErrorFile,"a")
    log = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + ' - Error:' + log + '\r\n'
    file.writelines(log)
    file.close()


if __name__ == '__main__':
    writeInfoLog("test")