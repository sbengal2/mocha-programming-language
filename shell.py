import mocha

while True:
    text = input('mocha > ')
    result,error = mocha.run('<stdin>',text)

    if error: print(error.as_string())
    else: print(result)