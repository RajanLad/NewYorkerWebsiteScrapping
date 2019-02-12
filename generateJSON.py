import json

# Push it to JSON

def generateJSONFile( contributors, var_for_no_hold_articles_phrase, contributors_links, contributor_description):
    # a Python object (dict):
    result=[]
    for i in range(0,len(contributors)):
        print("Forming JSON for " + str(i) + " out of " + str(len(contributors)))
        x= {
          'Contributor_name': str(contributors[i]),
          'Contributors_no_of_articles': str(var_for_no_hold_articles_phrase[i]),
          'Contributors_link':str(contributors_links[i]),
          'Contributors_description': str(contributor_description[i])
        }
        result.append(x)

    # convert into JSON:
    y = json.dumps(result)
    print(y)

    # push the json on to the JSON file
    with open('data.json', 'w') as outfile:
        json.dump(result, outfile, ensure_ascii=False, indent=4)

    return