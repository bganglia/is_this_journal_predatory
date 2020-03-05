import setuptools

setuptools.setup(
    name="is_this_journal_predatory",
    version="0.0.1",
    author="bganglia",
    author_email="bganglia892@gmail.com",
    description="Check whether a journal is listed in Beall's List from within Python.",
    long_description="",
    long_description_content_type="text/markdown",
    data_files=[("is_this_journal_predatory",["is_this_journal_predatory/predatory_journals.json"])],
    url="https://github.com/bganglia/is_this_journal_predatory/blob/master/check_predatory.py",
    packages=setuptools.find_packages(),
    classifiers=[], #fill in
    python_requires=">=3.6"
)
