# gif-animator

###copy all your images into /img

###resize images
<pre><code>mogrify -resize 50% *.png
</code></pre>

###crop & add text over images
<pre><code>python crop.py
</code></pre>

###generate gif
<pre><code>convert -delay 20 -loop 0 *.png animation.gif
convert animation.gif -fuzz 5% -layers Optimize optimised.gif
</code></pre>

###generate mp4
<pre><code>ffmpeg -f image2 -r 6 -pattern_type glob -i '*.png' output.mp4
</code></pre>

