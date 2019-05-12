Anidraw
==

Anidraw is a GIMP plugin inspired by Game Maker Studio 2's [draw while animating](https://youtu.be/VRPln502FO4?t=79) feature.  
In order to use it, go to Image -> Anidraw -> Start..., specify your desired
framerate and hit 'Ok'. Anidraw will now cycle through all layers in your image and you can draw as it cycles them.  
To stop Anidraw go to Image -> Anidraw -> Stop.  

Known issues:
  - [GIMP does not begin drawing on newly selected layers](https://gitlab.gnome.org/GNOME/gimp/issues/3374), so drawing must be done in quick strokes until this is fixed
  - GIMP does not wait for the image to refresh and so larger images may not appear in their entirety
  - Versions of GIMP prior to 2.10 will experience memory corruption
  - The dialog box remains
