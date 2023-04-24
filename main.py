import streamlit as st
from nodule_tree import predict_nodule
from nodule_tree_v2 import predict_nodule_v2

st.title("Outil pour l'aide dans la prise en charge thérapeutique des nodules thyroïdiens")

col1, col2, col3 = st.columns(3)
with col1:
    tsh = st.number_input('TSH (mUI/L)', 0.00, 200.00)
with col2:
    enceinte = st.selectbox('Femme enceinte / Projet grossesse / Nodule compressif', ('Oui', 'Non'))
with col3:
    adeno = st.selectbox('Adénopathies cervicales', ('cN0', 'cN1a', 'cN1b'))

col1, col2, col3 = st.columns(3)
with col1:
    eutirads = st.selectbox('Score EU-TIRADS', (2, 3, 4, 5))
with col2:
    cyto = st.selectbox('Cytologie : Score Bethesda', ('I', 'II', 'III', 'IV', 'V', 'VI', 'Non fait'))
with col3:
    tnod = st.number_input('Taille du nodule (mm)', 0, 1000)

col1, col2, col3 = st.columns(3)
with col1:
    nod_bilat_comp = st.selectbox('Nodule bilatéreaux compressif', ('Oui', 'Non'))
with col2:
    nod_bilat = st.selectbox('Nodule bilatéreaux', ('Oui', 'Non'))
with col3:
    cancer_bilat = st.selectbox('Cancer bilatéral ou Cancer isthmique', ('Oui', 'Non'))

col1, col2 = st.columns(2)
with col1:
    histo = st.selectbox("Histologie (lors de l'examen extemporané)",
                         ("En faveur d'un carcinome papillaire", "En faveur d'un nodule bénin", 'Non fait'))
with col2:
    scinti = st.selectbox('Scintigraphie', ("Présence d'un nodule autonome", 'Pas de nodule autonome', 'Non fait'))


if st.button('Run'):
    prediction = predict_nodule_v2(scinti, tnod, eutirads, tsh, enceinte, cyto, nod_bilat_comp, nod_bilat,
                                   adeno, cancer_bilat, histo)
    st.title(prediction)
