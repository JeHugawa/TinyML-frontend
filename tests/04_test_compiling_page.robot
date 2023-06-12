*** Settings ***
Resource          resource.robot
Suite Setup       Open Browser With CompilingUrl
Suite Teardown    Close Browser

*** Test Cases ***
Check Page Header
    Wait Until Page Contains    Compiling

Check That There Is Select A Model
    Page Should Contain    Select a trained model to compile.

Check That Page Contains Compiling Tab
    Page Should Contain    Compile a model

Select Model For Training
    Click Element    xpath://*[text()="Model"]
    Wait Until Page Contains    Select a model
    @{select_buttons}=    Get WebElements    xpath://*[text()="Select model"]


    Wait Until Page Contains Element    ${select_buttons[-1]}
    Click Element    ${select_buttons[-1]}
    Maximize Browser Window

    # käytä näitä klikataksesi sivupalkissa olevia linkkejä Device, Model 
    ${link_to_compiling}    Get WebElement    //*[text()="Compiling"]
    Execute Javascript    arguments[0].click();     ARGUMENTS    ${link_to_compiling} 
    
    Wait Until Page Contains    Compile a model

# Test Train A New Model
#    Input Text    xpath://input[@aria-label="Enter name for your model"]    Test
#    Input Text    xpath://input[@aria-label="Enter the number of epochs"]    1
#    Input Text    xpath://input[@aria-label="Enter the batch size"]    1
#    Input Text    xpath://input[@aria-label="Enter image width"]    96
#    Input Text    xpath://input[@aria-label="Enter image height"]    96

#    Click Element    xpath://*[text()="Sparse Categorical crossentropy"]

#    Click Element    xpath://*[text()="Train"]

#    Wait Until Page Contains    Model trained successfully!    30

# Select Trained Model
#    Input Text    xpath://input[@aria-label="Enter name for your model"]    Test
#    Input Text    xpath://input[@aria-label="Enter the number of epochs"]    1
#    Input Text    xpath://input[@aria-label="Enter the batch size"]    1
#    Input Text    xpath://input[@aria-label="Enter image width"]    96
#    Input Text    xpath://input[@aria-label="Enter image height"]    96

#    Click Element    xpath://*[text()="Sparse Categorical crossentropy"]

#    Click Element    xpath://*[text()="Train"]

#    Wait Until Page Contains    Model trained successfully!    30
   
#    ${link_to_models}    Get WebElement    //*[text()="Model"]
#    Execute Javascript    arguments[0].click();     ARGUMENTS    ${link_to_models}
   
#    Wait Until Page Contains    Train a model
#    @{select_model_buttons}=    Get WebElements    xpath://*[text()="Select model"]
#    Wait Until Page Contains Element    ${select_model_buttons[-1]} 
#    Click Element    ${select_model_buttons[-1]}
#    Page should Contain    Selected model
   