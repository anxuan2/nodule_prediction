import streamlit as st
from tree_vizualization import create_nodule_tree
from nodule_tree_v2 import predict_nodule, second_tree

if 'show_hidden' not in st.session_state:
    st.session_state['show_hidden'] = False

color_n = ['black' for _ in range(32)]
style_n = ['solid' for _ in range(32)]
color_e = ['black' for _ in range(36)]
style_e = ['solid' for _ in range(36)]

st.title("Outil pour l'aide dans la prise en charge thérapeutique des nodules thyroïdiens")

col1, col2 = st.columns(2)
tsh = col1.number_input('TSH (mUI/L)', 0.00, 200.00)
tnod = col1.number_input('Taille du nodule (mm)', 0, 1000)
scinti = col1.selectbox('Scintigraphie', ('Non fait', "Présence d'un nodule autonome", 'Pas de nodule autonome'))
eutirads = col2.selectbox('Score EU-TIRADS', (2, 3, 4, 5))
enceinte = col2.selectbox('Femme enceinte / Projet grossesse / Nodule compressif', ('Non', 'Oui'))

placeholder = st.empty()
bouton_run = placeholder.button('Run', key='button_1')

if bouton_run or st.session_state['show_hidden']:
    prediction, color_n, color_e, style_n, style_e = predict_nodule(tsh, tnod, eutirads, scinti, enceinte, color_n,
                                                                    style_n, color_e, style_e)
    if type(prediction) == str:
        st.session_state['show_hidden'] = False
        st.title(prediction)
        tree = create_nodule_tree(color_n, style_n, color_e, style_e)
        st.image(tree, use_column_width=False, width=1000)
    else:
        placeholder.empty()
        st.text('Please enter additional information')
        col1, col2 = st.columns(2)
        st.session_state['show_hidden'] = True
        bouton_run_2 = st.button('Run', key='button_2')
        nod_bilat = col1.selectbox('Nodule bilatéreaux', ('Non', 'Oui, nodules bilatéraux compressifs',
                                                          'Oui, nodules bilatéraux non compressifs'))
        cancer_bilat = col1.selectbox('Cancer bilatéral ou Cancer isthmique', ('Non', 'Oui'))
        adeno = col2.selectbox('Adénopathies cervicales', ('cN0', 'cN1a', 'cN1b'))
        cyto = col2.selectbox('Cytologie : Score Bethesda', ('I', 'II', 'III', 'IV', 'V', 'VI', 'Non fait'))
        histo = col2.selectbox("Histologie (lors de l'examen extemporané)",
                               ('Non fait', "En faveur d'un carcinome papillaire", "En faveur d'un nodule bénin"))
        if bouton_run_2:
            prediction, color_n, color_e, style_n, style_e = second_tree(cyto, nod_bilat, tnod, adeno, cancer_bilat,
                                                                         histo, color_n, style_n, color_e, style_e)
            st.title(prediction)
            tree = create_nodule_tree(color_n, style_n, color_e, style_e)
            st.image(tree, use_column_width=False, width=1000)


st.write("NB 1: L'algorithme de prise en charge se base sur le **consensus SFE-AFCE-SFMN 2022 sur la prise en charge des nodules thyroïdiens**.")
st.write("NB 2: L'utilisation est dédiée pour la prise en charge des nodules thyroïdiens. Il n'est pas à utiliser pour les autres pathologies thyroïdiennes telles que l'hypo ou l'hyperthyroïdie par exemple.")
