<main>
<article class="day-desc"><h2>--- Day 12: Garden Groups ---</h2><p>Why not search for the Chief Historian near the <a href="/2023/day/5">gardener</a> and his <a href="/2023/day/21">massive farm</a>? There's plenty of food, so The Historians grab something to eat while they search.</p>
<p>You're about to settle near a complex arrangement of garden plots when some Elves ask if you can lend a hand. They'd like to set up <span title='I originally wanted to title this puzzle "Fencepost Problem", but I was afraid someone would then try to count fenceposts by mistake and experience a fencepost problem.'>fences</span> around each region of garden plots, but they can't figure out how much fence they need to order or how much it will cost. They hand you a map (your puzzle input) of the garden plots.</p>
<p>Each garden plot grows only a single type of plant and is indicated by a single letter on your map. When multiple garden plots are growing the same type of plant and are touching (horizontally or vertically), they form a <em>region</em>. For example:</p>
<pre><code>AAAA
BBCD
BBCC
EEEC
</code></pre>
<p>This 4x4 arrangement includes garden plots growing five different types of plants (labeled <code>A</code>, <code>B</code>, <code>C</code>, <code>D</code>, and <code>E</code>), each grouped into their own region.</p>
<p>In order to accurately calculate the cost of the fence around a single region, you need to know that region's <em>area</em> and <em>perimeter</em>.</p>
<p>The <em>area</em> of a region is simply the number of garden plots the region contains. The above map's type <code>A</code>, <code>B</code>, and <code>C</code> plants are each in a region of area <code>4</code>. The type <code>E</code> plants are in a region of area <code>3</code>; the type <code>D</code> plants are in a region of area <code>1</code>.</p>
<p>Each garden plot is a square and so has <em>four sides</em>. The <em>perimeter</em> of a region is the number of sides of garden plots in the region that do not touch another garden plot in the same region. The type <code>A</code> and <code>C</code> plants are each in a region with perimeter <code>10</code>. The type <code>B</code> and <code>E</code> plants are each in a region with perimeter <code>8</code>. The lone <code>D</code> plot forms its own region with perimeter <code>4</code>.</p>
<p>Visually indicating the sides of plots in each region that contribute to the perimeter using <code>-</code> and <code>|</code>, the above map's regions' perimeters are measured as follows:</p>
<pre><code>+-+-+-+-+
|A A A A|
+-+-+-+-+     +-+
              |D|
+-+-+   +-+   +-+
|B B|   |C|
+   +   + +-+
|B B|   |C C|
+-+-+   +-+ +
          |C|
+-+-+-+   +-+
|E E E|
+-+-+-+
</code></pre>
<p>Plants of the same type can appear in multiple separate regions, and regions can even appear within other regions. For example:</p>
<pre><code>OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
</code></pre>
<p>The above map contains <em>five</em> regions, one containing all of the <code>O</code> garden plots, and the other four each containing a single <code>X</code> plot.</p>
<p>The four <code>X</code> regions each have area <code>1</code> and perimeter <code>4</code>. The region containing <code>21</code> type <code>O</code> plants is more complicated; in addition to its outer edge contributing a perimeter of <code>20</code>, its boundary with each <code>X</code> region contributes an additional <code>4</code> to its perimeter, for a total perimeter of <code>36</code>.</p>
<p>Due to "modern" business practices, the <em>price</em> of fence required for a region is found by <em>multiplying</em> that region's area by its perimeter. The <em>total price</em> of fencing all regions on a map is found by adding together the price of fence for every region on the map.</p>
<p>In the first example, region <code>A</code> has price <code>4 * 10 = 40</code>, region <code>B</code> has price <code>4 * 8 = 32</code>, region <code>C</code> has price <code>4 * 10 = 40</code>, region <code>D</code> has price <code>1 * 4 = 4</code>, and region <code>E</code> has price <code>3 * 8 = 24</code>. So, the total price for the first example is <code><em>140</em></code>.</p>
<p>In the second example, the region with all of the <code>O</code> plants has price <code>21 * 36 = 756</code>, and each of the four smaller <code>X</code> regions has price <code>1 * 4 = 4</code>, for a total price of <code><em>772</em></code> (<code>756 + 4 + 4 + 4 + 4</code>).</p>
<p>Here's a larger example:</p>
<pre><code>RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
</code></pre>
<p>It contains:</p>
<ul>
<li>A region of <code>R</code> plants with price <code>12 * 18 = 216</code>.</li>
<li>A region of <code>I</code> plants with price <code>4 * 8 = 32</code>.</li>
<li>A region of <code>C</code> plants with price <code>14 * 28 = 392</code>.</li>
<li>A region of <code>F</code> plants with price <code>10 * 18 = 180</code>.</li>
<li>A region of <code>V</code> plants with price <code>13 * 20 = 260</code>.</li>
<li>A region of <code>J</code> plants with price <code>11 * 20 = 220</code>.</li>
<li>A region of <code>C</code> plants with price <code>1 * 4 = 4</code>.</li>
<li>A region of <code>E</code> plants with price <code>13 * 18 = 234</code>.</li>
<li>A region of <code>I</code> plants with price <code>14 * 22 = 308</code>.</li>
<li>A region of <code>M</code> plants with price <code>5 * 12 = 60</code>.</li>
<li>A region of <code>S</code> plants with price <code>3 * 8 = 24</code>.</li>
</ul>
<p>So, it has a total price of <code><em>1930</em></code>.</p>
<p><em>What is the total price of fencing all regions on your map?</em></p>
</article>
<p>To begin, <a href="12/input" target="_blank">get your puzzle input</a>.</p>
<form action="12/answer" method="post"><input name="level" type="hidden" value="1"/><p>Answer: <input autocomplete="off" name="answer" type="text"/> <input type="submit" value="[Submit]"/></p></form>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=%22Garden+Groups%22+%2D+Day+12+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F12" target="_blank">Bluesky</a>
<a href="https://twitter.com/intent/tweet?text=%22Garden+Groups%22+%2D+Day+12+%2D+Advent+of+Code+2024&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F12&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
<a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' &amp;&amp; ms.length){this.href='https://'+ms+'/share?text=%22Garden+Groups%22+%2D+Day+12+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F12';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
</main>