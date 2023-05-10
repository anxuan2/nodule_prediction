import streamlit as st
col1, col2 = st.columns(2)


def predict_nodule_v2(tsh, tnod, eutirads, adeno, cyto, nod_bilat, scinti, enceinte,
                      cancer_bilat, histo):
    if tsh <= 0.4:
        return first_tree_left(scinti, enceinte, cyto, tnod, adeno, nod_bilat, cancer_bilat, histo)
    elif tsh > 0.4:
        return first_tree_right(eutirads, tnod, tsh, cyto, nod_bilat, adeno, cancer_bilat, histo, scinti, enceinte)


def first_tree_right(eutirads, tnod, tsh, cyto, nod_bilat, adeno, cancer_bilat, histo, scinti, enceinte):
    if eutirads == 2 or (eutirads == 3 and tnod <= 20) or (eutirads == 4 and tnod <= 15) or (eutirads == 5 and tnod <= 10):
        return 'Surveillance'
    else:
        if tsh < 1:
            return first_tree_left(scinti, enceinte, cyto, tnod, adeno, nod_bilat, cancer_bilat, histo)
        else:
            return second_tree(cyto, nod_bilat, tnod, adeno, cancer_bilat, histo)


def first_tree_left(scinti, enceinte, cyto, tnod, adeno, nod_bilat, cancer_bilat, histo):
    if scinti == "Présence d'un nodule autonome":
        if enceinte == 'Oui':
            return 'Chirurgie'
        elif enceinte == 'Non':
            return 'Iode radioactif'
    elif scinti == 'Non fait':
        return 'Faire scintigraphie'
    elif scinti == 'Pas de nodule autonome':
        return second_tree(cyto, nod_bilat, tnod, adeno, cancer_bilat, histo)

#######################################################################################################################


def second_tree(cyto, nod_bilat, tnod, adeno, cancer_bilat, histo):
    if cyto == 'II':
        return second_tree_left(nod_bilat)
    elif cyto == 'I' or cyto == 'III':
        return 'Contrôle de la cytoponction'
    elif cyto == 'IV' or cyto == 'V' or cyto == 'VI':
        return second_tree_right(nod_bilat, tnod, cyto, adeno, cancer_bilat, histo)
    elif cyto == 'Non fait':
        return 'faire cytoponction'


def second_tree_left(nod_bilat):
    if nod_bilat == 'Oui, nodules bilatéraux compressifs':
        return 'Thyroïdectomie totale'
    elif nod_bilat == 'Oui, nodules bilatéraux non compressifs' or nod_bilat == 'Non':
        return 'Surveillance'


def second_tree_right(nod_bilat, tnod, cyto, adeno, cancer_bilat, histo):
    if nod_bilat == 'Non':
        return third_tree(adeno, cyto, tnod, cancer_bilat, histo)
    elif nod_bilat == 'Oui, nodules bilatéraux compressifs' or nod_bilat == 'Oui, nodules bilatéraux non compressifs':
        if (cyto == 'IV' and tnod > 40) or (cyto == 'V' and tnod > 20) or (cyto == 'VI' and tnod > 20):
            if adeno == 'cN0':
                return 'Thyroïdectomie totale'
            else:
                return third_tree(adeno, cyto, tnod, cancer_bilat, histo)
        else:
            return third_tree(adeno, cyto, tnod, cancer_bilat, histo)

#######################################################################################################################


def third_tree(adeno, cyto, tnod, cancer_bilat, histo):
    if adeno == 'cN0':
        return third_tree_left(cyto, tnod, cancer_bilat, histo)
    elif adeno == 'cN1a':
        return 'Thyroïdectomie totale + curage central homolateral'
    elif adeno == 'cN1b':
        return 'Thyroïdectomie totale + curage latéral III et IV + curage central homolatéra'


def third_tree_left(cyto, tnod, cancer_bilat, histo):
    if cyto == 'I' or cyto == 'II' or cyto == 'III' or cyto == 'IV':
        return 'Loboisthmectomie'
    if cyto == 'V' or cyto == 'VI':
        return third_tree_central(tnod, cancer_bilat, histo)


def third_tree_central(tnod, cancer_bilat, histo):
    if cancer_bilat == 'Oui':
        return 'Thyroidectomie totale + curage central bilatéral'
    elif cancer_bilat == 'Non':
        return third_tree_right(tnod, histo)


def third_tree_right(tnod, histo):
    if tnod < 20:
        return 'Loboisthmectomie'
    elif tnod < 40:
        return 'Thyroïdectomie totale'
    elif tnod >= 40:
        if histo == "En faveur d'un carcinome papillaire":
            return 'Thyroïdectomie totale et Curage récurentiel homolatéral'
        elif histo == "En faveur d'un nodule bénin":
            return 'Thyroïdectomie totale'
        elif histo == 'Non fait':
            return 'Thyroïdectomie totale et Examen extemporané'
