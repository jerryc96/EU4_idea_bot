from DataBuilder import *
import time
import praw
import re
from fuzzywuzzy import fuzz
from ideaGroup.ideaGroup import ideaGroup
import mdFormatter as md
from culture.cultureLoader import *
from religion.religionLoader import *
import os

LIMIT_PER_COMMENT = 2
MAX_LIMIT = 4
TESTING_SUB = "testingground4bots"
PROD_SUB = "eu4"

countryTagLib = country_to_tag_library()
tagLib = gen_tag_library()
IdeaLib = gen_country_ideas_library()
nonNatIdeasLib = gen_non_national_ideas_library()
# shortcut for IdeaLib, so the program doesn't have to make a new ideaGroup object from scratch when one already exists.
IdeaGroupLib = {}


def bot_login():
    """Logs the bot into reddit through praw
    """
    print("SYSTEM: Logging in...")
    reddit = praw.Reddit(
        client_id=os.environ["client_id"],
        client_secret=os.environ["client_secret"],
        password=os.environ["password"],
        user_agent=os.environ["user_agent"],
        username=os.environ["username"],
    )
    print("SYSTEM: Logged in!")

    return reddit

def search_and_reply(reddit):
    '''
    look through the last 1000 comments for any query of national ideas: ex [[ prussia ]], then reply with the idea set
    '''
    print("SEARCH: Searching last 500 comments...")
    for comment in reddit.subreddit(PROD_SUB).comments(limit=500):
        if not comment.author == "EU4IdeaBot" and \
                is_request(comment.body) and not has_been_replied_to(str(comment.id)):
            reqs = re.findall(r"{(.*?)}", comment.body)

            if isinstance(reqs, list):
                numQueries = min(len(reqs), MAX_LIMIT)
                ind = 0
                step = min(LIMIT_PER_COMMENT, numQueries-ind)
                commentCurr = comment
                while ind < numQueries:
                    tmp = []
                    # make a search up the limit of queries per comment or the number of queries end
                    for i in range(ind, ind+step):
                        req = reqs[i]
                        print('SEARCH: Request for "' + req.strip() + '" received!')
                        try:
                            countryIdea = countrySearch(req)
                        except KeyError as e:
                            # PM to my account when a modifier isn't in the list
                            # change it so the bot recognizes previous comments and doesn't spam my inbox
                            comment.reply("u/EU4IdeaBot has encountered an error. \n" +
                                      "An error message with the details have been forwarded to the bot maintainer")
                            reddit.redditor('professormadlib').message('EU4IdeaBot Error', str(e))
                            return
                        tmp.append(format_to_comment(countryIdea))
                    # unifies tmp items inside a single reply
                    response = ""
                    for i in tmp:
                        response += i
                        response += "\n___\n"
                        response = comment_footer(response)
                    try:
                        # reply, then if there's any more countries that the user is searching for
                        # use the bot's previous reply as the new head, forming a comment chain.
                        commentCurr = commentCurr.reply(response)
                    except praw.exceptions.APIException as e:
                        print(e)
                        print("sleep for 10 minutes")
                        time.sleep(600)
                    ind += step
                    step = min(LIMIT_PER_COMMENT, numQueries - ind)
            # finish replying to one query comment
            print(f"finished replying to {comment.author}")
    print("finish reply")
    return


def has_been_replied_to(request_id):
    """Returns True if the comment with id request_id has already received a reply by the bot, False otherwise
    """
    request = reddit.comment(request_id)
    request.refresh()
    replies = request.replies.list()
    for r in replies:
        if r.author == "EU4IdeaBot" and str(r.parent()) == str(request_id):
            return True
    return False

def is_request(text):
    """Checks if text contains a valid request (entry inside braces '{ }')
    """
    return bool(re.search(r"[{][a-zA-Z0-9 '-+.]*[}]", text))

def countrySearch(name):
    '''
    find the closest match to the name is looking for.
    '''
    max = 0
    most_likely = ""
    # if the name is already a country tag, go directly to trigger based searching
    if is_tag(name):
        return trigger_search(name)
    # first, use fuzzy search to match the name with any country tag
    for country in countryTagLib:
        f = fuzz.ratio(country, name.lower())
        if f > max:
            max = f
            most_likely = country
    # then, use fuzzy search to match the name with any group national idea, generic or basic idea groups.
    for ideaset in nonNatIdeasLib:
        f = fuzz.ratio(ideaset, name.lower())
        if f > max:
            max = f
            most_likely = ideaset
    print(
        'SEARCH: Most likely: "' + most_likely + '", fuzz value = ' + str(max)
    )
    # if it's closest to a country name, start trigger Search to best match the idea set for that country
    if most_likely in countryTagLib:
        return trigger_search(countryTagLib[most_likely])
    # otherwise, it's not a country, and we can return an ideaGroup to reply.
    try:
        group = ideaGroup(most_likely, nonNatIdeasLib[most_likely])
        # IdeaGroupLib[most_likely] = group
        return group
    except KeyError as e:
        # key error will usually only happen if a modifier is missing from the modifier list, which means
        # I need to patch it in, as Custom ideas doesn't catch all of them.
        reddit.redditor('professormadlib').message('EU4IdeaBot Error', str(e))
        raise

def trigger_search(tag):
    '''
    mimic the way EU4 handles idea set triggers.

    first check if the tag satisfies any national idea triggers, then group idea triggers, finally default ideas if
    no triggers hit. Then beautify the idea name and return an IdeaGroup.
    '''
    country = tagLib[tag]
    nat_triggers = load_triggers(nationalTriggerPath)
    group_triggers = load_triggers(groupTriggerPath)
    # hit national ideas first to find a match
    for ideaName, trigger in nat_triggers.items():
        if trigger.evaluate(country):
            return ideaGroup(re.sub('_ideas', '', ideaName), IdeaLib[ideaName])
    # hit group idea sets next for a match
    for groupIdeaName, groupTrigger in group_triggers.items():
        if groupTrigger.evaluate(country):
            return ideaGroup(re.sub('_ideas', '', groupIdeaName), IdeaLib[groupIdeaName])
    # if nothing else hits, return generic ideas
    return ideaGroup('generic', nonNatIdeasLib['generic'])


def is_tag(name):
    '''
    check if the name is already a country tag, ie, PRU, TUR, BRA, etc.
    '''
    return name in tagLib


def format_to_comment(ideaSet):
    '''
    Given an ideaGroup and returns string with info formatted accordingly (using markdown syntax)
    '''
    response = ideaSet.to_comment()
    return response


def comment_footer(comment):
    comment += md.italic("This comment was made by u/EU4IdeaBot") + '. Please PM u/professormadlib for any questions \n'
    return comment

reddit = bot_login()

if __name__ == '__main__':
    while True:
        search_and_reply(reddit)
        print("SYSTEM: Sleeping for " + "5" + " seconds...")
        time.sleep(5)