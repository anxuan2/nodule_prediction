import streamlit as st
from nodule_tree import predict_nodule
from nodule_tree_v2 import predict_nodule_v2

st.title("Outil pour l'aide dans la prise en charge thérapeutique des nodules thyroïdiens")

col1, col2 = st.columns(2)
with col1:
    tsh = st.number_input('TSH (mUI/L)', 0.00, 200.00)
    tnod = st.number_input('Taille du nodule (mm)', 0, 1000)
    scinti = st.selectbox('Scintigraphie', ('Non fait', "Présence d'un nodule autonome", 'Pas de nodule autonome'))
    nod_bilat = st.selectbox('Nodule bilatéreaux', ('Non', 'Oui, nodules bilatéraux compressifs',
                                                    'Oui, nodules bilatéraux non compressifs'))
    cancer_bilat = st.selectbox('Cancer bilatéral ou Cancer isthmique', ('Non', 'Oui'))

with col2:
    eutirads = st.selectbox('Score EU-TIRADS', (2, 3, 4, 5))
    cyto = st.selectbox('Cytologie : Score Bethesda', ('I', 'II', 'III', 'IV', 'V', 'VI', 'Non fait'))
    adeno = st.selectbox('Adénopathies cervicales', ('cN0', 'cN1a', 'cN1b'))
    enceinte = st.selectbox('Femme enceinte / Projet grossesse / Nodule compressif', ('Non', 'Oui'))
    histo = st.selectbox("Histologie (lors de l'examen extemporané)",
                         ('Non fait', "En faveur d'un carcinome papillaire", "En faveur d'un nodule bénin"))


if st.button('Run'):
    prediction = predict_nodule_v2(scinti, tnod, eutirads, tsh, enceinte, cyto, nod_bilat,
                                   adeno, cancer_bilat, histo)
    st.title(prediction)

st.write('')
st.write('')
st.write('')

st.write("NB 1: L'algorithme de prise en charge se base sur le **consensus SFE-AFCE-SFMN 2022 sur la prise en charge des nodules thyroïdiens**.")
st.write("NB 2: L'utilisation est dédiée pour la prise en charge des nodules thyroïdiens. Il n'est pas à utiliser pour les autres pathologies thyroïdiennes telles que l'hypo ou l'hyperthyroïdie par exemple.")
