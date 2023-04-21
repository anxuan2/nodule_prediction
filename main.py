import streamlit as st

st.title('Nodule prediction')

tsh = st.number_input('TSH', 0.00, 200.00)
scinti = st.selectbox('Scinti', ('Oui (nodule autonome)', 'Non (pas de nodule autonome)', 'Non fait'))
adeno = st.selectbox('Adeno', ('cN0', 'cN1'))
eutirads = st.selectbox('Eutirads', ('2', '3', '4', '5'))
cyto = st.selectbox('Cyto', ('I', 'II', 'III', 'IV', 'V', 'VI', 'non fait'))
tnod = st.number_input('Tnod', 0, 1000)
histo = st.selectbox('Histo', ('Oui, carcinome papillaire', 'Non, bénin', 'Non fait'))

def predict_nodule(tsh, scinti, adeno, eutirads, cyto, tnod, histo):
    if tsh < 1:
        if scinti == 'Non fait':
            return 'Faire scintigraphie'
        elif scinti == 'Oui (nodule autonome)':
            return 'Iode radioactif ou chirurgie'
    else:
        if adeno == 'cN1':
            return 'thyroïdectomie totale avec curage récurentiel bilatéral'
        else:
            if eutirads == 2 or (eutirads == 3 and tnod <= 20) or (eutirads == 4 and tnod <= 15) or (eutirads == 5 and tnod <= 10):
                return 'Surveillance'
            else:
                if cyto == 'II':
                    return 'Surveillance'
                elif cyto =='I' or cyto == 'III':
                    return 'controle de la cytoponction'
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

if st.button('Run'):
    st.title(predict_nodule(tsh, scinti, adeno, eutirads, cyto, tnod, histo))