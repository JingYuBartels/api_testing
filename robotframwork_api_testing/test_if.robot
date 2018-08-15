*** Settings ***
Library  RequestsLibrary
Library  Collections

*** Test Cases ***
test_get_event_list
    ${payload}  Create Dictionary   eid=1

    Create Session  event   http://127.0.0.1:8000/api
    ${r}=  Get Request  event  /get_event_list/  params=${payload}
    should be equal as strings  ${r.status_code}  200
    Log     ${r.json()}
    ${dict}  set variable  ${r.json()}
    ${msg}  get from dictionary  ${dict}  message
    should be equal  ${msg}  success
    ${sta}  get from dictionary  ${dict}  status
    ${status}  evaluate  int(200)
    should be equal  ${sta}  ${status}

test_user_sign_success

    ${headers}  create dictionary  Content-Type=application/json
    create session  sign  http://127.0.0.1:8000/api  ${headers}

    ${payload}  create dictionary  eid=11 phone=7894539956
    ${r}=  post request  sign  /user_sign/  data=${payload}
    should be equal as strings  ${r.status_code}  200
    log  ${r.json()}
    ${dict}  set variable  ${r.json()}
    ${msg}  get from dictionary  ${dict}  message
    should be equal  ${msg}  sign success
    ${sta}  get from dictionary  ${dict} status
    ${status}  evaluate  int(200)
    should be equal  ${sta}  ${status}





