from datetime import datetime
import streamlit as st

from pages.sidebar import sidebar
from services import compile_service

state = st.session_state

st.set_page_config(
    page_title="Compiling",
    layout="wide"
)

state = st.session_state


def compile(*args):
    with st.spinner("Compiling..."):
        compiler = {"model_id": args[0],
                    "quant": args[1],
                    "c_array": args[2]
        }
        response = compile_service.compile_model(compiler)
        if response is not None:
            st.success("Model compiled succesfully.")
            state["compiled_model"] = response
        else:
            st.error("Could not compile model.")


def select_compiled_model(*args):
    state.compiled_model = {
        "id": args[0],
        "model_id": args[1],
        "created": args[2]
    }
    st.success(f"Selected model {state.compiled_model['id']}")


st.header("Available compiled models")

def list_compiled_models():
    compiled_models = compile_service.get_compiled_models()

    col = st.columns(11)
    col[0].write("ID")
    col[1].write("Parent model id")
    col[2].write("Created")
    for model in compiled_models:
        col = st.columns(11)
        created, model_id, path, id = model.values()
        created = datetime.fromisoformat(created)
        created = created.strftime("%d/%m/%Y %H:%M")
        col[0].write(id)
        col[1].write(model_id)
        col[2].write(created)
        col[3].button("Select model", key=f"s_{id}",
                      on_click=select_compiled_model,
                      args=(
                          id, model_id, created
                      ))


def compilation_tab():
    st.header("Compile a model")
    quant = st.selectbox("Quantization", [
        "no quantization", "quantization", "end-to-end 8bit quantization"
    ])

    c_array = st.selectbox("Generate C array model", [
        "Yes", "No"
        ])

    if "model" not in state:
        st.error("Select a trained model to compile.")
    else:
        st.button("Start compiling", on_click=compile, args=(str(state.model["id"]), quant, c_array))

def main():
    compilation_tab()
    list_compiled_models()
    sidebar.load_side_bar()

main()
