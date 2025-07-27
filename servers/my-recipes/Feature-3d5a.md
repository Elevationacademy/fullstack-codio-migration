We will be implementing a feature in this project which will be **Sensitivity Filter!**




We will be adding a filter to our original project. 

to the unlucky bunch of us with food sensitives we have dietary restrictions.
to enable support we are going to add a `filter` option that will **remove** any recipes containing "**ingredients** that include these **sensitives**.

you can use the following data to filter the sensitives

```js
dairyIngredients = ["Cream","Cheese","Milk","Butter","Creme","Ricotta","Mozzarella","Custard","Cream Cheese"]
glutenIngredients = ["Flour","Bread","spaghetti","Biscuits","Beer"]
```
---

so create the needed functionalities in the **Client** and the **Server** to make it work.

### NOTE

If we want to **filter** the recipes that do not contain `gluten` we want to make sure the ingredients in the `recipe` do not contain any `ingredients` that contain `gluten`.

so let's say we are given the following Recipe


```
{
"title": "Ice cream",
"thumbnail": "https://s7d1.scene7.com/is/image/mcdonalds/t-mcdonalds-Vanilla-Reduced-Fat-Ice-Cream-Cone:1-3-product-tile-desktop?wid=765&hei=472&dpr=off",
"href": "https://www.youtube.com/watch?v=mf4UZqv-EU8",
"ingredients": [
  "Sugar",
  "Ice",
  "Cream"
}

```

We need to be able to check if the recipe contains `gluten` or `dairy`.

and we can see it is `gluten` free because it does not contain any of the `ingredients` in the `gluten` `ingredients`.

however, it does contain `dairy` because it contains `"Cream"`


|||important
## NOTE

there are other gluten/dairy products that exist in the API that are not in the following arrays.
|||

