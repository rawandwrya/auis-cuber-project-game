def question_response (q,a,b):

  while (True):
      user_response = input(q).lower()
      if user_response==a or user_response ==b:
         break
      else:
        print("Please make sure to enter an acceptable rsponse")
  return user_response