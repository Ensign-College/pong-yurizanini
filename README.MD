# It's Game Time 🎮
--------------
Join our discord: [![](https://dcbadge.vercel.app/api/server/CRRh5sBwDp)](https://discord.gg/CRRh5sBwDp)

Your initial assignment for this course is intentionally straightforward to ease you into game programming. Instead of starting from scratch, we'll take the Pong example discussed in 
class and enhance it by adding logic to control one or both paddles, making it possible to play the game solo. This approach will be typical for problem sets in this course: taking 
lecture code and extending it to provide you with ample experience in working with fully developed games. You can even utilize these projects as templates or starting points for your 
own game creations.

Please note that the code won't run without LÖVE installed. Therefore, you must also address the installation of LÖVE by selecting the appropriate version for your system at 
[https://love2d.org](https://love2d.org/). If you encounter issues running LÖVE on macOS due to it being "from an unidentified developer," refer to 
[support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac](http://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac) 
for guidance.

### For detailed instructions on running games, visit the following page: <https://love2d.org/wiki/Getting_Started>

Once you have downloaded and installed the code and LÖVE, the actual modification you'll make to the codebase is relatively minor. However, it will require a comprehensive understanding 
of many code components. Therefore, make sure to watch Lecture 0 and thoroughly review the code to gain a solid grasp of its workings before diving into the assignment. Pay particular 
attention to how paddle movement is handled, including both the Paddle class and the code in main.lua that controls movement through keyboard input. Consider what should drive the 
movement if our objective is for the AI agent to deflect the ball back toward the player.

## Specification
-------------

Your task is to implement an AI-controlled paddle (either the left or right paddle) so that it consistently attempts to deflect the ball. Since the paddle can only move along the 
Y-axis, you'll need to devise a strategy for keeping the paddle in sync with the ball's position. The code sections where keyboard input is detected for each paddle present a suitable 
location to insert the required logic. Once either the left or right paddle (or both, if preferred) autonomously attempt to deflect the ball, your assignment will be complete.

## Errata
------

During the time when the course lectures were recorded, an older version of LÖVE (0.10.2) was used. Most aspects remain unchanged in the newer version 11 series of the framework, but 
there is one notable core change: functions like love.graphics.clear, which previously accepted four integer arguments representing red, green, blue, and alpha components (or RGBA), now 
accept floating-point values between 0 and 1. For example, the previous API call:

love.graphics.clear(255, 0, 0, 255)

now translates to:

love.graphics.clear(1, 0, 0, 1)

To convert from the old style to the new style, simply divide the components by 255. For instance, if you had a color with components 120, 30, 70, and 255, you would represent it as 
follows:

love.graphics.clear(120/255, 30/255, 70/255, 255/255)

## Licenses
This course includes material adapted from the "Game Development" course by Harvard University, licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International 
License (CC BY-NC-SA 4.0).

For course materials and assignments adapted from Harvard's course, please see the attributions within each module or assignment for specific content sources. All adapted materials are 
used in compliance with the terms of the CC BY-NC-SA 4.0 license.

For more information about the license, visit: https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode#languages
