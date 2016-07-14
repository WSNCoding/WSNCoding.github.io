from subprocess import PIPE, Popen
import time
def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

resultspath = "results"
print("Batch Command Line\nA WSNC project | Coded by TheM1n3r63")
outfile = open(resultspath+".txt",'a')
outfile.write("\n===\nSESSION STARTED: "+time.strftime("%d-%m-%Y %H:%M:%S"+'\n===\n'))
outfile.close()
while True:
    commandtorun = input("Input command to run: ")
    if commandtorun == "" :
        print("No command given")
    elif commandtorun.lower() == 'exit':
        break
    elif commandtorun.lower() == 'set output':
        resultspath = input('Set output file name: ')
        if resultspath[-4:] == '.txt':
            resultspath = resultspath[:-4]
    elif commandtorun.lower() == 'info':
        print('SYNTAX:\nSET OUTPUT   Change output file of command history.\nEXIT   Exit this terminal.\nHELP   Batch syntax help.\nINFO Get this information.\n\nLICENSE AND OWNERSHIP:\nThis project is under no license and is open for modification at will.\nSource code can be found on https://wsncoding.github.io/.\nA WSNC project | Coded by TheM1N3R63')
    else:
        result = cmdline(commandtorun).decode("utf-8")
        print(result)
        outfile = open(resultspath+".txt",'a')
        if result != '':
            outfile.write('\n===\nCommand run at: '+time.strftime("%d-%m-%Y %H:%M:%S")+'\nCommand run: '+commandtorun.upper()+'\n===\n')
            outfile.write(result)
            outfile.close()
        else:
            print('Command not recognised.')
outfile = open(resultspath+".txt",'a')
outfile.write("\n===\nSESSION TERMINATED: "+time.strftime("%d-%m-%Y %H:%M:%S")+'\n===\n')
outfile.close()
