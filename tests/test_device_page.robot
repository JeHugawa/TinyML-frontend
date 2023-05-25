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


