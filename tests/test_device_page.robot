*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        headlessfirefox
${DELAY}          0.10 seconds
${URL}            http://localhost:8501/Device/

*** Test Cases ***
Check Header For Registered Devices Table
    Open Browser    ${URL}    ${BROWSER}
    Wait Until Page Contains    All registered devices
    Close Browser

Check That Registered Devices Table Is Not Empty
    Open Browser    ${URL}    ${BROWSER}
    Wait Until Page Contains     Espressif ESP-EYE
    # Get Table Cell    locator    1    1


Remove Last Device in the List Test
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed              ${DELAY}
    Go To                           ${URL}    
    
    Wait Until Page Contains Element    xpath://*[text()="Remove"]

    @{delete_buttons}=    Get WebElements    xpath://*[text()="Remove"]

    Wait Until Page Contains Element    ${delete_buttons[-1]}
    Click Element    ${delete_buttons[-1]}
    Page Should Not Contain    remove me
    Close Browser

