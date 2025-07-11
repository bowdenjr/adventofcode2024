<main>
<article class="day-desc"><h2>--- Day 2: Red-Nosed Reports ---</h2><p>Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.</p>
<p>While the <a href="/2015/day/19">Red-Nosed Reindeer nuclear fusion/fission plant</a> appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they <em>still</em> talk about the time Rudolph was saved through molecular synthesis from a single electron.</p>
<p>They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.</p>
<p>The unusual data (your puzzle input) consists of many <em>reports</em>, one report per line. Each report is a list of numbers called <em>levels</em> that are separated by spaces. For example:</p>
<pre><code>7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
</code></pre>
<p>This example data contains six reports each containing five levels.</p>
<p>The engineers are trying to figure out which reports are <em>safe</em>. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:</p>
<ul>
<li>The levels are either <em>all increasing</em> or <em>all decreasing</em>.</li>
<li>Any two adjacent levels differ by <em>at least one</em> and <em>at most three</em>.</li>
</ul>
<p>In the example above, the reports can be found safe or unsafe by checking those rules:</p>
<ul>
<li><code>7 6 4 2 1</code>: <em>Safe</em> because the levels are all decreasing by 1 or 2.</li>
<li><code>1 2 7 8 9</code>: <em>Unsafe</em> because <code>2 7</code> is an increase of 5.</li>
<li><code>9 7 6 2 1</code>: <em>Unsafe</em> because <code>6 2</code> is a decrease of 4.</li>
<li><code>1 3 2 4 5</code>: <em>Unsafe</em> because <code>1 3</code> is increasing but <code>3 2</code> is decreasing.</li>
<li><code>8 6 4 4 1</code>: <em>Unsafe</em> because <code>4 4</code> is neither an increase or a decrease.</li>
<li><code>1 3 6 7 9</code>: <em>Safe</em> because the levels are all increasing by 1, 2, or 3.</li>
</ul>
<p>So, in this example, <code><em>2</em></code> reports are <em>safe</em>.</p>
<p>Analyze the unusual data from the engineers. <em>How many reports are safe?</em></p>
</article>
<p>Your puzzle answer was <code>321</code>.</p><p class="day-success">The first half of this puzzle is complete! It provides one gold star: *</p>
<article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the <span title="I need to get one of these!">Problem Dampener</span>.</p>
<p>The Problem Dampener is a reactor-mounted module that lets the reactor safety systems <em>tolerate a single bad level</em> in what would otherwise be a safe report. It's like the bad level never happened!</p>
<p>Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.</p>
<p>More of the above example's reports are now safe:</p>
<ul>
<li><code>7 6 4 2 1</code>: <em>Safe</em> without removing any level.</li>
<li><code>1 2 7 8 9</code>: <em>Unsafe</em> regardless of which level is removed.</li>
<li><code>9 7 6 2 1</code>: <em>Unsafe</em> regardless of which level is removed.</li>
<li><code>1 <em>3</em> 2 4 5</code>: <em>Safe</em> by removing the second level, <code>3</code>.</li>
<li><code>8 6 <em>4</em> 4 1</code>: <em>Safe</em> by removing the third level, <code>4</code>.</li>
<li><code>1 3 6 7 9</code>: <em>Safe</em> without removing any level.</li>
</ul>
<p>Thanks to the Problem Dampener, <code><em>4</em></code> reports are actually <em>safe</em>!</p>
<p>Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. <em>How many reports are now safe?</em></p>
</article>
<form action="2/answer" method="post"><input name="level" type="hidden" value="2"/><p>Answer: <input autocomplete="off" name="answer" type="text"/> <input type="submit" value="[Submit]"/></p></form>
<p>Although it hasn't changed, you can still <a href="2/input" target="_blank">get your puzzle input</a>.</p>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=I%27ve+completed+Part+One+of+%22Red%2DNosed+Reports%22+%2D+Day+2+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F2" target="_blank">Bluesky</a>
<a href="https://twitter.com/intent/tweet?text=I%27ve+completed+Part+One+of+%22Red%2DNosed+Reports%22+%2D+Day+2+%2D+Advent+of+Code+2024&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F2&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
<a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' &amp;&amp; ms.length){this.href='https://'+ms+'/share?text=I%27ve+completed+Part+One+of+%22Red%2DNosed+Reports%22+%2D+Day+2+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F2';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
</main>