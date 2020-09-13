# Project Overview

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Incomplete
|Day 1| Deploy backend | Complete
|Day 1| Priority Matrix / Timeline | Incomplete
|Day 2| Working RestAPI | Incomplete
|Day 3| Core Application Structure | Incomplete
|Day 4| MVP & Bug Fixes | Incomplete
|Day 5| Final Touches and Present | Incomplete


## Project Description
TO-DO APP

An app that allows the user to sign in and organize their to-do's, with an option of making them public
or private.

USER STORY:
The user will login and have access to create, edit and destroy their to-do's. The list could be 
viewed by others if set to public.

POST MVP:
Multiple visitors will be able to login and leave their comments on to-do's.


## App Build-out Links 
[Front-end deployed URL](https://https://gifted-varahamihira-15a125.netlify.app/#/)

[Front-end GitHub Repo](https://https://github.com/Kenal-Ortega/p4frontend)

[Back-end deployed URL](https://https://p4backend93.herokuapp.com/)

[Back-end GitHub Repo](https://https://github.com/Kenal-Ortega/p4backend)


## Time/Priority Matrix 

[Time and Priority Matrix](https://res.cloudinary.com/dinqukx6a/image/upload/v1598235735/Project%203/Music_Journal_TPM_backend_i50jc6.jpg)



#### MVP

- Use ruby on rails 
- Use an sql database using postgres 
- Create editor login
- Allow editor full C.R.U.D functionality
- Deploy on heroku

#### PostMVP 

- Allow visitors login access 
- Allow visitors full C.R.U.D functionality for their posts

## Functional Components
#### MVP
| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Create user model | H | 1hr | .5hr | 2hr|
| Give user C.R.U.D functionality | H | 2hr | 6hr | 10hr|
| Authorize user | H | 2hr | .5hr | 2hr|
| Deploy to heroku | H | 1hr| .5hr | 1hr |
| Troubleshooting/Research| H | 10hr | 2hr | 10hr|
| Data modeling | H | 3hrs| .5hr | 1hr |
| Total | H | 19hrs| 2hrs | 26hrs |

#### PostMVP
| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Allow for multiple users | L | 3hr | 3hr | 3hr|
| Give users C.R.U.D functionality | L | 3hr | N/A | N/A|
| Add search functionality via tags | L | 5hr | N/A | N/A|
| Total | H | 11hrs| N/A | 3hrs |

 

## Code Snippet

Able to import a whole excell sheet as data.  

```
require 'csv'
csv_text = File.read(Rails.root.join('lib','seeds', 'journal_seed.csv'))
csv = CSV.parse(csv_text, :headers => true, :encoding => 'ISO-8859-1')

```

