*** Settings ***
Resource          resource.robot
Suite Setup       Open Browser With InstallingURL
Suite Teardown    Close Browser

*** Test Cases ***
Check Header
    Wait Until Page Contains    Install model to MCU

Check Page Has Errors
    Page Should Contain    Please select a compiled model
    Page Should Contain    Please select a bridge
    Page Should Contain    Please select a device

# Select compiled model, bridge and device so that installing allows you
# to continue

Select Compiled Model And Bridge And Device    
    ${link_to_devices}    Get WebElement    //*[text()="Device"]
    Execute Javascript    arguments[0].click();     ARGUMENTS    ${link_to_devices} 
    
    Wait Until Page Contains    Device

    # Select device        
    Wait Until Page Contains Element    xpath://*[text()="Select device"]
    @{select_device_buttons}=    Get WebElements    xpath://*[text()="Select device"]
    Wait Until Page Contains Element    ${select_device_buttons[-1]}
    Click Element    ${select_device_buttons[-1]}
    Page Should Contain    You have selected

    # Select Bridge
    Wait Until Page Contains Element    xpath://*[text()="Select bridge"]
    ${select_bridge_buttons}    Get WebElements    xpath://*[text()="Select bridge"]
    Wait Until Page Contains Element    ${select_bridge_buttons[-1]}
    Execute Javascript    arguments[0].click();    ARGUMENTS    ${select_bridge_buttons[-1]}

    # Select compiled model
    ${link_to_compilation}    Get WebElement    //*[text()="Compiling"]
    Execute Javascript    arguments[0].click();     ARGUMENTS    ${link_to_compilation} 

    Wait Until Page Contains Element    xpath://*[text()="Select model"]
    ${select_compiled_buttons}    Get WebElements    xpath://*[text()="Select model"]
    Wait Until Page Contains Element    ${select_compiled_buttons[-1]}
    Execute Javascript    arguments[0].click();    ARGUMENTS    ${select_compiled_buttons[-1]}

    ${link_to_installing}    Get WebElement    //*[text()="Installing"]
    Execute Javascript    arguments[0].click();     ARGUMENTS    ${link_to_installing} 

Check For Install Button
    Wait Until Page Contains Element    xpath://*[text()="Install"]

Install To Device
    ${install_button}    Get WebElement    //p[text()="Install"]
    Wait Until Page Contains Element    ${install_button}
    Execute Javascript    arguments[0].click();    ARGUMENTS    ${install_button}
    Wait Until Page Contains    Model has been installed successfully to device