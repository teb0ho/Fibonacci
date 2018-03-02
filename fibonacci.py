def fib(n):
    
    a, b = 0, 1
    final_output = str(a) + ' ' + str(b)

    if n == 2:
        return final_output
    elif n == 1:
        return '0'
    else:
        count = 2
        while (count < n):
            if count < n:
                a = a + b
                final_output += ' ' + str(a)
                count += 1
            if count < n:
                b = a + b
                final_output += ' ' + str(b)
                count += 1

        return final_output

print "Enter the length you want for your Fibonacci sequence "
fib_length = int(raw_input('> '))
print fib(fib_length)
