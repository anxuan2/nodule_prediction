import streamlit as st
from tree_vizualization import create_nodule_tree
from nodule_tree_v2 import predict_nodule_v3
color_n = ['black' for _ in range(32)]
style_n = ['solid' for _ in range(32)]
color_e = ['black' for _ in range(36)]
style_e = ['solid' for _ in range(36)]

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
    adeno = st.selectbox('Adénopathies cervicales', ('cN0', 'cN1a', 'cN1b'))

    cyto = st.selectbox('Cytologie : Score Bethesda', ('I', 'II', 'III', 'IV', 'V', 'VI', 'Non fait'))
    enceinte = st.selectbox('Femme enceinte / Projet grossesse / Nodule compressif', ('Non', 'Oui'))
    histo = st.selectbox("Histologie (lors de l'examen extemporané)",
                         ('Non fait', "En faveur d'un carcinome papillaire", "En faveur d'un nodule bénin"))

if st.button('Run'):
    prediction, color_n, color_e, style_n, style_e = predict_nodule_v3(tsh, tnod, eutirads,
                                                                       adeno, cyto, nod_bilat, scinti,
                                                                       enceinte, cancer_bilat, histo,
                                                                       color_n, style_n, color_e, style_e)
    st.title(prediction)
    st.graphviz_chart(create_nodule_tree(color_n, style_n, color_e, style_e))
    #st.image(create_nodule_tree(color_n, style_n, color_e, style_e), width=1200)

st.write("NB 1: L'algorithme de prise en charge se base sur le **consensus SFE-AFCE-SFMN 2022 sur la prise en charge des nodules thyroïdiens**.")
st.write("NB 2: L'utilisation est dédiée pour la prise en charge des nodules thyroïdiens. Il n'est pas à utiliser pour les autres pathologies thyroïdiennes telles que l'hypo ou l'hyperthyroïdie par exemple.")

