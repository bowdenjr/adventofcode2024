<main>
<article class="day-desc"><h2>--- Day 3: Mull It Over ---</h2><p>"Our computers are having issues, so I have no idea if we have any Chief Historians <span title="There's a spot reserved for Chief Historians between the green toboggans and the red toboggans. They've never actually had any Chief Historians in stock, but it's best to be prepared.">in stock</span>! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the <a href="/2020/day/2">North Pole Toboggan Rental Shop</a>. The Historians head out to take a look.</p>
<p>The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"</p>
<p>The computer appears to be trying to run a program, but its memory (your puzzle input) is <em>corrupted</em>. All of the instructions have been jumbled up!</p>
<p>It seems like the goal of the program is just to <em>multiply some numbers</em>. It does that with instructions like <code>mul(X,Y)</code>, where <code>X</code> and <code>Y</code> are each 1-3 digit numbers. For instance, <code>mul(44,46)</code> multiplies <code>44</code> by <code>46</code> to get a result of <code>2024</code>. Similarly, <code>mul(123,4)</code> would multiply <code>123</code> by <code>4</code>.</p>
<p>However, because the program's memory has been corrupted, there are also many invalid characters that should be <em>ignored</em>, even if they look like part of a <code>mul</code> instruction. Sequences like <code>mul(4*</code>, <code>mul(6,9!</code>, <code>?(12,34)</code>, or <code>mul ( 2 , 4 )</code> do <em>nothing</em>.</p>
<p>For example, consider the following section of corrupted memory:</p>
<pre><code>x<em>mul(2,4)</em>%&amp;mul[3,7]!@^do_not_<em>mul(5,5)</em>+mul(32,64]then(<em>mul(11,8)mul(8,5)</em>)</code></pre>
<p>Only the four highlighted sections are real <code>mul</code> instructions. Adding up the result of each instruction produces <code><em>161</em></code> (<code>2*4 + 5*5 + 11*8 + 8*5</code>).</p>
<p>Scan the corrupted memory for uncorrupted <code>mul</code> instructions. <em>What do you get if you add up all of the results of the multiplications?</em></p>
</article>
<p>Your puzzle answer was <code>167650499</code>.</p><article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.</p>
<p>There are two new instructions you'll need to handle:</p>
<ul>
<li>The <code>do()</code> instruction <em>enables</em> future <code>mul</code> instructions.</li>
<li>The <code>don't()</code> instruction <em>disables</em> future <code>mul</code> instructions.</li>
</ul>
<p>Only the <em>most recent</em> <code>do()</code> or <code>don't()</code> instruction applies. At the beginning of the program, <code>mul</code> instructions are <em>enabled</em>.</p>
<p>For example:</p>
<pre><code>x<em>mul(2,4)</em>&amp;mul[3,7]!^<em>don't()</em>_mul(5,5)+mul(32,64](mul(11,8)un<em>do()</em>?<em>mul(8,5)</em>)</code></pre>
<p>This corrupted memory is similar to the example from before, but this time the <code>mul(5,5)</code> and <code>mul(11,8)</code> instructions are <em>disabled</em> because there is a <code>don't()</code> instruction before them. The other <code>mul</code> instructions function normally, including the one at the end that gets re-<em>enabled</em> by a <code>do()</code> instruction.</p>
<p>This time, the sum of the results is <code><em>48</em></code> (<code>2*4 + 8*5</code>).</p>
<p>Handle the new instructions; <em>what do you get if you add up all of the results of just the enabled multiplications?</em></p>
</article>
<p>Your puzzle answer was <code>95846796</code>.</p><p class="day-success">Both parts of this puzzle are complete! They provide two gold stars: **</p>
<p>At this point, you should <a href="/2024">return to your Advent calendar</a> and try another puzzle.</p>
<p>If you still want to see it, you can <a href="3/input" target="_blank">get your puzzle input</a>.</p>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=I%27ve+completed+%22Mull+It+Over%22+%2D+Day+3+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F3" target="_blank">Bluesky</a>
<a href="https://twitter.com/intent/tweet?text=I%27ve+completed+%22Mull+It+Over%22+%2D+Day+3+%2D+Advent+of+Code+2024&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F3&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
<a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' &amp;&amp; ms.length){this.href='https://'+ms+'/share?text=I%27ve+completed+%22Mull+It+Over%22+%2D+Day+3+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F3';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
</main>