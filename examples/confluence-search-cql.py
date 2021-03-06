# coding=utf-8
from atlassian import Confluence

"""This example shows how to use the cql
   More detail documentation located here https://developer.atlassian.com/server/confluence/advanced-searching-using-cql
"""

confluence = Confluence(url="http://localhost:8090", username="admin", password="admin")

WORD = "componentname"


def search_word(confluence, word):
    """
    Get all found pages with order by created date
    :param confluence:
    :param word:
    :return: json answer
    """
    cql = "siteSearch ~ {} order by created".format(word)
    answers = confluence.cql(cql)
    for answer in answers.get("results"):
        print(answer)


def search_word_in_space(confluence, space, word):
    """
    Get all found pages with order by created date
    :param confluence:
    :param space
    :param word:
    :return: json answer
    """
    cql = "space.key={} and (text ~ {})".format(space, word)
    answers = confluence.cql(cql, expand="space,body.view")
    for answer in answers.get("results"):
        print(answer)


if __name__ == "__main__":
    search_word(confluence=confluence, word=WORD)
    search_word_in_space(confluence=confluence, space="TST", word=WORD)
