<main>
<article class="day-desc"><h2>--- Day 10: Hoof It ---</h2><p>You all arrive at a <a href="/2023/day/15">Lava Production Facility</a> on a floating island in the sky. As the others begin to search the massive industrial complex, you feel a small nose boop your leg and look down to discover a <span title="i knew you would come back">reindeer</span> wearing a hard hat.</p>
<p>The reindeer is holding a book titled "Lava Island Hiking Guide". However, when you open the book, you discover that most of it seems to have been scorched by lava! As you're about to ask how you can help, the reindeer brings you a blank <a href="https://en.wikipedia.org/wiki/Topographic_map" target="_blank">topographic map</a> of the surrounding area (your puzzle input) and looks up at you excitedly.</p>
<p>Perhaps you can help fill in the missing hiking trails?</p>
<p>The topographic map indicates the <em>height</em> at each position using a scale from <code>0</code> (lowest) to <code>9</code> (highest). For example:</p>
<pre><code>0123
1234
8765
9876
</code></pre>
<p>Based on un-scorched scraps of the book, you determine that a good hiking trail is <em>as long as possible</em> and has an <em>even, gradual, uphill slope</em>. For all practical purposes, this means that a <em>hiking trail</em> is any path that starts at height <code>0</code>, ends at height <code>9</code>, and always increases by a height of exactly 1 at each step. Hiking trails never include diagonal steps - only up, down, left, or right (from the perspective of the map).</p>
<p>You look up from the map and notice that the reindeer has helpfully begun to construct a small pile of pencils, markers, rulers, compasses, stickers, and other equipment you might need to update the map with hiking trails.</p>
<p>A <em>trailhead</em> is any position that starts one or more hiking trails - here, these positions will always have height <code>0</code>. Assembling more fragments of pages, you establish that a trailhead's <em>score</em> is the number of <code>9</code>-height positions reachable from that trailhead via a hiking trail. In the above example, the single trailhead in the top left corner has a score of <code>1</code> because it can reach a single <code>9</code> (the one in the bottom left).</p>
<p>This trailhead has a score of <code>2</code>:</p>
<pre><code>...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
</code></pre>
<p>(The positions marked <code>.</code> are impassable tiles to simplify these examples; they do not appear on your actual topographic map.)</p>
<p>This trailhead has a score of <code>4</code> because every <code>9</code> is reachable via a hiking trail except the one immediately to the left of the trailhead:</p>
<pre><code>..90..9
...1.98
...2..7
6543456
765.987
876....
987....
</code></pre>
<p>This topographic map contains <em>two</em> trailheads; the trailhead at the top has a score of <code>1</code>, while the trailhead at the bottom has a score of <code>2</code>:</p>
<pre><code>10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01
</code></pre>
<p>Here's a larger example:</p>
<pre><code>89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
</code></pre>
<p>This larger example has 9 trailheads. Considering the trailheads in reading order, they have scores of <code>5</code>, <code>6</code>, <code>5</code>, <code>3</code>, <code>1</code>, <code>3</code>, <code>5</code>, <code>3</code>, and <code>5</code>. Adding these scores together, the sum of the scores of all trailheads is <code><em>36</em></code>.</p>
<p>The reindeer gleefully carries over a protractor and adds it to the pile. <em>What is the sum of the scores of all trailheads on your topographic map?</em></p>
</article>
<p>To begin, <a href="10/input" target="_blank">get your puzzle input</a>.</p>
<form action="10/answer" method="post"><input name="level" type="hidden" value="1"/><p>Answer: <input autocomplete="off" name="answer" type="text"/> <input type="submit" value="[Submit]"/></p></form>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=%22Hoof+It%22+%2D+Day+10+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F10" target="_blank">Bluesky</a>
<a href="https://twitter.com/intent/tweet?text=%22Hoof+It%22+%2D+Day+10+%2D+Advent+of+Code+2024&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F10&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
<a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' &amp;&amp; ms.length){this.href='https://'+ms+'/share?text=%22Hoof+It%22+%2D+Day+10+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F10';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
</main>