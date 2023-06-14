*** Settings ***
Resource            resource.robot
Suite Setup         Open Browser With DataUrl
Suite Teardown      Close Browser

*** Test Cases ***
Check Page Header
    Wait Until Page Contains    Data


Check That Page Contains Datasets
    Page Should Contain     Existing datasets


Check That Page Contains Adding New Dataset
    Page Should Contain     Add new dataset


Test Adding New Dataset
  Input Text    xpath://input[@aria-label="Dataset name"]    Test
  Input Text    xpath://input[@aria-label="Description for dataset (optional)"]     asdf
  Choose File   xpath://section[@aria-label="Choose image files"]/input    ${CURDIR}/test_image.png
  

  Click Element     xpath://*[text()="Add"]
  Wait Until Page Contains  New dataset added with images   15


Select Dataset
    @{select_buttons}=    Get WebElements   xpath://*[text()="Select"]


    Wait Until Page Contains Element    ${select_buttons[-1]}
    Click Element   ${select_buttons[-1]}
    Maximize Browser Window
