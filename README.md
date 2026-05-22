# Project Overview

The project is about analyzing questions related to tiquets, prices, and shows in NYC.
Since we have seen a lot of the questions related to shopping, as well as the common interest of team members about different sports shows, venues and exploring a relatively challenging dataset the choice was made to work on this project collectively.

## Team Members & Roles

1. Alina Tsui - Technical Lead
2. Oussama Fathi - Team Lead
3. Ye Morris - Data Analyst
4. Lofinda Beynis - Data Analyst
5. Shaina Smith - Data Analyst
6. Khadija Bangura- Coordinator/Analyst

## Availabilities and Schedule

- Thursday/Friday Team:
    -- Alina Tsui
    -- Oussama Fathi
    -- Khadija Bangura

- Weekend Team:
    -- Khadija Bangura
    -- Ye morris
    -- Shaina Smith
    -- Lofinda Beynis

- Meetings:
    -- Friday Meeting with Instructor
    -- Friday Meeting with Instructor 
    -- Thursday Post Carreer class

### Dataset Overview Questions

**What does your dataset explore?**  
This dataset explores how Ticketmaster event ticket price ranges vary based on event characteristics such as location, venue, category, and date.  
The goal is to analyze pricing patterns across concerts, artist performances, and sports events.
We are looking into the possibility of analyzing prices, but if not enough data is available we might also choose other items for analysis.

**What is your dependent variable in the data you are pulling from?**  
The dependent variable is the ticket price for each event, taken from the `priceRanges` field in the Event Details endpoint.  
This can be represented as either `min_price` or `max_price` for each event.

**Is this variable categorical or quantitative?**  
The dependent variable is quantitative because it contains numeric price values.  
This makes it appropriate for regression analysis and price prediction.

**What are your independent variables?**  
The independent variables include city, state, country, genre, event date, venue, source, and days until the event.  
These variables are used to explain differences in ticket prices between events.

**Are these variables quantitative or categorical?**  
The dataset includes both categorical and quantitative independent variables.  
City, venue, genre, and source are categorical, while days until event and distance can be quantitative.

**How many independent variables do you have?**  
The dataset has more than 5 independent variables.  
A typical version of the dataset can include 8 to 10 predictors, which provides enough variation for EDA and predictive modeling.

**How large is your dataset?**  
The dataset can be expanded to more than 1,000 rows by paging through event search results and combining multiple API queries.  
The Ticketmaster Discovery API covers a large number of events, so building a dataset large enough for analysis is realistic.