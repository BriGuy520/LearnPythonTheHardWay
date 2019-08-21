mystuff_dict = { 'apple': "I AM APPLES!" }
print(mystuff_dict['apple'])


import mystuff

mystuff.apple()

print(mystuff.tangerine)


class MyStuff(object):

  def __init__(self):
    self.tangerine = "And now a thousand years between."
  
  def apple(self):
    print("I AM A CLASSY APPLE!")


thing = MyStuff()
thing.apple()
print(thing.tangerine)