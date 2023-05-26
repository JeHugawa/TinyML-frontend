*** Settings ***
Resource          resource.robot
Suite Setup       Open Browser With DeviceUrl

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

Check That Register Device Button Opens Form
    Page Should Not Contain     Add a new device
    Click Button    Register this device
    Page Should Contain    Add a new device
