```
const rp = require('request-promise'); // you can use other libraries for this (like axios)
const $ = require('cheerio');
const URL = 'https://www.ebay.com/';

rp(URL)
  .then(function(html){
    const data = $('li.hl-cat-nav__js-tab>a', html);
    const resData = [];

    data.each(function (i, e) {
      const temp = {
        name: $(this).text(),
        link: $(this).attr().href
      }
      resData.push(temp);  
  });
  console.log(resData);


  })
  .catch(function(err) {
    console.log(err);
    //handle error
  });
```