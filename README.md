![Logo](/Client/img/logo.ico?raw=true "GroupYT")

# GroupYT
YouTube channel management for communities and groups

Have you ever wanted to build large (or small) team so you can help your channel grow, but you were afraid of giving away
your Google account password? Yes? Then you are in the right place! GroupYT can offer you a client to server interaction between
your uploaders and you.

## How does it work?

They upload video from their computer to your server (any linux distro VPS will do the trick), it gets
uploaded FROM SERVER to your YouTube channel, but flagged as "private", so you can review it and set it to "Public" later. 

*p.s. server script uses Google's OAuth2 to upload video to channel, so you are pretty much safe since your username and password
are not shown to user, nor script itself has way to determine your credentials.*

**I highly recommend you to make separate account for GroupYT on your server, due to security reasons.**

### Why GroupYT has to upload video to server instead of directly uploading it to YouTube?

I decided to make it like this because of security concerns. I was afraid of certain reverse engineering methods that could
harm you and your channel, so this is safest way to do this (probably, I'll make this optional in future releases).

## What are your plans for future?

I have many ideas, but I'll list most-important ones below:

* Make server script actually usable (around 50% done)
* Fix progress bar and make live status of on-going upload process
* Make it more configurable, adding config file AND "Options" menu (I'll add stuff like upload in background etc.)
* UI upgrade (it looks terrible now, I know)
* and more...

Having trouble setting this up? You've got questions for me? Hit me up on: brix1996[at]gmail.com !


