import logging

# create logger
lgr = logging.getLogger('Time taken')
lgr.setLevel(logging.DEBUG) # log all escalated at and above DEBUG
# add a file handler
fh = logging.FileHandler('Time_taken.csv')
fh.setLevel(logging.DEBUG) # ensure all messages are logged to file

# create a formatter and set the formatter for the handler.
frmt = logging.Formatter('%(name)s : %(message)s s')
fh.setFormatter(frmt)

# add the Handler to the logger
lgr.addHandler(fh)

# You can now start issuing logging statements in your code

lgr.info('an info message')
