*** Settings ***
Resource          resource.robot
Suite Setup       Open Browser With ObservingUrl
Suite Teardown    Close Browser

*** Test Cases ***
Check Page Header
    Wait Until Page Contains    Observing

Check That A Bridge Needs To Be Selected
    Page Should Contain    Bridge not selected. Please select it on the device page.

Check That A Device Needs To Be Selected
    Page Should Contain    Select device to observe.

Select Bridge And Check That Device Still Needs To Be Selected
    ${link_to_devices}    Get WebElement    xpath://*[text()="Device"]
    Execute Javascript    arguments[0].click();     ARGUMENTS    ${link_to_devices}

    Wait Until Page Contains    All registered bridges

    ${select_bridge}    Get WebElement    //*[text()="Select bridge"]
    Click Element    ${select_bridge}
    
    Page Should Contain    Successfully selected bridge

    ${link_to_observing}    Get WebElement    xpath://*[text()="Observing"]
    Execute Javascript    arguments[0].click();     ARGUMENTS    ${link_to_observing}

    Page Should Contain    Select device to observe.

Select Device And Be Ready To Start Observing
    ${link_to_devices}    Get WebElement    xpath://*[text()="Device"]
    Execute Javascript    arguments[0].click();     ARGUMENTS    ${link_to_devices}

    Wait Until Page Contains    All registered bridges

    ${select_device}    Get WebElement    //*[text()="Select device"]
    Click Element    ${select_device}
    
    Page Should Contain    You have selected

    ${link_to_observing}    Get WebElement    xpath://*[text()="Observing"]
    Execute Javascript    arguments[0].click();     ARGUMENTS    ${link_to_observing}

    ${start_observing}     Get WebElement    xpath://*[text()="Start"]
    ${stop_observing}      Get WebElement    xpath://*[text()="Stop"]

    Page Should Contain Element     ${start_observing}
    Page Should Contain Element     ${stop_observing}

Start And Stop Observing
    ${start_observing}     Get WebElement    xpath://*[text()="Start"]
    ${stop_observing}      Get WebElement    xpath://*[text()="Stop"]

    Click Element    ${start_observing}

    Wait Until Page Contains    Image is target:
    
    Click Element    ${stop_observing}

    Page Should Not Contain    Image is target:


   
   
    