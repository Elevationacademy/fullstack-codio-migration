
As noted earlier, you're mostly on your own for this, but here some guidelines to give you some headway.

  

**General**

  

The `Home` and `Catalog` links, as well as the **REFLIX** logo, should all be available throughout the entire app, consistently. The `Home` link should always go to `/` , and the `Catalog` link should always go to `/catalog`

  

Do **not** burn a lot of time on getting the CSS just right. This is a React project ~

  

You should have (at least) the following components:

-   **App** - this should handle all your routing
-   **Landing** - for your landing page
-   **Catalog** - for displaying your movies (catalog & rented), search bar, and budget
    -   **Movie** - a child of **Catalog** that renders a movie's image, title, and the `+` / `-` icon
-   **MovieDetail** - for the page that shows all the info about one movie

  

**Landing Page**

  

At first, you should only render the users in separate boxes. Clicking on any box should simply re-route the page to `/catalog` - **no need** to consider which user is currently active.

  

The **Landing** component should hold all the data about the users (their name and background color) in its own state.

  

**Catalog Page**

  

When the user first arrives to this page, they should only see the search bar, the **Catalog** section, and their budget.

Here is some data you can use for your catalog of movies:

```
[
  { id: 0, isRented: false, title: "Tarzan", year: 1999, img: "https://vignette.wikia.nocookie.net/disney-fan-fiction/images/4/42/Tarzan_2004_cover.jpg/revision/latest?cb=20140331030811", descrShort: "Tarzan was born into wealth but raised into incredible misfortune. Shiprweck, parents mauled by a jaguar. Luckily, a troop of gorillas took him in, but the Big Daddy gorilla never took a liking to him. That is, until the end when it's too late. Why is it too late? Watch and find out." },
  { id: 1, isRented: false, title: "The Lion King", img: "https://img00.deviantart.net/b782/i/2006/207/e/7/the_lion_king_front_cd_cover_by_peachpocket285.jpg", year: 1994, descrShort: "A young lion prince named Simba is born into wealth but raised into incredible misfortune. Trickster uncle, dying father, usurpation. Luckily, an unlikely meerkat-warthog pair take him in and teach him The Ways of the Bum Life. Be prepared for ghostly hallucinations, wild baboons, creepy crawlies." },
  { id: 2, isRented: false, title: "Beauty and the Beast", year: 1991, img: "https://images-na.ssl-images-amazon.com/images/I/81etFyb9N-L._SL1500_.jpg", descrShort: "A kickass woman named Belle who does not succumb to social norms gets crap from a bunch of village idiots, chief amongst them a total tool named Gaston. Belle shows everyone how great she is when she turns a beast (not Gaston) into a man. Love ensues, but then the villagers fall trap to severe group-think mentality led by the main tool himself." },
  { id: 3, isRented: false, title: "The Sword in the Stone", year: 1963, img: "https://www.disneyinfo.nl/images/laserdiscs/229-1-AS-front.jpg", descrShort: "Arthur is a young boy who just wants to be a knight's squire. Alas, he is dubbed 'Wart' early on, and it was all downhill from there for a while. On a hunting trip he falls in on Merlin, literally. Merlin is a possibly-mentally-unstable-and-ethically-dubious Wizard that turns Arthur into a literate, at-one-point harassed squirrel. Watch to find out what the heck that means." },
  { id: 4, isRented: false, title: "Beauty and the Beast", year: 2016, img: "https://images-na.ssl-images-amazon.com/images/I/51ArFYSFGJL.jpg", descrShort: "Basically the same as the original, except now Hermi-- Emma Wattson plays Belle, fittingly so some would say, given how actively progressive she is regarding women's rights. Rumor has it that in the bonus scenes she whips out a wand and turns Gaston into a toad, but in order to watch those scenes you need to recite a certain incantation." }
]
```
  

You must decide which **single** component holds **all** this data in its `state`

As for user interaction,

-   Each movie should have a `+` icon (or a separate button, if that's easier) that allows the user to rent the movie
    -   When **at least one** movie has been rented, the **Rented** section should be visible, along with all the rented movies
-   Rented movies should have a `-` icon (or a separate button) that allows the user to "un-rent" the movie
    -   Note that when no movies are rented, the user should not see the **Rented** section
-   Finally, when a movie is clicked, the page should re-route to `/movies/<movieID>` using the ID of the clicked movie
    -   In other words, clicking on a movie should take the user to the Movie Detail page.

  

**Movie Detail Page**

  

This page should show all the details about the movie. Title, year, image, and description. Nothing else is needed here.

  

Note that this page is **not a child** of **Movie** or **Catalog** - you should access it using `react-router-dom`'s `Link` tag when you click on a movie.