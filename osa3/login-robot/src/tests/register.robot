*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  matti  matti123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  koira1234
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kissa1234
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  karrikoira1243  kissa1234
    Output Should Contain  Username contains forbidden characters

Register With Valid Username And Too Short Password
    Input Credentials  karrikoira  kisu1
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kissakoira  pelkkiakirjaimia
    Output Should Contain  Password should not contain only alphabets

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123