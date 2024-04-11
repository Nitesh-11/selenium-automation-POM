Feature: Validate Login

    Background:
        Given Launch the browser
        When open the website
        Then Login page opened

    Scenario:
        And Provide the username "nitesharya37@gmail.com" and password "12345678"
        And Click on the Login button
        And Validate Login
        Then Close the browser