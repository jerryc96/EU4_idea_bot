from DataBuilder import *
import time
import praw
import re
from fuzzywuzzy import fuzz
from ideaGroup.ideaGroup import ideaGroup
import mdFormatter as md
import os

tagLib = gen_tag_library()
IdeaLib = gen_country_ideas_library(tagLib)
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
    print("SEARCH: Searching last 1,000 comments...")
    for comment in reddit.subreddit("eu4").comments(limit=1000):
        if not comment.author == "EU4IdeaBot" and \
                is_request(comment.body) and not has_been_replied_to(str(comment.id)):
            reqs = re.findall(r"{(.*?)}", comment.body)
            
            if isinstance(reqs, list):
                print(reqs)
                tmp = []
                for req in reqs:
                    print('SEARCH: Request for "' + req.strip() + '" received!')
                    try:
                        countryIdea = fuzzySearch(req)
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
                    comment.reply(response)
                except praw.exceptions.APIException as e:
                    print(e)
                    print("reached comment limit, sleep for 10 minutes")
                    time.sleep(600)
            else:
                print('SEARCH: Request for "' + reqs.strip() + '" received!')
                countryIdea = fuzzySearch(reqs)
                if not isinstance(countryIdea, ideaGroup):
                    # error will show which modifier is missing
                    response = str(countryIdea)
                else:
                    response = format_to_comment(countryIdea)
                    response = comment_footer(response)
                try:
                    comment.reply(response)
                except praw.exceptions.APIException as e:
                    print(e)
                    print("reached comment limit, sleep for 10 minutes")
                    time.sleep(600)
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

def fuzzySearch(name):
    '''
    use fuzzy search, find the closest match to the name is looking for.
    '''
    max = 0
    most_likely = ""
    for ideaset in IdeaLib:
        f = fuzz.ratio(ideaset, name)
        if f > max:
            max = f
            most_likely = ideaset

    print(
        'SEARCH: Most likely: "' + most_likely + '", fuzz value = ' + str(max)
    )
    # if most_likely in IdeaGroupLib:
    #     return IdeaGroupLib[most_likely]
    try:
        group = ideaGroup(most_likely, IdeaLib[most_likely])
        # IdeaGroupLib[most_likely] = group
        return group
    except KeyError as e:
        # key error will usually only happen if a modifier is missing from the modifier list, which means
        # I need to patch it in, as Custom ideas doesn't catch all of them.
        reddit.redditor('professormadlib').message('EU4IdeaBot Error', str(e))
        raise

def format_to_comment(ideaSet):
    '''
    Given an ideaGroup and returns string with info formatted accordingly (using markdown syntax)
    '''
    response = ideaSet.to_comment()
    return response

def comment_footer(comment):
    comment += md.italic("This comment was made by u/EU4IdeaBot") + '\n \n'
    comment += "Please PM u/professormadlib for any questions, as well as any tips to improve the bot. \n \n"
    comment += md.bold("Help is always welcome!")
    return comment

reddit = bot_login()

if __name__ == '__main__':
    while True:
        search_and_reply(reddit)
        print("SYSTEM: Sleeping for " + "10" + " seconds...")
        time.sleep(10)