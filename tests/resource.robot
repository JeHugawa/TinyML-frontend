*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        headlessfirefox
${DELAY}          0.05 seconds
${DeviceURL}      http://localhost:8501/Device/

*** Keywords ***
Open Browser With DeviceUrl    
	Open Browser    ${DeviceURL}    ${BROWSER}
	Set Selenium Speed	${DELAY}
