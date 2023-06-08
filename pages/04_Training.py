import streamlit as st
from services import training_service

from pages.sidebar import sidebar

state = st.session_state

st.set_page_config(
    page_title="Training",
    layout="wide"
)


st.header("Model Training Camp")

sidebar.load_side_bar()

state = st.session_state


def page_info(title):
    col = st.columns(4)
    col[0].title(title)
    with col[-1].expander("ℹ️ Help"):
        st.markdown("On this page you can train an image classifier.")
        st.markdown(
            "Set the parameters for training and click the train button.")
        st.markdown("[See the doc page for more info](/Documentation)")


def training_page():
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
            model = training_service.train_model(
                state.dataset["id"], model_name, parameters, loss_function)
        if type(model) != list:
            st.error(
                f"Error while training model {model['detail'][0]['loc'][1]}")
        st.success("Model trained successfully!")

        state.model = model[2]
        plot.image(model[1])
        test.image(model[0], caption=model[2]["prediction"])

        sidebar.load_side_bar()


page_info('Training')

training_page()
