*** Settings ***
Resource          resource.robot
Suite Setup       Open Browser With CompilingUrl
Suite Teardown    Close Browser

*** Test Cases ***
Check Page Header
    Wait Until Page Contains    Compiling

Check That A Trained Model Needs To Be Selected
    Page Should Contain    Select a trained model to compile.

Check That Page Contains Compiling Tab
    Page Should Contain    Compile a model

Select Model And Compile
    ${link_to_models}    Get WebElement    xpath://*[text()="Model"]
    Execute Javascript    arguments[0].click();     ARGUMENTS    ${link_to_models}

    Wait Until Page Contains    Select a model

    ${select_model}    Get WebElement    xpath://*[text()="Select model"]
    Execute Javascript    arguments[0].click();     ARGUMENTS    ${select_model}

    Page should Contain    Selected model

    ${link_to_compiling}    Get WebElement    xpath://*[text()="Compiling"]
    Execute Javascript    arguments[0].click();     ARGUMENTS    ${link_to_compiling}

    Page Should Contain    Compile a model

    Click Element    //*[contains(text(),"Start compiling")]

    Wait Until Page Contains    Model compiled succesfully.    30


 
   
   
    