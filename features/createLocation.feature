Feature: Create Location

    Background:
        Given Launch the browser
        When open the website
        Then Login page opened
        And Provide the username "nitesharya37@gmail.com" and password "12345678"
        And Click on the Login button
        And Validate Login

    Scenario:
        Then Navigate to Location tab
        And Click on Create button
        Then Enter the details for creating Location
        Then Click on Create
        # Then Go back to Location
        
        