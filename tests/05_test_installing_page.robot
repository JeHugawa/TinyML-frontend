*** Settings ***
Resource          resource.robot
Suite Setup       Open Browser With InstallingURL
Suite Teardown    Close Browser

*** Test Cases ***
Check Header
    Wait Until Page Contains    Install model to MCU

Check For Install Button
    Wait Until Page Contains Element    xpath://*[text()="Install"]