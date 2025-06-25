
Materialize, like other CSS Frameworks, uses a "Grid" system. This is _similar_ but **not** the same as the CSS Grid you've learned.

  

In short, Materialize uses a **12 column system**, and we take advantage of that using the `col` class, like so:

<iframe src="https://codepen.io/ElevationPen/embed/JVrbdW?height=265&amp;theme-id=0&amp;default-tab=html%2Cresult&amp;user=ElevationPen&amp;slug-hash=JVrbdW&amp;editable=true&amp;pen-title=Materialize%20Grid%20Example&amp;name=cp_embed_2?height=265&amp;theme-id=0&amp;default-tab=js,result?height=265&amp;theme-id=0&amp;default-tab=js,result" width="100%" height="265" frameborder="no" scrolling="no"></iframe>

---

Go ahead and experiment with the `s#` class - notice that the number represents how many `columns` each element should take.

  

In the above example, the first and second `div`s takes 3 columns, and the third `div` takes 6 columns, because of the `s3` and `s6` classes respectively - this is one limitation of this framework, by the way - **your columns must add up to 12**.

  

Notice also that you must wrap any `col`s inside of a `row` wrapper - this is a requirement when using Materialize's "Grid" system.