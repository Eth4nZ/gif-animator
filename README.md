# gif-animator


##copy all your image into <pre><code>/img
</code></pre>

###resize it
<pre><code>mogrify -resize 50% \*.png

###crop & add text over images
<pre><code>python crop.py
</code></pre>

###generate gif
<pre><code>convert -delay 20 -loop 0 \*.png animation.gif

