# Reddit Auto Post
> Automatically post on a subreddit

This is an easy to configure way to post on a subreddit (Reddit). There is only 1 file to configure and installation is explained very detailed.

![Official Reddit Icon](assets/reddit.png)

## Installation

Windows:
* Installing the required files
   * Clone this project to your local project folder
   ```
   $ git clone https://github.com/MobKill3r2006/RedditBotAutoPost.git
   ```
   * Go into the cloned folder
   ```
   $ cd RedditBotAutoPost
   ```
   * Install the requirements for the project
   ```
   $ pip install requirements.txt
   ```
* Creating the required assets on Reddit

   **The posts are made on the account that makes the app, so if you don't want the posts to show on your main account, I suggest you        create a second one**
   
   * Go to your [Reddit Apps](https://www.reddit.com/prefs/apps "Reddit Apps")
   * Click on **Create an(other) app**
   * Fill in a name and click on **Script**
   * Optional: Enter a description
   * The redirect uri is not used in this project, so you can just fill in something random like: **http://www.example.com**
   * Click create app
   Make sure to keep this page open as we need the information on it later.
* Modify ```config.json```
   * Open config.json
   * Edit the values to your personal information
   
   *Example of config.json*
   ```
   {
    "config": {
      "password": "password123",
      "client_id": "client_id123abc456def789",
      "client_secret": "client_secret123abc456def789",
      "username": "RedditUsername",
      "user_agent": "App description",
      "subreddit": "devreddit",
      "time": "21600",
      "title": "Post title shown on reddit"
    }
  }
  ```
     * Please note the following about `config.json`:
        * The `user_agent` isn't used for anything (As far as I know), so you can fill in something random or, this is what I do, a                description of the app
        * The `username` is your Reddit Username, not the app name
        * The `subreddit` is the name of the subreddit WITHOUT **r/**
        * The `time` is in seconds, and I suggest you don't post too often (once a day or if you have to once each few hours is                   recommended). In the example Im using 6 hours, 21600 seconds.
     * To change the body of the text, you have to go to `index.py` and change the value of `selftext = ""` to your body.
        * For text formatting visit [a formatting guide](https://www.reddit.com/r/HFY/wiki/ref/faq/formatting_guide "Formatting guide on           reddit")
   


## Usage example

After following the exact steps on how to install this project, you can finally try it out!
* Testing out the project!
  * I suggest changing the subreddit to `testingground4bots`, since it is a subreddit dedicated to bot spam, which is ideal for testing     our script!
  * Run `py index.py` to run our script
  * Go to [r/testingground4bots/new](http://www.reddit.com/r/testingground4bots/new "Testingground4bots subreddit") and check if you see your post!

**TO ACTUALLY AUTOMATICALLY POST YOU NEED TO HOST YOUR BOT ON A SERVER OR KEEP THE BOT RUNNING ON YOUR PC.** 
**SERVER RECOMMENDATION: [Heroku](http://heroku.com/ "Heroku.com")**

## Release History

* 1.0.0
    * First stable release

## Meta

[https://github.com/MobKill3r2006/](https://github.com/MobKill3r2006/ "My github page")
