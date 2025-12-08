**Ouedkniss GraphQL Endpoint: `listingMenu`**
=============================================

**Endpoint**
------------

`POST https://api.ouedkniss.com/graphql`

**Description**
---------------

The `listingMenu` GraphQL query retrieves the **main category menu** of Ouedkniss.\
It includes all top-level categories (e.g., "Immobilier", "Automobiles & Véhicules", "Téléphones & Accessoires"), along with metadata, icons, and internal IDs.

This is the starting point for scraping Ouedkniss listings by category.

* * * * *

**Request Headers**
-------------------

| Header | Value |
| --- | --- |
| accept | */* |
| accept-language | fr |
| authorization | *(empty for public access)* |
| content-type | application/json |
| locale | fr |
| origin | <https://www.ouedkniss.com> |
| referer | <https://www.ouedkniss.com/> |
| sec-ch-ua | "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99" |
| sec-ch-ua-mobile | ?0 |
| sec-ch-ua-platform | "Windows" |
| sec-fetch-dest | empty |
| sec-fetch-mode | cors |
| sec-fetch-site | same-site |
| user-agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome |
| x-app-version | "3.3.70" |
| x-referer | <https://www.ouedkniss.com/> |
| x-track-id | 40032f33-5178-4241-8fa6-60589683b9a9 |
| x-track-timestamp | 1765214181 |

> ⚠ Note: `authorization` header is empty, meaning the endpoint is **publicly accessible** without login.

* * * * *

**GraphQL Query**
-----------------

`query listingMenu($menuFilter: MenuFilterInput) {
  listingMenu: menuFetch(menuFilter: $menuFilter) {
    id
    name
    icon {
      light
      dark
      __typename
    }
    target {
      ... on Category {
        id
        name
        slug
        icon
        active
        rank
        delivery
        __typename
      }
      __typename
    }
    rank
    __typename
  }
}`

### **Variables**

`{
  "menuFilter": {
    "menuType": "LISTING_MENU"
  }
}`

* * * * *

**Response Structure**
----------------------

| Field | Type | Description |
| --- | --- | --- |
| `listingMenu` | Array | List of top-level menu items |
| `id` | String | Menu ID (internal) |
| `name` | String | Menu display name |
| `icon.light` | String | Light-mode icon URL |
| `icon.dark` | String | Dark-mode icon URL |
| `target.id` | String | Category ID |
| `target.name` | String | Category name |
| `target.slug` | String | Category URL slug |
| `target.icon` | String | Category icon URL |
| `target.active` | Boolean | Whether the category is active |
| `target.rank` | Int | Display rank |
| `target.delivery` | Boolean | Whether delivery is available for this category |
| `rank` | Int | Menu rank |
| `__typename` | String | GraphQL type info (always "Menu" or "Category") |

* * * * *

**Example Response**
--------------------

`{
  "data": {
    "listingMenu": [
      {
        "id": "4624",
        "name": "Immobilier",
        "icon": {
          "light": "https://cdn.ouedkniss.com/medias/images/k5/W9tzqU2LaDwmGY5JEXgRiyS0nUX7Qm2vUGfEV7OQ.png",
          "dark": "https://cdn.ouedkniss.com/medias/images/k5/IxXChgSA24BM5Vi3CSjSK0GrAinicksPwy4YbXcQ.png"
        },
        "target": {
          "id": "62",
          "name": "Immobilier",
          "slug": "immobilier",
          "icon": "https://cdn.ouedkniss.com/medias/images/k5/XY769APEVh0qPjDjHn7MtmdNt3wU2cx9BlG91kr6.png",
          "active": true,
          "rank": 1,
          "delivery": false
        },
        "rank": 5
      }
      // ... other categories
    ]
  }
}`

* * * * *

**Usage Notes**
---------------

-   This query is **read-only** and publicly accessible.

-   Returned categories contain `id` and `slug`, which are needed to fetch **listings per category**.

-   The `rank` field can be used to sort categories by display order.

-   `icon` URLs can be used for dashboards or visualization.