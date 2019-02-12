# NewYorkerWebsiteScrapping
This is first official python project to scrap contributors of NewYorker magazine and their relevent information.

**Libraries** : urllib.request, BeautifulSoup, re, unidecode, reportlab.platypus, reportlab.lib.styles, json
**Primary file to execute** : parse.py

**Website Used to Scrap** : New Yorker

![alt text](https://www.bronxdefenders.org/wp-content/uploads/2013/05/The-New-Yorker-Logo-1.gif) The New Yorker is an American magazine featuring journalism, commentary, criticism, essays, fiction, satire, cartoons, and poetry. It is published by Condé Nast. Started as a weekly in 1925, the magazine is now published 47 times annually, with five of these issues covering two-week spans.Although its reviews and events listings often focus on the cultural life of New York City, The New Yorker has a wide audience outside New York and is read internationally. It is well known for its illustrated and often topical covers its commentaries on popular culture and eccentric Americana, its attention to modern fiction by the inclusion of short stories and literary reviews, its rigorous fact checking and copy editing, its journalism on politics and social issues, and its single-panel cartoons sprinkled throughout each issue.[1]

**#1 We traverse the https://www.newyorker.com/contributors for the list** 
 Scrap for all the contributors at New Yorker. So for find all the list items of class : Contributors__name___KjAyf and adding it in variable and getting all
 
![alt text](https://raw.githubusercontent.com/RajanLad/NewYorkerWebsiteScrapping/master/contributor_list_screen_shot.png )





**#2 We traverse the https://www.newyorker.com/contributors/joan-acocella (an instance) for their BIO** 
This will collect the bio of individual authors.
![alt text](https://raw.githubusercontent.com/RajanLad/NewYorkerWebsiteScrapping/master/contributor_bio_screen_shot.png)







**#3 We traverse the https://www.newyorker.com/contributors/joan-acocella (an instance) for approx number of articles they have written** 
 This will collect the no of articles written by individual authors
![alt text](https://raw.githubusercontent.com/RajanLad/NewYorkerWebsiteScrapping/master/no_of_articles_screenshot.png)






**#4 We now write the information collected from previous steps and write in JSON file(data.json) and generate a PDF Report (NewYorkerReport.pdf)** 
Info we write in files are 
>Contributor's name
>Contributor's Website link
>Contributor's Bio
>Contributor's written articles count

** Eg. **
 
**https://github.com/RajanLad/NewYorkerWebsiteScrapping/blob/master/NewYorkerReport.pdf**
**https://github.com/RajanLad/NewYorkerWebsiteScrapping/blob/master/data.json**


Sources : [1] https://en.wikipedia.org/wiki/The_New_Yorker
