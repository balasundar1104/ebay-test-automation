Feature: Search the products on Ebay

  Scenario Template: Access a Product via category after applying multiple filters
    Given : Go to ebay.com on the browser
    Then : Search Electronics on the Ebay.com Website
    Then : Clear the Electronics search from the search bar
    When : Search the new category after clearing the old search category
    Then : Search the new category as Cellphones & Accessories
    Then : Select cell phones and smart phones option on the left side navigation panel
    Then : Select see all button under the brand filter
    Then : Select the filters for Screen Size, Brand and item location
    When : Click apply when after applying all the filter
