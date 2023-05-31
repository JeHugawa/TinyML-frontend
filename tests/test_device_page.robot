
*** Settings ***
Resource          resource.robot
Suite Setup       Open Browser With DeviceUrl
Suite Teardown    Close Browser

*** Test Cases ***
Check Header For Registered Devices Table
    Wait Until Page Contains    All registered devices

Check That Registered Devices Table Is Not Empty
    Page Should Contain     Espressif ESP-EYE

Check That Device Can Be Selected
    Wait Until Page Contains Element    xpath://*[text()="Select"]

    @{select_buttons}=    Get WebElements    xpath://*[text()="Select"]

    Wait Until Page Contains Element    ${select_buttons[-1]}
    Click Element    ${select_buttons[-1]}
    Page Should Contain    You have selected


Check That There Is A Connected Device
    Page Should Contain    Nano 33 BLE

Check Header For Connected Devices
    Page Should Contain    Connected devices

Check For Add Device Button
    Page Should Contain Button    Register this device

Remove Last Device in the List Test 
    Wait Until Page Contains Element    xpath://*[text()="Remove"]

    @{delete_buttons}=    Get WebElements    xpath://*[text()="Remove"]


    Wait Until Page Contains Element    ${delete_buttons[-1]}
    Click Element    ${delete_buttons[-1]}
    Page Should Contain    Device removed successfully.

Check That Register Device Button Opens Form
    Page Should Not Contain     Add a new device
    Click Button    Register this device
    Page Should Contain    Add a new device

Check Page Contains Register A Bridge
    Page Should Contain    Register a bridging device

Check Form To Register Bridge Opens Up
    Page Should Not Contain    IP address of the bridging server
    Click Element        //*[contains(text(),'Register a bridging device')]
    Page Should Contain    IP address of the bridging server

Selecting A Bridge Is Successful
    Click Element    //*[contains(text(),"Select bridge")]
    Page Should Contain    Successfully selected bridge
