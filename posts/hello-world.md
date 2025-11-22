---
title: "Hello World, or how I built this blog in 4 days with AI"
date: "2025-11-21"
tags: ["intro", "ai"]
---

Welcome to my new blog! I've taken a few cracks at making a blog in the past, but some recent inspiration from another blog I saw online made me want to give it another go. A simple static website, simple features, just a way to share some writing and professional links. This northstar vision, coupled with general Python + Cloud knowledge, and a *helluva* lot of code written by ChatGPT, has gotten me this site in a very short time.

## The Game Plan

I already knew the high level steps for creating my own website with Python, so before I started running code I made this short list of bullet points (and then never looked at it again until now lol):

```
Outcomes:
- Domain Name for blog and email (Done)
- Simple blog to publish written articles
    - Flask
- Mailing list when to notify when I’ve written a new article
- Analytics tracking
- Tag management for articles
- Code Repo on Github, Hosted on GCP, cost controlled
```

The first point, getting the domain name, was relatively simple. Asked ChatGPT where I could buy one, it suggested Cloudflare, OK I'm familiar with that, seems reputable/widely used (even though it just had a major outage in the last week), I make an account, buy this .ca domain for $30 on a two year plan, boom easy done.

The only things I haven't done yet are the mailing list and the analytics tracking, but everything else has been accomplished and is enough to get this blog up and running.

I think that if you've got a high level understanding of what you need to do, you understand the right steps, you can guide AI to build you what you want (atleast in relatively simple cases like this one). If you don't know the steps, maybe you could have the AI teach you and then take it from there, but you are essentially then getting a crash course and won't have enough prior context to understand why things are working.

## 95% of code taken straight from ChatGPT

I don't think I'm necessarily proud of this fact, honestly I'm not entirely sure how I feel about it yet, but it's true. Ignoring the markdown code in my project (i.e. the text written in the blog posts), here's how many lines of code were required to get this blog up and running:

<table border="1" cellspacing="0" cellpadding="4">
  <tr>
    <th>Language</th>
    <th>Files</th>
    <th>Code</th>
    <th>Comment</th>
    <th>Blank</th>
    <th>Total</th>
  </tr>
  <tr>
    <td><s>Markdown</s></td>
    <td><s>13</s></td>
    <td><s>2458</s></td>
    <td><s>11</s></td>
    <td><s>1408</s></td>
    <td><s>3877</s></td>
  </tr>
  <tr>
    <td>PostCSS</td>
    <td>2</td>
    <td>211</td>
    <td>13</td>
    <td>32</td>
    <td>256</td>
  </tr>
  <tr>
    <td>HTML</td>
    <td>7</td>
    <td>171</td>
    <td>8</td>
    <td>65</td>
    <td>244</td>
  </tr>
  <tr>
    <td>Python</td>
    <td>1</td>
    <td>135</td>
    <td>7</td>
    <td>38</td>
    <td>180</td>
  </tr>
  <tr>
    <td>Docker</td>
    <td>1</td>
    <td>13</td>
    <td>9</td>
    <td>9</td>
    <td>31</td>
  </tr>
  <tr>
    <td>pip requirements</td>
    <td>1</td>
    <td>12</td>
    <td>0</td>
    <td>1</td>
    <td>13</td>
  </tr>
  <tr>
    <td><b>Totals (no Markdown)</b></td>
    <td>12</td>
    <td>542</td>
    <td>37</td>
    <td>145</td>
    <td>724</td>
  </tr>
</table>

(used AI to help me make the rendering for this table too btw)

Out of those 724 lines, I'm honestly confident that I wrote less than 30 lines myself (~4%). I definitely had to tweak some of the lines that ChatGPT spat out at me, and I definitely did all the copying and pasting, but I wrote very little. Instead, I gave prompts like the following:

- *OK I have a domain name bought. help me create a flask website for a blog at blog.billwarker.ca*

- *here's my code, im getting URL not found error: [copied some code here]*

- *what is wrong with this code*

- *ok give me some good css styling, and I want the website to have a side pane section where I can add all the tags. something that resembles this [attached a picture here]*

- *help me create a simple dockerfile to build the app in cloud build/run in GCP*

I gave it some formatted desires as well:

```
in the side pane, i want to have a dates section under tags.
have it roll up to year, but then allow it to expand to a view of posts by month.

for example, top level looks like this:

2025 (4)

expanded Looks like this:

2025 (4)
    2025-12 (2)
    2025-11 (2)
```

Over the course of four evenings, about 2-3 hour long sessions (usually until I hit my cap of ChatGPT Free Plan limit on requests for the day), I copied and pasted and debugged until I got the site running the way I wanted on my local machine. 

## Deploying it on the Cloud and CI/CD

At this point in the process, my experience with the code-writing-adjacent aspects of software engineering took over and I didn't really have to lean on ChatGPT much to:

- Create a virtual environment in Python for the project and do package management stuff (i.e. requirements.txt file)
- Create a repo in Github and push my local code to that
- Create a webhook to that repo in GCP's Cloud Build and have it stream builds in
- Create a Cloud Run app on top of the Cloud Build containers (although I did have ChatGPT create the Dockerfile I used)

ChatGPT was still definitely helpful for general consulting here - it helped me understand whether I needed a load balancer for the website, how to make sure I don't get killed by any unexpected costs on GCP, and how web traffic would be served with the infrastructe I had set up. Again, a passing knowledge of web development was enough for me to get things done, and I think it also really helps that the whole point of GCP's product suite (and cloud development in general) is to abstract away a lot of the finer details.

## Thoughts about AI and the whole "Vibe Coding" process

I "Vibe Coded" my way through almost this entire project: telling ChatGPT what I wanted in plain langauge, plugging the resulting code into my development environment, having it debug its own errors (with my guidance), and rinsing-repeating this whole process until it got me where I wanted to go.

A huge amount of leverage is now available for those fluent enough in technology to describe what they want to AI/Agents/LLMs. I definitely feel a bit dumber for it - although I can say that I understand the code written by ChatGPT after seeing and integrating it myself, it definitely would've taken me way longer to write way shittier code. And at this point, for smaller projects like this one, why would I even bother?

I started the project thinking that OK, maybe I'll see the code that it spits out and type it into the editor myself so I can slowly follow along with the logic, learn the patterns its suggesting, and get the "muscle memory" of writing the code myself. Copying other people's code fullstop was how I originally learned to program years ago, anyways. That lasted maybe 10 minutes before I realized that I already have a job, have nothing to prove doing this for myself, and it's slow AF and boring. Vibe Coding lets me move sooo much faster. You still have to bang your head against problems that come up and figure out what's happening overall, but that process is sped up so much with AI writing and debugging the code for you that you stay in the creative/building zone for much more of the development time overall.

Would I be deeply concerned if critical software for banks, hospitals, transportation was being Vibe Coded with AI? Of course, but I also understand that there are already so many more checks and balances (i.e. testing) that are a part of deploying important code like that anyways.

Do I feel like continuing to develop code in this manner or leaning more on AI to write code will make be a better programmer over time? Probably not - I can see it being great for generalists to cover a lot of ground and be very useful, but I think a lot of the "deep thinking" part of coding and problem solving that actually makes you better/learn is completely skipped. It's definitely going to be used as a crutch.

Is Vibe Coding going to be the way of the future? Mixed bag here, because I can certainly see the vision of it "10x"ing developer productivity (i.e. the corporate wet dream). It's great for automating away a lot of the actual mundane work of gluing technologies together, doing stuff that's already been done, etc. And honestly, if it does continue to improve at doing stuff like that, I see why a bunch of people could get laid off. My prior experience took me a long way here, but I don't actually *feel* like I did that much...

If you're curious to see what all the AI-written code looks like, you can view it [here](https://github.com/billwarker/billwarker.ca). It surely could be improved in many ways, but hey, it works!