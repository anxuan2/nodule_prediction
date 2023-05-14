from graphviz import Digraph


def create_nodule_tree(color_n, style_n, color_e, style_e):
    dot = Digraph(comment='Arbre de décision pour le cancer de la thyroïde', format='png')
    # Créer les nœuds de l'arbre
    dot.node('tsh1', 'TSH <= 0.4', fillcolor=color_n[0], color=color_n[0], fontcolor=color_n[0], style=style_n[0])
    dot.node('scinti1', 'Scintigraphie', fillcolor=color_n[1], color=color_n[1], fontcolor=color_n[1], style=style_n[1])
    dot.node('euti1', 'Eutirads = 2 or (3 and tnod <= 20) or \n (4 and tnod <= 15) or \n (5 and tnod <= 10)?',
             fillcolor=color_n[2], color=color_n[2], fontcolor=color_n[2], style=style_n[2])
    dot.edge('tsh1', 'scinti1', 'Oui', fillcolor=color_e[0], color=color_e[0], fontcolor=color_e[0], style=style_e[0])
    dot.edge('tsh1', 'euti1', 'Non', fillcolor=color_e[1], color=color_e[1], fontcolor=color_e[1], style=style_e[1])

    dot.node('enceinte1', 'Femme enceinte \n ou projet', fillcolor=color_n[3], color=color_n[3], fontcolor=color_n[3], style=style_n[3])
    dot.node('scinti2', 'Faire scintigraphie', shape='box', fillcolor=color_n[4], color=color_n[4], fontcolor=color_n[4], style=style_n[4])
    dot.edge('scinti1', 'enceinte1', 'Nodule \n autonome', fillcolor=color_e[2], color=color_e[2], fontcolor=color_e[2], style=style_e[2])
    dot.edge('scinti1', 'scinti2', 'Non Fait', fillcolor=color_e[3], color=color_e[3], fontcolor=color_e[3], style=style_e[3])

    dot.node('chirurgie1', 'Chirurgie', shape='box', fillcolor=color_n[5], color=color_n[5], fontcolor=color_n[5], style=style_n[5])
    dot.node('iode1', 'Iode radioactif', shape='box', fillcolor=color_n[6], color=color_n[6], fontcolor=color_n[6], style=style_n[6])
    dot.edge('enceinte1', 'chirurgie1', 'Oui', fillcolor=color_e[4], color=color_e[4], fontcolor=color_e[4], style=style_e[4])
    dot.edge('enceinte1', 'iode1', 'Non', fillcolor=color_e[5], color=color_e[5], fontcolor=color_e[5], style=style_e[5])

    dot.node('tsh2', 'TSH > 1', fillcolor=color_n[8], color=color_n[8], fontcolor=color_n[8], style=style_n[8])
    dot.edge('euti1', 'tsh2', 'Non', fillcolor=color_e[7], color=color_e[7], fontcolor=color_e[7], style=style_e[7])

    dot.node('surveillance1', 'Surveillance', shape='box', fillcolor=color_n[7], color=color_n[7], fontcolor=color_n[7], style=style_n[7])
    dot.edge('euti1', 'surveillance1', 'Oui', fillcolor=color_e[6], color=color_e[6], fontcolor=color_e[6], style=style_e[6])

    dot.edge('tsh2', 'scinti1', 'Non', fillcolor=color_e[8], color=color_e[8], fontcolor=color_e[8], style=style_e[8])
    dot.node('cyto1', 'Cytoponction', fillcolor=color_n[9], color=color_n[9], fontcolor=color_n[9], style=style_n[9])
    dot.edge('scinti1', 'cyto1', 'Pas de nodule \n autonome', fillcolor=color_e[9], color=color_e[9], fontcolor=color_e[9], style=style_e[9])
    dot.edge('tsh2', 'cyto1', 'Oui', fillcolor=color_e[10], color=color_e[10], fontcolor=color_e[10], style=style_e[10])

    dot.node('cyto2', 'Contrôle de la cytoponction', shape='box', fillcolor=color_n[10], color=color_n[10], fontcolor=color_n[10], style=style_n[10])
    dot.edge('cyto1', 'cyto2', 'I / III', fillcolor=color_e[11], color=color_e[11], fontcolor=color_e[11], style=style_e[11])

    dot.node('bilat2', 'Nodule bilatéraux', fillcolor=color_n[11], color=color_n[11], fontcolor=color_n[11], style=style_n[11])
    dot.edge('cyto1', 'bilat2', 'IV / V / VI', fillcolor=color_e[12], color=color_e[12], fontcolor=color_e[12], style=style_e[12])

    dot.node('bilat1', 'Nodule bilatéraux compressif', fillcolor=color_n[12], color=color_n[12], fontcolor=color_n[12], style=style_n[12])
    dot.edge('cyto1', 'bilat1', 'II', fillcolor=color_e[13], color=color_e[13], fontcolor=color_e[13], style=style_e[13])

    dot.node('cyto3', 'Faire cytoponction', shape='box', fillcolor=color_n[13], color=color_n[13], fontcolor=color_n[13], style=style_n[13])
    dot.edge('cyto1', 'cyto3', 'Non fait', fillcolor=color_e[14], color=color_e[14], fontcolor=color_e[14], style=style_e[14])

    dot.node('surveillance2', 'Surveillance', shape='box',fillcolor=color_n[14], color=color_n[14], fontcolor=color_n[14], style=style_n[14])
    dot.node('thyroi1', 'Thyroïdectomie totale', shape='box', fillcolor=color_n[15], color=color_n[15], fontcolor=color_n[15], style=style_n[15])
    dot.edge('bilat1', 'surveillance2', 'Non', fillcolor=color_e[15], color=color_e[15], fontcolor=color_e[15], style=style_e[15])
    dot.edge('bilat1', 'thyroi1', 'Oui', fillcolor=color_e[16], color=color_e[16], fontcolor=color_e[16], style=style_e[16])

    dot.node('cyto4', '(cyto=IV et tnod>4cm) or \n (cyto=V/VI et tnod>2cm)', fillcolor=color_n[16], color=color_n[16], fontcolor=color_n[16], style=style_n[16])
    dot.node('adeno1', 'Adenopathies cervicales', ffillcolor=color_n[17], color=color_n[17], fontcolor=color_n[17], style=style_n[17])
    dot.edge('bilat2', 'cyto4', 'Oui', fillcolor=color_e[17], color=color_e[17], fontcolor=color_e[17], style=style_e[17])
    dot.edge('cyto4', 'adeno1', 'Oui', fillcolor=color_e[18], color=color_e[18], fontcolor=color_e[18], style=style_e[18])
    dot.edge('cyto4', 'adeno2', 'Non', fillcolor=color_e[35], color=color_e[35], fontcolor=color_e[35], style=style_e[35])
    dot.node('thyroi2', 'Thyroïdectomie totale', shape='box', fillcolor=color_n[18], color=color_n[18], fontcolor=color_n[18], style=style_n[18])
    dot.edge('adeno1', 'thyroi2', 'cN0', fillcolor=color_e[19], color=color_e[19], fontcolor=color_e[19], style=style_e[19])

    dot.node('adeno2', 'Adenopathies cervicales', fillcolor=color_n[19], color=color_n[19], fontcolor=color_n[19], style=style_n[19])
    dot.edge('bilat2', 'adeno2', 'Non', fillcolor=color_e[20], color=color_e[20], fontcolor=color_e[20], style=style_e[20])
    dot.edge('adeno1', 'adeno2', 'cN1a / cN1b', fillcolor=color_e[21], color=color_e[21], fontcolor=color_e[21], style=style_e[21])

    dot.node('thyroi3', 'Thyroïdectomie totale + \n curage cervical latéral III IV + \n curage centrale homolatéral',
             shape='box', fillcolor=color_n[20], color=color_n[20], fontcolor=color_n[20], style=style_n[20])
    dot.node('thyroi4', 'Thyroïdectomie totale + \n curage central homolatéral', shape='box', fillcolor=color_n[21], color=color_n[21], fontcolor=color_n[21], style=style_n[21])
    dot.edge('adeno2', 'thyroi3', 'cN1B', fillcolor=color_e[22], color=color_e[22], fontcolor=color_e[22], style=style_e[22])
    dot.edge('adeno2', 'thyroi4', 'cN1A', fillcolor=color_e[23], color=color_e[23], fontcolor=color_e[23], style=style_e[23])
    dot.node('cyto5', 'Cytoponction', fillcolor=color_n[22], color=color_n[22], fontcolor=color_n[22], style=style_n[22])
    dot.edge('adeno2', 'cyto5', 'cN0', fillcolor=color_e[24], color=color_e[24], fontcolor=color_e[24], style=style_e[24])

    dot.node('cancer1', 'Cancer bilatéral ou cancer isthmique', fillcolor=color_n[23], color=color_n[23], fontcolor=color_n[23], style=style_n[23])
    dot.node('lobo1', 'Loboisthmectomie', shape='box', fillcolor=color_n[24], color=color_n[24], fontcolor=color_n[24], style=style_n[24])
    dot.edge('cyto5', 'lobo1', 'I / II / \nIII / IV', fillcolor=color_e[25], color=color_e[25], fontcolor=color_e[25], style=style_e[25])
    dot.edge('cyto5', 'cancer1', 'V / VI', fillcolor=color_e[26], color=color_e[26], fontcolor=color_e[26], style=style_e[26])

    dot.node('tnod1', 'Taille nodule', fillcolor=color_n[25], color=color_n[25], fontcolor=color_n[25], style=style_n[25])
    dot.node('thyroi5', 'Thyroïdectomie totale + curage central bilatéral', shape='box', fillcolor=color_n[26], color=color_n[26], fontcolor=color_n[26], style=style_n[26])
    dot.edge('cancer1', 'tnod1', 'Non', fillcolor=color_e[27], color=color_e[27], fontcolor=color_e[27], style=style_e[27])
    dot.edge('cancer1', 'thyroi5', 'Oui', fillcolor=color_e[28], color=color_e[28], fontcolor=color_e[28], style=style_e[28])

    dot.node('lobo2', 'Loboisthmectomie', shape='box', fillcolor=color_n[27], color=color_n[27], fontcolor=color_n[27], style=style_n[27])
    dot.node('thyroi6', 'Thyroïdectomie totale', shape='box', fillcolor=color_n[28], color=color_n[28], fontcolor=color_n[28], style=style_n[28])
    dot.node('cancer2', 'Cancer papillaire', fillcolor=color_n[29], color=color_n[29], fontcolor=color_n[29], style=style_n[29])
    dot.edge('tnod1', 'lobo2', '<20mm', fillcolor=color_e[29], color=color_e[29], fontcolor=color_e[29], style=style_e[29])
    dot.edge('tnod1', 'thyroi6', '>=20mm et \n < 40mm', ffillcolor=color_e[30], color=color_e[30], fontcolor=color_e[30], style=style_e[30])
    dot.edge('tnod1', 'cancer2', '>=40mm', fillcolor=color_e[31], color=color_e[31], fontcolor=color_e[31], style=style_e[31])

    dot.node('thyroi7', 'Thyroïdectomie totale + examen extemporané', shape='box', fillcolor=color_n[30], color=color_n[30], fontcolor=color_n[30], style=style_n[30])
    dot.edge('cancer2', 'thyroi7', 'Non fait', fillcolor=color_e[32], color=color_e[32], fontcolor=color_e[32], style=style_e[32])
    dot.edge('cancer2', 'thyroi6', 'Non', fillcolor=color_e[33], color=color_e[33], fontcolor=color_e[33], style=style_e[33])
    dot.edge('cancer2', 'thyroi4', 'Oui', fillcolor=color_e[34], color=color_e[34], fontcolor=color_e[34], style=style_e[34])

    return dot.render('tree_nodule')
