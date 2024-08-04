import streamlit as st
import time
import random
import datetime

# Função para gerar uma cor aleatória
def get_random_color():
    return random.choice(['red', 'blue'])


st.title("Reaction time Game")

# Armazenar o estado da cor e o tempo quando a cor apareceu
if 'color' not in st.session_state:
    st.session_state.color = None
    st.session_state.time_color_appeared = None
    st.session_state.time_user_tapped = None

if 'tap_time' not in st.session_state:
    st.session_state.tap_time = None

# Botão para aumentar o volume
button = st.button('Start')
if button:
    # Atraso aleatório entre 1 e 4 segundos
    delay = random.uniform(1, 4)
    time.sleep(delay)

    # Exibir a cor aleatória
    st.session_state.color = get_random_color()
    st.session_state.time_color_appeared = time.time()
    
    st.write(f"Color appeared: {st.session_state.color}")

# Display color and detect user tap
if st.session_state.color:
    # Exibir a cor na tela
    st.markdown(
        f"<div style='width:300px; height:300px; background-color:{st.session_state.color};'></div>",
        unsafe_allow_html=True
    )

    # Registrar o tempo em que o usuário tocou na tela
    if st.button('Stop'):
        st.session_state.time_user_tapped = time.time()
        if st.session_state.time_color_appeared:
            time_elapsed = st.session_state.time_user_tapped - st.session_state.time_color_appeared
            # Salvar o tempo em um arquivo txt
            with open("reaction_times.txt", "a") as f:
                f.write(f"{datetime.datetime.now()}: {time_elapsed:.2f} seconds\n")
            st.write(f"Time elapsed: {time_elapsed:.2f} seconds")

        # Reset the state for next round
        st.session_state.color = None
        st.session_state.time_color_appeared = None
        st.session_state.time_user_tapped = None
