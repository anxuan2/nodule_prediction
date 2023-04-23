def predict_nodule(tsh, scinti, adeno, eutirads, cyto, tnod, histo):
    if tsh < 1:
        if scinti == 'Non fait':
            return 'Faire scintigraphie'
        elif scinti == 'Oui (nodule autonome)':
            return 'Iode radioactif ou chirurgie'
        elif scinti == 'Non (pas de nodule autonome)':
            return get_second_part_of_tree(adeno, eutirads, cyto, tnod, histo)
    else:
        return get_second_part_of_tree(adeno, eutirads, cyto, tnod, histo)


def get_second_part_of_tree(adeno, eutirads, cyto, tnod, histo):
    if adeno == 'cN1':
        return 'Thyroïdectomie totale avec curage récurentiel bilatéral'
    else:
        if eutirads == 2 or (eutirads == 3 and tnod <= 20) or (eutirads == 4 and tnod <= 15) or (eutirads == 5 and tnod <= 10):
            return 'Surveillance'
        else:
            if cyto == 'II':
                return 'Surveillance'
            elif cyto =='I' or cyto == 'III':
                return 'Contrôle de la cytoponction'
            elif cyto == 'IV':
                return 'Loboisthmectomie'
            elif cyto == 'V' or cyto == 'VI':
                if tnod <= 20:
                    return 'Loboisthmectomie'
                elif tnod < 40:
                    return 'Thyroïdectomie totale'
                else:
                    if histo == 'Oui, carcinome papillaire':
                        return 'Thyroïdectomie totale et Curage récurentiel homolatéral'
                    elif histo == 'Non, bénin':
                        return 'Thyroïdectomie totale'
                    else:
                        return 'Thyroïdectomie totale et Examen extemporané'
            elif cyto == 'non fait':
                return 'Faire cytoponction'