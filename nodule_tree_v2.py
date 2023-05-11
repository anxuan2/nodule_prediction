def predict_nodule_v3(tsh, tnod, eutirads, adeno, cyto, nod_bilat, scinti, enceinte,
                      cancer_bilat, histo, color_n, style_n, color_e, style_e):
    color_n[0] = 'red'
    if tsh <= 0.4:
        color_e[0] = 'red'
        color_n[1] = 'red'
        return first_tree_left(scinti, enceinte, cyto, tnod, adeno, nod_bilat, cancer_bilat, histo,
                               color_n, style_n, color_e, style_e)
    elif tsh > 0.4:
        color_e[1] = 'red'
        color_n[2] = 'red'
        return first_tree_right(eutirads, tnod, tsh, cyto, nod_bilat, adeno, cancer_bilat, histo, scinti, enceinte,
                                color_n, style_n, color_e, style_e)


def first_tree_right(eutirads, tnod, tsh, cyto, nod_bilat, adeno, cancer_bilat, histo, scinti, enceinte,
                     color_n, style_n, color_e, style_e):
    if eutirads == 2 or (eutirads == 3 and tnod <= 20) or (eutirads == 4 and tnod <= 15) or (eutirads == 5 and tnod <= 10):
        color_e[6] = 'red'
        color_n[7] = 'red'
        return 'Surveillance', color_n, color_e, style_n, style_e
    else:
        color_e[7] = 'red'
        color_n[8] = 'red'
        if tsh < 1:
            color_e[8] = 'red'
            color_n[1] = 'red'
            return first_tree_left(scinti, enceinte, cyto, tnod, adeno, nod_bilat, cancer_bilat, histo,
                                   color_n, style_n, color_e, style_e)
        else:
            color_e[10] = 'red'
            color_n[9] = 'red'
            return second_tree(cyto, nod_bilat, tnod, adeno, cancer_bilat, histo, color_n, style_n, color_e, style_e)


def first_tree_left(scinti, enceinte, cyto, tnod, adeno, nod_bilat, cancer_bilat, histo,
                    color_n, style_n, color_e, style_e):
    if scinti == "Présence d'un nodule autonome":
        color_e[2] = 'red'
        color_n[3] = 'red'
        if enceinte == 'Oui':
            color_e[4] = 'red'
            color_n[5] = 'red'
            return 'Chirurgie', color_n, color_e, style_n, style_e
        elif enceinte == 'Non':
            color_e[5] = 'red'
            color_e[6] = 'red'
            return 'Iode radioactif', color_n, color_e, style_n, style_e
    elif scinti == 'Non fait':
        color_e[3] = 'red'
        color_n[4] = 'red'
        return 'Faire scintigraphie', color_n, color_e, style_n, style_e
    elif scinti == 'Pas de nodule autonome':
        color_e[9] = 'red'
        color_n[9] = 'red'
        return second_tree(cyto, nod_bilat, tnod, adeno, cancer_bilat, histo, color_n, style_n, color_e, style_e)

#######################################################################################################################


def second_tree(cyto, nod_bilat, tnod, adeno, cancer_bilat, histo, color_n, style_n, color_e, style_e):
    if cyto == 'II':
        color_e[13] = 'red'
        color_n[12] = 'red'
        return second_tree_left(nod_bilat, color_n, style_n, color_e, style_e)
    elif cyto == 'I' or cyto == 'III':
        color_e[11] = 'red'
        color_n[10] = 'red'
        return 'Contrôle de la cytoponction', color_n, color_e, style_n, style_e
    elif cyto == 'IV' or cyto == 'V' or cyto == 'VI':
        color_e[12] = 'red'
        color_n[11] = 'red'
        return second_tree_right(nod_bilat, tnod, cyto, adeno, cancer_bilat, histo)
    elif cyto == 'Non fait':
        color_e[14] = 'red'
        color_n[13] = 'red'
        return 'faire cytoponction', color_n, color_e, style_n, style_e


def second_tree_left(nod_bilat, color_n, style_n, color_e, style_e):
    if nod_bilat == 'Oui, nodules bilatéraux compressifs':
        color_e[16] = 'red'
        color_n[15] = 'red'
        return 'Thyroïdectomie totale', color_n, color_e, style_n, style_e
    elif nod_bilat == 'Oui, nodules bilatéraux non compressifs' or nod_bilat == 'Non':
        color_e[15] = 'red'
        color_n[14] = 'red'
        return 'Surveillance', color_n, color_e, style_n, style_e


def second_tree_right(nod_bilat, tnod, cyto, adeno, cancer_bilat, histo, color_n, style_n, color_e, style_e):
    if nod_bilat == 'Non':
        color_e[20] = 'red'
        color_n[19] = 'red'
        return third_tree(adeno, cyto, tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e)
    elif nod_bilat == 'Oui, nodules bilatéraux compressifs' or nod_bilat == 'Oui, nodules bilatéraux non compressifs':
        color_e[17] = 'red'
        color_n[16] = 'red'
        if (cyto == 'IV' and tnod > 40) or (cyto == 'V' and tnod > 20) or (cyto == 'VI' and tnod > 20):
            color_e[18] = 'red'
            color_n[17] = 'red'
            if adeno == 'cN0':
                color_e[19] = 'red'
                color_n[18] = 'red'
                return 'Thyroïdectomie totale', color_n, color_e, style_n, style_e
            else:
                color_e[35] = 'red'
                color_n[19] = 'red'
                return third_tree(adeno, cyto, tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e)
        else:
            color_e[20] = 'red'
            color_n[19] = 'red'
            return third_tree(adeno, cyto, tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e)

#######################################################################################################################


def third_tree(adeno, cyto, tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e):
    if adeno == 'cN0':
        color_e[24] = 'red'
        color_n[22] = 'red'
        return third_tree_left(cyto, tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e)
    elif adeno == 'cN1a':
        color_e[23] = 'red'
        color_n[21] = 'red'
        return 'Thyroïdectomie totale + curage central homolateral', color_n, color_e, style_n, style_e
    elif adeno == 'cN1b':
        color_e[22] = 'red'
        color_n[20] = 'red'
        return 'Thyroïdectomie totale + curage latéral III et IV + curage central homolatéral', \
               color_n, color_e, style_n, style_e


def third_tree_left(cyto, tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e):
    if cyto == 'I' or cyto == 'II' or cyto == 'III' or cyto == 'IV':
        color_e[25] = 'red'
        color_n[24] = 'red'
        return 'Loboisthmectomie', color_n, color_e, style_n, style_e
    if cyto == 'V' or cyto == 'VI':
        color_e[26] = 'red'
        color_n[23] = 'red'
        return third_tree_central(tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e)


def third_tree_central(tnod, cancer_bilat, histo, color_n, style_n, color_e, style_e):
    if cancer_bilat == 'Oui':
        color_e[28] = 'red'
        color_n[26] = 'red'
        return 'Thyroidectomie totale + curage central bilatéral', color_n, color_e, style_n, style_e
    elif cancer_bilat == 'Non':
        color_e[27] = 'red'
        color_n[25] = 'red'
        return third_tree_right(tnod, histo, color_n, style_n, color_e, style_e)


def third_tree_right(tnod, histo, color_n, style_n, color_e, style_e):
    if tnod < 20:
        color_e[29] = 'red'
        color_n[27] = 'red'
        return 'Loboisthmectomie', color_n, color_e, style_n, style_e
    elif tnod < 40:
        color_e[30] = 'red'
        color_n[28] = 'red'
        return 'Thyroïdectomie totale', color_n, color_e, style_n, style_e
    elif tnod >= 40:
        color_e[31] = 'red'
        color_n[29] = 'red'
        if histo == "En faveur d'un carcinome papillaire":
            color_e[34] = 'red'
            color_n[21] = 'red'
            return 'Thyroïdectomie totale et Curage récurentiel homolatéral', color_n, color_e, style_n, style_e
        elif histo == "En faveur d'un nodule bénin":
            color_e[33] = 'red'
            color_n[28] = 'red'
            return 'Thyroïdectomie totale', color_n, color_e, style_n, style_e
        elif histo == 'Non fait':
            color_e[32] = 'red'
            color_n[30] = 'red'
            return 'Thyroïdectomie totale et Examen extemporané', color_n, color_e, style_n, style_e
