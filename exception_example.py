
def giveMeException():
    raise IndexError('I am the exception')


try:
    print('test')
    giveMeException()

except IndexError as ex:
    print(str(ex))

except Exception as ex:
    print(str(ex))

else:
    print('no exceptions raised')

finally:
    print('i am executed either way just there might be an exception')
