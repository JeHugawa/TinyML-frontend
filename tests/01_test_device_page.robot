
*** Settings ***
Resource          resource.robot
Suite Setup       Open Browser With DeviceUrl
Suite Teardown    Close Browser

*** Test Cases ***

Check That Register A Bridging Device Button Opens A Form
    Wait Until Page Contains    Register a bridging device
    Click Element    //*[contains(text(),"Register a bridging device")]
    Page Should Contain    IP address or URL of the bridging server
    Page Should Contain    Name of server (Optional)

Check Registering A Bridging Device Without An IP Address Results In Error
    Click Element    //*[contains(text(),"Add")]
    Wait Until Page Contains    Please enter IP address or URL of bridge.

# Check Registering A Bridging Device With Invalid IP Address Results In Error
# Check Bridgind Device Can Be Added With A Valid IP Address
# Checks including the Name of Server

Check Header For Connected Devices Table
    Page Should Contain    Connected devices

Check Clicking Register This Device Opens Up A Form
    Click Element    //*[contains(text(),"Register this device")]
    Page Should Contain    Add a new device

# Add tests for adding a new device with different valid and invalid parameters
# Test that clicking 'Add' works when adding a new device

Check Clicking Cancel When Registering A Device Cancels The Form
    Click Element    //*[contains(text(),"Cancel")]
    Page Should Not Contain    Add a new device

Check Header For All Registered Bridges Table
    Wait Until Page Contains    All registered bridges

# Add tests for removing and selecting a registered bridge

Check Header For All Registered Devices Table
    Wait Until Page Contains    All registered devices

# Add tests for removing, modifying and selecting registered devices

Check That All Registered Bridges Table Is Not Empty
    Wait Until Page Contains Element    xpath://*[text()="Remove bridge"]    10

Check That All Registered Devices Table Is Not Empty
    Wait Until Page Contains Element    xpath://*[text()="Remove device"]    10

Check That Device Can Be Selected
    Wait Until Page Contains Element    xpath://*[text()="Select device"]
    @{select_device_buttons}=    Get WebElements    xpath://*[text()="Select device"]
    Wait Until Page Contains Element    ${select_device_buttons[-1]}
    Click Element    ${select_device_buttons[-1]}
    Page Should Contain    You have selected

Check That There Is A Connected Device
    Page Should Contain    Nano 33 BLE

Check Header For Connected Devices
    Page Should Contain    Connected devices

Check For Register This Device Button
    Page Should Contain Button    Register this device

Remove Last Registered Bridge In The All Registered Bridges List Test 
    Wait Until Page Contains Element    xpath://*[text()="Remove bridge"]    30
    @{delete_bridge_buttons}=    Get WebElements    xpath://*[text()="Remove bridge"]
    Wait Until Page Contains Element    ${delete_bridge_buttons[-1]}
    Click Element    ${delete_bridge_buttons[-1]}
    Wait Until Page Contains    Bridge removed successfully.

Remove Last Registered Device In The All Registered Devices List Test 
    Wait Until Page Contains Element    xpath://*[text()="Remove device"]    30
    @{delete_device_buttons}=    Get WebElements    xpath://*[text()="Remove device"]
    Wait Until Page Contains Element   ${delete_device_buttons[-1]}
    Click Element    ${delete_device_buttons[-1]}
    Wait Until Page Contains    Device removed successfully.

Check That Register This Device Button Opens Form
    Click Element    //*[contains(text(),"Register this device")]
    Wait Until Page Contains    Add a new device

Check Page Contains Register A Bridge
    Wait Until Page Contains    Register a bridging device

    
