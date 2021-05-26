###global scope
testMode = True
def someFunction():
    global testMode
    testMode = False
    print(testMode)
someFunction()
print(testMode)
