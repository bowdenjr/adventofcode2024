<main>
<article class="day-desc"><h2>--- Day 7: Bridge Repair ---</h2><p>The Historians take you to a familiar <a href="/2022/day/9">rope bridge</a> over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?</p>
<p>When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.</p>
<p>You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and <em>stole all the operators</em> from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).</p>
<p>For example:</p>
<pre><code>190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
</code></pre>
<p>Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.</p>
<p>Operators are <em>always evaluated left-to-right</em>, <em>not</em> according to precedence rules. Furthermore, numbers in the equations cannot be rearranged. Glancing into the jungle, you can see elephants holding two different types of operators: <em>add</em> (<code>+</code>) and <em>multiply</em> (<code>*</code>).</p>
<p>Only three of the above equations can be made true by inserting operators:</p>
<ul>
<li><code>190: 10 19</code> has only one position that accepts an operator: between <code>10</code> and <code>19</code>. Choosing <code>+</code> would give <code>29</code>, but choosing <code>*</code> would give the test value (<code>10 * 19 = 190</code>).</li>
<li><code>3267: 81 40 27</code> has two positions for operators. Of the four possible configurations of the operators, <em>two</em> cause the right side to match the test value: <code>81 + 40 * 27</code> and <code>81 * 40 + 27</code> both equal <code>3267</code> (when evaluated left-to-right)!</li>
<li><code>292: 11 6 16 20</code> can be solved in exactly one way: <code>11 + 6 * 16 + 20</code>.</li>
</ul>
<p>The engineers just need the <em>total calibration result</em>, which is the sum of the test values from just the equations that could possibly be true. In the above example, the sum of the test values for the three equations listed above is <code><em>3749</em></code>.</p>
<p>Determine which equations could possibly be true. <em>What is their total calibration result?</em></p>
</article>
<p>Your puzzle answer was <code>66343330034722</code>.</p><p class="day-success">The first half of this puzzle is complete! It provides one gold star: *</p>
<article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a <em>third type of operator</em>.</p>
<p>The <a href="https://en.wikipedia.org/wiki/Concatenation" target="_blank">concatenation</a> operator (<code><span title='I think you mean ".".'>||</span></code>) combines the digits from its left and right inputs into a single number. For example, <code>12 || 345</code> would become <code>12345</code>. All operators are still evaluated left-to-right.</p>
<p>Now, apart from the three equations that could be made true using only addition and multiplication, the above example has three more equations that can be made true by inserting operators:</p>
<ul>
<li><code>156: 15 6</code> can be made true through a single concatenation: <code>15 || 6 = 156</code>.</li>
<li><code>7290: 6 8 6 15</code> can be made true using <code>6 * 8 || 6 * 15</code>.</li>
<li><code>192: 17 8 14</code> can be made true using <code>17 || 8 + 14</code>.</li>
</ul>
<p>Adding up all six test values (the three that could be made before using only <code>+</code> and <code>*</code> plus the new three that can now be made by also using <code>||</code>) produces the new <em>total calibration result</em> of <code><em>11387</em></code>.</p>
<p>Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. <em>What is their total calibration result?</em></p>
</article>
<form action="7/answer" method="post"><input name="level" type="hidden" value="2"/><p>Answer: <input autocomplete="off" name="answer" type="text"/> <input type="submit" value="[Submit]"/></p></form>
<p>Although it hasn't changed, you can still <a href="7/input" target="_blank">get your puzzle input</a>.</p>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=I%27ve+completed+Part+One+of+%22Bridge+Repair%22+%2D+Day+7+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F7" target="_blank">Bluesky</a>
<a href="https://twitter.com/intent/tweet?text=I%27ve+completed+Part+One+of+%22Bridge+Repair%22+%2D+Day+7+%2D+Advent+of+Code+2024&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F7&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
<a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' &amp;&amp; ms.length){this.href='https://'+ms+'/share?text=I%27ve+completed+Part+One+of+%22Bridge+Repair%22+%2D+Day+7+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F7';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
</main>