import streamlit as st
from datetime import datetime
from pages.sidebar import sidebar
from services import model_service

state = st.session_state

st.set_page_config(
    page_title="Model",
    layout="wide"
)

sidebar.load_side_bar()


def load_page_info(info):
    col = st.columns(4)
    col[0].title(info)
    with col[-1].expander("ℹ️ Help"):
        st.markdown(
            "On this page you can select an already trained model or train an image classifier.")
        st.markdown(
            "Set the parameters for training and click the train button.")
        st.markdown("[See the doc page for more info](/Documentation)")
    st.header("Select a model")


def select_model(*args):
    state.model = {
        "id": args[0],
        "description": args[1],
        "parameters": args[2],
        "dataset_id": args[3],
        "created": args[4]
    }
    st.success(f"Selected model {state.model['description']}")


def list_trained_models():
    models = model_service.get_models()

    col = st.columns(11)
    col[0].write("ID")
    col[1].write("Description")
    col[2].write("Epochs")
    col[3].write("Batch size")
    col[4].write("Dataset")
    col[5].write("Created")
    for model in models:
        col = st.columns(11)
        dataset_id, parameters, description, id, created, _ = model.values()
        created = datetime.fromisoformat(created)
        created = created.strftime("%d/%m/%Y %H:%M")
        col[0].write(id)
        col[1].write(description)
        col[2].write(parameters["epochs"])
        col[3].write(parameters["batch_size"])
        col[4].write(dataset_id)
        col[5].write(created)
        col[6].button("Select model", key=f"s_{id}_{description}",
                      on_click=select_model,
                      args=(
                          id, description, parameters, dataset_id, created
                      ))


def training():
    st.header("Train a model")
    if "dataset" not in state:
        st.error("No dataset was selected. Please select one on the Data page.")
        return

    st.write(
        ":red[Loss function can only choose Sparce Categorical crossentropy, other one fails]")
    st.subheader("Model Training Settings")
    model_name = st.text_input("Enter name for your model")
    epochs = st.number_input("Enter the number of epochs", min_value=int(0))
    batch_size = st.number_input("Enter the batch size", min_value=int(0))
    img_width = st.number_input("Enter image width", min_value=int(0))
    img_height = st.number_input(
        "Enter image height", min_value=int(0))
    loss_function = st.radio(
        "Choose a loss function", ("Categorical crossentropy", "Sparse Categorical crossentropy"))

# drawing stuff
    if st.button("Train"):
        with st.spinner("Training..."):
            plot = st.empty()
            test = st.empty()
            parameters = {
                "epochs": epochs,
                "img_width": img_width,
                "img_height": img_height,
                "batch_size": batch_size
            }
            model = model_service.train_model(
                state.dataset["id"], model_name, parameters, loss_function)
        if type(model) != list:
            st.error(
                f"Error while training model {model['detail'][0]['loc'][1]}")
        st.success("Model trained successfully!")

        state.model = model[2]
        plot.image(model[1])
        test.image(model[0], caption=model[2]["prediction"])


def main():
    load_page_info("Models")

    list_trained_models()

    training()


main()
