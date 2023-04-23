import streamlit as st
from nodule_tree import predict_nodule

st.title("Outil pour l'aide dans la prise en charge thérapeutique des nodules thyroïdiens")
col1, col2, col3 = st.columns(3)


with col1:
    tsh = st.number_input('TSH (mUI/L)', 0.00, 200.00)
with col2:
    scinti = st.selectbox('Scintigraphie', ("Présence d'un nodule autonome", 'Pas de nodule autonome', 'Non fait'))

with col3:
    adeno = st.selectbox('Adénopathies cervicales centrales', ('cN0', 'cN1'))

col1, col2, col3, col4 = st.columns(4)

with col1:
    eutirads = st.selectbox('Score EU-TIRADS', ('2', '3', '4', '5'))
with col2:
    cyto = st.selectbox('Cytologie : Score Bethesda', ('I', 'II', 'III', 'IV', 'V', 'VI', 'non fait'))
with col3:
    tnod = st.number_input('Taille du nodule (mm)', 0, 1000)
with col4:
    histo = st.selectbox("Histologie (lors de l'examen extemporané)",
                         ("En faveur d'un carcinome papillaire", "En faveur d'un nodule bénin", 'Non fait'))

if st.button('Run'):
    st.title(predict_nodule(tsh, scinti, adeno, eutirads, cyto, tnod, histo))
