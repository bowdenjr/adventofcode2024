<main>
<article class="day-desc"><h2>--- Day 9: Disk Fragmenter ---</h2><p>Another push of the button leaves you in the familiar hallways of some friendly <a href="/2021/day/23">amphipods</a>! Good thing you each somehow got your own personal mini submarine. The Historians jet away in search of the Chief, mostly by driving directly into walls.</p>
<p>While The Historians quickly figure out how to pilot these things, you notice an amphipod in the corner struggling with his computer. He's trying to make more contiguous free space by compacting all of the files, but his program isn't working; you offer to help.</p>
<p>He shows you the <em>disk map</em> (your puzzle input) he's already generated. For example:</p>
<pre><code>2333133121414131402</code></pre>
<p>The disk map uses a dense format to represent the layout of <em>files</em> and <em>free space</em> on the disk. The digits alternate between indicating the length of a file and the length of free space.</p>
<p>So, a disk map like <code>12345</code> would represent a one-block file, two blocks of free space, a three-block file, four blocks of free space, and then a five-block file. A disk map like <code>90909</code> would represent three nine-block files in a row (with no free space between them).</p>
<p>Each file on disk also has an <em>ID number</em> based on the order of the files as they appear <em>before</em> they are rearranged, starting with ID <code>0</code>. So, the disk map <code>12345</code> has three files: a one-block file with ID <code>0</code>, a three-block file with ID <code>1</code>, and a five-block file with ID <code>2</code>. Using one character for each block where digits are the file ID and <code>.</code> is free space, the disk map <code>12345</code> represents these individual blocks:</p>
<pre><code>0..111....22222</code></pre>
<p>The first example above, <code>2333133121414131402</code>, represents these individual blocks:</p>
<pre><code>00...111...2...333.44.5555.6666.777.888899</code></pre>
<p>The amphipod would like to <em>move file blocks one at a time</em> from the end of the disk to the leftmost free space block (until there are no gaps remaining between file blocks). For the disk map <code>12345</code>, the process looks like this:</p>
<pre><code>0..111....22222
02.111....2222.
022111....222..
0221112...22...
02211122..2....
022111222......
</code></pre>
<p>The first example requires a few more steps:</p>
<pre><code>00...111...2...333.44.5555.6666.777.888899
009..111...2...333.44.5555.6666.777.88889.
0099.111...2...333.44.5555.6666.777.8888..
00998111...2...333.44.5555.6666.777.888...
009981118..2...333.44.5555.6666.777.88....
0099811188.2...333.44.5555.6666.777.8.....
009981118882...333.44.5555.6666.777.......
0099811188827..333.44.5555.6666.77........
00998111888277.333.44.5555.6666.7.........
009981118882777333.44.5555.6666...........
009981118882777333644.5555.666............
00998111888277733364465555.66.............
0099811188827773336446555566..............
</code></pre>
<p>The final step of this file-compacting process is to update the <em>filesystem checksum</em>. To calculate the checksum, add up the result of multiplying each of these blocks' position with the file ID number it contains. The leftmost block is in position <code>0</code>. If a block contains free space, skip it instead.</p>
<p>Continuing the first example, the first few blocks' position multiplied by its file ID number are <code>0 * 0 = 0</code>, <code>1 * 0 = 0</code>, <code>2 * 9 = 18</code>, <code>3 * 9 = 27</code>, <code>4 * 8 = 32</code>, and so on. In this example, the checksum is the sum of these, <code><em>1928</em></code>.</p>
<p><span title="Bonus points if you make a cool animation of this process.">Compact the amphipod's hard drive</span> using the process he requested. <em>What is the resulting filesystem checksum?</em> <span class="quiet">(Be careful copy/pasting the input for this puzzle; it is a single, very long line.)</span></p>
</article>
<p>Your puzzle answer was <code>6390180901651</code>.</p><p class="day-success">The first half of this puzzle is complete! It provides one gold star: *</p>
<article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Upon completion, two things immediately become clear. First, the disk definitely has a lot more contiguous free space, just like the amphipod hoped. Second, the computer is running much more slowly! Maybe introducing all of that <a href="https://en.wikipedia.org/wiki/File_system_fragmentation" target="_blank">file system fragmentation</a> was a bad idea?</p>
<p>The eager amphipod already has a new plan: rather than move individual blocks, he'd like to try compacting the files on his disk by moving <em>whole files</em> instead.</p>
<p>This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt to move each file exactly once in order of <em>decreasing file ID number</em> starting with the file with the highest file ID number. If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move.</p>
<p>The first example from above now proceeds differently:</p>
<pre><code>00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
</code></pre>
<p>The process of updating the filesystem checksum is the same; now, this example's checksum would be <code><em>2858</em></code>.</p>
<p>Start over, now compacting the amphipod's hard drive using this new method instead. <em>What is the resulting filesystem checksum?</em></p>
</article>
<form action="9/answer" method="post"><input name="level" type="hidden" value="2"/><p>Answer: <input autocomplete="off" name="answer" type="text"/> <input type="submit" value="[Submit]"/></p></form>
<p>Although it hasn't changed, you can still <a href="9/input" target="_blank">get your puzzle input</a>.</p>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=I%27ve+completed+Part+One+of+%22Disk+Fragmenter%22+%2D+Day+9+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F9" target="_blank">Bluesky</a>
<a href="https://twitter.com/intent/tweet?text=I%27ve+completed+Part+One+of+%22Disk+Fragmenter%22+%2D+Day+9+%2D+Advent+of+Code+2024&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F9&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
<a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' &amp;&amp; ms.length){this.href='https://'+ms+'/share?text=I%27ve+completed+Part+One+of+%22Disk+Fragmenter%22+%2D+Day+9+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F9';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
</main>