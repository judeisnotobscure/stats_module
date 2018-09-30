#! /usr/bin/env python3

def mean_(list):
    """Used for finding the mean of a list
    Usage: mean_(list)

    list = any list of decimal numbers which are non text"""
    list_sum = 0
    try:
        for i in list:
            list_sum += int(i)
            return list_sum / len(list)
    except (TypeError, ValueError, ZeroDivisionError):
        print("""Used for finding the mean of a list
    Usage: mean_(list)
    
    list = any list of decimal numbers which are non text""")


def variance(list) :
    """this function returns the variance of a list which is the total population of a data set
    this function uses the funtoin mean()
    Usage: variance(list)
    
    list = any list of decimal numbers which are non text"""
    try:
        variance_list = 0
        for i in list:
            variance_list += (int(i) - mean_(list)) ** 2

        variance = variance_list / len(list)
        return variance
    except(ValueError, ZeroDivisionError, TypeError):
        print("""this function returns the variance of a list which is the total population of a data set
    this function uses the funtoin mean()
    Usage: variance(list)
    
    list = any list of decimal numbers which are non text""")


def sd(list):
    """This function returns the Standard deviation of a list
    Usage: sd(list)
    args:
    list = any list of decimal numbers which are non text"""
    try:
        standard_deviation = variance(list)**(1/2)
        return standard_deviation
    except(TypeError, ValueError, ZeroDivisionError):
        print("""This function returns the Standard deviation of a list
    Usage: sd(list)
    args:
    list = any list of decimal numbers which are non text""")

def factorial(n):
    """This is a recursive factorial function
    Usage: factorial(n)
    
    args:
    n = any positive number"""
    try:
        if n < 1:
            return 1
        else:
            n = n * factorial(n - 1)
            return n
    except(TypeError, ValueError):
        print("""This is a recursive factorial function
    Usage: factorial(n)
    
    args:
    n = any positive number""")

def choose(n, k):
    """This is a binomial coeficient nCk used in binomial probablilty
    this funtion uses factorial()
    Usage: choose(n, k)
    
    args:
    n = total number
    k = total number of sub-groups """
    try:
        return factorial(n)/(factorial(k) * factorial(n - k))
    except(ValueError, ZeroDivisionError, TypeError):
        print("""This is a binomial coeficient nCk used in binomial probablilty
    this funtion uses factorial()
    Usage: choose(n, k)
    
    args:
    n = total number
    k = total number of sub-groups """)


def bi_rand():
    """P(k successes in n attempts) = (nCk) p**k(1 − p)**(n−k)
    this function uses choses()
    Usage: bi_rand()

    Follow prompts for input for total attmpts/successes/%success in decimal"""
    try:
        total_attempts = int(input("what are the total attempts? "))
        total_success = int(input("What are the total succeses?"))
        p_success = float(input("What is the % likely of a success in decimal?"))
        return choose(total_attempts, total_success) * p_success ** total_success * (1-p_success)**(total_attempts-total_success)
    except(ValueError, TypeError):
        print( """P(k successes in n attempts) = (nCk) p**k(1 − p)**(n−k)
    this function uses choses()
    Usage: bi_rand()

    Follow prompts for input for total attmpts/successes/%success in decimal""")

def at_least(n, range):
    """This Function calculates multiple bi_rand() calls for fins at least % binomial random variables
    where n is the low and k is the high of your range of values to calculate
    Usage: at_least(n, range)
    
    args:
    n = low end of range
    range = range of values to calculate for"""
    try:
        p_success = float(input("What is the % likely of a success in decimal?")) 
        tally = []
        for i in range:
            tally.append(float(choose(n, i) * p_success ** i * (1-p_success)**(n-i)))
            print(tally)
        print(str(mean_(int(tally))))
    except(ValueError, TypeError):
        print("""This Function calculates multiple bi_rand() calls for fins at least % binomial random variables
    where n is the low and k is the high of your range of values to calculate
    Usage: at_least(n, range)
    
    args:
    n = low end of range
    range = range of values to calculate for""")

def bernoulli_variance(probablilty):
    """ This Function calculates bernoulli variance
    usage: bernoulli_variance(probability)

    probability = probability in decimal form.  ie... (0.1) for 10%"""
    try:
        variaace = probablilty*(1-probablilty)
        return variance
    except(ValueError, TypeError):
        print(""" This Function calculates bernoulli variance
    usage: bernoulli_variance(probability)

    probability = probability in decimal form.  ie... (0.1) for 10%""")


def geometric_rand_prob(probability, on_try, lessthan= False):
    """This funtion returns probablity of geometric random variables

    Usage:  geometric_rand_prob(probability, on_try, lessthan= optional

     args:
     probablity = probability of a success in decimal
     on_try = on which attempt to calculate for
     lessthan = (optional) if false calculates single number success: if True calculates less than or equal to on_try"""
    try:
        if lessthan == False:
            p = probability * (1 - probability) ** (on_try - 1)
            return p
        elif lessthan:
            p = 0
            for i in range(1, on_try + 1):
                p += probability * (1 - probability) ** (i - 1)
                print(probability * (1 - probability) ** (i - 1))
        return p
    except (ValueError, TypeError):
        print( """This funtion returns probablity of geometric random variables
        Usage:  geometric_rand_prob(probability, on_try, lessthan= optional)
        
     args:
     probablity = probability of a success in decimal
     on_try = on which attempt to calculate for
     lessthan = (optional) if false calculates single number success: if True calculates less than or equal to on_try""")

def mean_geometric_rand(probability):

    """This function returns the mean of a geometric probability

    Usage: mean_geometric_rand(probability)

    probability = probability of event occurring in decimal form ie. 0.7 for 70%"""
    try:
        mean = 1/probability
        return mean
    except (ValueError, ZeroDivisionError, TypeError):
        print(  """This function returns the mean of a geometric probability
    
    Usage: mean_geometric_rand(probability)
    
    probability = probability of event occurring in decimal form ie. 0.7 for 70%""")


def geometric_rand_variance(probability):
    """This function returns the Variance of random Geometric probability

    Usage: geometric_rand_variance(probability)

     probability = probability of event occurring in decimal form ie. 0.7 for 70%"""
    try:
        variance = (1-probability)/(probability ** 2)
        return variance
    except (ZeroDivisionError, TypeError, ValueError):
        print( """This function returns the Variance of random Geometric probability
    
    Usage: geometric_rand_variance(probability)
     
     probability = probability of event occurring in decimal form ie. 0.7 for 70%""")

if __name__ == "__main__":
    list = [66,67,67,68,68,68,68,69,69,69,69,70,70,71,71,72,73,75]

    print(mean_(list))
    print(variance(list))
    print(sd(list))
    print(factorial(4.2))
    print(choose(30,5))
    print(bi_rand())
    print(geometric_rand_prob(0.35, 3))