**Ouedkniss GraphQL Endpoint: `listingMenu`**
=============================================

**Endpoint**
------------

`POST https://api.ouedkniss.com/graphql`

**listingMenu**
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

**SearchQuery**
---------------

The `SearchQuery` GraphQL query allows you to **search for announcements** (listings) on Ouedkniss.\
It returns paginated results for a given category, including detailed information such as title, description, media, store info, price, and location.

This query is used to fetch actual listings for a category, e.g., real estate (`immobilier`).

* * * * *

**Request Headers**
-------------------

Same as `listingMenu` endpoint, with an updated `x-referer` if needed:

| Header | Value |
| --- | --- |
| accept | */* |
| accept-language | fr |
| authorization | *(empty for public access)* |
| content-type | application/json |
| locale | fr |
| origin | <https://www.ouedkniss.com> |
| referer | https://www.ouedkniss.com/{category-slug} |
| sec-ch-ua | "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99" |
| sec-ch-ua-mobile | ?0 |
| sec-ch-ua-platform | "Windows" |
| sec-fetch-dest | empty |
| sec-fetch-mode | cors |
| sec-fetch-site | same-site |
| user-agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome |
| x-app-version | "3.3.70" |
| x-referer | https://www.ouedkniss.com/{category-slug} |
| x-track-id | 40032f33-5178-4241-8fa6-60589683b9a9 |
| x-track-timestamp | 1765214181 |

* * * * *

**GraphQL Query**
-----------------

`query SearchQuery($q: String, $filter: SearchFilterInput, $mediaSize: MediaSize = MEDIUM) {
  search(q: $q, filter: $filter) {
    announcements {
      data {
        ...AnnouncementContent
        smallDescription {
          specification {
            codename
          }
          valueText
        }
        noAdsense
      }
      paginatorInfo {
        lastPage
        hasMorePages
      }
    }
    active {
      category {
        id
        name
        slug
        icon
        delivery
        children {
          id
          name
          slug
          icon
        }
      }
      count
      filter {
        cities { id name }
        regions { id name }
      }
    }
    suggested {
      category {
        id
        name
        slug
        icon
      }
      count
    }
  }
}

fragment AnnouncementContent on Announcement {
  id
  title
  slug
  createdAt: refreshedAt
  isFromStore
  isCommentEnabled
  userReaction {
    isBookmarked
    isLiked
  }
  hasDelivery
  deliveryType
  paymentMethod
  likeCount
  description
  status
  cities { id name slug region { id name slug } }
  store { id name slug imageUrl isOfficial isVerified viewAsStore }
  user { id }
  defaultMedia(size: $mediaSize) { mediaUrl mimeType thumbnail }
  price
  pricePreview
  priceUnit
  oldPrice
  oldPricePreview
  priceType
  exchangeType
  category { id slug }
}`

* * * * *

**Variables Example**
---------------------

`{
  "mediaSize": "MEDIUM",
  "q": null,
  "filter": {
    "categorySlug": "immobilier",
    "origin": null,
    "connected": false,
    "delivery": null,
    "regionIds": [],
    "cityIds": [],
    "priceRange": [],
    "exchange": null,
    "hasPictures": false,
    "hasPrice": false,
    "priceUnit": null,
    "fields": [],
    "page": 1,
    "orderByField": { "field": "REFRESHED_AT" },
    "count": 48
  }
}`

* * * * *

**Response Structure**
----------------------

**Top-level fields**

| Field | Type | Description |
| --- | --- | --- |
| `announcements` | Object | Paginated list of announcements |
| `active` | Object | Active filters & categories |
| `suggested` | Array | Suggested categories |

**Announcement fields**

| Field | Type | Description |
| --- | --- | --- |
| id | String | Unique announcement ID |
| title | String | Announcement title |
| slug | String | URL-friendly title |
| createdAt | String | DateTime of announcement creation |
| isFromStore | Boolean | True if from a verified store |
| isCommentEnabled | Boolean | Comments enabled |
| userReaction | Object | Bookmark / like info |
| hasDelivery | Boolean | Delivery available |
| deliveryType | String | Delivery type |
| paymentMethod | String | Payment method |
| likeCount | Int | Number of likes |
| description | String | Full description |
| cities | Array | List of cities for the announcement |
| store | Object | Store info (if applicable) |
| user | Object | User info (if private ad) |
| defaultMedia | Object | Media content: URL, thumbnail, MIME type |
| price | Number | Price if available |
| pricePreview | Number | Preview price |
| priceUnit | String | Currency or unit (e.g., MILLION) |
| oldPrice | Number | Previous price if available |
| oldPricePreview | Number | Previous price preview |
| priceType | String | e.g., NEGOTIABLE |
| exchangeType | String | e.g., NOT_EXCHANGEABLE |
| category | Object | Category info (id, slug) |
| smallDescription | Array | Key features / specs |
| noAdsense | Boolean | True if no adsense |

**Paginator Info**

| Field | Type | Description |
| --- | --- | --- |
| lastPage | Int | Last page number |
| hasMorePages | Boolean | True if more pages are available |

* * * * *

✅ This is the **main endpoint for scraping listings** in a category.

-   Use `categorySlug` in `filter` to change the category.

-   Use `page` to paginate through all listings.

-   Each announcement contains **all essential info for scraping**, including media URLs, price, and city.