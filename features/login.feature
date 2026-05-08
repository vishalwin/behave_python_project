Feature: login

Scenario: Successfull login
Given  user launches browser
When user enter username and password
And clicks login button
Then user should navigate to home page