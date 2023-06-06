import streamlit as st
from services import training_service

st.set_page_config(
    page_title="Training",
    layout="wide"
)

st.header("Model Training Camp")

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
    if "dataset_name" not in st.session_state:
        st.error("No dataset was selected. Please select one on the Data page.")
        return

    #model_path = st.session_state.selected_model["Model Path"]
    #train = (st.session_state.selected_dataset, model_path)
    #st.write(
    #    ":red[Training can say successful, but prediction has keyerror 0 and it fails NOTE! DO NOT SELECT CAR DETECTION AND FACE RECOGNITION!]")
    #st.subheader('Train a Keras model')

    st.write(
        ":red[Loss function can only choose Sparce Categorical crossentropy, other one fails]")
    st.subheader("Model Training Settings")
    model_name = st.text_input("Enter name for your model")
    epochs = st.number_input("Enter the number of epochs", min_value=int(0))
    batch_size = st.number_input("Enter the batch size", min_value=int(0))
    img_width = st.number_input("Enter image width", min_value=int(0))
    img_height = st.number_input(
    "Enter image height", min_value=int(0))
    loss_function = st.radio("Choose a loss function", ("Categorical crossentropy", "Sparse Categorical crossentropy"))
    
#drawing stuff
    if st.button("Train"):
        with st.spinner("Training..."):
            plot = st.empty()
            test = st.empty()
            model = training_service.train_model(
                state.dataset_id, model_name, epochs, img_width, img_height, batch_size, loss_function)
        st.success("Model trained successfully!")

        data = train.plot_statistics(
            history, epochs_range)
        tests, label = train.prediction(
            model, train_ds.class_names)
        if 'model' not in st.session_state:
            st.session_state.model = model
        plot.image(data)
        test.image(tests, caption=label)
        model.save(f"{model_path}/keras_model")
        st.success("Model saved!")


page_info('Training')
training_page()
