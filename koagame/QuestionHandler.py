def question_response (q,a,b):
    """
    the function will return either choice a or b

    Arguments:
    q: the question string
    a: choice a string
    b: choice b string
    """
    
    while (True):
        user_response = input(q).lower()
        if user_response==a or user_response ==b:
            break
        else:
            print("Please make sure to enter an acceptable rsponse")
    return user_response



