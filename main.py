import pandas as pd
import numpy as np
import csv

def grout_coulis():
    header = ['Product / Produit', 'Weight / Poids','Colour / Couleur', 'Description','Quantity / Quantité']
    data = [
        ['ALL-SET', '22.7KG', 'GRAY', 'MODIFIED', 0],
        ['SCHLUTER SET', '22.7KG', 'WHITE', 'UNMODIFIED', 11],
        ['ULTRALITE', '11.3KG', 'N/A', 'LIGHTWEIGHT MORTAR', 9],    
        ['KERAPOXY', '1GAL', 'FROST (77)', 'EPOXY GROUT AND MORTAR', 5],
        ['TYPE 1', '3.79L', 'n/a', 'TILE ADHESIVE', 2],
        ['FLEXCOLOR CQ', '1GAL', 'CHAMOIS (05)',	'READY-TO-USE',	1],
        ['FLEXCOLOR CQ', '1GAL', 'PEWTER (02)',	'READY-TO-USE', 1],
        ['FLEXCOLOR CQ', '1GAL', 'AVALANCHE (38)', 'READY-TO-USE',	1],
        ['FLEXCOLOR CQ', '1GAL', 'SILVER (27)', 'READY-TO-USE', 1],
        ['FLEXCOLOR CQ', '1GAL', 'RAIN (101)',	'READY-TO-USE', 2],
        ['FLEXCOLOR CQ', '1GAL', 'WHITE (00)',	'READY-TO-USE', 1],
        ['FLEXCOLOR CQ', '1GAL', 'WALNUT (106)', 'READY-TO-USE', 1],
        ['FLEXCOLOR CQ', '0.5GAL', 'SILVER (27)', 'READY-TO-USE', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'SILVER (27)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'WARM GRAY(93)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 2],
        ['ULTRACOLOR PLUS FA', '10LBS', 'AVALANCHE (38)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'CHARCOAL (47)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'IVORY (39)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'NAVAJO BROWN (35)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '10LBS', 'PEWTER (02)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '25LBS/11.3KG', 'PEWTER (02)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['ULTRACOLOR PLUS FA', '25LBS/11.3KG', 'SAHARA BEIGE (11)', 'RAPID SETTING ALL-IN-ONE GROUT REPLACEMENT', 1],
        ['KERACOLOR U', '4.54KG', 'SILVER (27)', 'UNSANDED GROUT WITH POLYMER', 1],
        ['KERACOLOR U', '4.54KG', 'MOCHA (42)', 'UNSANDED GROUT WITH POLYMER', 1]
        ]

    with open('grout_coulis.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(header)
        writer.writerows(data)

    df = pd.read_csv('grout_coulis.csv')
    df.to_excel('grout_coulis.xlsx', index=None, header=True)

grout_coulis()