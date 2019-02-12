from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def createPDFReport( contributors, var_for_no_hold_articles_phrase, contributors_links, contributor_description):

    # Create a doc
    sample_style_sheet = getSampleStyleSheet()
    flowables = []
    my_doc = SimpleDocTemplate('NewYorkerReport.pdf')

    # if you want to see all the sample styles, this prints them
    sample_style_sheet.list()

    paragraph_0_1 = Paragraph("New Yorker", sample_style_sheet['Heading1'])
    paragraph_0_2 = Paragraph("The New Yorker is an American magazine featuring journalism, commentary, criticism, essays, fiction, satire, cartoons, and poetry. It is published by Condé Nast. Started as a weekly in 1925, the magazine is now published 47 times annually, with five of these issues covering two-week spans.Although its reviews and events listings often focus on the cultural life of New York City, The New Yorker has a wide audience outside New York and is read internationally. It is well known for its illustrated and often topical covers its commentaries on popular culture and eccentric Americana, its attention to modern fiction by the inclusion of short stories and literary reviews, its rigorous fact checking and copy editing, its journalism on politics and social issues, and its single-panel cartoons sprinkled throughout each issue. ", sample_style_sheet['Heading4'])
    paragraph_0_3 = Paragraph("The New Yorker est un magazine américain présentant des articles de journalisme, commentaires, critiques, essais, fiction, satire, dessins animés et poésie. Il est publié par Condé Nast. Lancé comme hebdomadaire en 1925, le magazine est désormais publié 47 fois par an, dont cinq numéros couvrent une période de deux semaines. Bien que ses critiques et ses événements soient souvent consacrés à la vie culturelle de la ville de New York, le New Yorker a public en dehors de New York et est lu à l'international. Il est bien connu pour ses couvertures illustrées et souvent d'actualité, ses commentaires sur la culture populaire et l'americana excentrique, son intérêt pour la fiction moderne par l'inclusion de nouvelles et de critiques littéraires, sa vérification rigoureuse des faits et sa révision, son journalisme politique et social. numéros, et ses caricatures à panneau unique parsèment chaque numéro.", sample_style_sheet['Heading4'])
    paragraph_0_4 = Paragraph("There are "+ str(len(contributors)) + " contributors at New Yorker", sample_style_sheet['Heading4'])
    paragraph_0_5 = Paragraph("----------------------------------------------------------------------------------------------------------------------------------", sample_style_sheet['Heading4'])

    flowables.append(paragraph_0_1)
    flowables.append(paragraph_0_2)
    flowables.append(paragraph_0_3)
    flowables.append(paragraph_0_4)
    flowables.append(paragraph_0_5)

    for i in range(0,len(contributors)):

        print("Generating report for " + str(i) + " out of " + str(len(contributors)))

        paragraph_1 = Paragraph(str(contributors[i]), sample_style_sheet['Heading1'])

        paragraph_2 = Paragraph(
            str(var_for_no_hold_articles_phrase[i]),
            sample_style_sheet['Heading4']
        )

        paragraph_3 = Paragraph(
            str(contributors_links[i]),
            sample_style_sheet['Heading4']
        )

        paragraph_4 = Paragraph(
            str(contributor_description[i]),
            sample_style_sheet['Heading6']
        )

        paragraph_5 = Paragraph(
            str(" "),
            sample_style_sheet['Heading4']
        )

        flowables.append(paragraph_1)
        flowables.append(paragraph_2)
        flowables.append(paragraph_3)
        flowables.append(paragraph_4)
        flowables.append(paragraph_5)

    my_doc.build(flowables)

    return