
Today we're introducing JSON - **J**ava**S**cript **O**bject **N**otation.

  

From the name, you can probably guess it's going to be pretty similar to something you've already worked with and know well: JS objects.

  

In particular, we're going to talk about

  

-   What JSON is and its history
-   Why you want to use JSON
-   How to read and write JSON
-   How to design a JSON document

  

----------

  

#### **HISTORY**

  

Back in the day, when [real programmers wrote in FORTRAN](http://www.catb.org/jargon/html/story-of-mel.html), people had little need to send data between different computers - after all, there really weren't that many of them!

  

As computers became more affordable and ubiquitous, the need for them to communicate with one another grew. [Ethernet](https://en.wikipedia.org/wiki/Ethernet) was invented in the early 1970's to allow computers to communicate easily, and quickly became standardized. At this point virtually all computers knew how to speak to one another using Ethernet's special language, also known as a **protocol**.

  

With the rise of the [Internet](https://en.wikipedia.org/wiki/History_of_the_Internet), the desire to simplify communication between computers grew accordingly. New [protocols](https://en.wikipedia.org/wiki/Internet_protocol_suite) were invented to allow this, and today virtually all computers know how to communicate using them.

  

Even though we now have these special, low-level protocols that computers use to communicate, it takes humans a lot of mental effort to read, write, and code them - not to mention how error-prone that can be!

  

Instead, people have designed different formats over the years (like [Telnet](https://en.wikipedia.org/wiki/Telnet), [SOAP](https://en.wikipedia.org/wiki/SOAP), [XML](https://en.wikipedia.org/wiki/XML), and [HTML](https://en.wikipedia.org/wiki/HTML)) to make the messages that computers send one another easier to read, write, and manipulate for humans.

  

This lesson is all about [**JSON**](http://json.org/), one of the reigning champions (if not _the_ reigning champion) of all high-level data formats.