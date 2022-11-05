Feature: Hotel_Module
  Background: Common Steps
    Given Open the browser and enter the valid url
    When  Click on hotel button


  Scenario Outline:User should be search hotels in the application successfully
    When   Click on india radio button
    When   Enter the city name"<city_name>"
    When   Select check in  and check out dates
    When   Select number of guests and rooms
    When   Click on search button
    When   Click on search location and enter hotel name "<Hotel_name>"
    When   Click on view room options and select room
    When   Enter guest First name "<first_name>"
    When   Enter guest Last name "<last_name>"
    When   Enter guest Email ID "<email_id>"
    When   Enter guest Mobile number "<mb_number>"
    When   Proceed to payment option
    When   Enter Card number "<card_number>"
    When   Enter Name on card "<name_on_card>"
    When   Enter Expiry date "<exp_date>"
    When   Enter CVV "<cvv>"
    When   Click on Pay
    Then   Verify hotelpage should be displayed
    Examples:
    | city_name | Hotel_name  | first_name  | last_name | email_id  | mb_number | card_number | name_on_card  | exp_date  | cvv |
    | Mumbai    | Rester Xpress Santacruz | sourabh | Patil     | abc12@gmail.com | 9876543210  | 556454589654  | sourabh patil | 0423  |  986  |
    | Pune      | Hotel Dreamland|  Sourabh | Patil     | abc12@gmail.com | 9876543210  | 556454589654  | sourabh patil | 0423  |  986  |