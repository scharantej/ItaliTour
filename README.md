## Flask Application Design for a Travel Planner for Italy

### HTML Files

- **index.html**: The main page where the user inputs their travel preferences.
- **itinerary.html**: The page that displays the planned itinerary based on the user's preferences.
- **error.html**: The page that handles any errors that occur during the application's execution.

### Routes

**URL**: `/`
**Method**: `GET`
**View function**: `home`
**Purpose**: Renders the `index.html` page and allows the user to input their travel preferences.

**URL**: `/itinerary`
**Method**: `POST`
**View function**: `create_itinerary`
**Purpose**: Accepts the user's input and generates an itinerary based on their preferences. The itinerary is displayed on the `itinerary.html` page.

**URL**: `/error`
**Method**: `GET`
**View function**: `error`
**Purpose**: Handles any errors that occur during the application's execution and displays the `error.html` page.