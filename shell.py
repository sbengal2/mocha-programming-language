import mocha

while True:
    text = input('mocha > ')
    result,error = mocha.run('No File Name',text)

    if error: print(error.as_string())
    else: print(result)