
#### **COMMON PITFALLS**

  

For the following examples, determine whether this is good or bad use of Async/Await. Consider the rules we defined earlier.


```js
class ApiManager {

    constructor(stocksAPI, renderer) {
        this.stocksAPI = stocksAPI
        this.renderer = renderer
    }

    async fetchStockData(ticker) {
        let stockData = await $.get(`${this.stocksAPI}/${ticker}`)
        this.renderer.render(stockData)
    }
} 
```
  

First try to answer on your own:
<details><summary>  
Click here to reveal the answer.  
</summary>
Yes this is perfectly fine. Adheres to all the rules. No problem. A-OK. Great code. Very modern.
</details>
  
```js
const getData = async function () {
    let data = await $.get('/data')
    return data
}

const result = getData()
```
  

First try to answer on your own:
<details><summary>  
Click here to reveal the answer.  
</summary>
  

No - this is bad. The rule says that **all async functions return a promise, no matter what** - therefore the value of `result` will be a `Promise`, and **not** the result from the GET request, _even though_ we used `await`. The await only applies **to the scope of the function**.
</details>

```js
const getArticles = async function(){
    let articles = await $.get('/articles')
    return articles
}

const innocentFunc = function(){
    let articles = getArticles()
    render(articles)
}

innocentFunc()
```
  

First try to answer on your own:
<details><summary>  
Click here to reveal the answer.  
</summary>
  

No - this is bad. The rule says that **if you use `async`, then all the ancestor functions must be async when returning data back**.

If we want this to work, we must make `innocentFunc` an `async` function as well, and use `await getArticles()`
</details>

```js
const nbaFetcher = async function () {
    let nbaData = await request('/nbaAPI')
    console.log(nbaData)
}

nbaFetcher()
```
  

First try to answer on your own:
<details><summary>  
Click here to reveal the answer.  
</summary>
  

No - this is bad. The rule says that **you can only use `await` on `then` able operations.** The `request` module in Node **does not** return a promise, therefore we cannot use `await` here.
</details>

```js
const requestBankInfo = async function(){
    let info = await $.get('/bankAPI')
    return info
}

let bankInfo = await requestBankInfo()
```
  

First try to answer on your own:
<details><summary>  
Click here to reveal the answer.  
</summary>
  

No - this is bad. The rule says that **you cannot use `await` outside of an `async` function**
</details>
  
```js
const loadAllUserData = async function (user) {
    let twitterData = await $.get('/twitter/' + user.name)
    let facebookData = await $.get('/facebook/' + user.name)
    let linkedinData = await $.get('/linkedin/' + user.name)

    render({
        twitter: twitterData,
        fb: facebookData,
        li: linkedinData
    })
}
```
  

First try to answer on your own:
<details><summary>  
Click here to reveal the answer.  
</summary>

Technically, this is fine.

**But**. The problem with the above is that **it will slow down your code** - this is because every line has to finish executing (i.e. the whole GET request must finish) before moving on to the next line


But the whole point of writing asynchronous code is the ability to do things simultaneously. In the above, the Facebook data doesn't depend on the Twitter data - there's no reason for the second request to wait for the first to finish. This would be better to execute with promises/callbacks.
</details>

```js
const loadBook = async function (title) {
    let bookISBN = await $.get('/titleAPI/' + title)
    let bookData = await $.get('/bookApi/' + bookISBN)

    render(bookData)
}

loadBook()
```
 

First try to answer on your own:
<details><summary>  
Click here to reveal the answer.  
</summary>

Yes sweet mother of Moses - this is a perfect usecase for `async` / `await` - the `bookApi` **does** depend on the `titleAPI` to finish, so the second request **does** need to wait for the first to finish. Excellent.
</details>

