import is_this_journal_predatory

def test_check_predatory():
    predatory_checker = is_this_journal_predatory.PredatoryInfo()
    returned_message = predatory_checker.is_predatory("Academic Journals")
    expected_message = "The journal Academic Journals at http://www.academicjournals.org/ is listed as a predatory journal in Beall's List."
    assert returned_message == expected_message
