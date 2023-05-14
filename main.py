import streamlit as st
from nodule_tree_v2 import predict_nodule, first_tree_left, second_tree
from display_func import display_results, prepare_button_display, display_encinte_scinti, display_other_parameters, display_first_parameters

if 'show_hidden' not in st.session_state:
    st.session_state['show_hidden'] = False
if 'show_hidden_2' not in st.session_state:
    st.session_state['show_hidden_2'] = False

color_n = ['black' for _ in range(32)]
style_n = ['solid' for _ in range(32)]
color_e = ['black' for _ in range(36)]
style_e = ['solid' for _ in range(36)]

st.title("Outil pour l'aide dans la prise en charge thérapeutique des nodules thyroïdiens")

tsh, tnod, eutirads = display_first_parameters()

placeholder = st.empty()
bouton_run = placeholder.button('Run', key='button_1')

if bouton_run or st.session_state['show_hidden'] or st.session_state['show_hidden_2']:
    prediction_1, color_n, color_e, style_n, style_e = predict_nodule(tsh, tnod, eutirads, color_n, style_n,
                                                                    color_e, style_e)
    if prediction_1 != 'second_tree' and prediction_1 != 'first_tree_left':
        st.session_state['show_hidden'] = False
        st.session_state['show_hidden_2'] = False
        display_results(prediction_1, color_n, style_n, color_e, style_e)

    else:
        st.session_state['show_hidden'] = True
        st.text('Please enter additional information')
        enceinte, scinti = display_encinte_scinti()
        bouton_run_2, placeholder_2 = prepare_button_display(placeholder, 'button_2')
        if bouton_run_2 or st.session_state['show_hidden_2']:
            st.session_state['show_hidden'] = False
            prediction_2, _, _, _, _ = first_tree_left(scinti, enceinte, color_n, style_n, color_e, style_e)
            if prediction_2 == 'second_tree':
                _, color_n, color_e, style_n, style_e = first_tree_left(scinti, enceinte, color_n, style_n, color_e,
                                                                        style_e)
            if prediction_1 != 'second_tree' and prediction_2 != 'second_tree':
                prediction_2, color_n, color_e, style_n, style_e = first_tree_left(scinti, enceinte, color_n, style_n,
                                                                                 color_e, style_e)
                display_results(prediction_2, color_n, style_n, color_e, style_e)

            else:
                st.session_state['show_hidden_2'] = True
                st.text('Please enter additional information')
                nod_bilat, cancer_bilat, adeno, cyto, histo = display_other_parameters()
                bouton_run_3, placeholder_3 = prepare_button_display(placeholder_2, 'button_3')
                if bouton_run_3:
                    prediction_3, color_n, color_e, style_n, style_e = second_tree(cyto, nod_bilat, tnod, adeno, cancer_bilat,
                                                                                 histo, color_n, style_n, color_e, style_e)
                    display_results(prediction_3, color_n, style_n, color_e, style_e)


st.write("NB 1: L'algorithme de prise en charge se base sur le **consensus SFE-AFCE-SFMN 2022 sur la prise en charge des nodules thyroïdiens**.")
st.write("NB 2: L'utilisation est dédiée pour la prise en charge des nodules thyroïdiens. Il n'est pas à utiliser pour les autres pathologies thyroïdiennes telles que l'hypo ou l'hyperthyroïdie par exemple.")
