<main>
<article class="day-desc"><h2>--- Day 6: Guard Gallivant ---</h2><p>The Historians use their fancy <a href="4">device</a> again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year <a href="/2018/day/5">1518</a>! It turns out that having direct access to history is very convenient for a group of historians.</p>
<p>You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single <em>guard</em> is patrolling this part of the lab.</p>
<p>Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?</p>
<p>You start by making a map (your puzzle input) of the situation. For example:</p>
<pre><code>....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
</code></pre>
<p>The map shows the current position of the guard with <code>^</code> (to indicate the guard is currently facing <em>up</em> from the perspective of the map). Any <em>obstructions</em> - crates, desks, alchemical reactors, etc. - are shown as <code>#</code>.</p>
<p>Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:</p>
<ul>
<li>If there is something directly in front of you, turn right 90 degrees.</li>
<li>Otherwise, take a step forward.</li>
</ul>
<p>Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):</p>
<pre><code>....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
</code></pre>
<p>Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:</p>
<pre><code>....#.....
........&gt;#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
</code></pre>
<p>Reaching another obstacle (a spool of several <em>very</em> long polymers), she turns right again and continues downward:</p>
<pre><code>....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
</code></pre>
<p>This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):</p>
<pre><code>....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
</code></pre>
<p>By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. <em>Including the guard's starting position</em>, the positions visited by the guard before leaving the area are marked with an <code>X</code>:</p>
<pre><code>....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
</code></pre>
<p>In this example, the guard will visit <code><em>41</em></code> distinct positions on your map.</p>
<p>Predict the path of the guard. <em>How many distinct positions will the guard visit before leaving the mapped area?</em></p>
</article>
<p>Your puzzle answer was <code>5516</code>.</p><p class="day-success">The first half of this puzzle is complete! It provides one gold star: *</p>
<article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab. From the safety of a supply closet, you time travel through the last few months and <a href="/2018/day/4">record</a> the nightly status of the lab's guard post on the walls of the closet.</p>
<p>Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large for them to safely search the lab without getting caught.</p>
<p>Fortunately, they are <em>pretty sure</em> that adding a single new obstruction <em>won't</em> cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get <span title="This vulnerability was later fixed by having the guard always turn left instead."><em>stuck in a loop</em></span>, making the rest of the lab safe to search.</p>
<p>To have the lowest chance of creating a time paradox, The Historians would like to know <em>all</em> of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.</p>
<p>In the above example, there are only <code><em>6</em></code> different positions where a new obstruction would cause the guard to get stuck in a loop. The diagrams of these six situations use <code>O</code> to mark the new obstruction, <code>|</code> to show a position where the guard moves up/down, <code>-</code> to show a position where the guard moves left/right, and <code>+</code> to show a position where the guard moves both up/down and left/right.</p>
<p>Option one, put a printing press next to the guard's starting position:</p>
<pre><code>....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.<em>O</em>^---+.
........#.
#.........
......#...
</code></pre>
<p>Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:<p>
<pre><code>....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......<em>O</em>.#.
#.........
......#...
</code></pre>
<p>Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:</p>
<pre><code>....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+<em>O</em>#.
#+----+...
......#...
</code></pre>
<p>Option four, put an alchemical retroencabulator near the bottom left corner:</p>
<pre><code>....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#<em>O</em>+---+...
......#...
</code></pre>
<p>Option five, put the alchemical retroencabulator a bit to the right instead:</p>
<pre><code>....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..<em>O</em>+-+...
......#...
</code></pre>
<p>Option six, put a tank of sovereign glue right next to the tank of universal solvent:</p>
<pre><code>....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#<em>O</em>..
</code></pre>
<p>It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing. The important thing is having enough options that you can find one that minimizes time paradoxes, and in this example, there are <code><em>6</em></code> different positions you could choose.</p>
<p>You need to get the guard stuck in a loop by adding a single new obstruction. <em>How many different positions could you choose for this obstruction?</em></p>
</p></p></article>
<form action="6/answer" method="post"><input name="level" type="hidden" value="2"/><p>Answer: <input autocomplete="off" name="answer" type="text"/> <input type="submit" value="[Submit]"/></p></form>
<p>Although it hasn't changed, you can still <a href="6/input" target="_blank">get your puzzle input</a>.</p>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=I%27ve+completed+Part+One+of+%22Guard+Gallivant%22+%2D+Day+6+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F6" target="_blank">Bluesky</a>
<a href="https://twitter.com/intent/tweet?text=I%27ve+completed+Part+One+of+%22Guard+Gallivant%22+%2D+Day+6+%2D+Advent+of+Code+2024&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F6&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
<a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' &amp;&amp; ms.length){this.href='https://'+ms+'/share?text=I%27ve+completed+Part+One+of+%22Guard+Gallivant%22+%2D+Day+6+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F6';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
</main>