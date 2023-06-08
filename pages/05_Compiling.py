import time
import streamlit as st

from pages.sidebar import sidebar
from services import compile_service

state = st.session_state

st.set_page_config(
    page_title="Compiling",
    layout="wide"
)

state = st.session_state

# mocking for dev only
state.model = "Face recognition"
state.model_id = 1

def compile(*args):
    with st.spinner("Compiling..."):
        time.sleep(1)
        compiler = {"model_id": args[0],
                    "quant": args[1],
                    "c_array": args[2]
        }
        response = compile_service.compile_model(compiler)
        # add compiled model id to state
        state.compiled_model_id = 0.5 # mock
        st.success(response)


st.header("Available compiled models")
compiled_models = compile_service.get_compiled_models()

st.write(compiled_models)


def compilation_tab():
    st.header("Compilation settings")    
    st.write("Hello")
    quant = st.selectbox("Quantization", [
        "no quantization", "quantization", "end-to-end 8bit quantization"
    ])

    c_array = st.selectbox("Generate C array model", [
        "Yes", "No"
        ])

    if "model" not in state:
        st.error("No model selected.")
    else:
        st.button("Compile", on_click=compile, args=(str(state.model_id), quant, c_array))

def main():
    compilation_tab()

main()

sidebar.load_side_bar()

st.header("Model compilation makes them tiny")
