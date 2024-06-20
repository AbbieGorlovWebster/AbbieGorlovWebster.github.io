import csv

with open('E:\Sheppey Is Ours Website\AbbieGorlovWebster.github.io\Events.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    next(csv_reader)

    with open('E:\Sheppey Is Ours Website\AbbieGorlovWebster.github.io\Events Output.txt', 'w') as f:
        
        for row in csv_reader:
            print("\t<div class=\"hl Width80\"></div>\n", file=f)
            
            print("\t<div class=\"Event Width80\">", file=f)
            print("\t\t<div class=\"FlexRow\">", file=f)
            print("\t\t\t<div class=\"TextContainer\" id=\"Date\">", file=f)
            print("\t\t\t\t<p class=\"TextCenter BlackText Weight700 Size24 TextLeft\">", row[1], "</p>", sep="", file=f)
            print("\t\t\t</div>\n", file=f)
            
            print("\t\t\t<div class=\"TextContainer\" id=\"Details\">", file=f)
            print("\t\t\t\t<h2 class=\"TextCenter BlackText Weight700 Size24 TextLeft\">", row[0], "</h2>", sep="", file=f)
            
            if(row[6]!=""):
                print("\t\t\t\t<input type=\"checkbox\" id=\"EventToggle",line_count,"\" /> <label for=\"EventToggle",line_count,"\" class=\"EventToggleLabel Weight700\">Event Details</label>", sep="", file=f)
                if(row[7]!=""):
                    print("\t\t\t\t<a class=\"MoreButton Weight700\" href=\"",row[7],"\">Book Your Ticket Here</a>", sep="", file=f)
                print("\t\t\t\t<div class=\"ExpandableDetails\">", file=f)
                print("\t\t\t\t\t",row[6],sep="", file=f)
                print("\t\t\t\t</div>", file=f)
            print("\t\t\t</div>\n", file=f)
            
            print("\t\t\t<div class=\"TextContainer\" id=\"Time\">", file=f)
            if(row[3] != ""):
                print("\t\t\t\t<p class=\"TextCenter BlackText Weight700 Size24 TextRight\">",row[2]," - ",row[3],"</p>",sep="", file=f)
            else:
                print("\t\t\t\t<p class=\"TextCenter BlackText Weight700 Size24 TextRight\">",row[2],"</p>",sep="", file=f)
                
            print("\t\t\t\t<p class=\"TextCenter BlackText Weight400 Size18 TextRight\">",row[4],"<br>",row[5],"</p>",sep="", file=f)
            print("\t\t\t</div>", file=f)
            print("\t\t</div>", file=f)
            print("\t</div>\n", file=f)
            
            line_count += 1
        
        print("\t<div class=\"hl Width80\"></div>", file=f)

