*** Settings ***
Library           SeleniumLibrary
Library           BuiltIn

*** Variables ***
${BROWSER}        headlessfirefox
${DELAY}          0.5 seconds
${DeviceURL}      http://localhost:8501/Device/
${ModelURL}       http://localhost:8501/Model/
${CompilingURL}   http://localhost:8501/Compiling/
${ObservingURL}   http://localhost:8501/Observing/


*** Keywords ***
Open Browser With DeviceUrl    
	Open Browser    ${DeviceURL}    ${BROWSER}
	Set Selenium Speed	${DELAY}

Open Browser With ModelUrl
	Open Browser    ${ModelURL}    ${BROWSER}
	Set Selenium Speed	${DELAY}

Open Browser With CompilingUrl
  Open Browser    ${CompilingURL}    ${BROWSER}
	Set Selenium Speed	${DELAY}

Open Browser With ObservingUrl
  Open Browser    ${ObservingURL}    ${BROWSER}
	Set Selenium Speed	${DELAY}
