"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ["what", "does", "this", "line", "do", "?"]
# I think this will print "word"
for word in some_words:
    print(word) # it printed every value in the list one by one
# I think this will print everything in the list
for x in some_words:
    print(x)    # it printed every value in the list one by one
# I think this will print every words in the list except the question mark
print(some_words)   # it prints ['what', 'does', 'this', 'line', 'do', '?']
# I think this will print some_words contains more than 3 words
if len(some_words) > 3:     #it prints "some_words contains more than 3 words" because the length of (some_words)is greater than 3
    print("some_words contains more than 3 words")  #it prints "some_words contains more than 3 words"

# I think this will print a namedtuple containing six attributes
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) # it prints uname_result(system='Windows', node='MSI', release='10', version='10.0.19045', machine='AMD64')


usefulFunction()
