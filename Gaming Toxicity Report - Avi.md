* Gaming Toxicity Report \- Avi  
* Initial Steps:  
  * Watched a couple hours of Twitch, looking for patterns that lead to toxicity to determine which games and types of streamers to get data from.  
  * Found [twitch-dl](https://github.com/ihabunek/twitch-dl) to download Twitch VODs via video ID  
* Pivot:  
  * Couldn’t use Twitch because of TOS so pivoted to Kick and spent a bit of time again scrolling through Kick to find patterns that lead to toxicity/data  
  * Eventually decided on games and needed to get links, Jayden recommended using Selenium IDE  
    * Via Selenium IDE, I would just open up to [kick.com](http://kick.com) and ran through a bunch of actions that would need to be taken to collect URLs (test files are included in Github repo)  
    * Using these test scripts, created a script (called kick\_scraper.py) that autonomously opens up Kick and begins to collect 18+ video URLs from the predetermined games.  
      * \*Note: To run the script simply type “python3 kick\_scraper.py” in the command line, but ensure that the ENGLISH macro has been set to the appropriate number on Kick. This can be determined by going to [https://kick.com/categories/games](https://kick.com/categories/games) and using the index at which English is displayed under the “Filter by” tab (uses 1 indexing, not 0 indexing)  
    * After creating kick\_scraper.py and running to get URLs, created another script called remove\_duplicates.py to consolidate multiple txt files without repeating links.  
* Face blurring:  
  * Ultimately cannot figure out anymore how to output a new mp4 file with blurred face, but was using [BlurryFaces](https://github.com/asmaamirkhan/BlurryFaces) with this [Tensorflow model](https://github.com/yeephycho/tensorflow-face-detection).