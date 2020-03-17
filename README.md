# is_this_journal_predatory
Check whether a journal is predatory from within Python.


# example:
import is_this_journal_predatory 


journalURL = "http://www.academeresearchjournals.org/"

is_this_journal_predatory.is_predatory(journalURL)      #outputs message about whether the input URL is predatory
