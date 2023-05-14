import streamlit as st
from tree_vizualization import create_nodule_tree


def display_results(prediction, color_n, style_n, color_e, style_e):
    st.title(prediction)
    tree = create_nodule_tree(color_n, style_n, color_e, style_e)
    st.image(tree, use_column_width=False, width=1000)


def display_button(old_placeholder, unique_button_key):
    old_placeholder.empty()
    new_placeholder = st.empty()
    bouton_run = new_placeholder.button('Run', key=unique_button_key)
    return bouton_run, new_placeholder


def display_first_parameters():
    col1, col2 = st.columns(2)
    tsh = col1.number_input('TSH (mUI/L)', 0.00, 200.00)
    tnod = col1.number_input('Taille du nodule (mm)', 0, 1000)
    eutirads = col2.selectbox('Score EU-TIRADS', (2, 3, 4, 5))
    return tsh, tnod, eutirads


def display_encinte_scinti():
    col1, col2 = st.columns(2)
    enceinte = col2.selectbox('Femme enceinte / Projet grossesse / Nodule compressif', ('Non', 'Oui'))
    scinti = col1.selectbox('Scintigraphie',
                            ('Non fait', "Présence d'un nodule autonome", 'Pas de nodule autonome'))
    return enceinte, scinti


def display_other_parameters():
    col1, col2 = st.columns(2)
    nod_bilat = col1.selectbox('Nodule bilatéreaux', ('Non', 'Oui, nodules bilatéraux compressifs',
                                                      'Oui, nodules bilatéraux non compressifs'))
    cancer_bilat = col1.selectbox('Cancer bilatéral ou Cancer isthmique', ('Non', 'Oui'))
    adeno = col2.selectbox('Adénopathies cervicales', ('cN0', 'cN1a', 'cN1b'))
    cyto = col2.selectbox('Cytologie : Score Bethesda', ('I', 'II', 'III', 'IV', 'V', 'VI', 'Non fait'))
    histo = col1.selectbox("Histologie (lors de l'examen extemporané)",
                           ('Non fait', "En faveur d'un carcinome papillaire", "En faveur d'un nodule bénin"))
    return nod_bilat, cancer_bilat, adeno, cyto, histo
