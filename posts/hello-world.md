---
title: "Hello World (or alternatively, how I actually 'Vibe Coded' this blog in 4 days with AI)"
date: "2025-11-21"
tags: ["intro", "ai"]
---

Welcome to my new blog! I've taken a few cracks at making a blog in the past, but some recent inspiration has made me want to give it another go. A simple static website, simple features, just a way to share some writing and professional links. This northstar vision, coupled with my experience in Python programming and Google Cloud Platform (GCP) knowledge, and a... *helluva* lot of code written by ChatGPT, has gotten me this personal site in a very short time. This was my first time successfully "vibe coding" on an end-to-end project, so read on for my general thoughts on the entire process.

## The Game Plan

I already knew the high level steps for creating a website with Python and the Flask package, so before I started any coding I made a short list of milestones (and then never looked at it again until now):

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

Getting the domain name was relatively simple. I asked ChatGPT where I could buy one and it suggested Cloudflare. OK, I'm familiar with that, plenty of big websites run on it (even though it just had a major outage in the last week). I make an account, buy this .ca domain ($30 on a two year plan), boom easy done. Then I began the Python coding.

The only things I haven't done yet are the mailing list and the analytics tracking, but everything else has been accomplished at the time of writing. More than enough to get this blog up and running online.

From a planning POV, I think that if you've got a high level understanding of what you need to do, you understand the right steps, you can guide AI towards what you want to build (atleast in relatively projects like this one). If you don't know the general steps beforehand, maybe you can still have the AI teach you and then take things from there, but then you're essentially getting a crash course and won't have enough prior knowledge to truly understand when/why things don't work. You're flying blind, letting AI fully take the wheel.

## 95% of code taken straight from ChatGPT

I don't think I'm necessarily proud of this fact (honestly not entirely sure how I feel about it yet) but it's true. Ignoring the markdown code in my project (i.e. the text written in the blog posts), here's how many lines were required to get this blog up and running:

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

I used ChatGPT to help me make all of the markdown rendering for this table too, by the way.

Out of the total 724 lines I'm estimating that I wrote less than 30 of them myself (less than 5%). I definitely had to tweak some of the code that ChatGPT spat out at me, and I definitely did all the copying and pasting (wasn't working with an integrated development environment). But honestly I wrote very little. Instead, I mainly gave ChatGPT prompts like the following:

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

Over the course of four evenings while I was on a nice vacation with my family in Berlin, in 2-3 hour long sessions (usually until I hit my cap of ChatGPT Free Plan limit on requests for the day), I prompted and copied and pasted and debugged until I got the site running the way I wanted on my local machine. "Vibe coded" my way through.

## Deploying it on the Cloud and CI/CD

At this point in the process, my experience with GCP took over and I didn't really have to lean on ChatGPT much to:

- Create a virtual environment in Python for the project and do package management stuff (i.e. requirements.txt file)
- Create a repository in Github and push my local code to that
- Create a webhook to that repo in the GCP Cloud Console, turning on Cloud Build and have it stream builds from my Github Repo
- Create a Cloud Run app on top of the Cloud Build containers (although I did have ChatGPT help create the Dockerfile I used)

ChatGPT was definitely still helpful for general consulting here, helping me understand whether or not I needed a load balancer for the website, how to make sure I don't get myself slapped with any unexpected costs by using GCP, and how much web traffic I could expect to reasonably serve with the amount of compute I allowed for the project in Cloud Run. Again, my passing knowledge of web development was enough for me to get things done, but I also think it really helped that the whole point of GCP's product suite (and cloud development in general) is to abstract away a lot of the finer details anyways.

## Thoughts about Vibe Coding and reflecting on the entire process

I "Vibe Coded" my way through most of the coding for this entire project: telling ChatGPT what I wanted in plain English, plugging the code it spat out into my development environment, asking it to help me debug all the errors. Rinse and repeat until it got me to where I wanted to go.

I think Vibe Coding definitely offers a huge amount of leverage to those fluent enough in technology and software fields to write code quickly. I definitely feel a bit dumber for it though, not taking the time to slowly produce the logic myself as I would've on any other project. I understand the code that ChatGPT gave me and am thankful that I didn't have to go through all of the typing to produce it myself after seeing and integrating it myself - it definitely would've taken me way longer to write code that was probably a bit worse (at least without all of the best practices synthesized through the LLM).

Would I be deeply concerned if this is how mission critical software for banks, hospitals, transportation, etc was being produced? Of course, but I also understand that there are typically many prior established checks and balances (i.e. testing, security) that are a part of deploying important code like that anyways.

Do I feel like personally continuing to develop code in this manner, or leaning more on AI in general, will atrophy my own thinking and tech skills? I see the risk - AI can be great for generalists with a shallow understanding of many things, but I think that a lot of the "deep thinking" that comes from codin yourself, the work that **builds your actual experience and intuition, is completely skipped**. You could definitely end up using AI as a crutch to your detriment.

Is Vibe Coding going to be the way of the future? Not sure; I can also see the vision of it "10X"ing developer productivity and allowing teams to move very fast. It's great for automating away the tedium of writing code and handling repetitive tasks. It's great for spitting out formatting. Honestly, if AI continues to improve at doing more stuff like that, I can see it being pretty great. Just use with caution. But at least in this project, ChatGPT took me a looooong way here - I don't actually *feel* like I did that much...

If you're curious to see what the code looks like, you can view it [here](https://github.com/billwarker/billwarker.ca). I'm sure it could be improved in many ways, but hey, it works!