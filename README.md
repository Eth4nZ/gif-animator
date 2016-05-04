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
</code></pre>

