import csv

with open('E:\Sheppey Is Ours Website\AbbieGorlovWebster.github.io\Events.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    next(csv_reader)

    for row in csv_reader:
        print("\t<div class=\"hl Width80\"></div>\n")
        
        print("\t<div class=\"Event Width80\">")
        print("\t\t<div class=\"FlexRow\">")
        print("\t\t\t<div class=\"TextContainer\" id=\"Date\">")
        print("\t\t\t\t<p class=\"TextCenter BlackText Weight700 Size24 TextLeft\">", row[1], "</p>", sep="")
        print("\t\t\t</div>\n")
        
        print("\t\t\t<div class=\"TextContainer\" id=\"Details\">")
        print("\t\t\t\t<h2 class=\"TextCenter BlackText Weight700 Size24 TextLeft\">", row[0], "</h2>", sep="")
        print("\t\t\t\t<input type=\"checkbox\" id=\"EventToggle",line_count,"\" /> <label for=\"EventToggle",line_count,"\" class=\"EventToggleLabel Weight700\">Event Details</label>", sep="")
        print("\t\t\t\t<div class=\"ExpandableDetails\">")
        print("\t\t\t\t\t<p class=\"TextCenter BlackText Weight400 Size18 TextLeft\">",row[5],"</p>",sep="")
        print("\t\t\t\t</div>")
        print("\t\t\t</div>\n")
        
        print("\t\t\t<div class=\"TextContainer\" id=\"Time\">")
        print("\t\t\t\t<p class=\"TextCenter BlackText Weight700 Size24 TextRight\">",row[2],"</p>",sep="")
        print("\t\t\t\t<p class=\"TextCenter BlackText Weight400 Size18 TextRight\">",row[3],"<br>",row[4],"</p>",sep="")
        print("\t\t\t</div>")
        print("\t\t</div>")
        print("\t</div>\n")
        
        line_count += 1

print("\t<div class=\"hl Width80\"></div>")