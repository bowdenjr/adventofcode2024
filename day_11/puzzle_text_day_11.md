<main>
<article class="day-desc"><h2>--- Day 11: Plutonian Pebbles ---</h2><p>The ancient civilization on <a href="/2019/day/20">Pluto</a> was known for its ability to manipulate spacetime, and while The Historians explore their infinite corridors, you've noticed a strange set of physics-defying stones.</p>
<p>At first glance, they seem like normal stones: they're arranged in a perfectly <em>straight line</em>, and each stone has a <em>number</em> engraved on it.</p>
<p>The strange part is that every time you <span title="No, they're not statues. Why do you ask?">blink</span>, the stones <em>change</em>.</p>
<p>Sometimes, the number engraved on a stone changes. Other times, a stone might <em>split in two</em>, causing all the other stones to shift over a bit to make room in their perfectly straight line.</p>
<p>As you observe them for a while, you find that the stones have a consistent behavior. Every time you blink, the stones each <em>simultaneously</em> change according to the <em>first applicable rule</em> in this list:</p>
<ul>
<li>If the stone is engraved with the number <code>0</code>, it is replaced by a stone engraved with the number <code>1</code>.</li>
<li>If the stone is engraved with a number that has an <em>even</em> number of digits, it is replaced by <em>two stones</em>. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: <code>1000</code> would become stones <code>10</code> and <code>0</code>.)</li>
<li>If none of the other rules apply, the stone is replaced by a new stone; the old stone's number <em>multiplied by 2024</em> is engraved on the new stone.</li>
</ul>
<p>No matter how the stones change, their <em>order is preserved</em>, and they stay on their perfectly straight line.</p>
<p>How will the stones evolve if you keep blinking at them? You take a note of the number engraved on each stone in the line (your puzzle input).</p>
<p>If you have an arrangement of five stones engraved with the numbers <code>0 1 10 99 999</code> and you blink once, the stones transform as follows:</p>
<ul>
<li>The first stone, <code>0</code>, becomes a stone marked <code>1</code>.</li>
<li>The second stone, <code>1</code>, is multiplied by 2024 to become <code>2024</code>.</li>
<li>The third stone, <code>10</code>, is split into a stone marked <code>1</code> followed by a stone marked <code>0</code>.</li>
<li>The fourth stone, <code>99</code>, is split into two stones marked <code>9</code>.</li>
<li>The fifth stone, <code>999</code>, is replaced by a stone marked <code>2021976</code>.</li>
</ul>
<p>So, after blinking once, your five stones would become an arrangement of seven stones engraved with the numbers <code>1 2024 1 0 9 9 2021976</code>.</p>
<p>Here is a longer example:</p>
<pre><code>Initial arrangement:
125 17

After 1 blink:
253000 1 7

After 2 blinks:
253 0 2024 14168

After 3 blinks:
512072 1 20 24 28676032

After 4 blinks:
512 72 2024 2 0 2 4 2867 6032

After 5 blinks:
1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32

After 6 blinks:
2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
</code></pre>
<p>In this example, after blinking six times, you would have <code>22</code> stones. After blinking 25 times, you would have <code><em>55312</em></code> stones!</p>
<p>Consider the arrangement of stones in front of you. <em>How many stones will you have after blinking 25 times?</em></p>
</article>
<p>Your puzzle answer was <code>185205</code>.</p><p class="day-success">The first half of this puzzle is complete! It provides one gold star: *</p>
<article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The Historians sure are taking a long time. To be fair, the infinite corridors <em>are</em> very large.</p>
<p><em>How many stones would you have after blinking a total of 75 times?</em></p>
</article>
<form action="11/answer" method="post"><input name="level" type="hidden" value="2"/><p>Answer: <input autocomplete="off" name="answer" type="text"/> <input type="submit" value="[Submit]"/></p></form>
<p>Although it hasn't changed, you can still <a href="11/input" target="_blank">get your puzzle input</a>.</p>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=I%27ve+completed+Part+One+of+%22Plutonian+Pebbles%22+%2D+Day+11+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F11" target="_blank">Bluesky</a>
<a href="https://twitter.com/intent/tweet?text=I%27ve+completed+Part+One+of+%22Plutonian+Pebbles%22+%2D+Day+11+%2D+Advent+of+Code+2024&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F11&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
<a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' &amp;&amp; ms.length){this.href='https://'+ms+'/share?text=I%27ve+completed+Part+One+of+%22Plutonian+Pebbles%22+%2D+Day+11+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F11';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
</main>