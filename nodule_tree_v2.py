def predict_nodule(tsh, tnod, eutirads, color_n, style_n, color_e, style_e):
    color_n = color_n.copy()
    style_n = style_n.copy()
    color_e = color_e.copy()
    style_e = style_e.copy()
    color_n[0] = 'red'
    style_n[0] = 'bold'
    if tsh <= 0.4:
        color_e[0] = 'red'
        color_n[1] = 'red'
        style_e[0] = 'bold'
        style_n[1] = 'bold'
        return 'first_tree_left', color_n, color_e, style_n, style_e
    elif tsh > 0.4:
        color_e[1] = 'red'
        color_n[2] = 'red'
        style_e[1] = 'bold'
        style_n[2] = 'bold'
        return first_tree_right(eutirads, tnod, tsh, color_n, style_n, color_e, style_e)


def first_tree_right(eutirads, tnod, tsh, color_n, style_n, color_e, style_e):
    if eutirads == 2 or (eutirads == 3 and tnod <= 20) or (eutirads == 4 and tnod <= 15) or (eutirads == 5 and tnod <= 10):
        color_e[6] = 'red'
        color_n[7] = 'red'
        style_e[6] = 'bold'
        style_n[7] = 'bold'
        return 'Surveillance', color_n, color_e, style_n, style_e
    else:
        color_e[7] = 'red'
        color_n[8] = 'red'
        style_e[7] = 'bold'
        style_n[8] = 'bold'
        if tsh < 1:
            color_e[8] = 'red'
            color_n[1] = 'red'
            style_e[8] = 'bold'
            style_n[1] = 'bold'
            return 'first_tree_left', color_n, color_e, style_n, style_e
        else:
            color_e[10] = 'red'
            color_n[9] = 'red'
            style_e[10] = 'bold'
            style_n[9] = 'bold'
            return 'second_tree', color_n, color_e, style_n, style_e


def first_tree_left(scinti, enceinte, color_n, style_n, color_e, style_e):
    color_n = color_n.copy()
    style_n = style_n.copy()
    color_e = color_e.copy()
    style_e = style_e.copy()
    if scinti == "Présence d'un nodule autonome":
        color_e[2] = 'red'
        color_n[3] = 'red'
        style_e[2] = 'bold'
        style_n[3] = 'bold'
        if enceinte == 'Oui':
            color_e[4] = 'red'
            color_n[5] = 'red'
            style_e[4] = 'bold'
            style_n[5] = 'bold'
            return 'Chirurgie', color_n, color_e, style_n, style_e
        elif enceinte == 'Non':
            color_e[5] = 'red'
            color_n[6] = 'red'
            style_e[5] = 'bold'
            style_n[6] = 'bold'
            return 'Iode radioactif', color_n, color_e, style_n, style_e
    elif scinti == 'Non fait':
        color_e[3] = 'red'
        color_n[4] = 'red'
        style_e[3] = 'bold'
        style_n[4] = 'bold'
        return 'Faire scintigraphie', color_n, color_e, style_n, style_e
    elif scinti == 'Pas de nodule autonome':
        color_e[9] = 'red'
        color_n[9] = 'red'
        style_e[9] = 'bold'
        style_n[9] = 'bold'
        return 'second_tree', color_n, color_e, style_n, style_e

#######################################################################################################################


def second_tree(cyto, nod_bilat, tnod, adeno, cancer_bilat, histo, color_n, style_n, color_e, style_e):
    if cyto == 'II':
        color_e[13] = 'red'
        color_n[12] = 'red'
        style_e[13] = 'bold'
        style_n[12] = 'bold'
        return second_tree_left(nod_bilat, color_n, style_n, color_e, style_e)
    elif cyto == 'I' or cyto == 'III':
        color_e[11] = 'red'
        color_n[10] = 'red'
        style_e[11] = 'bold'
        style_n[10] = 'bold'
        return 'Contrôle de la cytoponction', color_n, color_e, style_n, style_e
    elif cyto == 'IV' or cyto == 'V' or cyto == 'VI':
        color_e[12] = 'red'
        color_n[11] = 'red'
        style_e[12] = 'bold'
        style_n[11] = 'bold'
        return second_tree_right(nod_bilat, tnod, cyto, adeno, cancer_bilat, histo, color_n, style_n, color_e, style_e)
    elif cyto == 'Non fait':
        color_e[14] = 'red'
        color_n[13] = 'red'
        style_e[14] = 'bold'
        style_n[13] = 'bold'
        return 'faire cytoponction', color_n, color_e, style_n, style_e


def second_tree_left(nod_bilat, color_n, style_n, color_e, style_e):
    if nod_bilat == 'Oui, nodules bilatéraux compressifs':
        color_e[16] = 'red'
        color_n[15] = 'red'
        style_e[16] = 'bold'
        style_n[15] = 'bold'
        return 'Thyroïdectomie totale', color_n, color_e, style_n, style_e
    elif nod_bilat == 'Oui, nodules bilatéraux non compressifs' or nod_bilat == 'Non':
        color_e[15] = 'red'
        color_n[14] = 'red'
        style_e[15] = 'bold'
        style_n[14] = 'bold'
        return 'Surveillance', color_n, color_e, style_n, style_e


def second_tree_right(nod_bilat, tnod, cyto, adeno, cancer_bilat, histo, color_n, style_n, color_e, style_e):
    if nod_bilat == 'Non':
        color_e[20] = 'red'
        color_n[19] = 'red'
        style_e[20] = 'bold'
        style_n[19] = 'bold'
        return third_tree(adeno, cyto, tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e)
    elif nod_bilat == 'Oui, nodules bilatéraux compressifs' or nod_bilat == 'Oui, nodules bilatéraux non compressifs':
        color_e[17] = 'red'
        color_n[16] = 'red'
        style_e[17] = 'bold'
        style_n[16] = 'bold'
        if (cyto == 'IV' and tnod > 40) or (cyto == 'V' and tnod > 20) or (cyto == 'VI' and tnod > 20):
            color_e[18] = 'red'
            color_n[17] = 'red'
            style_e[18] = 'bold'
            style_n[17] = 'bold'
            if adeno == 'cN0':
                color_e[19] = 'red'
                color_n[18] = 'red'
                style_e[19] = 'bold'
                style_n[18] = 'bold'
                return 'Thyroïdectomie totale', color_n, color_e, style_n, style_e
            else:
                color_e[21] = 'red'
                color_n[19] = 'red'
                style_e[21] = 'bold'
                style_n[19] = 'bold'
                return third_tree(adeno, cyto, tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e)
        else:
            color_e[20] = 'red'
            color_n[19] = 'red'
            style_e[20] = 'bold'
            style_n[19] = 'bold'
            return third_tree(adeno, cyto, tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e)

#######################################################################################################################


def third_tree(adeno, cyto, tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e):
    if adeno == 'cN0':
        color_e[24] = 'red'
        color_n[22] = 'red'
        style_e[24] = 'bold'
        style_n[22] = 'bold'
        return third_tree_left(cyto, tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e)
    elif adeno == 'cN1a':
        color_e[23] = 'red'
        color_n[21] = 'red'
        style_e[23] = 'bold'
        style_n[21] = 'bold'
        return 'Thyroïdectomie totale + curage central homolateral', color_n, color_e, style_n, style_e
    elif adeno == 'cN1b':
        color_e[22] = 'red'
        color_n[20] = 'red'
        style_e[22] = 'bold'
        style_n[20] = 'bold'
        return 'Thyroïdectomie totale + curage latéral III et IV + curage central homolatéral', \
               color_n, color_e, style_n, style_e


def third_tree_left(cyto, tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e):
    if cyto == 'I' or cyto == 'II' or cyto == 'III' or cyto == 'IV':
        color_e[25] = 'red'
        color_n[24] = 'red'
        style_e[25] = 'bold'
        style_n[24] = 'bold'
        return 'Loboisthmectomie', color_n, color_e, style_n, style_e
    if cyto == 'V' or cyto == 'VI':
        color_e[26] = 'red'
        color_n[23] = 'red'
        style_e[26] = 'bold'
        style_n[23] = 'bold'
        return third_tree_central(tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e)


def third_tree_central(tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e):
    if cancer_bilat == 'Oui':
        color_e[28] = 'red'
        color_n[26] = 'red'
        style_e[28] = 'bold'
        style_n[26] = 'bold'
        return 'Thyroidectomie totale + curage central bilatéral', color_n, color_e, style_n, style_e
    elif cancer_bilat == 'Non':
        color_e[27] = 'red'
        color_n[25] = 'red'
        style_e[27] = 'bold'
        style_n[25] = 'bold'
        return third_tree_right(tnod, histo, color_n, style_n, color_e, style_e)


def third_tree_right(tnod, histo, color_n, style_n, color_e, style_e):
    if tnod < 20:
        color_e[29] = 'red'
        color_n[27] = 'red'
        style_e[29] = 'bold'
        style_n[27] = 'bold'
        return 'Loboisthmectomie', color_n, color_e, style_n, style_e
    elif tnod < 40:
        color_e[30] = 'red'
        color_n[28] = 'red'
        style_e[30] = 'bold'
        style_n[28] = 'bold'
        return 'Thyroïdectomie totale', color_n, color_e, style_n, style_e
    elif tnod >= 40:
        color_e[31] = 'red'
        color_n[29] = 'red'
        style_e[31] = 'bold'
        style_n[29] = 'bold'
        if histo == "En faveur d'un carcinome papillaire":
            color_e[34] = 'red'
            color_n[21] = 'red'
            style_e[34] = 'bold'
            style_n[21] = 'bold'
            return 'Thyroïdectomie totale et Curage récurentiel homolatéral', color_n, color_e, style_n, style_e
        elif histo == "En faveur d'un nodule bénin":
            color_e[33] = 'red'
            color_n[28] = 'red'
            style_e[33] = 'bold'
            style_n[28] = 'bold'
            return 'Thyroïdectomie totale', color_n, color_e, style_n, style_e
        elif histo == 'Non fait':
            color_e[32] = 'red'
            color_n[30] = 'red'
            style_e[32] = 'bold'
            style_n[30] = 'bold'
            return 'Thyroïdectomie totale et Examen extemporané', color_n, color_e, style_n, style_e
