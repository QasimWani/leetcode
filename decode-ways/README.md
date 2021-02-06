<h2>91. Decode Ways</h2><h3>Medium</h3><hr><div><p>A message containing letters from <code>A-Z</code> can be <strong>encoded</strong> into numbers using the following mapping:</p>

<pre>'A' -&gt; "1"
'B' -&gt; "2"
...
'Z' -&gt; "26"
</pre>

<p>To <strong>decode</strong> an encoded message, all the digits must be mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, <code>"111"</code> can have each of its <code>"1"</code>s be mapped into <code>'A'</code>s to make <code>"AAA"</code>, or it could be mapped to <code>"11"</code> and <code>"1"</code> (<code>'K'</code> and <code>'A'</code> respectively) to make <code>"KA"</code>. Note that <code>"06"</code> cannot be mapped into <code>'F'</code> since <code>"6"</code> is different from <code>"06"</code>.</p>

<p>Given a&nbsp;string <code>s</code> containing only digits, return <em>the <strong>number</strong> of ways to <strong>decode</strong> it</em>.</p>

<p>The answer is guaranteed to fit in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "12"
<strong>Output:</strong> 2
<strong>Explanation:</strong> "12" could be decoded as "AB" (1 2) or "L" (12).
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "226"
<strong>Output:</strong> 3
<strong>Explanation:</strong> "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "0"
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no character that is mapped to a number starting with 0. The only valid mappings with 0 are 'J' -&gt; "10" and 'T' -&gt; "20".
Since there is no character, there are no valid ways to decode this since all digits need to be mapped.
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> s = "06"
<strong>Output:</strong> 0
<strong>Explanation:</strong> "06" cannot be mapped to "F" because the zero at the beginning of the string can't make a valid character.&nbsp;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> contains only digits and may contain leading zero(s).</li>
</ul>
</div>